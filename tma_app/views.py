from django.shortcuts import render, redirect

from .models import Items, TmaRequests
from .forms import ItemsForm, DenyRequestForm, OrderItemForm

item_headers = {'item_id': 'asc',
            'item_group': 'asc',
            'unit_of_measurement': 'asc',
            'quantity': 'asc',
            'price_without_vat': 'asc',
            'status': 'asc',
            'storage_location': 'asc',
            'contact_person': 'asc'}

requests_headers = {'request_id': 'asc',
            'employee_name': 'asc',
            'item_id': 'asc',
            'unit_of_measurement': 'asc',
            'quantity': 'asc',
            'price_without_vat': 'asc',
            'comment': 'asc',
            'status': 'asc'}

def index(request):
    """The home page for tma"""
    return render(request, 'tma_app/index.html')

def items(request):
    """Show all items"""
    sort = request.GET.get('sort')
    items = Items.objects.all()
    if sort is not None:
        items = items.order_by(sort)
        if item_headers[sort] == "des":
            items = items.reverse()
            item_headers[sort] = "asc"
        else:
            item_headers[sort] = "des"

    context = {'items': items}
    return render(request, 'tma_app/items.html', context)

def requests(request):
    """Show all requests"""
    sort = request.GET.get('sort')
    requests = TmaRequests.objects.all()
    if sort is not None:
        requests = requests.order_by(sort)
        if requests_headers[sort] == "des":
            requests = requests.reverse()
            requests_headers[sort] = "asc"
        else:
            requests_headers[sort] = "des"

    context = {'requests': requests}
    return render(request, 'tma_app/requests.html', context)

def new_item(request):
    """Add a new item"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = ItemsForm()
    else:
        # POST data submitted; process data
        form = ItemsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tma_app:items')

    # display a blank or invalid form.
    context = {'form': form}
    return render(request, 'tma_app/new_item.html', context)

def edit_item(request, item_id):
    """Edit existing item"""
    item = Items.objects.get(item_id=item_id)

    if request.method != 'POST':
        # Initial request; pre fill form with the current entry
        form = ItemsForm(instance=item)
    else:
        # POST data submitted; process data
        form = ItemsForm(instance=item, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tma_app:items')

    context = {'item': item, 'form': form}
    return render(request, 'tma_app/edit_item.html', context)

def delete_item(request, item_id):
    """Delete chosen item"""
    item = Items.objects.get(item_id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('tma_app:items')

    context = {'item': item}
    return render(request, 'tma_app/delete_request.html', context)

def deny_request(request, request_id):
    """Deny the request and set it's status to 'denied' - also ask for comment if possible"""
    item = TmaRequests.objects.get(request_id=request_id)

    if request.method != 'POST':
        # Initial request; pre fill form with the current entry
        form = DenyRequestForm(instance=item)
    else:
        # POST data submitted; process data
        form = DenyRequestForm(instance=item, data=request.POST)
        if form.is_valid():
            form.instance.status = "Denied"
            form.save()
            return redirect('tma_app:requests')

    context = {'item': item, 'form': form}
    return render(request, 'tma_app/deny_request.html', context)

def approve_request(request, request_id):
    """Aprove chosen request"""
    item = TmaRequests.objects.get(request_id=request_id)
    item2 = Items.objects.get(item_id=request_id)

    if request.method == 'POST':
        item2.quantity -= item.quantity
        item.status = "Approved"
        item.save()
        item2.save()
        return redirect('tma_app:requests')


    context = {'item': item}
    return render(request, 'tma_app/approve_request.html', context)

def order_item(request, item_id):
    """Order an item"""
    item = Items.objects.get(item_id=item_id)

    if request.method != 'POST':
        # No data submitted, create pre filled form
        form = OrderItemForm(instance=item)
    else:
        # Post data submitted; process data
        form = OrderItemForm(data=request.POST)
        if form.is_valid():
            form.instance.status = "New"
            form.save()
            return redirect('tma_app:items')

    context = {'item': item, 'form': form}
    return render(request, 'tma_app/order_item.html', context)

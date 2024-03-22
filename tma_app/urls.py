"""Defines URL patterns for tma"""

from django.urls import path

from . import views

app_name = 'tma_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all items.
    path('items/', views.items, name='items'),
    # Page that shows list of purchase requests.
    path('requests/', views.requests, name='requests'),
    # Page for adding a new item.
    path('new_item/', views.new_item, name='new_item'),
    # Page for editing selected item
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    # Page for deleting selected item
    path('delete_item/<int:item_id>', views.delete_item, name='delete_item'),
    # Page for denying requests
    path('deny_request/<int:request_id>', views.deny_request, name='deny_request'),
    # Page for approving requests
    path('approve_request/<int:request_id>', views.approve_request, name='approve_request'),
    # Page for ordering items
    path('order_item/<int:item_id>', views.order_item, name='order_item')
]

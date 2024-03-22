from django.http import Http404
from django.shortcuts import render, redirect


def group_required(*groups):

    def decorator(function):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name__in=groups).exists():
                return function(request, *args, **kwargs)
            return render(request, 'tma_app/lack_permissions.html')

        return wrapper

    return decorator
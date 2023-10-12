from django.shortcuts import render
from .models import MenuItem


def menu_view(request, menu_name):
    menu_items = MenuItem.objects.filter(name=menu_name).select_related('parent', 'children')

    menu_items = menu_items.only('title', 'url', 'is_active')

    context = {'menu_items': menu_items}
    return render(request, 'menu/menu.html', context)

from django import template
from .. import models

register = template.Library()

def draw_menu(menu_name, parent=None, current_url=""):
    menu = MenuItem.objects.filter(name=menu_name, parent=parent).select_related('parent')
    html = "<ul>"
    for item in menu:
        is_active = current_url == item.url
        html += f"<li {'class=active' if is_active else ''}><a href='{item.url}'>{item.title}</a>"
        sub_menu = draw_menu(menu_name, item, current_url)
        if sub_menu:
            html += sub_menu
        html += "</li>"
    html += "</ul>"
    return html

register.simple_tag(name='draw_menu')(draw_menu)

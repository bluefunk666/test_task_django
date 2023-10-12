from .models import MenuItem

class ActiveMenuItemMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        active_menu_item = MenuItem.objects.filter(url=request.path).first()

        if active_menu_item:
            active_menu_item.is_active = True
            active_menu_item.save()

        response = self.get_response(request)

        if active_menu_item:
            active_menu_item.is_active = False
            active_menu_item.save()

        return response

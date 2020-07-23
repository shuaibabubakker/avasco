from django.http import HttpResponse
from django.shortcuts import redirect

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            print("GROUP: " ,group)
            if group == 'admin':
                return view_func(request, *args, **kwargs)
        return HttpResponse('You are not authorized to view this page')
    return wrapper_function
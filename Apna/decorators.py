from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User

def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
                print("gurpreet")
            if group in allowed_roles:
                print("gurpreethih")
                return view_func(request,*args,**kwargs)

            else:
                return HttpResponse("you are not authorized")
        return wrapper_func
    return decorator


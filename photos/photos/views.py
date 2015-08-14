from django.shortcuts import render
import django.contrib.auth as auth
from django.http import HttpResponseRedirect


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        next = request.POST["next"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect("/login")
    else:
        return render(request, "login.html", {"next": request.GET.get("next", "/")})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

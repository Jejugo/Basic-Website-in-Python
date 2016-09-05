from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Login
from django.http import Http404

def indexlogin(request):
    all_login = Login.objects.all()
    if request.method == 'POST':
        try:
            for login in all_login:
                if Login.objects.get(login.username) and Login.objetcs.get(login.password):
                    return HttpResponse("<h5> Successfully logged in</h5>")

        except Login.DoesNotExist:
            raise Http404("Login Doesn't exist")

    return render(request, 'login/login.html')


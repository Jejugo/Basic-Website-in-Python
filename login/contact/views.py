from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('Name', ''):
            errors.append('Enter a name.')
        if not request.POST.get('City', ''):
            errors.append('Enter a city')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')

        if not errors:
            try:
                send_mail(
                    'Email from Website',
                    request.POST['Message'],
                    request.POST.get('email'),
                    ['goes.jeffjulian@gmail.com'],
                )
                return HttpResponse('Thank you, form has been submitted successfully')
            except Exception as err:
                return HttpResponse(str(err))

    return render(request, 'contact/index.html', {'errors': errors})

# _*_ coding: utf-8 _*_
from django.shortcuts import render_to_response, HttpResponse
from django.contrib import auth
from models import User
from forms import RegistrationForm
from ftrend.additions import random_str, translit
from additions import registration_valid


def login(request):
    args = {}
    if request.GET:
        email = request.GET['email']
        password = request.GET['password']
        try:
            user = User.objects.get(email=email)
            user = auth.authenticate(username=user.username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponse("true")
            else:
                args['form_error'] = "Данные введены не верно!"
        except User.DoesNotExist:
            args['form_error'] = "Пользователя с таким email не существует!"
    return render_to_response("login.html", args)


def registration(request):
    args = {'form': RegistrationForm()}
    if request.GET:
        form = RegistrationForm(request.GET)
        password = request.GET['password']
        errors = registration_valid(request)
        if len(errors) == 0:
            new_user = User()
            new_user.first_name = request.GET['first_name']
            new_user.email = request.GET['email']
            new_user.username = translit(new_user.first_name) + "_" + random_str(6)
            new_user.set_password(password)
            new_user.save()
            user = auth.authenticate(username=new_user.username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
            return render_to_response("registration_ready.html")
        else:
            args['form'] = form
            args.update(errors)
    return render_to_response("registration.html", args)


def account_view(request):
    return render_to_response("my_account.html", {
        'user': request.user,
        'user_active': request.user.is_authenticated(),
    })
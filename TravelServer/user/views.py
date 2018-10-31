# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from user.models import Route
import json
import rsa_util

# Create your views here.


class LoginForm(forms.Form):
    
    email = forms.CharField()
    password = forms.CharField()

class RegisterForm(forms.Form):
    
    username = forms.CharField()
    password = forms.CharField()
    email = forms.CharField()


def GetPublicKey(request):

    content = {}
    if request.method == 'GET':
        content = {
            'Status': True,
            'PublicKey_n':str(rsa_util.public_key.n),
            'PublicKey_e':str(rsa_util.public_key.e)
        }
    else:
        return HttpResponse(status=400)
    response_text = json.dumps(content)
    resp = HttpResponse(response_text, content_type='application/json')
    return resp  


def UserAuthentication(request):

    content = {}
    # print request.POST.viewkeys()
    # print request.body.decode('utf-8','ignore')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            try:
                received_json_data = json.loads(request.body.decode('utf-8','ignore'))
                form = LoginForm(received_json_data)
            except Exception,e:
                print e
                return HttpResponse(status=403)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # password = rsa_util.decrypt(password)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                content = {
                    'Status': True,
                    'email': email,
                    'password':password,
                    'username':user.username,
                }
            else:
                content = {
                    'Status': False,
                    'PublicKey_n':str(rsa_util.public_key.n),
                    'PublicKey_e':str(rsa_util.public_key.e)
                }
        else:
            return HttpResponse(status=400)
    elif request.method == 'GET':
        if request.user.is_authenticated:
            content = {
                    'Status': True,
                }
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)

    response_text = json.dumps(content)
    resp = HttpResponse(response_text, content_type='application/json')
    return resp  



def Logout(request):

    content = {}
    if request.method == 'GET':
        logout(request)
        content = {
            'Status': True,
        }
    else:
        return HttpResponse(status=400)

    response_text = json.dumps(content)
    resp = HttpResponse(response_text, content_type='application/json')
    return resp  



def Register(request):

    content = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if not form.is_valid():
            try:
                received_json_data = json.loads(request.body.decode('utf-8','ignore'))
                form = RegisterForm(received_json_data)
            except Exception,e:
                print e
                return HttpResponse(status=403)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            try:
                user = get_user_model().objects.create_user(username=username, email=email,password=password)
                content = {
                    'Status': True,
                    'email': email,
                    'password':password,
                    'username':username,
                }
            except Exception,e:
                return HttpResponse(status=403)
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)

    response_text = json.dumps(content)
    resp = HttpResponse(response_text, content_type='application/json')
    return resp 


def UserInfo(request):

    api = request.POST.get('api')
    content = {}
    if not request.user.is_authenticated:
        print "Anonymous"
        return HttpResponse(status=403)
    if api == 'changePassword':
        password = request.POST.get('password')
        try:
            request.user.set_password(password)
            request.user.save()
            content['Status'] = True
        except Exception,e:
            print e
            return HttpResponse(status=404)
    elif api == 'saveRoute':
        route_str = request.POST.get('route')
        route_id = request.POST.get('route_id')
        try:
            route_json = json.loads(route_str)
            route = Route.objects.create(route=json.dumps(route_json[1]),description=json.dumps(route_json[0]),user=request.user,route_id=route_id)
            request.user.route_set.add(route)
            content['Status'] = True
        except Exception,e:
            print e
            return HttpResponse(status=404)
    elif api == 'getRouteList':
        route_set = request.user.route_set.all()
        route_list = []
        for r in list(route_set):
            route_list.append([r.route_id,json.loads(r.description),json.loads(r.route)])
        content = {
            'Status':True,
            'RouteList':route_list
        }
    elif api == 'deleteRoute':
        route_id = request.POST.get('route_id')
        try:
            Route.objects.get(route_id=route_id).delete()
            content['Status'] = True
        except Exception,e:
            print e
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=400)

    response_text = json.dumps(content)
    resp = HttpResponse(response_text, content_type='application/json')
    return resp    
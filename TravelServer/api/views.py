# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse,Http404
import json
import DBQuery
# Create your views here.

def Interfaces(request):
    
    api = request.GET.get('api')
    content = {}
    if api == 'getSceneList':
        cityID = request.GET.get('CityID')
        try:
            result = DBQuery.getSceneList(cityID)
            if result:
                content['Status'] = True
                content['SceneList'] = result
            else:
                return HttpResponse(status=404)
        except Exception,e:
            print e
            return HttpResponse(status=404)
    elif api == 'getSceneInfo':
        sceneID = request.GET.get('SceneID')
        try:
            result = DBQuery.getSceneInfo(sceneID)
            if result:
                content['Status'] = True
                content['SceneInfo'] = result
            else:
                return HttpResponse(status=404)
        except Exception,e:
            print e
            return HttpResponse(status=404)
    elif api == 'getDistance':
        placeFrom = request.GET.get('PlaceFrom')
        placeTo = request.GET.get('PlaceTo')
        try:
            result = DBQuery.getDistance(placeFrom,placeTo)
            if result:
                content['Status'] = True
                content['Distance'] = result
            else:
                return HttpResponse(status=404)
        except Exception,e:
            print e
            return HttpResponse(status=404)
    elif api == 'getHotelList':
        cityID = request.GET.get('CityID')
        try:
            result = DBQuery.getHotelList(cityID)
            if result:
                content['Status'] = True
                content['HotelList'] = result
            else:
                return HttpResponse(status=404)
        except Exception,e:
            print e
            return HttpResponse(status=404)
    elif api == 'getHotelInfo':
        hotelID = request.GET.get('HotelID')
        try:
            result = DBQuery.getHotelInfo(hotelID)
            if result:
                content['Status'] = True
                content['HotelInfo'] = result
            else:
                return HttpResponse(status=404)
        except Exception,e:
            print e
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=400)


    response_text = json.dumps(content)
    resp = HttpResponse(response_text, content_type='application/json')
    return resp      

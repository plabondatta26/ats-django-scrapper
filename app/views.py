import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serilizer import *
from rest_framework import status
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from .scrapper import scrapper_controller
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
import html_to_json
from .models import *


# Create your views here.


class ReceiveLocation(CreateAPIView):
    serializer_class = LocationSerializer

    def post(self, request):
        loc = request.data.get("address", None)
        if loc:
            data = scrapper_controller(loc)
            obj, created = LocationModel.objects.get_or_create(address=loc)
            if created:
                obj.json_data = data
                obj.save()
            else:
                if obj.json_data == data:
                    pass
                else:
                    obj.json_data = data
                obj.save()
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)


def zillow_scrapper(request):
    if request.method == 'POST':
        link = request.POST.get('zilink')
        print(link)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(link)
        parent_of_data = driver.find_element_by_class_name('hdp__sc-1gqth4d-0')
        html_data = parent_of_data.get_attribute('innerHTML')
        output_json = html_to_json.convert(html_data)
        location = output_json["h1"][0]["_values"][0] + output_json["h1"][0]["_values"][1]
        driver.close()
        data = scrapper_controller(location)
        print(data)
        return render(request, 'form.html', data)
    data = {'homewise': {'searched_address': '24634 N 36th Ave Glendale, AZ 85310-4321',
                         'result': {'address_title': 'Sunrise at Stetson Hills Homeowners Association', 'state':
                             'Glendale , AZ 85310', 'Managed by:': 'Planned Development Services'}},
            'condocerts': {'message': 'No data found'}, 'sentry': {'message': 'No data found'},
            'first_finder': {'message': 'No data found'}, 'market': {'result': 'No data found'},
            'estoppels': {'message': 'Invalid Address'}, 'execution_time': 367.743628}

    return render(request, 'form.html', {"data": data})


def zillow_address(request):
    if request.method == 'POST':
        link = request.POST.get('zilink')
        driver = webdriver.Chrome(ChromeDriverManager().install())
        html_data = None
        driver.get(link)
        parent_of_data = driver.find_element_by_class_name('Spacer-c11n-8-62-4__sc-17suqs2-0')
        html_data = parent_of_data.get_attribute('innerHTML')
        output_json = html_to_json.convert(html_data)
        driver.close()
    return render(request, 'form.html')

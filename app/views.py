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
            # obj, created = LocationModel.objects.get_or_create(address=loc)
            # if created:
            #     obj.json_data = data
            #     obj.save()
            # else:
            #     if obj.json_data == data:
            #         pass
            #     else:
            #         obj.json_data = data
            #     obj.save()
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serilizer import *
from rest_framework import status
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from .scrapper import scrapper_controller
# Create your views here.


class ReceiveLocation(APIView):
    def post(self, request):
        loc = request.data.get("address", None)
        if loc:
            data = scrapper_controller(loc)
            print(data)
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)


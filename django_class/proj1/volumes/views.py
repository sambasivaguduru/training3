# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def fun(a):
    return HttpResponse("hello firefox!!")

class Service(APIView):
	def get(self, format=None):
		return Response("this is get resp")
	def post(self, format=None):
		return Response("this is post resp")

	def put(self, format=None):
		return Response("this is put resp")
	def delete(self, format=None):
		return Response("this is delete resp")



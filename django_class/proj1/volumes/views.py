# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun(a):
    return HttpResponse("hello firefox!!")
def filesystems_view(request):
	return HttpResponse(["filesystm1", "filesystem2"])

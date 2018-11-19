# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from volumes.models import Cluster
from rest_framework import status

# Create your views here.


def fun(a):
    return HttpResponse("hello firefox!!")


class ClusterAPI(APIView):
    def post(self, format=None):
        data = self.request.data
        cluster = Cluster(name=data["name"],
                          username=data["username"],
                          password=data["password"],
                          ip=data["ip"])
        #cluster = Cluster(**data)
        cluster.save()
        return Response("Cluster created successfully!!")

    def get(self, format=None, cluster_id=None):
    	if cluster_id:
    		data = Cluster.objects.filter(id=cluster_id)
    	else:
        	data = Cluster.objects.all()
        # data_details = []
        # for row in data:
        # 	row_details={"name": row.name,"ip": row.ip}
        # 	data_details.append(row_details)

        data_details = [{"name": row.name,
                         "username": row.username,
                         "password": row.password,
                         "ip": row.ip} for row in data]
        return Response(data_details)
    def delete(self,  format=None, cluster_id=None):
    	if not cluster_id:
    		return Response("cluster id mandatory!!", 
    			status=status.HTTP_400_BAD_REQUEST)
    	cluster=Cluster.objects.get(id=cluster_id)
    	cluster.delete()
    	return Response("OK deleted")

class Service(APIView):
    def get(self, format=None):
        return Response("this is get resp")

    def post(self, format=None):
        print "*" * 20
        print self.request.data
        print "*" * 20
        return Response("this is post resp")

    def put(self, format=None):
        return Response("this is put resp")

    def delete(self, format=None):
        return Response("this is delete resp")

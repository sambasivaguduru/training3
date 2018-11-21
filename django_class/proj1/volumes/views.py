# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from volumes.models import Cluster
from rest_framework import status
from serializers import ClusterSerializer

# Create your views here.


def fun(a):
    return HttpResponse("hello firefox!!")

resp = {"status":"","errors":"","data":""}

class ClusterAPI(APIView):
    def post(self, format=None):
        ser = ClusterSerializer(data=self.request.data)
        if ser.is_valid():
            ser.save()
            resp.update({
                "status":"success",
                "data":ser.data,
                })
            return Response(resp)
        else:
            error = ser._errors
            resp.update({
                "status":"failed",
                "error":error,
                })
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)

        # # data = self.request.data
        # # user_name = data["username"]
        
        # # cluster = Cluster(name=data["name"],
        # #                   username=data["username"],
        # #                   password=data["password"],
        # #                   ip=data["ip"])
        # # #cluster = Cluster(**data)
        # # cluster.save()
        # return Response("Cluster created successfully!!")

    def get(self, format=None, cluster_id=None):
    	if cluster_id:
    		data = Cluster.objects.filter(id=cluster_id)
    	else:
        	data = Cluster.objects.all()
        ser = ClusterSerializer(data, many=True)
        # data_details = []
        # for row in data:
        # 	row_details={"name": row.name,"ip": row.ip}
        # 	data_details.append(row_details)

        # data_details = [{"name": row.name,
        #                  "username": row.username,
        #                  "password": row.password,
        #                  "ip": row.ip} for row in data]
        return Response(ser.data)
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

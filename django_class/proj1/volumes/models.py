# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cluster(models.Model):
		name = models.CharField(max_length=60)
		ip = models.CharField(max_length=60)
		username = models.CharField(max_length=60)
		password=models.CharField(max_length=20)
class Protocol(models.Model):
	name = models.CharField(max_length=60)

class SVM(models.Model):
	name = models.CharField(max_length=60)
	cluster = models.ForeignKey(Cluster, on_delete=models.PROTECT)
	protocols = models.ManyToManyField(Protocol)

class Volume(models.Model):
	name = models.CharField(max_length=60)
	size=models.IntegerField()
	svm=models.ForeignKey(SVM, on_delete=models.PROTECT)
	protocol=models.ForeignKey(Protocol, on_delete=models.PROTECT)



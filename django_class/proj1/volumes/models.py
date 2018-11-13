# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cluster(models.Model):
		name = models.CharField(max_length=60)
		ip = models.CharField(max_length=60)
		username = models.CharField(max_length=60)
		password=models.CharField(max_length=20)



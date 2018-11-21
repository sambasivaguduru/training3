from rest_framework import serializers
from volumes.models import Cluster

class ClusterSerializer(serializers.ModelSerializer):
	# columns

	class Meta:
		# configuration..
		model = Cluster
		fields="__all__" #["name","ip"]

	def validate_name(self,value):
		if not value.isalnum():
			raise serializers.ValidationError("name not valid")
		return value
		
	def validate_ip(self, value):
		if value.count(".")!=3:
			raise serializers.ValidationError("Ip not valid")
		return value

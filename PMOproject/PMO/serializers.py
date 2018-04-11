from rest_framework import serializers
from PMO.models import Case

class CaseSerializer(serializers.Serializer):
	created_time = serializers.DateTimeField()
	level = serializers.CharField(max_length=10)
	description = serializers.CharField()
	action = serializers.CharField()
	cost = serializers.CharField(max_length=100)
	casualties = serializers.CharField(max_length=100)
	status = serializers.CharField(max_length=10, allow_blank = True)
	comment = serializers.CharField(max_length=100, allow_blank = True)
	approved = serializers.NullBooleanField(default = None)
	
	def create(self, validated_data):
		return Case.objects.create(**validated_data)
		
	def update(self,instance, validated_data):
		instance.created_time = validated_data.get('created_time', instance.created_time)
		instance.level = validated_data.get('level', instance.level)
		instance.description = validated_data.get('description', instance.description)
		instance.action = validated_data.get('action', instance.action)
		instance.cost = validated_data.get('cost', instance.cost)
		instance.casualties = validated_data.get('casualties', instance.casualties)
		instance.status = validated_data.get('status', instance.status)
		instance.comment = validated_data.get('comment', instance.comment)
		instance.approved = validated_data.get('approved', instance.approved)
		instance.save()
		return instance
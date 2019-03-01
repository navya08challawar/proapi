from rest_framework import serializers
from proapp.models import reportcard

class ReportSerializer(serializers.ModelSerializer):
	class Meta:
		model=reportcard
		fields=("class_name","stud_name","eng","tel","hindi","bio")

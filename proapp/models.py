# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class reportcard(models.Model):
	class_name=models.CharField(max_length=20)
	stud_name=models.CharField(max_length=20)
	eng=models.IntegerField()
	tel=models.IntegerField()
	hindi=models.IntegerField()
	bio=models.IntegerField()
	
	def __str__(self):
		return self.stud_name,self.class_name
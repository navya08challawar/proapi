# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from proapp.models import reportcard
from proapp.serializers import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
	queryset=reportcard.objects.all()
	serializer_class=ReportSerializer

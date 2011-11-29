#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django import forms
# Create your models here.
#TODO create a models to save playlist

class UploadFileForm(forms.Form):
    file  = forms.FileField(label='mp3')
    dest = forms.CharField(label='dest', max_length=50, required=False, help_text=u'目标文件夹,如:陈奕迅')


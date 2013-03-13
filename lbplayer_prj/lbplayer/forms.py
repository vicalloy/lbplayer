# -*- coding: utf-8 -*-
from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(label='mp3')
    dest = forms.CharField(label='dest', max_length=50, required=False, help_text='目标文件夹,如:陈奕迅')

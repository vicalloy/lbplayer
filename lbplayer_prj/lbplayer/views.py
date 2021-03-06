#encoding=utf-8
from __future__ import unicode_literals

import os
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .helper import render_json_response, gen_childs, keys2medias
import settings as lbp_settings
from .forms import UploadFileForm


def player(request):
    template_name = 'lbplayer/player.html'
    ctx = {'form': UploadFileForm()}
    return render(request, template_name, ctx)


def handle_uploaded_file(dest, file):
    try:
        dest_dir = os.path.join(lbp_settings.LBP_MEDIA_ROOT, dest)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
    except:  # use media root if makedir failed
        dest_dir = lbp_settings.LBP_MEDIA_ROOT
    path = os.path.join(dest_dir, file.name)
    f = open(path, 'wb+')
    for chunk in file.chunks():
        f.write(chunk)
    f.close()


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            dest = form.cleaned_data['dest']
            handle_uploaded_file(dest, request.FILES['file'])
    return redirect('/')


def sel_media(request):
    pass
    template_name = 'lbplayer/sel_media.html'
    ctx = {}
    return render(request, template_name, ctx)


@csrf_exempt
def ajax_childs(request):
    key = request.GET.get('key', '')
    nodes = gen_childs(lbp_settings.LBP_MEDIA_ROOT, key)
    if not key:
        root_node = {"title": "目录",
                "key": "__root__",
                "isFolder": True,
                "isLazy": True,
                "url": "",
                "children": nodes}
        nodes = [root_node]
    return render_json_response(nodes)


@csrf_exempt
def ajax_medias(request):
    keys = request.POST.get("keys", "")
    keys = keys.split(',')
    medias = keys2medias(keys, lbp_settings.LBP_MEDIA_ROOT)
    return render_json_response(medias)

#!/usr/bin/python  
#encoding=utf-8  
from django import template
from django.shortcuts import render_to_response
from django.contrib.csrf.middleware import csrf_exempt

from helper import render_json_response, gen_childs, keys2medias
import settings as lbp_settings

def player(request):
    pass
    template_name = 'lbplayer/player.html'
    ctx = {}
    return render_to_response(template_name, ctx, 
            context_instance=template.RequestContext(request))

def sel_media(request):
    pass
    template_name = 'lbplayer/sel_media.html'
    ctx = {}
    return render_to_response(template_name, ctx, 
            context_instance=template.RequestContext(request))

@csrf_exempt
def ajax_childs(request):
    key = request.GET.get('key', '')
    nodes = gen_childs(lbp_settings.LBP_MEDIA_ROOT, key)
    if not key:#ROOT
        root_node = {"title": u"目录",
                "key": "__root__",
                "isFolder": True,
                "isLazy": True,
                "url": "",
                "children": nodes,
                }
        nodes = [root_node]
    return render_json_response(nodes)

@csrf_exempt
def ajax_medias(request):
    keys = request.POST.get("keys", "");
    keys = keys.split(',')
    medias = keys2medias(keys, lbp_settings.LBP_MEDIA_ROOT)
    return render_json_response(medias)

#encoding=utf-8
from __future__ import unicode_literals

import sys
if sys.version > '3':
    PY3 = True
else:
    PY3 = False
import os
import os.path
import json
try:
    from urllib import quote
except:
    from urllib.parse import quote


from django.http import HttpResponse

from . import settings as lbp_settings


def render_json_response(data):
    return HttpResponse(json.dumps(data), mimetype='application/json')


def decode_fn(fn):
    if PY3:
        return fn
    encode = lbp_settings.LBP_FILENAME_ENCODE
    encode = encode.upper()
    if encode == 'UTF-8':
        return fn
    return fn.decode(encode, 'ignore').encode('UTF-8')


def fmt_fn(media_root, fn):
    fn = fn[len(media_root):].replace('\\', '/')
    fn = decode_fn(fn)
    url = lbp_settings.LBP_MEDIA_PREFIX + quote(fn)
    return url


def key_from_string(s):
    """
    Calculate a unique key for an arbitrary  string.
    """
    return "_" + hex(hash(s))[3:]


def find_folder_by_key(root_path, key):
    """Search rootPath and all sub folders for a directory that matches the key."""
    for root, dirs, files in os.walk(root_path):
        for name in dirs:
            full_path = os.path.join(root, name)
            file_key = key_from_string(full_path)
            if key == file_key:
                return full_path
    return None


def gen_childs(root_path, key=None):
    if key:
        folder_path = find_folder_by_key(root_path, key)
    else:
        folder_path = root_path
    if not folder_path:
        return []
    nodes = []
    file_nodes = []
    for fn in os.listdir(folder_path):
        full_fn = os.path.join(folder_path, fn)
        isdir = os.path.isdir(full_fn)
        if not isdir and not lbp_settings.LBP_IS_MEDIA_FUNC(fn):
            continue
        node = {"title": decode_fn(fn),
                "key": key_from_string(full_fn),
                "isFolder": isdir,
                "isLazy": isdir,
                }
        if isdir:
            nodes.append(node)
        else:
            file_nodes.append(node)
    nodes.extend(file_nodes)
    return nodes


def get_all_medias(media_root, root_path):
    medias = []
    for root, dirs, files in os.walk(root_path):
        for fn in files:
            full_fn = os.path.join(root, fn)
            if not lbp_settings.LBP_IS_MEDIA_FUNC(full_fn):
                continue
            medias.append({'name': decode_fn(fn),
                'mp3': fmt_fn(media_root, full_fn), })
    return medias


def keys2medias(keys, root_path):
    if "__root__" in keys:
        return get_all_medias(root_path, root_path)
    medias = []
    for root, dirs, files in os.walk(root_path):
        for name in dirs:
            full_path = os.path.join(root, name)
            file_key = key_from_string(full_path)
            if file_key not in keys:
                continue
            medias.extend(get_all_medias(root_path, full_path))
        for name in files:
            full_fn = os.path.join(root, name)
            file_key = key_from_string(full_fn)
            if file_key in keys:
                node = {'name': decode_fn(name),
                        'mp3': fmt_fn(root_path, full_fn),
                        }
                medias.append(node)
    return medias

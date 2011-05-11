from django.conf import settings

def is_media(fn):
    return fn.upper().endswith('.MP3')

def decode_fn(fn):
    return fn.decode('GBK', 'ignore').encode('UTF-8')

LBP_MEDIA_PREFIX = getattr(settings, 'LBP_MEDIA_PREFIX', '/music/')
LBP_MEDIA_ROOT = getattr(settings, 'LBP_MEDIA_ROOT', './')
LBP_DECODE_FN_FUNC = getattr(settings, 'LBP_DECODE_FN_FUNC', decode_fn)
LBP_IS_MEDIA_FUNC = getattr(settings, 'LBP_IS_MEDIA_FUNC', is_media)

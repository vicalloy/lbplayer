from django.conf import settings


def is_media(fn):
    return fn.upper().endswith('.MP3')

LBP_MEDIA_PREFIX = getattr(settings, 'LBP_MEDIA_PREFIX', '/music/')
LBP_MEDIA_ROOT = getattr(settings, 'LBP_MEDIA_ROOT', './')
LBP_FILENAME_ENCODE = getattr(settings, 'LBP_FILENAME_ENCODE', 'UTF-8')
LBP_IS_MEDIA_FUNC = getattr(settings, 'LBP_IS_MEDIA_FUNC', is_media)

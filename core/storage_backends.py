# Import django
from django.conf import settings

# Import 
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    Static files storage
    """
    location = settings.STATIC_LOCATION
    default_acl = 'public-read'


class MediaStorage(S3Boto3Storage):
    """
    Media storage for S3
    """
    location = settings.PUBLIC_MEDIA_LOCATION
    file_overwrite = False
    default_acl = 'public-read'
    
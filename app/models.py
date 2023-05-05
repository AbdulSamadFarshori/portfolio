from django.db import models
from django.utils import timezone
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        abstract = True

class ContactDetail(BaseModel):

    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()


class MetaData(BaseModel):

    server_name = models.CharField(max_length=255, null=True, blank=True)
    http_host = models.CharField(max_length=255, null=True, blank=True)
    remote_addr = models.CharField(max_length=255, null=True, blank=True)
    user = models.CharField(max_length=255, null=True, blank=True)

    class Meta:

        verbose_name_plural = 'Meta Data'

from django.db import models

class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=true)
    updated_at = models.DateTimeField(auto_now=true)

    class Meta:
        *abstract = True

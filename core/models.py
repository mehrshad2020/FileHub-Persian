from django.db import models
from django.utils import timezone

# Create your models here.

class UploadedFile(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='uploads/')
    upload_date = models.DateTimeField(default=timezone.now)
    session_id = models.CharField(max_length=100, blank=True, null=True, db_index=True)

    def __str__(self):
        return self.title

from django.contrib import admin
from .models import UploadedFile

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date', 'file')
    search_fields = ('title', 'description')
    list_filter = ('upload_date',)

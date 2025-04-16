from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.http import Http404
from .models import UploadedFile
from .forms import UploadFileForm

def get_or_create_session_id(request):
    if not request.session.session_key:
        request.session.save()
    return request.session.session_key

def home(request):
    return render(request, 'core/home.html')

class FileListView(ListView):
    model = UploadedFile
    template_name = 'core/file_list.html'
    context_object_name = 'files'
    ordering = ['-upload_date']
    
    def get_queryset(self):
        session_id = get_or_create_session_id(self.request)
        return UploadedFile.objects.filter(session_id=session_id).order_by('-upload_date')

class FileDetailView(DetailView):
    model = UploadedFile
    template_name = 'core/file_detail.html'
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        session_id = get_or_create_session_id(self.request)
        if obj.session_id != session_id:
            raise Http404("شما اجازه دسترسی به این فایل را ندارید")
        return obj

class FileUploadView(CreateView):
    model = UploadedFile
    template_name = 'core/file_upload.html'
    form_class = UploadFileForm
    success_url = reverse_lazy('file-list')
    
    def form_valid(self, form):
        form.instance.session_id = get_or_create_session_id(self.request)
        return super().form_valid(form)

class FileDeleteView(DeleteView):
    model = UploadedFile
    template_name = 'core/file_confirm_delete.html'
    success_url = reverse_lazy('file-list')
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        session_id = get_or_create_session_id(self.request)
        if obj.session_id != session_id:
            raise Http404("شما اجازه حذف این فایل را ندارید")
        return obj

from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,UpdateView,DeleteView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Notes
# Create your views here.



class NotesList(ListView):
    model = Notes
    context_object_name ='notes'
    template_name = 'Notes/home.html'
    ordering = ['-date_created']

class NoteDetailView(LoginRequiredMixin,DetailView):
    model = Notes
    template_name = 'Notes/note_detail.html'


class CreateNoteView(LoginRequiredMixin,CreateView):
    model = Notes
    template_name = 'Notes/note_create.html'
    fields = ['title','notes']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NoteDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Notes
    template_name='Notes/delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False


class NoteEditView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Notes
    template_name = 'Notes/note_create.html'
    fields = ['title','notes']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False



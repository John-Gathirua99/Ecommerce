from django.urls import path
from . import views
from .views import NotesList,CreateNoteView,NoteDetailView,NoteDeleteView,NoteEditView
urlpatterns = [
    path('',NotesList.as_view(),name ='home'),
    path('new/',CreateNoteView.as_view(),name = 'new-note'),
    path('note/detail/<int:pk>/',NoteDetailView.as_view(),name = 'detail'),
    path('note/<int:pk>/delete/',NoteDeleteView.as_view(),name = 'delete'),
    path('note/<int:pk>/edit/',NoteEditView.as_view(),name = 'edit'),
]
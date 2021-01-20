from django.urls import path
from .views import TodoView, NotesView, DeleteView, HomeView

app_name = 'main'
urlpatterns = [
    path('todo/<str:email>/', TodoView, name='main'),
    path('notes/<str:email>/', NotesView, name='notes'),
    path('home/<str:email>/', HomeView, name='home'),
    path('notes/<str:email>/<int:notes_id>', DeleteView, name='notes')
]
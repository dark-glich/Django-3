"""todo_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from login.views import SignupView, SigninView
from main.views import TodoView, NotesView, DeleteView, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SignupView, name='signup'),
    path('signup/', SignupView, name='signup'),
    path('login/', SigninView, name='login'),
    path('', include('main.urls'))


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


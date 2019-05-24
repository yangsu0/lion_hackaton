"""lionproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import project.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',project.views.home, name='home'),
    path('card/',project.views.card, name='card'),
    path('Add/', project.views.Add , name='Add'),
    path('click/<int:card_id>',project.views.click, name = 'click'),
    path('reset/', project.views.reset ,name='reset'),
    path('rank/', project.views.rank, name='rank'),
    path('submit/', project.views.submit, name='submit'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
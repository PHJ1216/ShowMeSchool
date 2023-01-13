from django.contrib import admin
from django.urls import path, include
import project.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('project.urls')),

]

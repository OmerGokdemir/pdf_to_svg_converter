from django.urls import path
from .views import upload_and_convert, converted_list

urlpatterns = [
    path('upload/', upload_and_convert, name='upload'),
    path('converted/', converted_list, name='converted_list'),
]

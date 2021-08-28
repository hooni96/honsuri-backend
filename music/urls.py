from django.urls import path
from .views import MusicView  


app_name = 'music'

urlpatterns = [
    path('music', MusicView.as_view(), name='music'),
]

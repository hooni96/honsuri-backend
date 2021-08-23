from django.urls import include, path
from .views import MusicView  

app_name = 'music'

urlpatterns = [
    path('music/', MusicView.as_view(), name='music'),
]

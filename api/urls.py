from django.urls import path
from .views import GeneratePost

urlpatterns = [
    path('generate', GeneratePost.as_view()),
]
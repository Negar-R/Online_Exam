from django.urls import path 
from .views import postAnswers

urlpatterns = [
    path('answer/<int:user_id>' , postAnswers),
]

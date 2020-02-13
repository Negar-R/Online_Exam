from django.urls import path
from .views import getQuestions

urlpatterns = [
    path('exam/<int:user_id>' , getQuestions),
]

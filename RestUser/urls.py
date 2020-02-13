from django.urls import path
from .views import registeration , ShowQuestions , CheckAns

urlpatterns = [
    path('validate' , registeration.as_view()),
    path('questions' , ShowQuestions.as_view()),
    path('ans' , CheckAns.as_view()),
]

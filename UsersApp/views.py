from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from QuestionsApp.models import Question
from .models import Profile , Question_Profile
import json

# Create your views here.

@csrf_exempt
def postAnswers(request , user_id):

    if request.method == 'POST':

        correct = 0
        wrong = 0

        body_msg = request.body.decode('utf-8')
        msg = json.loads(body_msg)

        user = Profile.objects.get(id = user_id)

        for i in msg:

            soal = Question.objects.get(id = i)

            obj = Question_Profile.objects.get(profile = user , question = soal)
            obj.ans = msg[i]
            obj.save()

            if soal.answer == msg[i]:
                correct += 1
                obj.is_correct = "True"
                obj.save()

            else:
                wrong += 1
                obj.is_correct = "False"
                obj.save()

        darsad = ((3*(correct) - (wrong))/(3*20))*100

        myJson = {"Result" : darsad , "Correct Ans" : correct , "Wrong Ans" : wrong} 

        return JsonResponse(myJson)             
                


from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.authtoken.models import Token 
from rest_framework.permissions import IsAuthenticated

from .models import Profile_Second
from QuestionsApp.models import Question

import random
import json

# Create your views here.

class registeration(APIView):

    def post(self , request):

        username = request.data.get('username')
        password = request.data.get('password')
        address = request.data.get('address')

        user , _ = User.objects.get_or_create(username = username , password = password)

        token , _ = Token.objects.get_or_create(user = user)

        profile , _ = Profile_Second.objects.get_or_create(user = user , address = address , tokenKey = str(token.key))


        return Response({'token': token.key})


class ShowQuestions(APIView):

    permission_classes = [IsAuthenticated]

    def get(self , request):
        soal_list = []

        randomId = random.sample(range(1 , 20) , 5)
        print(randomId)

        for i in randomId:
            q = Question.objects.get(id = i)
            soal_list.append({"Number" : q.id , "Question" : q.question , "Gozine1" : q.firstChoice , "Gozine2" : q.secondChoice , "Gozine3" : q.thirdChoice , "Gozine4" : q.forthChoice})

        myJson = {"Contest" : soal_list}

        return Response(myJson)     

class CheckAns(APIView):

    permission_classes = [IsAuthenticated]

    def post(self , request):
        correct = 0
        wrong = 0

        body_msg = request.body.decode('utf-8')
        msg = json.loads(body_msg)
        
        for i in msg:

            soal = Question.objects.get(id = i)

            if soal.answer == msg[i]:
                correct += 1

            else:
                wrong += 1

        darsad = ((3*(correct) - (wrong))/(3*20))*100

        myJson = {"Result" : darsad , "Correct Ans" : correct , "Wrong Ans" : wrong} 

        return Response(myJson)            




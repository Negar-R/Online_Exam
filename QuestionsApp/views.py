from django.shortcuts import render
from django.http import JsonResponse
from .models import Question
from UsersApp.models import Profile , Question_Profile
import csv , os
import random

# Create your views here.

# with open("/media/negar/New Volume/Python/BootCamp/DjangoCodes/UsersContest/QuestionsApp/soalat.csv") as csvfile:
#     reader = csv.reader(csvfile , delimiter = ',')

#     reader = list(reader)
#     print(type(reader))
#     reader.remove(reader[0])

#     for column in reader:
#         print("salam") 
#         print(column)       
#         p = Question(question = column[0],firstChoice = column[1],
#         secondChoice = column[2],thirdChoice = column[3],forthChoice = column[4],answer = column[5])  
#         p.save()


def getQuestions(request , user_id):

    soal_list = []

    randomId = random.sample(range(1 , 20) , 5)

    if request.method == 'GET':

        for i in randomId:
            q = Question.objects.get(id = i)
            soal_list.append({"Number" : q.id , "Question" : q.question , "Gozine1" : q.firstChoice , "Gozine2" : q.secondChoice , "Gozine3" : q.thirdChoice , "Gozine4" : q.forthChoice})

            user = Profile.objects.get(id = user_id)
            obj = Question_Profile(profile = user , question = q)
            obj.save()

        myJson = {"Contest" : soal_list}

        return JsonResponse(myJson)       


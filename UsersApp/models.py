from django.db import models
from django.contrib.auth.models import User
from QuestionsApp.models import Question

# Create your models here.

class Profile(models.Model):

    add_choices = (
        ('T' , 'Tehran') ,
        ('O' , 'Other')
    )
    user = models.OneToOneField(User, verbose_name = ("User"), on_delete = models.CASCADE)
    questions = models.ManyToManyField(Question)

    phone = models.IntegerField()
    address = models.CharField(max_length = 100 , choices = add_choices)

    def __str__(self):
        return self.user.username
    
    


class Question_Profile(models.Model):

    profile = models.ForeignKey(Profile , on_delete=models.CASCADE)
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    ans = models.CharField(max_length = 50)
    is_correct = models.CharField(max_length = 50 , null = True , blank = True)
    
    
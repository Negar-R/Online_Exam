from django.db import models

# Create your models here.

print("dar model hastim ****")

class Question(models.Model):

    question = models.TextField()
    firstChoice = models.CharField(max_length = 255)
    secondChoice = models.CharField(max_length = 255)
    thirdChoice = models.CharField(max_length = 255)
    forthChoice = models.CharField(max_length = 255)
    answer = models.CharField(max_length = 10)

    def __str__(self):
        return self.question 
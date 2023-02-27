from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionModel(models.Model):
    question = models.CharField(max_length=5000)
    timeStamp = models.DateTimeField(auto_now_add=True, editable=False)
    userRef = models.ForeignKey(User, on_delete=models.CASCADE)
from django.contrib import admin

from .models import QuestionModel
# Register your models here.

class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ['question', 'timeStamp', 'userRef']

admin.site.register(QuestionModel, QuestionModelAdmin)
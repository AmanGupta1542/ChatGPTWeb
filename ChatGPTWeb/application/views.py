from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import openai

from .models import QuestionModel
# Create your views here.


openai.api_key = "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"
model_engine = "text-davinci-002"

def index(request):
    if 'loggedinUser' in request.session:
        data_dict = {'history':QuestionModel.objects.filter(userRef=request.user).order_by('-timeStamp').values()}
        data_dict = {}
        return render(request, 'application/index.html', context=data_dict)
    else:
        return redirect("/user/login")

def query(request):
    if 'loggedinUser' not in request.session: return redirect("/user/login")
    data_dic = {'status' : 'error', 'data': 'Something went wrong!'}
    if request.method == 'POST':
        question = request.POST.get('que')
        if question:
            try:
                res = QuestionModel(question= question, userRef=request.user)
                res.save()
                answer = openai.Completion.create(model="text-davinci-003", prompt=question, temperature=0.9, max_tokens=1024)
                if answer:
                    data_dic['status'] = 'success'
                    data_dic['data'] = answer['choices'][0]['text']
                    # data_dic['history'] = QuestionModel.objects.filter(userRef=request.user).order_by('-timeStamp').values()
            except Exception as e:
                data_dic['data'] = 'Internal server error'
    return JsonResponse(data_dic, safe=False)

    
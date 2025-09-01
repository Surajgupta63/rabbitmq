from django.shortcuts import render
from django.http import HttpResponse
from .rabbitmq import publish_message
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = json.dumps(data)
        publish_message(message)
        return JsonResponse({"msg": "message pushed into RabbitMQ"})
    
    return JsonResponse({"msg": "wrong method"})
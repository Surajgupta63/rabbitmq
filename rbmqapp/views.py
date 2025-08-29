from django.shortcuts import render
from django.http import HttpResponse
from .rabbitmq import publish_message


# Create your views here.

def index(request):
    publish_message("Hi this is a message from rbmqapp")
    return HttpResponse("massege pushed into RabbitMQ")
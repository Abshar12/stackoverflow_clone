from django.shortcuts import render
from django.http import HttpResponse
from html5lib import serialize
from .models import Questions
from rest_framework import viewsets
from .serializers import questionserializer
from bs4 import BeautifulSoup
import requests
import json


# Create your views here.
def index(requests):
    return HttpResponse ("Success")

class QuestionAPI(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = questionserializer

def latest(request):
    try:
    
        url = "https://stackoverflow.com/questions"

        r = requests.get(url)
#print (r.text)

        soup = BeautifulSoup (r.text , "html.parser")
#print (soup)
        questions_data = {"questions" : []}

        questions = soup.select(".s-post-summary--content")
        for i in questions:
            q = i.select_one(".s-link").getText()

            question = Questions()
            question.question = q

            question.save()

            

        return HttpResponse("Data fetched from stackoverflow")
    except :
        return HttpResponse("Failed")


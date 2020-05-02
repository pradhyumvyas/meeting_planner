from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meeting.models import Meeting

# Create your views here.
def welcome(request):
    return render(request, "website/index.html", {'message':"Created By Pradhyum Vyas",
                                                  'meeting_count':Meeting.objects.count(),
                                                  'meeting':Meeting.objects.all(),
                                                  'date':(datetime.today().date())})

def status(request):
    return render(request, "website/status.html")

def date(request):
    return HttpResponse({})
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting, Room
from datetime import datetime
from django.forms import modelform_factory

# Create your views here.

def details(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meeting/details.html", {'meeting': meeting,
                                                    'message': "Created By Pradhyum Vyas",
                                                    'date': (datetime.today().date())})

def all_meeting(request):
    all_meeting = Meeting.objects.all()
    return render(request, {'all_meeting': all_meeting})

def remove(request):
    return render(request, "meeting/remove.html", {'message': "Created By Pradhyum Vyas",
                                                  'meeting_count': Meeting.objects.count(),
                                                  'meeting': Meeting.objects.all(),
                                                   'clear':Meeting.delete()})

def rooms(request):
    return render(request, "meeting/rooms.html", {'room':Room.objects.all(),
                                                  'message': "Created By Pradhyum Vyas",
                                                  'date': (datetime.today().date())})

NewMeeting = modelform_factory(Meeting, exclude=[])
def form(request):
    if request.method == "POST":
        form = NewMeeting(request.POST)

        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = NewMeeting
    return render(request, 'meeting/new.html', {'form': form})
from django.shortcuts import render
from .models import Event
from .forms import EventForm
from django.views import View
from django.http import Http404, HttpResponseRedirect, JsonResponse, HttpResponse 

# Create your views here.

# def lobby(request):
#     return render(request, 'chat/lobby.html')

def getEvents(request):
    events  = Event.objects.all()
    return JsonResponse({"events":list(events.values())})


class EventFormView(View):
    
    # def get(self, request):
    #   form = EventForm()
    #   events = Event.objects
    #   return render(request, 'home.html', context={'form': form, 'events': events})

    def get(self, request):
        form = EventForm()
        events = Event.objects
        return render(request, 'chat/lobby.html', context={'form': form, 'events': events})


    def connect(self):
        self.accept()


    def post(self, request):
        form = EventForm(request.POST)
       
        if form.is_valid():
            Event.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'chat/lobby.html', context={'form': form})


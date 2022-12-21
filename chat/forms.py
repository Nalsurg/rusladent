from django.forms import ModelForm
from chat.models import Event

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ["title", "resourceId", "start_time", "end_time"]
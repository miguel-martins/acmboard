from .models import Task, EventCard
from django.contrib.auth.models import User
from bootstrap_modal_forms.forms import BSModalForm

class TaskForm(BSModalForm):
    class Meta:
        model = Task
        fields = ['description']

class EventCardForm(BSModalForm):
    class Meta:
        model = EventCard
        fields = ['event_name', 'small_description', 'big_description', 'date', 'room']
        
class EventJoinForm(BSModalForm):
    class Meta:
        model = EventCard
        fields = []

class TaskJoinForm(BSModalForm):
    class Meta:
        model = Task
        fields = []

class UserForm(BSModalForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
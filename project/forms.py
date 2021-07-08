from django import forms
from core.models import Habit


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ["name", "goal",]
from django import forms
from core.models import Habit, Record


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ["name", "goal", "amount"]




class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ["date", "performance", "amount"]
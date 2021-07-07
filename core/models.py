from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

class User(AbstractUser):
    def __str__(self):
        return self.username



### Habit class
class Habit(models.Model):
    created_date = models.DateField(default=date.today)
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="habits")
    goal = models.IntegerField()
    
    def __str__(self):
        return self.name

    


class Record (models.Model):
    date = models.DateField(null=True)
    performance = models.IntegerField(null=True)
    habit_name = models.ForeignKey(Habit, on_delete=models.CASCADE,
                               related_name="records", null=True)

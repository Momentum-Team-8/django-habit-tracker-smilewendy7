from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.db.models.constraints import UniqueConstraint

class User(AbstractUser):
    def __str__(self):
        return self.username



### Habit class
class Habit(models.Model):
    created_date = models.DateField(default=date.today)
    ## unique name
    name = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="habits",null=True)
    goal = models.IntegerField()
    amount = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

    


class Record (models.Model):
    date = models.DateField(null=True)
    performance = models.IntegerField(null=True)
    amount = models.CharField(max_length=20,null=True)
    habit_name = models.ForeignKey(Habit, on_delete=models.CASCADE,
                               related_name="records", null=True)

### unique record
    class Meta:
        constraints = [
            UniqueConstraint(fields=["habit_name", "date"], name="unique_record")
        ]

# habit_name_id is different for different user; user email?? 
    def __str__(self):
        return f"{self.date} {self.habit_name} {self.habit_name_id}"




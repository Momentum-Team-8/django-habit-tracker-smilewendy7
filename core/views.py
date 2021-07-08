from core.models import Habit
from django.shortcuts import redirect, render, get_object_or_404
from project.forms import HabitForm

# Create your views here.


## login /log out

## create habit /delete habit/ track habit --- (add record/ edit record/update records )/ 


### homepage
def homepage(request):
    if request.user.is_authenticated:
        return redirect(to="habit_list")

    return render(request, "habits/home.html")

## habit list
def habit_list(request):
    habits = Habit.objects.all()
    return render(request,  "habits/habit_list.html",
                  {"habits": habits})


## add habit 

def add_habit(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save()
            habit.save()
            habit.author = request.user
            habit.save()
            return redirect(to='habit_list')
    return render(request, "habits/add_habit.html", {"form": form})


## habit details
def show_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, "habits/show_habit.html", {"habit": habit})
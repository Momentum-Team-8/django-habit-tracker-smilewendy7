from core.models import Habit, Record
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Count


from project.forms import HabitForm, RecordForm

# Create your views here.


## login /log out

## create habit /delete habit/ track habit --- (add record/ edit record/update records )/ 


### homepage
def homepage(request):
    if request.user.is_authenticated:
        return redirect(to="habit_list")

    return render(request, "habits/home.html")

## habit list --- only the user's habits
def habit_list(request):
    user = request.user
    habits = Habit.objects.filter(author=user)
    return render(request,  "habits/habit_list.html",
                  {"habits": habits,
                  })


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

## delete habit 
def delete_habit(request, pk):
    habit = get_object_or_404(request.user.habits, pk=pk)

    if request.method == 'POST':
        habit.delete()
        return redirect(to='habit_list')

    return render(request, "habits/delete_habit.html",
                  {"habit": habit})



## habit details
def show_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    ## label: date
    labels = []

    ###data: performace
    data = []


    queryset = Record.objects.filter(habit_name_id=habit.id).order_by("date")
    for record in queryset:
        labels.append(str(record.date))
        data.append(record.performance)

    
    return render(request, "habits/show_habit.html",
        {
            "habit": habit, "record_form": RecordForm(),
            'labels': labels,
            'data': data,
            'queryset': queryset,
        },
    
    )


#### add record
def add_habit_record(request,pk):
    habit= get_object_or_404(request.user.habits, pk=pk)
    if request.method == "POST": 
        form = RecordForm(data=request.POST)
        if form.is_valid():
            habit_record = form.save(commit=False)
            habit_record.habit = habit
            habit_record.save()
            ### solve the id issue 
            habit_record.habit_name = habit
            habit_record.save()
            return redirect(to="show_habit", pk=habit.pk)
    else:
        form = RecordForm()

    return render(
        request, "habits/add_habit_record.html", {"form": form, "habit": habit}
    )


### edit record 

def edit_record(request, record_pk, id):
    habit= get_object_or_404(request.user.habits, id=id)
    habit_record = get_object_or_404(Record, pk=record_pk)
    if request.method == 'GET':
        form = RecordForm(instance=habit_record)
    else:
        form = RecordForm(data=request.POST, instance=habit_record)
        if form.is_valid():
            form.save()
            return redirect(to='show_habit', pk=habit.id)

    return render(request, "habits/edit_record.html", {
        "form": form,
        "habit_record": habit_record,
        "habit": habit
    })

from django.shortcuts import render,redirect
from .models import task
from .forms import create_task_form
from login.models import Users


def TodoView(request, email):
    if request.method == 'POST':
        return redirect('main:home', email=email)
    try:
        error = None
        user = Users.objects.get(email=email)
        username = f"{user.first_name} {user.last_name}"

    except Users.DoesNotExist:
        error = "User does not exist"
        username = None
        user = None
    context = {
        'user':user,
        'username': username,
        'error': error,
        'email': email,
    }
    return render(request, 'main.html', context)


def NotesView(request, email):
    if request.method == 'POST':
        if request.POST.get("home"):
            return redirect('main:home', email=email)
    try:
        user = Users.objects.get(email=email)
        error = None
        form = create_task_form(request.POST or None)
        if form.is_valid():
            note = form.cleaned_data['task_text']
            user = email 
            task.objects.create(task_text=note, user=user)
            form = create_task_form()

    except Users.DoesNotExist:
        error = "User does not exist"
        form = None
    
    notes = task.objects.filter(user=email).order_by('-date')
    print(error)
    context = {
        'form' : form,
        'notes': notes,
        'error': error,
        'email': email
    }
    return render(request, 'notes.html', context)


def DeleteView(request, email ,notes_id):
    obj = task.objects.get(id=notes_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('main:notes', email=email)
    context = {
        'note':obj
    }
    return render(request, 'delete_veiw.html', context)

def HomeView(request, email):
    if request.method == 'POST':
        if request.POST.get("notes"):
            return redirect('main:notes', email=email)
        if request.POST.get("todo"):
            return redirect('main:main', email=email)

    try:
        error = None
        user = Users.objects.get(email=email)
        username = f"{user.first_name} {user.last_name}"

    except Users.DoesNotExist:
        error = "User does not exist"
        user = None
        username = None

    return render(request, 'home_view.html', {'error':error, 'user':user, 'username':username, 'email':email})
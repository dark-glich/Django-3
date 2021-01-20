from django.shortcuts import render, redirect
from .models import Users
from .forms import login_form, signup_form 
def SignupView(request):
    form = login_form(request.POST or None)
    created, email = None, None
    
    if form.is_valid():
        obj, created = Users.objects.get_or_create(email=form.cleaned_data['email'])
        email = form.cleaned_data['email']
        if created == True:
            obj.delete()
            form.save()
            form = login_form()
            return redirect('main:home', email=email)

    context = {
        'form': form,
        'created':created, 
        'email':email
    }
    return render(request, 'signup.html', context)


def SigninView(request, *args, **kwargs):
    form = signup_form(request.POST or None)
    created, email = None, None
    if form.is_valid():
        email = form.cleaned_data['email']
        obj, created = Users.objects.get_or_create(email=email,password=form.cleaned_data['password'])
        if created == True:
            obj.delete()

        else:
            form = signup_form()
            return redirect('main:home', email=email)

    context={
        'form':form, 
        'created':created, 
        'email':email
    }
    return render(request, 'signup2.html', context)
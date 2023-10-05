from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import registerForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Welcome {username}, Your account is created.")
            return redirect('login')
        
    else:
        form = registerForm
    return render(request,'users/registers.html',{'form':form})

@login_required
def profilepage(request):
    return render(request,'users/profile.html')
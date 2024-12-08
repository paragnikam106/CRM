from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, AddRecord, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from .models import Tracking
from django.contrib import messages

# Create your views here.

def main(request):
    return render(request,'main.html')




def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account successfully created")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")

    context = {'form': form}
    return render(request, 'register.html', context=context)



def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request,user)
                messages.success(request, "You are Logged in")
                return redirect('tracking')
            else:
                messages.error(request,"Invalid username or password")
            
    context = {'form':form}
    return render(request,'login.html',context=context)

def logout(request):
    auth.logout(request)

    messages.success(request,'Logout successfully')
    return redirect('login')

def tracking(request):
    
    trc = Tracking.objects.all()
    context = {'trc':trc}
    return render(request,'tracking.html',context)


def add(request):
    form = AddRecord()

    if request.method == "POST":
        form = AddRecord(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request,'Your record added successfully')

            return redirect('tracking')
    context = {'form': form}
    return render(request,'addrecord.html',context=context)

def updaterecord(request,pk):
    trc = Tracking.objects.get(id=pk)
    form = UpdateRecordForm(instance=trc)

    if request.method=="POST":
        form = UpdateRecordForm(request.POST,instance=trc)

        if form.is_valid():
            form.save()
            messages.success(request,"Record updated successfully")

            return redirect('tracking')
    context = {'form':form}
    return render(request,'updaterecord.html',context)

def delete(request,pk):
    trc = Tracking.objects.get(id=pk)
    trc.delete()
    messages.success(request,'Record deleted successfully')

    return redirect('tracking')




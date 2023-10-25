from django.contrib import messages, auth
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from todoapp.models import Task


def new2(request):
    context= {'success': False}
    if request.method == "POST":
        title=request.POST['title']
        desc=request.POST['desc']
        date=request.POST['date']
        print(title,desc,date)
        ins=Task(taskTitle=title,taskDesc=desc,taskDate=date)
        ins.save()
        context= {'success': True}
    return render(request, "index.html",context)
def tasks(request):
    allTasks=Task.objects.all().values()
    context={'tasks':allTasks}
    return render(request, "tasks.html",context)
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect("login")
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect ("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
                return redirect ("register")
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)


                user.save()
                return redirect('login')
            # print("user created")
        else:
            messages.info(request,"password not matching")
            return redirect("register")

        return redirect('/')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
def delete(request, id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect("/tasks")
def update(request,id):
    task=Task.objects.get(id=id)
    template=loader.get_template('update.html')
    context={
        'task':Task,
    }
    return HttpResponse(template.render(context,request))
def updaterecord(request,id):
    title=request.POST['title']
    desc=request.POST['desc']
    date=request.POST['date']
    task=Task.objects.get(id=id)
    task.taskTitle=title
    task.taskDesc=desc
    task.taskDate=date
    task.save()
    return HttpResponse(reverse('index'))


               

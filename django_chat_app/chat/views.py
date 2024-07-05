from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Chat, Message

@login_required(login_url='/login/')

def index(request):
    if request.method == 'POST':
        chat = Chat.objects.get(id=1)
        Message.objects.create(
            chat = chat,
            text = request.POST['textmessage'],
            author = request.user,
            receiver = request.user
        )
    chatMessages = Message.objects.filter(chat__id = 1)
    return render(request, 'chat/index.html', {'messages' : chatMessages})

def login_view(request):
    redirectRout = request.GET.get('next')
    if request.method == 'POST':
        user = authenticate(username= request.POST['username'], password= request.POST['password'])
        if user:
            login(request, user)
            return redirect('/chat/')
        else:
            return render(request, 'auth/login.html', {'wrongUser': True, 'redirectRout': redirectRout})                
        
    return render(request, 'auth/login.html', {'redirectRout': redirectRout})

def signin_view(request):
   redirectRout = request.GET.get('next')
   if request.method == 'POST':
    name = request.POST['username']
    mail = request.POST['mail']
    password = request.POST['password']
    user = User.objects.create_user(name, mail, password)
    user.last_name = "Lennon"
    user.save()
    if user:
        login(request, user)
        return redirect('/chat/')
   return render(request, 'signin/signin.html', {'redirectRout': redirectRout}) 
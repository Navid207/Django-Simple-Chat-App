from django.shortcuts import render
from .models import Chat, Message

def index(request):
    if request.method == 'POST':
        print('Received data: '  + request.POST['textmessage'])
        chat = Chat.objects.get(id=1)
        Message.objects.create(
            chat = chat,
            text = request.POST['textmessage'],
            author = request.user,
            receiver = request.user
        )
        chatMessages = Message.objects.filter(chat__id = 1)
    return render(request, 'chat/index.html', {'messages' : chatMessages})


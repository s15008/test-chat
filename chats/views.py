from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.core import serializers
from .models import Message, Board, User

import json
from datetime import datetime

def index(request, board_id):
    print('index() board_id', board_id)
    message_list = Message.objects.filter(board_id__id=board_id).order_by('-pub_date')

    message_list[0]
    context = {'message_list': message_list}
    return render(request, 'chats/index.html', context)

def get_message(request, board_id):
    '''更新分のメッセージを送信
    '''
    if request.method == 'POST':
        print('get_message() board_id', board_id)
        latest_message_id = request.POST.get('latest_message_id')
        lmpdt = request.POST.get('latest_message_pub_date')
        latest_message_pub_date = datetime.strptime(lmpdt, Message.DATETIME_FORMAT)
        updated_message_list = []
        updated_message_list = Message.objects\
            .filter(board_id__id=board_id)\
            .filter(pub_date__gt=latest_message_pub_date)\
            .exclude(id=latest_message_id)

        data = []
        for message in updated_message_list:
            data.append({'id': message.id,
                'user_name': message.user_id.user_name,
                'message': message.message,
                'pub_date': message.get_formated_pub_date()})
        #json.dumps(data)
        #data = serializers.serialize("json", data)
        #print(updated_message_list)
        #print(data)
        return JsonResponse({'data': data}, safe=False)

    return HttpResponse('failed', content_type='text/plain')

def post_message(request, board_id):
    '''メッセージをDBに追加
    '''
    if request.method == 'POST':
        print(request.POST.get('board_id'))
        board = Board.objects.get(id=request.POST.get('board_id'))
        user = User.objects.get(user_id=request.POST.get('user_id'))
        text = request.POST.get('text')
        pub_date = timezone.now()

        mess = Message(board_id=board, user_id=user, message=text, pub_date=pub_date)
        mess.save()

        return HttpResponse('successful', content_type="text/plain")

    return HttpResponse('failed', content_type='text/plain')

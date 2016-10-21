from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import information

@csrf_exempt
def postNewInfo(request):
    if request.method == 'POST':
        tag_id = request.POST['tag_id']
        sender_id = request.POST['sender_id']

        reply = {}

        try:
            newInfo = information.objects.create(tag_id=tag_id, sender_id=sender_id)
            print(newInfo)
            newInfo.save()
            reply['result'] = "ok"
            print('Salvo')
        except Exception as e:
            reply['result'] = "Error while saving data to database"

        return JsonResponse(reply)
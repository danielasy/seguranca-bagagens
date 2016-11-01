from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Passageiro,Bagagem
from datetime import datetime
from pprint import pprint

'''
GET     /passageiros
    lista todos os passageiros
POST    /passageiros
    cria novo passageiro
GET     /passageiros/<documento>
    lista passageiro com documento = <documento>
GET     /passageiros/<documento>/bagagens
    lista todas as bagagens do passageiro com documento = <documento>
POST    /passageiros/<documento>/bagagens
    cria nova bagagem para passageiro com documento = <documento>

GET     /bagagens
    lista todas as bagagens

GET     /tags
    lista todas as tags

GET     /leituras
    lista todas as leituras de tags
POST    /leituras
    cria nova leitura de tag
'''

@csrf_exempt
def passageiros(request):
    if request.method == 'GET':
        result = Passageiro.objects()
        return HttpResponse(result.to_json(), content_type="application/json")
    if request.method == 'POST':
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        data_nascimento = request.POST['data_nascimento']
        documento = request.POST['documento']
        nacionalidade = request.POST['nacionalidade']

        reply = {}

        try:
            passageiro = Passageiro.objects.create(nome=nome, sobrenome=sobrenome, data_nascimento=datetime.strptime(data_nascimento, '%d/%m/%Y'), documento=documento, nacionalidade=nacionalidade)
            passageiro.save()
            reply['result'] = "ok"
        except Exception as e:
            reply['result'] = "Error while saving data to database"

        return JsonResponse(reply)

@csrf_exempt
def bagagens(request, documento):
    if request.method == 'GET':
        result = Bagagem.objects(documento=documento)
        return HttpResponse(result.to_json(), content_type="application/json")
    if request.method == 'POST':
        localizacao = request.POST['localizacao']
        peso = request.POST['peso']

        reply = {}

        try:
            bagagem = Bagagem(documento=documento,localizacao=localizacao,peso=peso)
            bagagem.save()
            reply['result'] = "ok"
        except Exception as e:
            reply['result'] = "Error while saving data to database"

        return JsonResponse(reply)

# @csrf_exempt
# def leituras(request):
#     if request.method == 'POST':
#         tag_id = request.POST['tag_id']
#         sender_id = request.POST['sender_id']

#         reply = {}

#         try:
#             newInfo = information.objects.create(tag_id=tag_id, sender_id=sender_id)
#             newInfo.save()
#             reply['result'] = "ok"
#         except Exception as e:
#             reply['result'] = "Error while saving data to database"

#         return JsonResponse(reply)
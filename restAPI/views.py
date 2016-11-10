from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Passageiro,Bagagem,Tag,Leitura
from datetime import datetime
import json
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
POST    /tags
    cria nova tag
GET     /tags/<tag_id>
    lista passageiro ou bagagem relacionada a tag

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
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        data_nascimento = request.POST.get('nascimento')
        documento = request.POST.get('documento')
        nacionalidade = request.POST.get('nacionalidade')
        tag = request.POST.get('tag')

        reply = {}

        try:
            passageiro = Passageiro.objects.create(nome=nome, sobrenome=sobrenome, data_nascimento=datetime.strptime(data_nascimento, '%d/%m/%Y'), documento=documento, nacionalidade=nacionalidade, tag_id=tag)
            passageiro.save()
            reply['result'] = "ok"
        except Exception as e:
            reply['result'] = "Error while saving data to database"

        return JsonResponse(reply)

@csrf_exempt
def passageiro(request, documento):
    if request.method == 'GET':
        result = Passageiro.objects(documento=documento)
        return HttpResponse(result.to_json(), content_type="application/json")

@csrf_exempt
def bagagens(request):
    if request.method == 'GET':
        result = Bagagem.objects()
        return HttpResponse(result.to_json(), content_type="application/json")

@csrf_exempt
def passageiro_bagagens(request, documento):
    if request.method == 'GET':
        result = Bagagem.objects(documento=documento)
        return HttpResponse(result.to_json(), content_type="application/json")
    if request.method == 'POST':
        localizacao = request.POST.get('localizacao')
        peso = request.POST.get('peso')
        tag_id = request.POST.get('tag_id')

        reply = {}

        try:
            bagagem = Bagagem(documento=documento,localizacao=localizacao,peso=peso, tag_id=tag_id)
            bagagem.save()
            reply['result'] = "ok"
        except Exception as e:
            reply['result'] = "Error while saving data to database"

        return JsonResponse(reply)

@csrf_exempt
def localizacao(request):
    if request.method == 'POST':
        localizacao = request.POST.get('localizacao')
        documento = request.POST.get('documento')

        reply = {}

        try:
            result = Bagagem.objects(documento=documento)
            for k in result:
                k.update(set__localizacao=str(localizacao))
            reply['result'] = "Ok"
        except Exception as e:
            reply['result'] = "Error while saving data to database"

        return JsonResponse(reply)

@csrf_exempt
def tags(request):
    if request.method == 'GET':
        result = Tag.objects()
        return HttpResponse(result.to_json(), content_type="application/json")
    if request.method == 'POST':
        tag_id = request.POST.get('tag_id')

        reply = {}

        try:
            tag = Tag(tag_id=tag_id)
            tag.save()
            reply['result'] = "Ok"
        except Exception as e:
            reply['result'] = "Error while saving data to database"

        return JsonResponse(reply)

@csrf_exempt
def tags_identificacao(request, tag_id):
    if request.method == 'GET':
        result = Passageiro.objects(tag_id=tag_id)
        if not result:
            result = Bagagem.objects(tag_id=tag_id)
        return HttpResponse(result.to_json(), content_type="application/json")

@csrf_exempt
def leituras(request):
    if request.method == 'POST':
        tag_id = request.POST['tag_id']
        sender_id = request.POST['sender_id']

        reply = {}

        try:
            leitura = Leitura.objects.create(tag_id=tag_id, sender_id=sender_id)
            leitura.save()
            reply['result'] = "ok"
        except Exception as e:
            reply['result'] = "Error while saving data to database"

        return JsonResponse(reply)

    else:
        json_result = []
        tags = Tag.objects()
        for tag in tags:
            passageiros = Passageiro.objects(tag_id=tag.tag_id)
            for passageiro in passageiros:
                each = {'tipo': 'passageiro',
                'nome': passageiro.nome,
                'documento': passageiro.documento,
                'tag': tag.tag_id}

                json_result.append(each)

            bagagens = Bagagem.objects(tag_id=tag.tag_id)
            for bagagem in bagagens:
                each = {'tipo': 'bagagem',
                'localizacao': bagagem.localizacao,
                'documento': bagagem.documento,
                'tag': tag.tag_id}

                json_result.append(each)

        return HttpResponse(json.dumps(json_result), content_type="application/json")

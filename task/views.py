from django.shortcuts import render
from django.http import HttpResponse

class tarefa(object):
    def __init__(self, titulo, data):
        self.titulo=titulo
        self.data=data
    def __str__(self):
        return self.titulo

def home(request):
    return HttpResponse("Olá")
def sobre(request):
    return HttpResponse("Mário Lúccio")
def tarefa(request):
    return HttpResponse("Tarefa"+str(ano)+"/"+str(mes))

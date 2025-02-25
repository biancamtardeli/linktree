from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get (self, request):
        links = Link.objects.all()
        perfil = Perfil.objects.first()
        redes_sociais = RedeSocial.objects.all()
        icones = Icone.objects.first()
        return render(request, 'index.html', {'links': links, 'perfil': perfil, 'redes_sociais': redes_sociais, 'icone': icones})
    def post(self, request):
        pass

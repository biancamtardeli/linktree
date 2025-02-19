from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get (self, request):
        links = Link.objects.all()
        perfil = Perfil.objects.first()
        redes_sociais = RedeSocial.objects.all()
        subtitulo = Subtitulo.objects.first()
        return render(request, 'index.html', {'links': links, 'perfil': perfil, 'redes_sociais': redes_sociais, 'subtitulo': subtitulo})
    def post(self, request):
        pass

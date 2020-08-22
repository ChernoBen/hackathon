from django.forms import ModelForm
from .models import Conteudo



class ConteudoForm(ModelForm):
    class Meta:
        model = Conteudo
        fields = ['titulo','imagem','tel','descricao','cep',]




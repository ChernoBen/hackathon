from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Conteudo
from .forms import ConteudoForm

def home(request):
    conteudos = Conteudo.objects.all()
    return render(request,'homepage/home.html',{'conteudos': conteudos})

def sou_mei(request):
    return render(request,'soumei.html')


def post_new(request):
    
    if request.method == "POST":
        form = ConteudoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.save()
            return redirect('core/post_detail',pk=post.pk)
    else:
        form = ConteudoForm
        return render(request,'core/post_edit.html',{'form': form})


def post_edit(request,pk):
    post = get_object_or_404(Conteudo,pk=pk)
    if request.method == "POST":
        form = ConteudoForm(request.POST,instance=post)
        post = form.save(commit=False)
        post.usuario = request.user()
        post.save()
        return redirect ('home',pk=post.pk)
    else:
        form = ConteudoForm(instance=post)
        return render(request,'core/post_edit.html',{'form': form})





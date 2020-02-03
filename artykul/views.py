from django.shortcuts import render, get_object_or_404, redirect
from artykul.models import Artykul
from django.db.models import Q
from artykul.forms import ArtykulSearchForm, ArtykulForm
from django.urls.base import reverse_lazy

def artykul_create(request):
    form = ArtykulForm()
    if request.POST:
        form = ArtykulForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('artykul-list'))
    return render(request, template_name='artykul/artykul_create.html', context={'form':form},)

def artykuly(request):
    form = ArtykulSearchForm()
    pharse = ""
    if request.POST:
        form = ArtykulSearchForm(request.POST)
        if form.is_valid():
            pharse = form.cleaned_data.get("pharse", "artykul-list")
            
    lista_artykulow = Artykul.objects.filter(Q(tytul__icontains=pharse)
                                             |Q(autor__icontains=pharse)
                                             |Q(tresc__icontains=pharse))
    return render(request,
                  template_name='artykul/artykuly.html',
                  context={'artykuly':lista_artykulow,
                           "form":form})
    
def artykul(request, pk):
    artykul = get_object_or_404(Artykul, pk=pk)
    return render(request,
                  template_name='artykul/artykul.html',
                  context={'artykul':artykul,})
    
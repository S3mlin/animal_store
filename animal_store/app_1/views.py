from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Animal
from .forms import EntryForm
from django.core.exceptions import ObjectDoesNotExist
from taggit.models import Tag
from django.core.paginator import Paginator
from .serializers import AnimalSerializer
from rest_framework.generics import ListAPIView

def index(request):
    all_tags = Tag.objects.all()
    pagination = Paginator(Animal.objects.order_by('id'), 8)
    page_number = request.GET.get('page')
    animal_list = pagination.get_page(page_number)
    lower_num = animal_list.number - 1
    higher_num = animal_list.number + 1
    context = {'all_tags' : all_tags, 'animal_list': animal_list, 'lower_num' : lower_num, 'higher_num' : higher_num}
    return render(request, 'animal_store/index.html', context)

def entry(request):
    form = EntryForm()

    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/animal-store/')

    context = {'form' : form}
    return render(request, 'animal_store/entry.html', context)

def delete(request, animal_id):
    if not animal_id.isdigit():
        return redirect('/animal-store/')
        
    try:
        animal = Animal.objects.get(id=animal_id)
        animal.delete()
        return redirect('/animal-store/')
        
    except ObjectDoesNotExist:
        return redirect('/animal-store/')
        

def edit(request, animal_id):
    if not animal_id.isdigit():
        return redirect('/animal-store/')
    
    try:
        animal = Animal.objects.get(id=animal_id)
        form = EntryForm(initial= {'animalName' : animal.animalName, 'imageURl' : animal.imageURl,
                     'category' : animal.category, 'status' : animal.status}, instance = animal)

        if request.method == 'POST':
            form = EntryForm(request.POST, request.FILES, instance=animal)
            if form.is_valid():
                form.save()
                return redirect('/animal-store/')
    
    except ObjectDoesNotExist:
        return redirect('/animal-store/')
    
    if request.method == 'GET':
        context = {'form' : form}
        return render(request, 'animal_store/edit.html', context)

def delete_tag(request, tag_id):
    if not tag_id.isdigit():
        return redirect('/animal-store/')

    try:
        tag = Tag.objects.get(id=tag_id)
        tag.delete()
        return redirect('/animal-store/')
    
    except ObjectDoesNotExist:
        return redirect('/animal-store/')

def selected_tag(request, tag_id):
    if not tag_id.isdigit():
        return redirect('/animal-store/')
    
    try:
        Tag.objects.get(id=tag_id)
        tag = Tag.objects.filter(id=tag_id)
        tag1 = list(tag)
        all_tags = Tag.objects.all()
        pagination = Paginator(Animal.objects.filter(tags__name__in=tag1), 8)
        page_number = request.GET.get('page')
        animal_list = pagination.get_page(page_number)
        lower_num = animal_list.number - 1
        higher_num = animal_list.number + 1
        context = {'all_tags' : all_tags, 'animal_list': animal_list, 'lower_num' : lower_num, 'higher_num' : higher_num}
        return render(request, 'animal_store/index.html', context)

    except ObjectDoesNotExist:
        return redirect('/animal-store/')

class AnimalListAPIView(ListAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    

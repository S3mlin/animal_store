from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from app_1.models import Animal


@api_view(['POST'])
@parser_classes([JSONParser])
def entry(request, format=None):
    """
    A view that can accept POST requests with JSON content.
    """
    data = None
    data = request.data
    
    animal_name = data.get('animalName')
    animal_category = data.get('category')
    animal_imageURL = data.get('imageURl')
    animal_status = data.get('status')
    if None in [animal_name, animal_category, animal_imageURL, animal_status]:
        return Response({'msg': 'wrong_data'})
    animal = Animal.objects.create(animalName=animal_name, category=animal_category, 
                    imageURl=animal_imageURL, status= animal_status)
    animal.save()
    return Response({'msg': 'successfully created animal', 'id': str(animal.id)})


@api_view(['POST'])
@parser_classes([JSONParser])
def edit(request, format=None):
    """
    A view that can accept POST requests with JSON content.
    """
    data = None
    data = request.data
    
    animal_id = data.get('id')
    animal_name = data.get('animalName')
    animal_category = data.get('category')
    animal_imageURL = data.get('imageURl')
    animal_status = data.get('status')
    if None in [animal_id, animal_name, animal_category, animal_imageURL, animal_status]:
        return Response({'msg': 'wrong_data'})
    animal = Animal.objects.get(id=animal_id)
    animal.animalName=animal_name
    animal.category=animal_category
    animal.imageURl=animal_imageURL
    animal.status=animal_status
    animal.save()
    return Response({'msg': 'successfully edited animal', 'id': str(animal.id)})

@api_view(['POST'])
@parser_classes([JSONParser])
def delete(request, format=None):
    """
    A view that can accept POST requests with JSON content.
    """
    data = None
    data = request.data
    
    animal_id = data.get('id')
    if None in [animal_id]:
        return Response({'msg': 'wrong_data'})
    animal = Animal.objects.get(id=animal_id)
    animal.delete()
    return Response({'msg': 'successfully deleted animal'})


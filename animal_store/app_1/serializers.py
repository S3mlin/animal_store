from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from .models import Animal


class AnimalSerializer(TaggitSerializer ,serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Animal
        fields =('id', 'animalName', 'category', 'imageURl', 'status', 'image', 'tags')
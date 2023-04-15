from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from books.models import *



# class BookModel:
#     def __init__(self, title, description):
#         self.title = title
#         self.description = description




class BooksSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    author = serializers.CharField(max_length=255)
    pub_date = serializers.IntegerField(max_value=9999)
    genre_id = serializers.IntegerField()
    is_published = serializers.BooleanField(default=True)
    slug = serializers.SlugField()
    image = serializers.ImageField()


    def create(self, validated_data):
        return Books.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.author = validated_data.get("author", instance.author)
        instance.pub_date = validated_data.get("pub_date", instance.pub_date)
        instance.genre_id = validated_data.get("genre_id", instance.genre_id)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.image = validated_data.get("image", instance.image)

        return instance



# def encode():
#     model = BookModel('title', 'ghjkl')
#     model_sr = BooksSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

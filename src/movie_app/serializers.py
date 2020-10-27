from rest_framework import serializers

from .models import Actor, Director, Movie

class ActorObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        feilds = ('id', 'name')

class MovieSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField(many=False)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'actor', 'director')

class ActorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)
    
    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies')

class DirectorSerializer(serializers.ModelSerializer):
    actors = ActorObjectSerializer(many=True)
    
    class Meta:
        model = Director
        fields = ('id', 'name', 'actors')


##see docs many to many related field
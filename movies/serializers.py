from rest_framework import serializers

from movies.models import Artist, Movie


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('first_name', 'last_name')


class MovieSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('title', 'synopsis', 'year', 'artists')
from rest_framework import serializers

from movies.models import Artist, Movie


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('first_name', 'last_name')


class MovieSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('title', 'synopsis', 'year', 'artists')

    def create(self, validated_data):
        artists_data = validated_data.pop('artists')
        movie = Movie.objects.create(**validated_data)
        artists_list = []
        for artist_data in artists_data:
            artist, created = Artist.objects.get_or_create(**artist_data)
            movie.artists.add(artist)
        movie.save()
        return movie
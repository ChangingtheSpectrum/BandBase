from rest_framework import serializers
from bandAPI.models import Band, Album, Song

class BandSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializes bands"""

	class Meta:
		model = Band
		fields = ('id', 'url', 'name', 'origin', 'date_formed')

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Album
		fields = ('title', 'date_released', 'run_time')

	def create(self, validated_data):
		album = Album (
			title = validated_data['title'],
		)

		album.save()

		return album

class SongSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Song
		fields = ('title', 'length')

	def create(self, validated_data):
		song = Song (
			title = validated_data['title'],
		)

		song.save()

		return song


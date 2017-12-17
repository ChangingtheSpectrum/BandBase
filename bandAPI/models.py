from django.db import models

class Band(models.Model):
	name = models.CharField(max_length=100, null=False)
	origin = models.CharField(max_length=100, null=True)
	date_formed = models.DateField()

	def __str__(self):
		return self.name

class Album(models.Model):
	title = models.CharField(max_length=100, null=False)
	date_released = models.DateField()
	run_time = models.TimeField()
	band = models.ForeignKey(
		Band,
		on_delete=models.CASCADE,
	)

	def __str__(self):
		return self.title

class Song(models.Model):
	title = models.CharField(max_length=100, null=False)
	length = models.TimeField()
	album = models.ForeignKey(
		'Album',
		on_delete=models.CASCADE,
	)

	def __str__(self):
		return self.title
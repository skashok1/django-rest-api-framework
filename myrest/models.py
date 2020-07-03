from django.db import models

class Hero(models.Model):
	#owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE, default ="", Null =True)
	name = models.CharField(max_length=60)
	alias = models.CharField(max_length=60)

	def __str__(self):
		return self.name


from django.db import models
from django.db import models

# Create your models here.
from django.db import models

class Journalist(models.Model):
    name = models.CharField(max_length=200)
    j_id = models.IntegerField()

    section = models.CharField(max_length=400)

    def __str__(self) :
        return f'{self.name} whom id number {self.j_id} and work in {self.section} section'

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Journalist, on_delete=models.CASCADE)
    body = models.TextField()
# Create your models here.

from django.contrib import admin
from .models import Journalist, Post
# Register your models here.
admin.site.register(Post)
admin.site.register(Journalist)


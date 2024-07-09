from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    auther = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_index=True)
    created = models.DateField(auto_now_add=True)

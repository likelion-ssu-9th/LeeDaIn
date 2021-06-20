from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to = "webstagram/", blank=True, null=True)
    writer = models.ForeignKey(User, related_name="post", on_delete=CASCADE, default='')
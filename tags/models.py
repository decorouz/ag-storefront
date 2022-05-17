from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)


class TagItem(models.Model):
    # Type -> Product, Video, Project, Blog Post, Course
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    target_ct = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # content type
    target_id = models.PositiveIntegerField()  # object id
    target = GenericForeignKey("target_ct", "target_id")  # content object

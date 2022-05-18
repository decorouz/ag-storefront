from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class TaggedItemManager(models.Manager):
    def get_tag_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)

        return TaggedItem.objects.select_related("tag").filter(
            target_ct=content_type, target_id=obj_id
        )


# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # Type -> Product, Video, Project, Blog Post, Course
    objects = TaggedItemManager()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    target_ct = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # content type
    target_id = models.PositiveIntegerField()  # object id
    target = GenericForeignKey("target_ct", "target_id")  # content object

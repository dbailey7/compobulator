from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Mp_archetype(models.Model):
    id1 = models.CharField(primary_key=True, max_length=64, unique=True, blank=False)
    gid = models.UUIDField(default=uuid.uuid4)
    crtdate = models.DateField()
    crtby = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.crtby + '-' + str(self.crtdate) + '-' + self.id

    def get_absolute_url(self):
        return reverse("compobulator_app:detail", kwargs={'pk':self.pk})

class Mp_element(models.Model):
    fldname = models.CharField(primary_key=True, max_length=64, unique=True, blank=False)
    fldtype = models.CharField(max_length=64)
    gid = models.UUIDField(default=uuid.uuid4)
    archetypeid = models.UUIDField(default=uuid.uuid4)
    crtdate = models.DateField()
    crtby = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.crtby + '-' + str(self.crtdate) + '-' + self.id

    def get_absolute_url(self):
        return reverse("compobulator_app:url_elem_detail", kwargs={'pk':self.pk})

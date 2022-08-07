import uuid
from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Relationship(models.TextChoices):
        FRIEND = "Friend"
        FAMILY = "Family"
        WORK = "Work"
        OTHER = "Other"
        

class Contact(BaseModel):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone_number= models.CharField(max_length=20, blank=True, null=True)
    relation_ship = models.CharField(
        max_length=50,
        choices=Relationship.choices,
        default=Relationship.OTHER)

    def __str__(self):
        return f'{self.first_name} - {self.created_by.username}'

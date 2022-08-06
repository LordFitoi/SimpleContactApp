import uuid
from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name} - {self.created_by.username}'


class Relationship(models.TextChoices):
        FRIEND = "Friend"
        FAMILY = "Family"
        WORK = "Work"
        OTHER = "Other"
        

class Contact(BaseModel):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number= models.CharField(max_length=20)
    relation_ship = models.CharField(
        max_length=50,
        choices=Relationship.choices,
        default=Relationship.OTHER)
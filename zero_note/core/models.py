import uuid
from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50, blank=True, null=True)


class Budget(BaseModel):
    amount = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=125, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
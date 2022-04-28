import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


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


class Categories(models.TextChoices):
    HOUSING = "Housing"
    TRANSPORTATION = "Transportation"
    FOOD = "Food"
    UTILITIES = "Utilities"
    INSURANCE = "Insurance"
    HEALTHCARE = "Healthcare"
    DEBT = "Debt"
    PERSONAL = "Personal"
    ENTERTAINMENT = "Entertainment"
    MISCELLANEOUS = "Miscellaneous"


class BudgetSheet(BaseModel):
    date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.MISCELLANEOUS)

    @classmethod
    def get_default_pk(cls):
        user = User.objects.get_or_create(username="Guest")[0]
        sheet = cls.objects.get_or_create(
            name="Sheet", created_by=user)[0]

        return sheet.pk


class Budget(BaseModel):
    amount = models.FloatField(blank=True, null=True)
    category = models.CharField(
        max_length=50,
        choices=Categories.choices,
        default=Categories.MISCELLANEOUS)
        
    sheet = models.ForeignKey(
        BudgetSheet,
        on_delete=models.CASCADE,
        default=BudgetSheet.get_default_pk)

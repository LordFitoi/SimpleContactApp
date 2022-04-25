from .models import Budget, BudgetSheet
from rest_framework import serializers


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = "__all__"


class BudgetSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetSheet
        fields = "__all__"


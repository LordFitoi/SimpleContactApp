from .models import Budget, BudgetSheet
from .serializers import BudgetSerializer, BudgetSheetSerializer
from rest_framework import viewsets


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class BudgetSheetViewSet(viewsets.ModelViewSet):
    queryset = BudgetSheet.objects.all()
    serializer_class = BudgetSheetSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Budget, BudgetSheet
from .serializers import BudgetSerializer, BudgetSheetSerializer


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sheet', 'category']
    
    def create(self, request, *args, **kwargs):
        request.data["created_by"] = self.request.user 
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        print(serializer.errors)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return super().create(self, request, *args, **kwargs)


class BudgetSheetViewSet(viewsets.ModelViewSet):
    queryset = BudgetSheet.objects.all()
    serializer_class = BudgetSheetSerializer
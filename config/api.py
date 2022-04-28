from django.urls import path, include
from rest_framework.routers import DefaultRouter
from zero_note.core.viewsets import BudgetViewSet, BudgetSheetViewSet

router = DefaultRouter()
router.register("budgets", BudgetViewSet)
router.register("budgets-sheets", BudgetSheetViewSet)


app_name = "api"
urlpatterns = router.urls
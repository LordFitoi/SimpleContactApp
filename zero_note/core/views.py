from re import template
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "pages/home.html"


class BudgetView(TemplateView):
    template_name = "pages/budget.html"

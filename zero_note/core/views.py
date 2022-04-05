from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse("budget"))

class BudgetView(TemplateView):
    template_name = "pages/budget.html"

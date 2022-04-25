from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import BudgetSheet
from .serializers import BudgetSheetSerializer
from .forms import CreateBudgetSheetForm


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse("budget"))


class BudgetView(LoginRequiredMixin, FormView):
    template_name = "pages/budget.html"
    model = BudgetSheet
    serializer = BudgetSheetSerializer
    form_class = CreateBudgetSheetForm
    
    def get_success_url(self) -> str:
        return reverse("budget")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.model.objects.filter(
            created_by = self.request.user
        )
        serializer = self.serializer(queryset, many=True)
        context["sheets"] = [
            dict(item) for item in serializer.data
        ]

        return context

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        cleaned_data["created_by"] = self.request.user.id
        serializer = self.serializer(data=cleaned_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return super().form_valid(form)
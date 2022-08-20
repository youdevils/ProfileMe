from django.shortcuts import render
from website.forms import PersonForm

from django.views.generic import (
    TemplateView,
    # CreateView,
    FormView,
    # ListView,
    # UpdateView,
    # RedirectView,
)

class WhoAmI(FormView):

    template_name = "index.html"
    form_class = PersonForm    
    success_url = "results/"

    def form_valid(self, form):
        return super().form_valid(form)

class Results(TemplateView):

    template_name = "results.html"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return render(request, self.template_name, context=context)

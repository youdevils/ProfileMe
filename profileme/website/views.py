from django.shortcuts import render

from django.views.generic import (
    TemplateView,
    # CreateView,
    # FormView,
    # ListView,
    # UpdateView,
    # RedirectView,
)


class Home(TemplateView):

    # Set Template
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        # Process Year Selector Use | Update Dashboard Year

        # Package Template Data
        context = super().get_context_data(**kwargs)
        # context.update() Add Custom Context Data
        return render(request, self.template_name, context=context)

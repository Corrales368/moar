from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class AdminHomeView(TemplateView):
    template_name = "administration/home/home.html"


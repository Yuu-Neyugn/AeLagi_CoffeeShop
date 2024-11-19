from django.views.generic import TemplateView
from .models import AboutUs, OurTeam

class IndexView(TemplateView):
    template_name = "home/index.html"

class AboutUsView(TemplateView):
    template_name = "home/about-us.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["AboutUs"] = AboutUs.objects.all()
        context["OurTeam"] = OurTeam.objects.all()

        return context
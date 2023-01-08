from django.views.generic import TemplateView


class Contacts(TemplateView):
    template_name = 'footer/contacts.html'


class FollowUs(TemplateView):
    template_name = 'footer/follow_us.html'


class AboutUs(TemplateView):
    template_name = 'footer/about_us.html'


class Sponsors(TemplateView):
    template_name = 'footer/sponsors.html'


class FAQ(TemplateView):
    template_name = 'footer/FAQ.html'

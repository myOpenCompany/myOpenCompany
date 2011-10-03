from django.views.generic.simple import direct_to_template

def home_view(request):
    return direct_to_template(request, template="home.html")
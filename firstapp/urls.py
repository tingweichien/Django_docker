from django.urls import path
from . import views
from .models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="home.html",
)

urlpatterns = [
    path('index/', views.index, name='index'),
    path("hello_view/", views.hello_view, name='hello_view'),
    path("", home_list_view, name="home"),
    #path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log",)
]


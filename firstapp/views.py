from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .forms import LogMessageForm
from .models import LogMessage
from django.shortcuts import redirect
from django.views.generic import ListView


# Create your views here.
def index(request):
    return HttpResponse("Hello world~ you are at firstapp index function.")

# Create your views here.
def hello_view(request):
    return render(
        request,
        'hello_django.html',
        {
        'name' : "Tim",
        'data' : "Hello Django",
        'now' : datetime.now(),
        }
    )

# Replace the existing home function with the one below
def home(request):
    return render(request, "home.html")

class HomeListView(ListView):
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context



def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")


def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(
                    request,
                    "log_message.html",
                    {"form": form},
                    )



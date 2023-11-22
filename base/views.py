from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {"id": 1, "name": "Let's run python!"},
    {"id": 2, "name": "Design with me!"},
    {"id": 3, "name": "Frontend Developer!"},
]


# Create your views here.
def home(request):
    context = {"rooms": rooms}
    return render(request, "home.html", context)
    # return render(request, "home.html", {"rooms": rooms})


def room(request):
    return render(request, "room.html")

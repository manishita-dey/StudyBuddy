from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# rooms = [
#     {"id": 1, "name": "Let's run python!"},
#     {"id": 2, "name": "Design with me!"},
#     {"id": 3, "name": "Frontend Developer!"},
# ]


# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)
    # return render(request, "home.html", {"rooms": rooms})


def room(request, pk):
    # room = None
    # for i in rooms:
    #     if i["id"] == int(pk):
    #         room = i
    room = Room.objects.get(id=pk)
    context = {"room": room}
    return render(request, "base/room.html", context)

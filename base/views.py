from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

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


def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "base/room_form.html", context)


def update_room(request, pk):
    room = Room.objects.get(pk=pk)
    form = RoomForm(instance=room)  # form will be pre filled with room values

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "base/room_form.html", context)


def delete_room(request, pk):
    room = Room.objects.get(pk=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj": room})

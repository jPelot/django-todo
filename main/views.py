from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout

from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

from .models import Item, Course
# Create your views here.



def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    user = request.user
    if request.method == "POST":
        if not "course" in  request.POST:
            return HttpResponseRedirect(reverse("index"))
        
        course = request.POST["course"]
        due = request.POST["due"]
        description = request.POST["description"]
        try:
            item = Item.objects.create(description=description, course=user.courses.filter(name=course).first(), user=user, due=due)
        except ValidationError:
            pass
        return HttpResponseRedirect(reverse("index"))
    return render(request, "main/index.html", {
        "user":user,
        "courses":user.courses.all(),
        "items":user.items.order_by('due').all()
    })



def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,password=password)
        if user is not None:
            dj_login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "main/login.html", {
                "message" : "Invalid credentials."
            })
    return render(request, "main/login.html")



def new(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username, "", password)
        dj_login(request, user)
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "main/new.html")



def logout(request):
    if request.user.is_authenticated:
        dj_logout(request)
    return HttpResponseRedirect(reverse("index"))



def remove(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    item = request.user.items.filter(id=id).first()
    if item:
        item.delete()
    print(id)
    return HttpResponseRedirect(reverse("index"))



def classes(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    user = request.user
    if request.method == "POST":
        name = request.POST["name"]
        short = request.POST["short"]
        item = Course.objects.create(user=user, name=name, short=short)
        return HttpResponseRedirect(reverse("classes"))
    
    return render(request, "main/courses.html", {
        "user":user,
        "courses":user.courses.all(),
        "items":user.items.all()
    })



def remove_class(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    course = request.user.courses.filter(id=id).first()
    if course:
        course.delete()
    return HttpResponseRedirect(reverse("classes"))
    
from django.shortcuts import render, redirect
from .models import Name, Topping
from .forms import NameForm, CommentForm
from .models import Name

# Create your views here.

# when a URL request matches the pattern we just defined,
# Django looks for a function called inex() in the views.py file


def index(request):
    """the homepage for pizzeria"""
    return render(request, "pizzerias/index.html")


def names(request):
    n = Name.objects.order_by("date_added")
    # A context is a dictionary in whicht he keys are names we'll use
    # in the template to access the data, and the values are the data we
    # need to send to the template. In this case, there's one key-value pair,
    # which contains the set of topics we'll display on the page.
    context = {"n": n}

    # when building a page that uses data, we pass the context variable to render()
    # as well as the request object and the path to the template

    return render(request, "pizzerias/names.html", context)


def name(request, name_id):
    # just like we did in MyShell.py
    name = Name.objects.get(id=name_id)
    # foreign key can be accessed using '_set'
    toppings = name.topping_set.order_by(
        "-date_added"
    )  # -date_added is descending order
    context = {"name": name, "toppings": toppings}

    return render(request, "pizzerias/name.html", context)


def new_name(request):
    if request.method != "POST":
        # no data submitted;create a blank form (create an instance of NameForm)
        # bc we included no arguments when instantiating TopicForm, Django
        # creates a blank form that the user can fill out.
        form = NameForm()
    else:
        # POST data submitted;processdata
        # we make an instance of TopicForm and pass it the data entered by the user, stored in
        # request.POST
        form = NameForm(data=request.POST)
        # the is_valid method checks all required fields have been
        # filled in (all fields in a form are required by default) and that the
        # data entered matches the field types expected
        if form.is_valid():
            # write the data from the form to the database
            form.save()
            # redirect the user's borwser to the topics page
            return redirect("pizzerias:names")

        # display a blank form using the new_name.html template
    context = {"form": form}
    return render(request, "pizzerias/new_name.html", context)


def new_comment(request, name_id):
    name = Name.objects.get(id=name_id)
    if request.method != "POST":
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            # when we call save(), we include the argument commit=False to tell Django
            # to create a new entry object and assign it to new_entry withouts aving it
            # to the database yet.
            new_comment = form.save(commit=False)
            # assign the topic of the new entry based on the topic we pulled form topic_id
            new_comment.name = name
            new_comment.save()
            form.save()
            return redirect("pizzerias:name", name_id=name_id)

    context = {"form": form, "name": name}
    return render(request, "pizzerias/new_comment.html", context)

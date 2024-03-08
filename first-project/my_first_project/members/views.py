from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q
import random

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def testing(request):
    # specific = Member.objects.filter(Q(first_name='Toluwanimi') | Q(first_name='Ben')).values()
    specific = Member.objects.filter(first_name__startswith='T').values()
    orderby = Member.objects.all().order_by('first_name').values()
    mymembers = Member.objects.all().values()
    mydata = Member.objects.all()
    first_names = Member.objects.values_list('first_name', flat=True)
    random_name = random.choice(first_names)
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
        'x': ['Apple', 'Banana', 'Cherry'],
        'y': ['Apple', 'Banana', 'Cherry'],
        'fruits': ['Grapes', 'Mango', 'Orange', 'Lemon', 'Watermelon', 'Apple'],
        'first_name': random_name,
        'mymembers' : mymembers,
        'mydata' : mydata,
        'myname': specific,
        'orderby': orderby,
    }
    return HttpResponse(template.render(context, request))

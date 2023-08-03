from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "name":"khim"
    }

    # context ={
    #   'students' : students,
    # }
    students = models.Students.objects.all()

    context ['students'] = students

    return render(request, 'main.html',context)
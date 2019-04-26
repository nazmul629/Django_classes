from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentInfo


def all_students(request):
    all_student=StudentInfo.objects.all()
    contxt={"students":all_student}
    return render(request,'student/student.html',contxt)

def st_result(request):
    all_student=StudentInfo.objects.filter(Result__gte=80)
    contxt={"students":all_student}
    return render(request,'student/st_rslt.html',contxt)


def district(request):
    all_student=StudentInfo.objects.filter(District__startswith='d')
    contxt={"students":all_student}
    return render(request,'student/st_dis.html',contxt)

# def all_roll(request):
#     all_student=StudentInfo.objects.filter(Roll%2 == 0)
#     contxt={"students":all_student}
#     return render(request,'student/roll.html',contxt)
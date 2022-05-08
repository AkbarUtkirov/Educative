from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.admin.views.decorators import (
    staff_member_required as _staff_member_required,
)

# Create your views here.
from dashboard.models import Note, Course


def index(requests):
    user = requests.user
    course = Course.objects.all().filter(teacher_id=user.id)

    ctx = {
        'courses': course,
        'user': user
    }

    return render(requests, 'dashboard/index.html', ctx)


def admin_index(requests, pk=None, nott=None):
    if pk:
        root = User.objects.get(pk=pk)
        root.is_staff = True
        root.save()
        note = Note.objects.all().filter(teacher_id=pk, status=True).first()

        note.status = False
        note.save()


    elif nott:
        note = Note.objects.filter(teacher_id=nott, status=True).first()
        note.status = False
        note.save()

    user = requests.user
    notes = Note.objects.all().filter(status=True)
    ctx = {
        'notes': notes,
        'user': user,
        'ln': len(notes)
    }
    return render(requests, 'dashboard/notefications.html')


def admin_notes(requests):
    user = requests.user
    notes = Note.objects.all().filter(status=True)
    ctx = {
        'notes': notes,
        'user': user,
        "ln": len(notes)
    }

    return render(requests, 'dashboard/notefications.html', ctx)


def admin_teacher(request):
    teachers = User.objects.all().filter(is_superuser=False)

    ctx = {
        "teachers": teachers
    }
    return render(request, 'dashboard/teacher_list.html', ctx)


def admin_course(request):
    course = Course.objects.all().filter()

    ctx = {
        'courses': course
    }
    return render(request, 'dashboard/courses.html', ctx)

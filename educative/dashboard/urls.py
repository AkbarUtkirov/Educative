from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='dashboard_index'),
    path('dash/admin/', admin_index, name='dashboard_admin'),
    path('dash/admin/<int:pk>/', admin_index, name='dashboard_admin_may'),
    path('dash/admin/s/<int:nott>/', admin_index, name='dashboard_admin_not'),
    path('dash/notes/', admin_notes, name='dashboard_admin_notefcations'),

    path('dash/teachers/', admin_teacher, name='admin_teacher'),

    path('dash/course/', admin_course, name='admin_course'),
]



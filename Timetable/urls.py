"""
URL configuration for Timetable project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("Coursereg", views.register_course),
    path("viewcourse",views.view_courses),
    path('coursedel/<int:id>/', views.course_delete),
    path('courseupd/<int:id>/', views.course_update),
    path('subregister', views.register_subject),
    path('viewsub', views.view_subjects),
    path('subdel/<int:id>/', views.subject_delete),
    path('subupd<int:id>/', views.subject_update),
    path('staffreg', views.register_staff),
    path('viewstaff', views.view_staffs),
    path('staffdel/<int:id>/', views.staff_delete),
    path('staffupd/<int:id>/', views.staff_update),
    path("assignmentsview", views.assignment_list),
    path("assigncr", views.assignment_create),
    path("assignmentsupd/<int:id>/", views.assignment_update),
    path("assignmentsdel/<int:id>/", views.assignment_delete),
    path("periodsview", views.period_list),
    path("periodscr", views.period_create),
    path("periodsupd/<int:id>/", views.period_update),
    path("periodsdel/<int:id>/", views.period_delete),
path('timetable/', views.generate_timetable),
]





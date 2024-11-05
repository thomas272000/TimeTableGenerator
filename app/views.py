from django.shortcuts import render,redirect
from .models import CourseModel,StaffModel,SubjectModel,StaffSubjectAssignmentModel,PeriodModel
from datetime import time

# Create your views here.
def register_course(request):
    if request.method == 'POST':
        name=request.POST.get("name")
        course_obj=CourseModel()
        course_obj.name=name
        course_obj.save()
        return redirect("/viewcourse")
    return render(request,"Course.html")

def view_courses(request):
    courses = CourseModel.objects.all()
    return render(request, "viewcourse.html", {"courses": courses})
def course_delete(request,id):
    courses = CourseModel.objects.get(id=id)
    courses.delete()
    return redirect("/viewcourse")

def course_update(request,id):
    course=CourseModel.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get("name")
        course.name=name
        course.id=id
        course.save()
        return redirect("/viewcourse")
    return render(request,"Courseupd.html",{"course":course})


def register_subject(request):
    courses = CourseModel.objects.all()
    if request.method == 'POST':
        name = request.POST.get("name")
        course_id = request.POST.get("course")

        course = CourseModel.objects.filter(id=course_id)
        if course:
            subject_obj = SubjectModel(course=course, name=name)
            subject_obj.save()
        return redirect('/subjects')
    return render(request, "Subject.html", {"courses": courses})



def view_subjects(request):
    subjects = SubjectModel.objects.all()
    return render(request, "viewsubjects.html", {"subjects": subjects})



def subject_delete(request, id):
    subject = SubjectModel.objects.get(id=id)
    subject.delete()
    return redirect("/subjects")



def subject_update(request, id):
    subject = SubjectModel.objects.get(id=id)
    courses = CourseModel.objects.all()
    if subject and request.method == 'POST':
        name = request.POST.get("name")
        course_id = request.POST.get("course")
        course = CourseModel.objects.get(id=course_id)
        if course:
            subject.course = course
            subject.name = name
            subject.save()
        return redirect("/subjects")
    return render(request, "Subjectupd.html", {"subject": subject, "courses": courses})


def register_staff(request):
    if request.method == 'POST':
        name=request.POST.get("name")
        staff_obj=StaffModel()
        staff_obj.name=name
        staff_obj.save()
        return redirect("/viewstaff")
    return render(request,"staffreg.html")

def view_staffs(request):
    staff = StaffModel.objects.all()
    return render(request, "viewstaff.html", {"staff": staff})
def staff_delete(request,id):
    staff = StaffModel.objects.get(id=id)
    staff.delete()
    return redirect("/viewstaff")

def staff_update(request,id):
    staff=StaffModel.objects.get(id=id)
    print(staff)
    if request.method == 'POST':
        name=request.POST.get("name")
        staff.name=name
        staff.id=id
        staff.save()
        return redirect("/viewstaff")
    return render(request,"staffeupd.html",{"staff":staff})


def assignment_list(request):
    assignments = StaffSubjectAssignmentModel.objects.all()
    return render(request, "assignmentlist.html", {"assignments": assignments})


def assignment_create(request):
    if request.method == 'POST':
        staff_id = request.POST.get("staff")
        subject_id = request.POST.get("subject")
        staff = StaffModel.objects.get(id=staff_id)
        subject = SubjectModel.objects.get(id=subject_id)
        assignment = StaffSubjectAssignmentModel()
        assignment.staff = staff
        assignment.subject = subject
        assignment.save()
        return redirect("/assignmentsview")
    staff_members = StaffModel.objects.all()
    subjects = SubjectModel.objects.all()
    return render(request, "assignmentform.html", {"staff_members": staff_members, "subjects": subjects})



def assignment_update(request, id):
    assignment = StaffSubjectAssignmentModel.objects.filter(id=id)
    if request.method == "POST":
        staff_id = request.POST.get("staff")
        subject_id = request.POST.get("subject")
        assignment.staff = StaffModel.objects.get(id=staff_id)
        assignment.subject = SubjectModel.objects.get(id=subject_id)
        assignment.save()
        return redirect("/assignmentsview")
    staff_members = StaffModel.objects.all()
    subjects = SubjectModel.objects.all()
    return render(request, "assignmentupdform.html", {"assignment": assignment, "staff_members": staff_members, "subjects": subjects})


def assignment_delete(request, id):
    assignment = StaffSubjectAssignmentModel.objects.get(id=id)
    assignment.delete()
    return redirect("/assignmentsview")



def period_create(request):
    if request.method == 'POST':
        course_id = request.POST.get("course")
        day = request.POST.get("day")
        period_number = request.POST.get("period_number")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        subject_id = request.POST.get("subject")
        staff_id = request.POST.get("staff")


        period = PeriodModel()
        period.course_id = course_id
        period.day = day
        period.period_number = period_number
        period.start_time = start_time
        period.end_time = end_time
        period.subject_id = subject_id
        period.staff_id = staff_id
        period.save()

        return redirect("/periodsview")

    courses = CourseModel.objects.all()
    subjects = SubjectModel.objects.all()
    staff_members = StaffModel.objects.all()
    return render(request, "periodform.html", {"courses": courses, "subjects": subjects, "staff_members": staff_members})


def period_update(request, id):
    period = PeriodModel.objects.get(id=id)
    if period:
        if request.method == 'POST':
            course_id = request.POST.get("course")
            day = request.POST.get("day")
            period_number = request.POST.get("period_number")
            start_time = request.POST.get("start_time")
            end_time = request.POST.get("end_time")
            subject_id = request.POST.get("subject")
            staff_id = request.POST.get("staff")


            period.course_id = course_id
            period.day = day
            period.period_number = period_number
            period.start_time = start_time
            period.end_time = end_time
            period.subject_id = subject_id
            period.staff_id = staff_id
            period.save()
            return redirect("/periodsview")

        courses = CourseModel.objects.all()
        subjects = SubjectModel.objects.all()
        staff_members = StaffModel.objects.all()
        return render(request, "periodformupd.html", {"period": period, "courses": courses, "subjects": subjects, "staff_members": staff_members})

    return redirect("/periodsview")


def period_list(request):
    periods = PeriodModel.objects.all()
    return render(request, "periodlist.html", {"periods": periods})


def period_delete(request, id):
    period = PeriodModel.objects.get(id=id)
    period.delete()
    return redirect("/periodsview")





def generate_timetable(request):

    time_slots = [
        (time(9, 0), time(10, 0)),
        (time(10, 0), time(11, 0)),
        (time(11, 0), time(12, 0)),
        (time(12, 0), time(13, 0)),
    ]
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    timetable = {}
    courses = CourseModel.objects.all()

    for course in courses:
        timetable[course.name] = {}


        day_index = 0
        while day_index < len(days):
            day = days[day_index]
            periods = []
            period_number = 1

            for start, end in time_slots:

                existing_period = PeriodModel.objects.filter(
                    course_id=course.id, day=day, period_number=period_number
                )

                if not existing_period.exists():

                    subjects = SubjectModel.objects.filter(course_id=course.id)
                    staff_members = StaffModel.objects.exclude(
                        periods__day=day,
                        periods__period_number=period_number
                    )


                    if subjects and staff_members:

                        period = PeriodModel()
                        period.course_id = course.id
                        period.subject_id = subjects[0].id
                        period.staff_id = staff_members[0].id
                        period.day = day
                        period.period_number = period_number
                        period.start_time = start
                        period.end_time = end
                        period.save()
                    else:
                        period = None
                else:

                    period = existing_period[0]


                periods.append(period)
                period_number += 1


            timetable[course.name][day] = periods
            day_index += 1


    return render(request, 'timetable.html', {'timetable': timetable})


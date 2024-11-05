from django.contrib import admin
from .models import CourseModel,StaffModel,SubjectModel,StaffSubjectAssignmentModel,PeriodModel

# Register your models here.
admin.site.register(CourseModel)
admin.site.register(SubjectModel)
admin.site.register(StaffModel)
admin.site.register(StaffSubjectAssignmentModel)
admin.site.register(PeriodModel)
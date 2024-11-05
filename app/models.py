from django.db import models

# Create your models here.


class CourseModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubjectModel(models.Model):
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StaffModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StaffSubjectAssignmentModel(models.Model):
    staff = models.ForeignKey(StaffModel, on_delete=models.CASCADE, related_name='assignments')
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE, related_name='assignments')

    def __str__(self):
        return f"{self.staff.name} teaches {self.subject.name}"

class PeriodModel(models.Model):

    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='periods')
    day = models.CharField(max_length=10)
    period_number = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE, null=True, blank=True, related_name='periods')
    staff = models.ForeignKey(StaffModel, on_delete=models.CASCADE, null=True, blank=True, related_name='periods')


    def __str__(self):
        return f"{self.course.name} - {self.day} Period {self.period_number}: {self.start_time} to {self.end_time}"
from django.db import models
import uuid

# Create your models here.


class AcademyDetails(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    academy_name = models.CharField(max_length=100)
    academy_description = models.TextField()
    featured_video_link = models.CharField(max_length=1000)
    staff_count = models.IntegerField(default=12)
    student_count = models.IntegerField(default=239)
    courses_count = models.IntegerField(default=10)

    def __str__(self):
        return str(self.academy_name)


class CourseDuration(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    course_duration = models.CharField(max_length=200)

    def __str__(self):
        return str(self.course_duration)


class Faculties(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    faculty_name = models.CharField(max_length=200)
    faculty_image = models.ImageField(default='default/faculty.jpg', null=True, blank=True, upload_to='faculties/')
    # faculty_course = models.ForeignKey('Courses',on_delete=models.CASCADE, null=True )
    faculty_description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.faculty_name)


class Courses(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    course_name = models.CharField(max_length=300)
    course_description = models.TextField()
    course_image = models.ImageField(default='default/default.jpg', null=True, blank=True, upload_to='courses/')
    course_duration = models.ForeignKey(CourseDuration, on_delete=models.CASCADE, null=True)
    course_faculty = models.ForeignKey(Faculties, on_delete=models.CASCADE, null=True)
    course_seat_available = models.IntegerField(default=10)

    def __str__(self):
        return str(self.course_name)


class StudentSayAboutUs(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    student_name = models.CharField(max_length=200)
    student_description = models.TextField(max_length=500)
    student_course = models.ForeignKey(Courses,  on_delete=models.CASCADE, null=True)
    student_image = models.ImageField(default='default/student.jpg', null=True, blank=True, upload_to='students/')

    def __str__(self):
        return str(self.student_name)


class Poster(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    poster_image = models.ImageField(null=False, blank=False, upload_to='poster/')

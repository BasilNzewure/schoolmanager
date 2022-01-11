from django.contrib import admin
from userapp.models import Courses, BookCourse

# Register your models here.

class CoursesModelAdmin(admin.ModelAdmin):
    list_display = ("id", "course_name", "duration", "faculty")

class BookCourseModelAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "commence_date", "end_date")

admin.site.register(Courses, CoursesModelAdmin)
admin.site.register(BookCourse, BookCourseModelAdmin)


from django.contrib import admin
from .models import (
    Instructor,
    Learner,
    Course,
    Question,
    Choice,
    Lesson,
    Enrollment,
    Submission,
)


# Instructor configuration
class InstructorAdmin(admin.ModelAdmin):
    fields = ['user', 'full_time']


# Lesson inline configuration
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Course configuration
class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]


# Register models
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Learner)
admin.site.register(Course, CourseAdmin)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Submission)

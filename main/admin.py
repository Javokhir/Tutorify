from django.contrib import admin
from . models import Tutor, Organization, Learner, Subject, Course, Announcement

# Register your models here.


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['tutor', ]


@admin.register(Learner)
class LearnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['tutor', 'subject', 'price']
    list_filter = ['price', 'subject']
    search_fields = ['subject', 'description']


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['tutor', 'subject', 'description']

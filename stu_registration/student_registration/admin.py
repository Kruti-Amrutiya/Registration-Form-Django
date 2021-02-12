from django.contrib import admin
from .models import Student

admin.site.site_header = 'My admin'


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("fullname", "dob", "roll_num", "gender", "mobile", "email", "subject")
    list_filter = ("roll_num", )
    ordering = ('fullname',)
    search_fields = ("fullname",)
    fieldsets = (
        ('Required Information', {
            'description': "These fields are required.",
            'fields': (('fullname', 'dob'), ('email', 'gender'))
         }),
        ('Optional Information', {
            'classes': ('collapse',),
            'fields': ('roll_num', 'mobile', 'subject')
        }),
    )

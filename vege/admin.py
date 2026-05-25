from django.contrib import admin
from vege.models import Receipe, Department, StudentID, Students

# Register your models here.
from .models import*

admin.site.register(Receipe)
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Students)
admin.site.register(Subject)

class SubjectMarkAdmin(admin.ModelAdmin):
    list_display=['student','subject','marks']
admin.site.register(SubjectMarks,SubjectMarkAdmin)


print("ADMIN LOADED SUCCESSFULLY")




from django.db.models import Sum

class ReportCardAdmin(admin.ModelAdmin):
    list_display=['student','student_rank','total_marks','date_of_report_card_generation']


    def total_marks(self,obj):
        subject_marks=SubjectMarks.objects.filter(student=obj.student)
        marks=subject_marks.aggregate(marks=Sum('marks'))



        return marks['marks']
    

admin.site.register(ReportCard,ReportCardAdmin)
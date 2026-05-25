from faker import Faker
fake=Faker()
from .models import*
import random


# def seed_db(n=10)->None:
#     for _ in range(n):
#         departments_objs=Department.objects.all()
#         random_index=random.randint(0,len(departments_objs)-1)
#         student_id=f'STU-0{random.randint(100,999)}'
#         department=departments_objs[random_index]
#         student_name=fake.name()
#         student_email=fake.email()
#         student_age=random.randint(20,30)
#         student_address=fake.address()

#         student_id_obj=StudentID.objects.create(student_id=student_id)


#         student_obj=Students.objects.create(
#             department=department,
#             student_id=student_id_obj,
#             student_name=student_name,
#             student_email=student_email,
#             student_age=student_age,
#             student_address=student_address,












#         )

from faker import Faker
fake = Faker()

from .models import *
import random
import random
from .models import Students, Subject, SubjectMarks


def create_subject_marks(n):
    try:
        # Sare students lao
        students = Students.objects.all()

        # Sare subjects lao
        subjects = Subject.objects.all()

        # Har student ke liye
        for student in students:

            # Har subject ke liye
            for subject in subjects:

                # Random marks create karo
                SubjectMarks.objects.create(
                    student=student,
                    subject=subject,
                    marks=random.randint(0, 100)
                )

        print("Subject marks created successfully")

    except Exception as e:
        print(e)

def seed_db(n=10) -> None:
    departments_objs = list(Department.objects.all())  # 🔥 outside loop (efficient)
    try:
        for _ in range(n):
            department = random.choice(departments_objs)

            student_id = f'STU-0{random.randint(100,999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20,30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id=student_id)

            student_obj = Students.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address,
                )
    
    except Exception as e:
               print(e)       

from django.db.models import Sum

def generate_report_card():
     current_rank=-1
     ranks=Students.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks','-student_age')

     i=1
     for rank in ranks:
          ReportCard.objects.create(
               student=rank,
               student_rank=i
          )
          i+=1
               
               

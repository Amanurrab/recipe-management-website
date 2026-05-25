from django.shortcuts import render,redirect
from .models import*
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Students
from django.core.paginator import Paginator
# Create your views here.


@login_required(login_url="/login/")
def receipes(request):
    if request.method=="POST":


        data=request.POST
        receipe_image=request.FILES['receipe_image']

        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        print(receipe_name)
        print(receipe_description)
        # print(receipe_image)
        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description,

        )

        return redirect('/receipes/')
    

    
    queryset=Receipe.objects.all()





    search_query = request.GET.get('search')

    if search_query:
        queryset = queryset.filter(receipe_name__icontains=search_query)


    context={'receipes':queryset}

    return render(request,'receipes.html',context)


def delete_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    
    return redirect('/receipes/')

def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    if request.method=="POST":


        data=request.POST
        receipe_image=request.FILES.get('receipe_image')

        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')

        
        # print(receipe_image)
        
        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description

        if receipe_image:
            queryset.receipe_image=receipe_image

        queryset.save()
        return redirect('/receipes/')


    context={'receipe':queryset}
    return render(request,'update_receipe.html',context)



def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
       
        password = request.POST.get('password')
        

        print("DATA:", username, password)


        
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/receipes/')

       
       

    return render(request,'login.html')


def logout_page(request):
    
    logout(request)
    return redirect('/login/')








from django.db.models import Q


def get_students(request):
    queryset=Students.objects.all()

    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset=queryset.filter(
            Q(student_name__icontains=search)|
           
            Q(student_id__student_id__icontains=search)|
            Q(student_email__icontains=search)|
             Q(department__department__icontains=search)|
             Q(student_age__icontains=search)
            
            
            )
    
    paginator = Paginator(queryset, 10)

    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    
    return render(request,'report/students.html',{'queryset':page_obj})





def marks(request):
    query=SubjectMarks.objects.all()
    return render(request,'report/students.html',{'query':query})




from django.db.models import Sum

def see_marks(request,student_id):
    queryset=SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks=queryset.aggregate(total_marks=Sum('marks'))


    print(total_marks)


   
    current_rank=1
    ranks=Students.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks','-student_age')
    i=1
    for rank in ranks:
        if student_id==rank.student_id.student_id:
            current_rank=i
            break
        i=i+1

    return render(request,'report/see_marks.html',{'queryset':queryset,'total_marks':total_marks,'current_rank':current_rank})























































# def register_page(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         email=request.POST.get('email')
#         password=request.POST.get('password')
       
#         confirm_password=request.POST.get(' confirm_password')
#         if password != confirm_password:
#             return render(request, 'register.html', {'error': 'Passwords do not match'})
        
#           # User already exists check
#         if User.objects.filter(username=username).exists():
#             return render(request, 'register.html', {'error': 'Username already taken'})

#         user=User.objects.create(
#             username=username,

#             email=email,
           

#         )
#         user.set_password(password)
#         user.save()
#         return redirect("/register/")

#     return render(request,'register.html')

    
    
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        print("DATA:", username, email, password, confirm_password)

        if not username or not email or not password or not confirm_password:
            return render(request, 'register.html', {'error': 'All fields required'})

        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Password not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        # ✅ BEST WAY
        user=User.objects.create_user(
            username=username,
            email=email,
            
        )
        user.set_password(password)
        user.save()

        print("USER CREATED ✅")

        return redirect('/login/')

    return render(request, 'register.html')







def login_user(request):
    return render(request,'facelogin.html')
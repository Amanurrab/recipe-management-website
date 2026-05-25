"""
URL configuration for ch8 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   # include जरूरी है
from app1 import views
import vege.views as views

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('app1.urls')), 
    path('receipes/', views.receipes),
    path('delete-receipe/<int:id>/',views.delete_receipe),
    path('update-receipe/<int:id>/',views.update_receipe),
    path('login/',views.login_page),
    path('logout/',views.logout_page),
    path('userlogin/',views.login_user),
    path('studentss/',views.get_students),
    path('see_markss/<str:student_id>/',views.see_marks,name='see_marks'),
    path('register/',views.register_page),
    path('about/',include('app1.urls')),
    path('contact/',include('app1.urls')),
    path('app2/',include('app2.urls')),  # 👈 app1 connect किया
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)
    
urlpatterns+=staticfiles_urlpatterns()
    
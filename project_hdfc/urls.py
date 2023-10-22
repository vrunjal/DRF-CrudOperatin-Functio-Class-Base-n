
from django.contrib import admin
from django.urls import path,include
from app_api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/<str:pk>',views.student_api),
    path('studentapi/',views.student_api),


]

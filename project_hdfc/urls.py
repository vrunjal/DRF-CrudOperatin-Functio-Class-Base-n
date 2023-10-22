
from django.contrib import admin
from django.urls import path,include
from app_api.views import student_api
from app_api_classbased import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/<str:pk>',views.student_api),
    path('studentapi/',student_api),
    path('studentapi1/',views.StudentAPI.as_view()),


]

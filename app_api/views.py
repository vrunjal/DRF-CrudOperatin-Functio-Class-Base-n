from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_api(request):
    if request.method=="GET":
       json_data= request.body
       stream=io.BytesIO(json_data)
       print(f"\n\n\n\n\n\n{stream}\n\n\n\n")
       pythondata=JSONParser().parse(stream)
       print(f"\n\n\n\n\n\n{pythondata}\n\n\n\n") 
       id=pythondata.get('id',None)
       if id is not None:
           stu=Student.objects.get(id=id)
           serializer=StudentSerializer(stu)
           json_data=JSONRenderer().render(serializer.data)
           return HttpResponse(json_data,content_type='application/json')
       stu=Student.objects.all()
       serializer=StudentSerializer(stu,many=True)
       json_data=JSONRenderer().render(serializer.data)
       return HttpResponse(json_data,content_type='application/json')
# def student_api(request,pk=None):
#     if request.method == "GET":
#         if pk is not None:
#             data = Student.objects.get(id=pk)
#             serializer = StudentSerializer(data)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')
#         data = Student.objects.all()
#         serializer = StudentSerializer(data,many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')


    if request.method=="POST":
            json_data=request.body
            #to convert json data to python IO(native)
            stream=io.BytesIO(json_data)
            print(f"\n\n\n\n\n\n{stream}\n\n\n\n")
            pythondata=JSONParser().parse(stream)
            print(f"\n\n\n\n\n\n{pythondata}\n\n\n\n")
            serializer=StudentSerializer(data=pythondata)
            if serializer.is_valid():
                serializer.save()
                res={'msg':'Data created'}
                json_data=JSONRenderer().render(res)
                return HttpResponse(json_data,content_type='application/json')
            json_data=JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type='application/json')


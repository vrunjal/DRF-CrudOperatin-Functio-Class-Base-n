from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse ,JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_api(request):
    if request.method == "GET":
        json_data=request.body    #client side data which is stored in json_data
        print(f'\n\n\n\n\n{json_data}\n\n\n\n\n')
        stream = io.BytesIO(json_data)  #stream data
        print(f"\n\n\n\n\n{stream}\n\n\n\n")
        pythondata= JSONParser().parse(stream) #convert stream data into python data
        print(f"\n\n\n\n\n\n{pythondata}\n\n\n\n")
        id=pythondata.get('id',None) #if there is id then pass it otherwise pass None
        print(id)
        if id is not None:     #if id not None
            stu=Student.objects.get(id=id)   #if they have specific value then it will retrieve specific data
            serializer =StudentSerializer(stu)  #python native data type conversion
            json_data=JSONRenderer().render(serializer.data) #converted to json data
            return HttpResponse(json_data,content_type='application/json')   #return it back
        stu=Student.objects.all()   #in case when there is no specific id retrive/call.
        serializer=StudentSerializer(stu,many=True)  #to except more than one data
        json_data=JSONRenderer().render(serializer.data) #converted to json data
        return HttpResponse(json_data,content_type='application/json')   #return it back


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
            json_data=request.body       #client side data
            #to convert json data to python IO(native)
            stream=io.BytesIO(json_data)        
            print(f"\n\n\n\n\n\n{stream}\n\n\n\n")       
            # pythondata=JSONParser().parse(stream)           python nativedata type
            print(f"\n\n\n\n\n\n{pythondata}\n\n\n\n")
            serializer=StudentSerializer(data=pythondata)      #complex data conversion /Deserialization
            if serializer.is_valid():             #validation check
                serializer.save()                  #save data
                res={'msg':'Data created'}
                json_data=JSONRenderer().render(res)
                return HttpResponse(json_data,content_type='application/json')
            json_data=JSONRenderer().render(serializer.errors)         #error than show error.
            return HttpResponse(json_data,content_type='application/json')

 
    if request.method == "PUT":    #use id compulsury in postman otherwise it will show error.
         json_data=request.body
         stream=io.BytesIO(json_data)
         pythondata=JSONParser().parse(stream)  #python data
         id=pythondata.get('id')   #from this point you find that id
         stu=Student.objects.get(id=id)    #and send above id here    and this is complex data
        #  serializer=StudentSerializer(stu,data=pythondata)   #this will convert into python data   Full update
         serializer=StudentSerializer(stu,data=pythondata,partial=True)   #this will convert into python data  Partial Update
         if serializer.is_valid():
              serializer.save()
              res={'msg':'Data Updated'}
              json_data=JSONRenderer().render(res)
              return HttpResponse(json_data,content_type="application/json")
         json_data=JSONRenderer().render(serializer.error)
         return HttpResponse(json_data,content_type="application/json")
    
    if request.method =="DELETE":    #id is compulsury in postman
         json_data=request.body
         stream=io.BytesIO(json_data)
         pythondata=JSONParser().parse(stream)
         id=pythondata.get('id')
         stu=Student.objects.get(id=id)
         stu.delete()
         res={'msg':'Data Deleted'}
        #  json_data=JSONRenderer().render(res)
        #  return HttpResponse(json_data,content_type="application/json")
         return JsonResponse(res,safe=False)
         
         




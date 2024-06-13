from django.shortcuts import render
from rest_framework.parsers import JSONParser
import io
from rest_framework import serializers
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            resp = {'msg': 'Data created successfully!'}
            json_data= JSONRenderer().render(resp)
            return HttpResponse(json_data,content_type= 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)

        #for partial update add (partial=True)--->
        serializer = StudentSerializer(stu, data=pythondata, partial=True)

        #for complete update- partial=True not required
        #serializer = StudentSerializer(stu, data= pythondata)
        if serializer.is_valid():
            serializer.save()
            resp = {'msg' : 'Data updated successfully!'}
            json_data = JSONRenderer().render(resp)
            return HttpResponse(json_data, content_type= 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        resp = {'msg': 'Data deleted successfully!'}
        json_data = JSONRenderer().render(resp)
        return HttpResponse(json_data, content_type='application/json')
    #json_data = JSONRenderer().render(serializer.errors)
   # return HttpResponse(json_data, content_type= 'application/json')
        return JsonResponse(resp, safe=False)



# Create your views here.
# @csrf_exempt
# #func for get request(Read)
# def student_api(request):
#     if request.method == "GET":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')

#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')
    
    #func for create data
    # if request.method == 'POST':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     pythondata = JSONParser().parse(stream)
    #     serializer = StudentSerializer(data = pythondata)
    #     if serializer.is_valid():
    #         serializer.save()
    #         resp = {'msg': 'Data created successfully!'}
    #         json_data= JSONRenderer().render(resp)
    #         return HttpResponse(json_data,content_type= 'application/json')
    #     json_data = JSONRenderer().render(serializer.errors)
    #     return HttpResponse(json_data, content_type='application/json')
    
    #func for update data
    # if request.method == 'PUT':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     pythondata = JSONParser().parse(stream)
    #     id = pythondata.get('id')
    #     stu = Student.objects.get(id=id)

    #     #for partial update add (partial=True)--->
    #     serializer = StudentSerializer(stu, data=pythondata, partial=True)

    #     #for complete update- partial=True not required
    #     #serializer = StudentSerializer(stu, data= pythondata)
    #     if serializer.is_valid():
    #         serializer.save()
    #         resp = {'msg' : 'Data updated successfully!'}
    #         json_data = JSONRenderer().render(resp)
    #         return HttpResponse(json_data, content_type= 'application/json')
    #     json_data = JSONRenderer().render(serializer.errors)
    #     return HttpResponse(json_data, content_type='application/json')


    #func to delete data
#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         resp = {'msg': 'Data deleted successfully!'}
#         json_data = JSONRenderer().render(resp)
#         return HttpResponse(json_data, content_type='application/json')
#     #json_data = JSONRenderer().render(serializer.errors)
#    # return HttpResponse(json_data, content_type= 'application/json')
#     return JsonResponse(resp, safe=False)
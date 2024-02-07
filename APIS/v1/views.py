import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser

from Books.models import Books
from APIS.v1.serializers import BooksSerializer


@csrf_exempt
def get_details(request):
    if request.method == 'GET':
        book_details = Books.objects.all()
        serializer = BooksSerializer(book_details, many=True)
        return JsonResponse(serializer.data, safe=False)


    elif request.method == 'POST':
        #print(request.body)
        data = JSONParser().parse(request)
        print(data)
        #data = request.data
        serializer = BooksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        #print(data)
        book_id=data.get('id')
        books_det=Books.objects.get(id=book_id)
        serializer = BooksSerializer(books_det,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        #print(data)
        book_id=data.get('id')
        books_det=Books.objects.get(id=book_id)
        serializer = BooksSerializer(books_det,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        #print(data)
        book_id=data.get('id')
        books_det=Books.objects.get(id=book_id)
        books_det.delete()
        return HttpResponse("Deleted")
    else:
        return HttpResponse("Invalid Request")
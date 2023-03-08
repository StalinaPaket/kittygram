from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Cat
from .serializers import CatSerializer



class APICat(APIView):
    def get(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CatSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APICatDetail(APIView):
    
    def get(self, request, pk):
        cat = Cat.objects.get(id=pk)
        serializer = CatSerializer(cat, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        cat = Cat.objects.get(id=pk)
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        cat = Cat.objects.get(id=pk)
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, requset, pk):
        cat = Cat.objects.get(id=pk)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
# def cat_detail(request, pk):
#     cat = Cat.objects.get(id=pk)
#     if request.method == 'PATCH' or request.method == 'PUT':
#         serializer = CatSerializer(cat, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         cat.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     serializer = CatSerializer(cat, many=False)
#     return Response(serializer.data)

# Create your views here.
from rest_framework import serializers
from rest_framework import views
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ManageUserSerializer
from .models import ManageUserModels



class ListManageUserViews(APIView):
    def get(self,request):
        querySet = ManageUserModels.objects.all()
        serializer_class = ManageUserSerializer(querySet, many=True)
        return Response(serializer_class.data)

class DetailManageUserViews(APIView):
    def get(self, request, pk):
        querySet = ManageUserModels.objects.get(id=pk)
        serializer_class = ManageUserSerializer(querySet, many=False)
        return Response(serializer_class.data)   

class CreateManageUserViews(APIView):
    def post(self, request):
        serializer_class = ManageUserSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors)

class UpdateManageUserViews(APIView):
    def post(self, request, pk):
        querySet = ManageUserModels.objects.get(id=pk)
        serializer_class = ManageUserSerializer(instance=querySet, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
        return Response(serializer_class.data)


class DeleteManageUserViews(APIView):
    def get(self, request, pk):
        # querySet = ManageUserModels.objects.get(id=pk)
        user_instance = ManageUserModels.objects.get(id=pk)
        user_instance.delete()
        return Response('Deleted')
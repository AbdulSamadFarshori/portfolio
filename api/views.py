from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from app.models import ContactDetail
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class TestingApiView(APIView):

    # permission_classes = (AllowAny,)

    def post(self, request):
        args = request.data
        obj = ContactDetail.objects.create(**args)
        obj.save()
        print(args)

        return Response({'status':'success', 'msg': 'success', 'error':'', 'data': ''})
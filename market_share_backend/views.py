from rest_framework.views import APIView

# from django.http import Http404,HttpResponseBadRequest,HttpResponseNotFound
# from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
# from rest_framework import serializers,parsers

from rest_framework.permissions import IsAuthenticated
import rest_framework.permissions


class Test(APIView):
    permission_classes = [rest_framework.permissions.AllowAny]

    def get(self, request):

        return Response({"test": "test"})

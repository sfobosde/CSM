import uuid

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import JsonResponse
import json

# Create your views here.
@api_view(["GET"])
def test(request):
    return JsonResponse({
            "name": "Detail 12345",
            "material_id": "rttrt"
    }, status=200)
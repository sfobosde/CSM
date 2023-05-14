import json

from django.http import JsonResponse

from ..DTOModels.IDetailTemplate import IDTOModel

from rest_framework.response import Response
from rest_framework.decorators import api_view

from types import SimpleNamespace

from .. import DBContext

from .BaseController import BaseController

class OrderController(BaseController):
    @api_view(["GET", "POST"])
    @staticmethod
    def handle_request(request):
        controller_objects = ["order"]

        response = JsonResponse({
            "message":"Action received but not handled."
        }, status=201)

        try:
            BaseController.validate_request(request, controller_objects)
        except Exception as Error:
            response = BaseController.handle_error(error=Error)

        return response
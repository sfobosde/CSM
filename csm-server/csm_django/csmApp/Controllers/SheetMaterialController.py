import json
from .ApiErrors import UrlParametersError, RequestError, DataValidationError
from .ErrorHandler import handle_error

from django.http import JsonResponse

from ..DTOModels.IDetailTemplate import IDetailTemplate

from rest_framework.response import Response
from rest_framework.decorators import api_view

from types import SimpleNamespace

from .. import DBContext

from .BaseController import BaseController

class SheetMaterialController(BaseController):

    # Handle request with detail objects.
    @api_view(["GET", "POST"])
    def handle_request(request):
        controller_objects = ["sheet", "material"]

        response = JsonResponse({
            "message":"Action received but not handled."
        }, status=201)

        try:
            # Check is request valid.
            BaseController.validate_request(request, controller_objects=controller_objects)

            object = str(request.GET['object'])
            action = str(request.GET['action'])
        
            # Make action as detail template.
            if (object == 'template'):
                pass
            

        except Exception as error:
            response = handle_error(error)
    
        return response
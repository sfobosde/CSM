import json
from .ApiErrors import UrlParametersError, RequestError, DataValidationError
from .ErrorHandler import handle_error

from django.http import JsonResponse

from ..DTOModels.IDetailTemplate import IDetailTemplate

from rest_framework.response import Response
from rest_framework.decorators import api_view

from types import SimpleNamespace

from .. import DBContext

from .DetailController import validate_request

# Handle request with detail objects.
@api_view(["GET", "POST"])
def handle_request(request):
    response: JsonResponse

    try:
        # Check is request valid.
        validate_request(request)

        object = str(request.GET['object'])
        action = str(request.GET['action'])
        
        # Make action as detail template.
        if (object == 'template'):
            response = handle_detail_template(request.body, action)
            

    except Exception as error:
        response = handle_error(error)
    
    return response
import json
from .ApiErrors import UrlParametersError, RequestError
from .ErrorHandler import handle_error

from django.http import JsonResponse

from ..DTOModels.IDetailTemplate import IDetailTemplate

from rest_framework.response import Response
from rest_framework.decorators import api_view

from types import SimpleNamespace

from .. import DBContext

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

# Check is request contains required parameters.
def validate_request(request):
    
    object = str(request.GET['object'])
    
    if (not object 
        or len(object) <= 0): 
        raise UrlParametersError("Parameter 'object' is required in URL parameters.")
    
    if (not object.__eq__("detail") 
        and not object.__eq__("template")
        or object.__contains__(" ")):
        raise UrlParametersError(f"Value of parameter 'object' can be 'detail' or 'template'. Current value: {object}")
    
    action = str(request.GET['action'])

    if (not action 
        or len(action) <= 0): 
        raise UrlParametersError("Parameter 'action' is required in URL parameters.")
    
    if (not action.__eq__("add") 
        and not action.__eq__("update")
        and not action.__eq__("delete")
        and not action.__eq__("get")
        or action.__contains__(" ")):
        raise UrlParametersError(f"Value of parameter 'action' can be 'add', 'update', 'get' or 'delete'. Current value: {action}")
    
    if ((action == "add"
            or action == "update")
        and not request.method == "POST"):
        raise RequestError(f"Action type {action} require request type: POST. Current: {request.method}")
    


# Handle request related to detail template.
def handle_detail_template(body, action) -> JsonResponse:
    detail_template: IDetailTemplate = json.loads(body, object_hook=lambda d: SimpleNamespace(**d))

    if action == "add":
        detail_template = DBContext.create_detail_template(detail_template)

    return JsonResponse({"message":"Data received successfully"})


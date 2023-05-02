from .ApiErrors import UrlParametersError
from .ErrorHandler import handle_error

from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Handle request with detail objects.
@api_view(["GET", "POST"])
def handle_request(request):
    try:
        # Check is request valid.
        validate_request(request)


    except Exception as error:
        return handle_error(error)
    
    return Response(str(request))

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
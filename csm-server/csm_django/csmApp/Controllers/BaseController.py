from .ApiErrors import *

from django.utils.datastructures import MultiValueDictKeyError

from django.http import JsonResponse

# Base Controller module.
class BaseController():
    @staticmethod
    # Check is request contains required parameters.
    def validate_request(request, controller_objects, controller_actions = ["add", "get", "update", "delete"]):
        object = str(request.GET['object'])
        action = str(request.GET['action'])

        if (not object 
            or len(object) <= 0): 
            raise UrlParametersError("Parameter 'object' is required in URL parameters.")
    
        if (not controller_objects.__contains__(object)):
            raise UrlParametersError(f"Value of parameter 'object' can be {controller_objects}. Current value: {object}")
    
        if (not action 
            or len(action) <= 0): 
            raise UrlParametersError("Parameter 'action' is required in URL parameters.")
    
        if (not controller_actions.__contains__(action)):
            raise UrlParametersError(f"Value of parameter 'action' can be {controller_actions}. Current value: {action}")
    
        if ((action == "add"
            or action == "update")
            and not request.method == "POST"):
            raise RequestError(f"Action type {action} require request type: POST. Current: {request.method}")
        
        if (action == "get"
            and not request.method == "GET"):
            raise RequestError(f"Action type {action} require request type: GET. Current: {request.method}")
        
    # Handle requset exceptions.
    @staticmethod
    def handle_error(error) -> JsonResponse:
        # Required parameter not found in URL.
        if (isinstance(error, MultiValueDictKeyError)):
            return JsonResponse({
                "message": f"No required URL parameter: {error}"
            },
            status = 400)
    
        # No value in url parameter.
        if isinstance(error, UrlParametersError):
            return JsonResponse({
                "message": f"Error in URL parameters: {error}"
            },
            status = 400)
    
        if isinstance(error, RequestError):
            return JsonResponse({
                "message": f"Request error: {error}"
            },
            status = 500)
        
        if (isinstance(error, DataValidationError)):
            return JsonResponse({
                "message": f"Validation error: {error}"
            },
            status = 400)
        
        if (isinstance(error, NonExistValue)):
            return JsonResponse({
                "message": f"Value Error: {error}"
            },
            status = 400)
    
        return JsonResponse({
                "message": f"Unhandled error: {error}"
            },
            status = 500)
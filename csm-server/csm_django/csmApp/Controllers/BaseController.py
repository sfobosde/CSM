from .ApiErrors import *

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
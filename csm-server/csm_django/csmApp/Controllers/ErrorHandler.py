from .ApiErrors import UrlParametersError

from django.utils.datastructures import MultiValueDictKeyError

from django.http import JsonResponse

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
    
    return JsonResponse({
            "message": f"Unhandled error: {error}"
        },
        status = 400)
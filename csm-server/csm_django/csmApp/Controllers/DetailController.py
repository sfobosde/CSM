import json

from django.http import JsonResponse

from ..DTOModels.IDetailTemplate import *

from rest_framework.response import Response
from rest_framework.decorators import api_view

from types import SimpleNamespace

from .. import DBContext

from .BaseController import *

class DetailController(BaseController):
    # Handle request with detail objects.
    @staticmethod
    @api_view(["GET", "POST"])
    def handle_request(request):
        controller_objects = ["detail", "template"]

        response = JsonResponse({
            "message":"Action received but not handled."
        }, status=201)

        try:
            BaseController.validate_request(request=request, controller_objects = controller_objects)

            object = str(request.GET['object'])
            action = str(request.GET['action'])
        
            # Make action as detail template.
            if (object == 'template'):
                if action == "get":
                    response = DBContext.get_all_templates()
                else:
                    response = DetailController.handle_detail_template(request.body, action)
            
        except Exception as error:
            response = BaseController.handle_error(error)
    
        return response

    # Handle request related to detail template.
    @staticmethod
    def handle_detail_template(body, action) -> JsonResponse:
        detail_template: IDTOModel = json.loads(body, object_hook=lambda d: SimpleNamespace(**d))

        if action == "add":
            IDetailTemplate.validate(detail_template)
            detail_template = DBContext.create_detail_template(detail_template)

            return JsonResponse({"message":"Data received successfully"})



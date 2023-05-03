import json

from django.http import JsonResponse

from ..DTOModels.IDetailTemplate import IDTOModel
from ..DTOModels.IMaterial import IMaterial

from rest_framework.response import Response
from rest_framework.decorators import api_view

from types import SimpleNamespace

from .. import DBContext

from .BaseController import BaseController


class SheetMaterialController(BaseController):
    # Handle request with sheetmaterial objects.
    @staticmethod
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
            if (object == 'material'):
                response = SheetMaterialController.handle_material_request(request.body, action=action)
            

        except Exception as error:
            response = BaseController.handle_error(error)
    
        return response
    
    # Handle action with material
    @staticmethod
    def handle_material_request(body, action):
        response = JsonResponse({})

        material: IDTOModel = json.loads(body, object_hook=lambda d: SimpleNamespace(**d))

        if action == "add":
            IMaterial.validate(material)
            material = DBContext.create_material(material)
            return JsonResponse({"message":"Data received successfully"})

        if action == "get":
            response = DBContext.get_all_materials()

        return response
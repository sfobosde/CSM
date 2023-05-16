import json

from django.http import JsonResponse

from ..DTOModels.IDetailTemplate import IDTOModel
from ..DTOModels.IMaterial import IMaterial
from ..DTOModels.ISheetMaterial import ISheetMaterial

from rest_framework.response import Response
from rest_framework.decorators import api_view

from types import SimpleNamespace

from .. import DBContext

from .BaseController import BaseController


class SheetMaterialController(BaseController):
    # Get all materials.
    # /material/all.
    @staticmethod
    @api_view(["GET"])
    def get_all_materials(request):
        response = JsonResponse({}, status=201)

        try:
            response = DBContext.get_all_materials()
        except Exception as error:
            response = BaseController.handle_error(error)

        return response

    # Get all sheets.
    # /sheet/all.
    @staticmethod
    @api_view(["GET"])
    def get_all_sheet_materials(request):
        response = JsonResponse({}, status=201)

        try:
            response = DBContext.get_all_sheet_materials()
        except Exception as error:
            response = BaseController.handle_error(error)

        return response
    
    # Create new material
    # /material/add
    @staticmethod
    @api_view(["POST"])
    def create_material(request):
        response = JsonResponse({}, status = 201)

        try:
            material: IDTOModel = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))
            
            IMaterial.validate(material)

            material = DBContext.create_material(material)

            response = JsonResponse(data=material)
        except Exception as error:
            response = BaseController.handle_error(error)

        return response
    
    # Create new sheet
    # /sheet/add
    @staticmethod
    @api_view(["POST"])
    def create_sheet(request):
        response = JsonResponse({}, status = 201)

        try:
            sheet: IDTOModel = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))
            
            ISheetMaterial.validate(sheet)

            sheet = DBContext.create_sheet_material(sheet)

            response = JsonResponse(data=sheet)
        except Exception as error:
            response = BaseController.handle_error(error)

        return response
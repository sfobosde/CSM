import json

from django.http import JsonResponse

from ..DTOModels.IDetailTemplate import *
from ..DTOModels.IDetailParams import *

from rest_framework.response import Response
from rest_framework.decorators import api_view

from types import SimpleNamespace

from .. import DBContext

from .BaseController import *

class DetailController(BaseController):
    # Get all Templates.
    # /template/all
    @staticmethod
    @api_view(["GET"])
    def get_all_templates(request):
        response = JsonResponse({}, status=201)

        try:
            response = DBContext.get_all_templates()
        except Exception as error:
            response = BaseController.handle_error(error)

        return response
    
    # Get all details.
    # /detail/all
    @staticmethod
    @api_view(["GET"])
    def get_all_details(request):
        response = JsonResponse({}, status=201)

        try:
            response = DBContext.get_all_details()
        except Exception as error:
            response = BaseController.handle_error(error)

        return response

    # Create detail.
    # /detail/add
    @staticmethod
    @api_view(["POST"])
    def create_detail(request):
        response = JsonResponse({}, status = 201)

        try:
            detail: IDTOModel = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))
            
            IDetailParams.validate(detail)

            detail = DBContext.create_detail(detail)

            response = JsonResponse(data=detail)
        except Exception as error:
            response = BaseController.handle_error(error)

        return response
    
    # Create template.
    # /template/add
    @staticmethod
    @api_view(["POST"])
    def create_template(request):
        response = JsonResponse({}, status = 201)

        try:
            template: IDTOModel = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))
            
            IDetailTemplate.validate(template)

            template = DBContext.create_detail_template(template)

            response = JsonResponse(data=template)
        except Exception as error:
            response = BaseController.handle_error(error)

        return response


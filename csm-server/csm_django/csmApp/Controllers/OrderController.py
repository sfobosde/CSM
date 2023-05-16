import json

from django.http import JsonResponse

from ..DTOModels.IDetailTemplate import IDTOModel
from ..DTOModels.ICuttingOrder import ICuttingOrder

from rest_framework.response import Response
from rest_framework.decorators import api_view

from types import SimpleNamespace

from .. import DBContext

from .BaseController import BaseController

class OrderController(BaseController):
    # Get Orders List.
    # /order/all.
    @staticmethod
    @api_view(["GET"])
    def get_all_orders(request):
        response = JsonResponse({}, status=201)

        try:
            response = DBContext.get_all_orders()
        except Exception as error:
            response = BaseController.handle_error(error)

        return response

    # Add Order from request.
    # /order/add.
    @staticmethod
    @api_view(["POST"])
    def create_order(request):
        response = JsonResponse({}, status=201)

        try:
            order: IDTOModel = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))

            ICuttingOrder.validate(order)

            order = DBContext.create_order(order)
            response = JsonResponse({"id":order.id})
        except Exception as error:
            response = BaseController.handle_error(error)

        return response

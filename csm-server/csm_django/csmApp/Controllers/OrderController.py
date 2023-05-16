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
    # Handle request with order.
    @api_view(["GET", "POST"])
    @staticmethod
    def handle_request(request):
        controller_objects = ["order"]

        response = JsonResponse({
            "message":"Action received but not handled."
        }, status=201)

        try:
            BaseController.validate_request(request, controller_objects)

            object = str(request.GET['object'])
            action = str(request.GET['action'])

            if (object == 'order'):
                if (action == "get"):
                    response = DBContext.get_all_orders()
                else:
                    response = OrderController.handle_order_request(body=request.body, action=action)
        except Exception as Error:
            response = BaseController.handle_error(error=Error)

        return response
    
    @staticmethod
    def handle_order_request(body, action):
        response = JsonResponse({}, status=201)

        order: IDTOModel = json.loads(body, object_hook=lambda d: SimpleNamespace(**d))

        if action == "add":
            ICuttingOrder.validate(order)

            order = DBContext.create_order(order)
            response = JsonResponse({"message":"Data received successfully"})

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

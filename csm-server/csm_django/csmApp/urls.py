from . import views

from django.urls import path, re_path, include
from .Controllers.DetailController import DetailController
from .Controllers.SheetMaterialController import SheetMaterialController
from .Controllers.OrderController import OrderController

urlpatterns = [
    re_path(r'materials/$', SheetMaterialController.handle_request),

    # Create new detail.
    path("detail/add", DetailController.create_detail),
    # Create new detail.
    path("detail/all", DetailController.get_all_details),

    # Create new template.
    path("template/add", DetailController.create_template),
    # Get all templates.
    path("template/all", DetailController.get_all_templates),

    # Create order.
    path("order/add", OrderController.create_order),
    # Get Orders List.
    path("order/all", OrderController.get_all_orders),
    # Get Order by id
    re_path(r'order/$', OrderController.get_order)
]

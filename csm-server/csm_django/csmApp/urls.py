from . import views

from django.urls import path, re_path, include
from .Controllers.DetailController import DetailController
from .Controllers.SheetMaterialController import SheetMaterialController
from .Controllers.OrderController import OrderController

urlpatterns = [
    # Get all materials.
    path("material/all", SheetMaterialController.get_all_materials),
    # Create new material.
    path("material/add", SheetMaterialController.create_material),

    # Get all sheet materials.
    path("sheet/all", SheetMaterialController.get_all_sheet_materials),
    # Create new sheet material.
    path("sheet/add", SheetMaterialController.create_sheet),


    # Create new detail.
    path("detail/add", DetailController.create_detail),
    # Get all details.
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

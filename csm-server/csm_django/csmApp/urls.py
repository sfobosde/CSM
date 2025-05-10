from . import views
from .Controllers.metadata import get_model_metadata

from .DTOModels.IMaterial import IMaterial
from .DTOModels.ISheetMaterial import ISheetMaterial
from .DTOModels.IDetailParams import IDetailParams
from .DTOModels.IDetailTemplate import IDetailTemplate
from .DTOModels.ICuttingOrder import OrderDetail

from django.urls import path, re_path, include
from .Controllers.DetailController import DetailController
from .Controllers.SheetMaterialController import SheetMaterialController
from .Controllers.OrderController import OrderController

urlpatterns = [
    # Get all materials.
    path("material/all", SheetMaterialController.get_all_materials),
    # Create new material.
    path("material/add", SheetMaterialController.create_material),
    path("material/meta", get_model_metadata(IMaterial)),

    # Get all sheet materials.
    path("sheet/all", SheetMaterialController.get_all_sheet_materials),
    # Create new sheet material.
    path("sheet/add", SheetMaterialController.create_sheet),
    path("sheet/meta", get_model_metadata(ISheetMaterial)),


    # Create new detail.
    path("detail/add", DetailController.create_detail),
    # Get all details.
    path("detail/all", DetailController.get_all_details),
    path("detail/meta", get_model_metadata(IDetailParams)),


    # Create new template.
    path("template/add", DetailController.create_template),
    # Get all templates.
    path("template/all", DetailController.get_all_templates),
    path("template/meta", get_model_metadata(IDetailTemplate)),

    # Create order.
    path("order/add", OrderController.create_order),
    # Get Orders List.
    path("order/all", OrderController.get_all_orders),
    path("order/meta", get_model_metadata(OrderDetail)),

    # Get Order by id
    re_path(r'order/$', OrderController.get_order),
    # Generate cutting maps.
    re_path(r'order/create_maps$', OrderController.generate_maps)
]

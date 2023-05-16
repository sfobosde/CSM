from . import views

from django.urls import path, re_path, include
from .Controllers.DetailController import DetailController
from .Controllers.SheetMaterialController import SheetMaterialController
from .Controllers.OrderController import OrderController

urlpatterns = [
    re_path(r'details/$', DetailController.handle_request),
    re_path(r'materials/$', SheetMaterialController.handle_request),

    # Create order.
    path("order/add", OrderController.create_order),
    # Get Orders List.
    path("order/all", OrderController.get_all_orders),
]

from . import views

from django.urls import path, re_path, include
from .Controllers.DetailController import DetailController
from .Controllers.SheetMaterialController import SheetMaterialController
from .Controllers.OrderController import OrderController

urlpatterns = [
    re_path(r'details/$', DetailController.handle_request),
    re_path(r'materials/$', SheetMaterialController.handle_request),
    re_path(r'orders/$', OrderController.handle_request),
    re_path(r'orders/order/$', OrderController.get_order)
]

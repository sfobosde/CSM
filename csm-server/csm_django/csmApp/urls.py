from . import views

from django.urls import path, re_path, include
from .Controllers.DetailController import DetailController
from .Controllers.SheetMaterialController import SheetMaterialController

urlpatterns = [
    re_path(r'details/$', DetailController.handle_request),
    re_path(r'material/$', SheetMaterialController.handle_request),
]

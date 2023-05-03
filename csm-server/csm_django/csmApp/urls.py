from . import views

from django.urls import path, re_path, include
from .Controllers.DetailController import DetailController

urlpatterns = [
    re_path(r'details/$', DetailController.handle_request),
]

from .IDTOModel import IDTOModel
from .IDetailParams import IDetailParams

from .ICuttingOrder import IOrderDetail, ICuttingOrder

from ..Controllers.ApiErrors import *
import uuid
import datetime

from typing import List

class ICuttingOrder(IDTOModel):
    name: str
    orderDate: datetime.date
    details: List[IOrderDetail]

    @staticmethod
    def validate(order):
        if (not hasattr(order, "name") or not order.name):
            raise DataValidationError("Missed required parameter: name")
        
        if (not hasattr(order, "orderDate") or not order.orderDate):
            raise DataValidationError("Missed required parameter: orderDate")
        
        if (not hasattr(order, "details") 
            or not order.details):
            raise DataValidationError("Missed required parameter: name")
        
        if (len(order.details) < 1):
            raise DataValidationError("Order must contain minimum 1 detail.")
        
        

class IOrderDetail(IDTOModel):
    count: int

    @staticmethod
    def validate(orderDetail):
        if (not hasattr(orderDetail, "id") or not orderDetail.id):
            raise DataValidationError("Missed required parameter: id")
        
        if (not hasattr(orderDetail, "count") or not orderDetail.count):
            raise DataValidationError("Missed required parameter: count")
        
        if (orderDetail.count < 1):
            raise DataValidationError("Detail count minimal value: 1.")

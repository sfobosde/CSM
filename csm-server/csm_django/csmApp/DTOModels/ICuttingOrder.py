from .IDTOModel import IDTOModel

from ..Controllers.ApiErrors import *
import uuid
import datetime

class ICuttingOrder(IDTOModel):
    name: str
    orderDate: datetime.date
    details: list

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
        
        for detail in order.details:
            IOrderDetail.validate(detail)
        
        

class IOrderDetail(IDTOModel):
    count: int
    detail_id: uuid.uuid4

    @staticmethod
    def validate(orderDetail):
        if (not hasattr(orderDetail, "detail_id") or not orderDetail.detail_id):
            raise DataValidationError("Missed required parameter: detail_id")
        
        if (not hasattr(orderDetail, "count") or not orderDetail.count):
            raise DataValidationError("Missed required parameter: count")
        
        if (orderDetail.count < 1):
            raise DataValidationError("Detail count minimal value: 1.")
        


class OrderDetail(IOrderDetail):
    order_id: uuid.uuid4
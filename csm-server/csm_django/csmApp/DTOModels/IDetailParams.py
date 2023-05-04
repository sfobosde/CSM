from .IDTOModel import IDTOModel
from ..Controllers.ApiErrors import *
import uuid

class IDetailParams(IDTOModel):
    template_id: uuid
    material_id: uuid
    name: str
    addtitional_data: str

    @staticmethod
    def validate(detail):
        if (not hasattr(detail, "template_id") or not detail.template_id):
            raise DataValidationError("Missed required parameter: template_id")
        
        if (not hasattr(detail, "material_id") or not detail.material_id):
            raise DataValidationError("Missed required parameter: material_id")
        
        if (not hasattr(detail, "template_id") or not detail.template_id):
            raise DataValidationError("Missed required parameter: name")
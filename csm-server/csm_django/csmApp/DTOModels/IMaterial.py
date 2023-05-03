from .IDTOModel import IDTOModel
from ..Controllers.ApiErrors import *

class IMaterial(IDTOModel):
    name: str

    @staticmethod
    def validate(material):
        if (hasattr(material, "name") or not material.name):
            raise DataValidationError("Missed required parameter: name")

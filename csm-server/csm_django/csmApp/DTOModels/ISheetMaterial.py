from .IDTOModel import IDTOModel
from ..Controllers.ApiErrors import *
import uuid

# Model of seet material.
class ISheetMaterial(IDTOModel):
    lenght: int
    width: str
    fitness: int
    material_id: uuid

    @staticmethod
    def validate(sheet):
        # if (not hasattr(sheet, "length") or not sheet.length):
        #     raise DataValidationError("Missed required parameter: length")
    
        if (not hasattr(sheet, "width") or not sheet.width):
            raise DataValidationError("Missed required parameter: width")

        if (not hasattr(sheet, "fitness") or not sheet.fitness):
            raise DataValidationError("Missed required parameter: fitness")
        
        if (not hasattr(sheet, "material_id") or not sheet.material_id):
            raise DataValidationError("Missed required parameter: material_id")
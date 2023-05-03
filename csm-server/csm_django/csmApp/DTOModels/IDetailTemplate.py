from .IDTOModel import *
from ..Controllers.ApiErrors import *

# Interface to serialize DetailTemplate from json.
class IDetailTemplate(IDTOModel):
    file_link: str
    name: str
    length: int
    width: int
    fitness: int
    additional_data: str

    # Validate required fields.
    @staticmethod
    def validate(template):
        if (not hasattr(template, "name") or not template.name):
            raise DataValidationError("Missed required parameter: name")

        if (not hasattr(template, "length") or not template.length):
            raise DataValidationError("Missed required parameter: length")
    
        if (not hasattr(template, "width") or not template.width):
            raise DataValidationError("Missed required parameter: width")

        if (not hasattr(template, "fitness") or not template.fitness):
            raise DataValidationError("Missed required parameter: fitness")

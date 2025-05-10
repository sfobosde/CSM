import json
import typing
from dataclasses import dataclass, field
from typing import Any, List, get_type_hints, get_origin, get_args
from django.http import JsonResponse
from rest_framework.decorators import api_view
import uuid

@dataclass
class FieldInfo:
    code: str
    type: str
    isArray: bool

    def to_dict(self):
        return {
            "code": self.code,
            "type": self.type,
            "isArray": self.isArray,
        }


def class_to_json_field_info(cls: type) -> str:
    """
    Analyzes a class and returns a JSON string representing its fields.

    Args:
        cls: The class to analyze.

    Returns:
        A JSON string containing an array of objects, where each object
        describes a field in the class with the properties:
        "code" (str): The name of the field.
        "type" (str): The type of the field.
        "isArray" (bool): Whether the field is an array (List/typing.List).
    """

    field_infos: List[FieldInfo] = []
    type_hints = get_type_hints(cls)

    for code, hinted_type in type_hints.items():
        is_array = False
        field_type_str = get_readable_type_name(hinted_type) # Use the helper function

        origin = get_origin(hinted_type)
        args = get_args(hinted_type)

        if origin is list or origin is typing.List:
            is_array = True
            if args:
                element_type = args[0]
                field_type_str = get_readable_type_name(element_type)  # Type of elements

            else:
                field_type_str = "any" # Lowercase for consistency

        field_info = FieldInfo(
            code=code,
            type=field_type_str,
            isArray=is_array,
        )
        field_infos.append(field_info)

    # Convert list of dataclass instances to a list of dictionaries
    field_infos_dict = [fi.to_dict() for fi in field_infos]

    return json.dumps(field_infos_dict, indent=4)  # indent for readability


def get_readable_type_name(type_hint: type) -> str:
    """
    Returns a human-readable string representation of a type hint.
    """
    if type_hint is str:
        return "string"  # Lowercase for consistency
    elif type_hint is int:
        return "integer"  # Lowercase
    elif type_hint is float:
        return "number"   # More generic term for JSON
    elif type_hint is bool:
        return "boolean"  # Lowercase
    elif type_hint is Any:
        return "any"      # Lowercase
    else:
        return "any"  # Fallback
    
def get_model_metadata(model: type):
    print("get_model_metadata")
    @api_view(["GET"])
    def get_metadata(request: any):
        print("get_metadata")
        try:
            json_data = class_to_json_field_info(model)  # Call your function
            # Parse JSON to ensure it is a valid JSON object before sending the response
            data = json.loads(json_data)
            return JsonResponse(data=data, safe=False, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return get_metadata
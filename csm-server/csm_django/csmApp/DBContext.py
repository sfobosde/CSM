from .models import *
from .DTOModels import IDetailTemplate
from .DTOModels import IMaterial
from .DTOModels import ISheetMaterial
from .DTOModels import IDetailParams
from .DTOModels import IDTOModel

import uuid

from .serializer import *

from rest_framework.response import Response

from .Controllers.ApiErrors import *

from django.db import models

# Create new Detail template in database.
def create_detail_template(detail_template: IDetailTemplate.IDetailTemplate) -> IDetailTemplate.IDetailTemplate:
    detail_template.id = uuid.uuid4()

    db_template = DetailTemplate.objects.create(id=detail_template.id)

    update_detail_template_data(detail_template, db_template)
    
    return detail_template

# Update of existing db template.
def update_detail_template_data(template: IDetailTemplate.IDetailTemplate, db_template: DetailTemplate):
    db_template.name = template.name or ""
    db_template.length = template.length or 0
    db_template.width = template.width or 0
    db_template.fitness = template.fitness or 0

    if (hasattr(template, "file_link") and template.file_link):
        db_template.file_link = template.file_link

    if (hasattr(template, "additional_data") and template.additional_data):
        db_template.additional_data = template.additional_data

    db_template.save()

# Get list of all detail templates
def get_all_templates():
    templates =  DetailTemplate.objects.all()

    serializer = DetailTemplateSerializer(templates, many=True)

    return Response(serializer.data)

# Create new Material object
def create_material(material: IMaterial.IMaterial) -> IMaterial.IMaterial:
    material.id = uuid.uuid4()

    db_material = Material.objects.create(id=material.id)

    update_material_data(material, db_material)

    return material

# Update of existing db material.
def update_material_data(material: IMaterial.IMaterial, db_material: Material):
    db_material.name = material.name

    db_material.save()

# Get list of all detail templates
def get_all_materials():
    materials =  Material.objects.all()

    serializer = MaterialSerializer(materials, many=True)

    return Response(serializer.data)

# Create new sheet Material object
def create_sheet_material(sheet_material: ISheetMaterial.ISheetMaterial) -> ISheetMaterial.ISheetMaterial:
    sheet_material.id = uuid.uuid4()

    db_material = SheetMaterialParams.objects.create(id=sheet_material.id)

    update_sheet_material_data(sheet_material, db_material)

    return sheet_material

# Updating sheet material data.
def update_sheet_material_data(sheet_material: ISheetMaterial.ISheetMaterial, db_sheet_material: SheetMaterialParams):
    # Try find 
    if (is_object_exists(Material, sheet_material.material_id)):
        db_sheet_material.material_id = sheet_material.material_id

        db_sheet_material.length = sheet_material.lenght
        db_sheet_material.width = sheet_material.width
        db_sheet_material.fitness = sheet_material.fitness

        db_sheet_material.save()
    else:
        raise NonExistValue(f"No material with id:{sheet_material.material_id}")

# Check object exists id db by id.
def is_object_exists(model: models.Model, id) -> bool:
    try:
        model.objects.get(id=id)

        return True
    except:
        return False

# Get list of all detail templates.
def get_all_sheet_materials():
    sheets =  SheetMaterialParams.objects.all()

    serializer = SheetMaterialParamsSerializer(sheets, many=True)
    
    return Response(serializer.data)

# Create detail from templte and meterial id.
def create_detail(detail: IDetailParams.IDetailParams):
    detail.id = uuid.uuid4()

    db_detail = DetailParameters.objects.create(id = detail.id)

    update_detail_data(detail, db_detail)

    return detail

# Update exists detail data.
def update_detail_data(detail: IDetailParams.IDetailParams, db_detail: DetailParameters):
    if (not is_object_exists(DetailTemplate, detail.template_id)):
        raise NonExistValue(f"No template with id:{detail.template_id}")
    
    if (not is_object_exists(Material, detail.material_id)):
        raise NonExistValue(f"No material with id:{detail.material_id}")
    
    db_detail.template_id = detail.template_id
    db_detail.material_id = detail.material_id
    db_detail.name = detail.name

    if (hasattr(detail, "addtitional_data") and detail.additional_data):
        db_detail.additional_data = detail.addtitional_data

    db_detail.save()

# Get list of all details.
def get_all_details():
    details =  DetailParameters.objects.all()

    serializer = DetailParametersSerializer(details, many=True)
    
    return Response(serializer.data)
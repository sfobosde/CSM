from .models import *
from .DTOModels import IDetailTemplate
import uuid

from .serializer import *

from rest_framework.response import Response

# Create new Detail template in database.
def create_detail_template(detail_template: IDetailTemplate.IDetailTemplate) -> IDetailTemplate.IDetailTemplate:
    detail_template.id = uuid.uuid4()

    db_template = DetailTemplate.objects.create(id=detail_template.id)

    update_detail_template_data(detail_template, db_template)
    
    return detail_template

# Update of existing db entity.
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
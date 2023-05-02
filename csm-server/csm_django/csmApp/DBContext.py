from .models import *
from .DTOModels import IDetailTemplate
import uuid

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

    try:
        db_template.file_link = template["file_link"] or ""
    except:
        pass

    try:
        db_template.additional_data = template["additional_data"] or ""
    except:
        pass

    db_template.save()
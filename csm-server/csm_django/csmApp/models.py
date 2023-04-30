from django.db import models
import uuid

# Шаблон детали.
class DetailTemplate(models.Model):
    # ID шаблона детали.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Ссылка на файл детали.
    file_link = models.CharField(max_length=100, blank=False, default = '', null=True)

    # Название детали.
    name = models.CharField(max_length=100, blank=False, default='', null=True)

    # Длина детали.
    length = models.IntegerField()

    # Ширина детали.
    width = models.IntegerField()

    # Толщина детали.
    fitness = models.IntegerField()

    # Дополнительные данные о детали.
    additional_data = models.CharField(max_length=100, blank=False, default='', null=True)
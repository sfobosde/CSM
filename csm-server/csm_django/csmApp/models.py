from django.db import models
import uuid

# Detail template.
class DetailTemplate(models.Model):
    # ID of template.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Model file link.
    file_link = models.CharField(max_length=100, blank=False, default = '', null=True)

    # Template name.
    name = models.CharField(max_length=100, blank=False, default='', null=True)

    # Detail length.
    length = models.IntegerField(null=True)

    # Detail width.
    width = models.IntegerField(null=True)

    # Detail fitness.
    fitness = models.IntegerField(null=True)

    # Addition data might be as json or text.
    additional_data = models.CharField(max_length=100, blank=False, default='', null=True)


# Detail params.
class DetailParameters(models.Model):
    # Detail id.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Detail template id.
    template_id = models.UUIDField(null=True)

    # Material id.
    material_id = models.UUIDField(null=True)

    # Detail name.
    name = models.CharField(max_length=100, blank=False, default='', null=True)

    # Addition data might be as json or text.
    additional_data = models.CharField(max_length=100, blank=False, default='', null=True)


# Materials.
class Materials(models.Model):
    # Material id.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Material name.
    name = models.CharField(max_length=100, blank=False, default='', null=True)


# Sheet material params.
class SheetMaterialParams(models.Model):
    # Sheet id.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Sheet length.
    length = models.IntegerField(null=True)

    # Sheet width.
    width = models.IntegerField(null=True)

    # Sheet fitness.
    fitness = models.IntegerField(null=True)

    # Material id.
    material_id = models.UUIDField(null=True)


# Detail arranging on map.
class DetailMapArranging(models.Model):
    # Arrange id.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Map detail arranged on
    map_id = models.UUIDField(null=True)

    # The detail id.
    detail_id = models.UUIDField(null=True)

    # X axes start coordinate.
    x_coord = models.IntegerField(null=True)

    # Y axes start coordinate.
    y_coord = models.IntegerField(null=True)

    # Rotating angel.
    rotating = models.IntegerField(null=True)


# Cutting map.
class CuttingMap(models.Model):
    # Map id.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Sheet id.
    sheet_id = models.UUIDField(null=True)

    # Square of map captured rectangle.
    square = models.IntegerField(null=True)

    # Refuse as unused material
    refuse_square = models.IntegerField(null=True)


# Details in cutting order.
class OrderDetails(models.Model):
    # Order detail as item of collection id.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Order id.
    order_id = models.UUIDField(null=True)

    # Detail id.
    detail_id = models.UUIDField(null=True)

    # Current detail count in order.
    detail_count = models.IntegerField(null=True)


# Cutting Order.
class CuttingOrder(models.Model):
    # Orderd id.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Order name.
    name = models.CharField(max_length=100, blank=False, default='', null=True)

    # Execution date.
    date = models.DateField(null=True)

    # order status id.
    status_id = models.UUIDField(null=True)


# Cuttin maps in order.
class CuttingMapInOrder(models.Model):
    # Id of cutting map arrangement in order.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Order id.
    order_id = models.UUIDField(null=True)

    # Map id.
    map_id = models.UUIDField(null=True)


# Order Status.
class OrderStatus(models.Model):
    # Status id.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Status name.
    name = models.CharField(max_length=100, blank=False, default='', null=True)

from rest_framework import serializers
import csmApp.models as model

# Detail templates.
class DetailTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.DetailTemplate
        fields = ('id', 
                  'file_link',
                  'name',
                  'length',
                  'width',
                  'fitness',
                  'additional_data')

# Detail Parameters.
class DetailParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.DetailParameters
        fields = ('id', 
                  'template_id',
                  'material_id',
                  'name',
                  'additional_data')

# Materials.        
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.Materials
        fields = ('id', 
                  'name')
        
# Sheet materials.
class SheetMaterialParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.SheetMaterialParams
        fields = ('id', 
                  'length',
                  'width',
                  'fitness',
                  'material_id')

# Detail positions on map.        
class DetailMapArrangingSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.DetailMapArranging
        fields = ('id', 
                  'map_id',
                  'detail_id',
                  'x_coord',
                  'y_coord',
                  'rotating')
        
# Cutting maps data.
class CuttingMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.CuttingMap
        fields = ('id', 
                  'sheet_id',
                  'square',
                  'refuse_square')

# Detail list to cutting for order.
class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.OrderDetails
        fields = ('id', 
                  'order_id',
                  'detail_id',
                  'detail_count')

# Cutting order.
class CuttingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.CuttingOrder
        fields = ('id', 
                  'name',
                  'date',
                  'status_id')

# Cutting maps in order.
class CuttingMapInOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.CuttingMapInOrder
        fields = ('id', 
                  'order_id',
                  'map_id')

# Order statuses.
class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.OrderStatus
        fields = ('id', 
                  'name')

from rest_framework import serializers
import csmApp.models as model

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
        
class DetailParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.DetailParameters
        fields = ('id', 
                  'template_id',
                  'material_id',
                  'name',
                  'additional_data')
        
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.DetailParameters
        fields = ('id', 
                  'name')
        
class SheetMaterialParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.DetailParameters
        fields = ('id', 
                  'length',
                  'width',
                  'fitness',
                  'material_id')
        
class DetailMapArrangingSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.DetailParameters
        fields = ('id', 
                  'map_id',
                  'detail_id',
                  'x_coord',
                  'y_coord',
                  'rotating')
        
class CuttingMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.DetailParameters
        fields = ('id', 
                  'sheet_id',
                  'square',
                  'refuse_square')
        
class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.DetailParameters
        fields = ('id', 
                  'order_id',
                  'detail_id',
                  'detail_count')
        
class CuttingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.DetailParameters
        fields = ('id', 
                  'name',
                  'date',
                  'status_id')
        
class CuttingMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.DetailParameters
        fields = ('id', 
                  'order_id',
                  'map_id')
        
class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.DetailParameters
        fields = ('id', 
                  'name')

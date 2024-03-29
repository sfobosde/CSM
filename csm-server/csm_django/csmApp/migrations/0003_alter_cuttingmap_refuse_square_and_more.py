# Generated by Django 4.2 on 2023-05-02 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csmApp', '0002_cuttingmap_cuttingmapinorder_cuttingorder_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuttingmap',
            name='refuse_square',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cuttingmap',
            name='sheet_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='cuttingmap',
            name='square',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cuttingmapinorder',
            name='map_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='cuttingmapinorder',
            name='order_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='cuttingorder',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='cuttingorder',
            name='status_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='detailmaparranging',
            name='detail_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='detailmaparranging',
            name='map_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='detailmaparranging',
            name='rotating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='detailmaparranging',
            name='x_coord',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='detailmaparranging',
            name='y_coord',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='detailparameters',
            name='material_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='detailparameters',
            name='template_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='detailtemplate',
            name='fitness',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='detailtemplate',
            name='length',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='detailtemplate',
            name='width',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='detail_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='detail_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='order_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='sheetmaterialparams',
            name='fitness',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheetmaterialparams',
            name='length',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheetmaterialparams',
            name='material_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='sheetmaterialparams',
            name='width',
            field=models.IntegerField(null=True),
        ),
    ]

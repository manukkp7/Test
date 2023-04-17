from rest_framework import serializers
from appmcc.models import District, Taluka, Village, Proponent, Boundingsurvey, Plotlocalbody, Plotsurveynumloc, Document, Fieldinspection, Dronesurveydetails, Quantification, Payment


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = District
        fields = "__all__"


class TalukaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Taluka
        fields = "__all__"


class VillageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Village
        fields = "__all__"


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proponent
        fields = "__all__"


class ProponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proponent
        fields = "__all__"


class BoundingsurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boundingsurvey
        fields = "__all__"


class PlotlocalbodySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plotlocalbody
        fields = "__all__"


class PlotsurveynumlocSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plotsurveynumloc
        fields = "__all__"


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"


class FieldinspectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fieldinspection
        fields = "__all__"


class DronesurveydetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dronesurveydetails
        fields = "__all__"


class QuantificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quantification
        fields = "__all__"


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

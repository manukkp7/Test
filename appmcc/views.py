from django.shortcuts import render
from rest_framework import viewsets
from appmcc.models import District, Taluka, Village, Proponent, Boundingsurvey, Plotlocalbody, Plotsurveynumloc, Document, Fieldinspection, Dronesurveydetails, Quantification, Payment
from appmcc.serializers import DistrictSerializer, TalukaSerializer, VillageSerializer, ProponentSerializer, BoundingsurveySerializer, PlotlocalbodySerializer, PlotsurveynumlocSerializer, DocumentSerializer, FieldinspectionSerializer, DronesurveydetailsSerializer, QuantificationSerializer, PaymentSerializer
# Create your views here.


def home(request):
    return render(request, 'home.html')


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class TalukaViewSet(viewsets.ModelViewSet):
    queryset = Taluka.objects.all()
    serializer_class = TalukaSerializer


class VillageViewSet(viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer


class ProponentViewSet(viewsets.ModelViewSet):
    queryset = Proponent.objects.all()
    serializer_class = ProponentSerializer


class BoundingsurveyViewSet(viewsets.ModelViewSet):
    queryset = Boundingsurvey.objects.all()
    serializer_class = BoundingsurveySerializer


class PlotlocalbodyViewSet(viewsets.ModelViewSet):
    queryset = Plotlocalbody.objects.all()
    serializer_class = PlotlocalbodySerializer


class PlotsurveynumlocViewSet(viewsets.ModelViewSet):
    queryset = Plotsurveynumloc.objects.all()
    serializer_class = PlotsurveynumlocSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class FieldinspectionViewSet(viewsets.ModelViewSet):
    queryset = Fieldinspection.objects.all()
    serializer_class = FieldinspectionSerializer


class DronesurveydetailsViewSet(viewsets.ModelViewSet):
    queryset = Dronesurveydetails.objects.all()
    serializer_class = DronesurveydetailsSerializer


class QuantificationViewSet(viewsets.ModelViewSet):
    queryset = Quantification.objects.all()
    serializer_class = QuantificationSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

from . import views
from appmcc.views import DistrictViewSet, TalukaViewSet, VillageViewSet, ProponentViewSet, BoundingsurveyViewSet, PlotlocalbodyViewSet, PlotsurveynumlocViewSet, DocumentViewSet, FieldinspectionViewSet, DronesurveydetailsViewSet, QuantificationViewSet, PaymentViewSet
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'district/', DistrictViewSet)
router.register(r'taluka', TalukaViewSet)
router.register(r'village', VillageViewSet)
router.register(r'proponent', ProponentViewSet)
router.register(r'boundingsurvey', BoundingsurveyViewSet)
router.register(r'plotlocalbody', PlotlocalbodyViewSet)
router.register(r'plotsurveynumloc', PlotsurveynumlocViewSet)
router.register(r'document', DocumentViewSet)
router.register(r'fieldinspection', BoundingsurveyViewSet)
router.register(r'dronesurveydetails', DronesurveydetailsViewSet)
router.register(r'quantification', QuantificationViewSet)
router.register(r'payment', PaymentViewSet)

urlpatterns = [
    path('api', include(router.urls), name="api"),
    path('', views.home, name='home')

]

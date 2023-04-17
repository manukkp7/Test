from django.contrib import admin
from .models import Payment, Plotlocalbody, Plotsurveynumloc, Proponent, Fieldinspection, Quantification, Dronesurveydetails, Document, Boundingsurvey, District, Taluka, Village

admin.site.register(District)
admin.site.register(Taluka)
admin.site.register(Village)
admin.site.register(Proponent)
admin.site.register(Fieldinspection)
admin.site.register(Quantification)
admin.site.register(Dronesurveydetails)
admin.site.register(Document)
admin.site.register(Boundingsurvey)
admin.site.register(Plotsurveynumloc)
admin.site.register(Plotlocalbody)
admin.site.register(Payment)

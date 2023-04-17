from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.datetime_safe import datetime
# Create your models here.


class District(models.Model):
    district_name = models.CharField(max_length=50)
    district_cd = models.CharField(max_length=5)

    def __str__(self):
        return self.district_name


class Taluka(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    taluka_name = models.CharField(max_length=50)

    def __str__(self):
        return self.taluka_name


class Village(models.Model):
    taluka = models.ForeignKey(Taluka, on_delete=models.CASCADE, null=True)
    village_name = models.CharField(max_length=50)

    def __str__(self):
        return self.village_name


class Proponent(models.Model):

    frn = models.IntegerField(null=True, blank=True)
    applicationtype = models.IntegerField(null=True, blank=True)
    concessiontype = models.IntegerField(null=True, blank=True)
    fileno = models.CharField(max_length=250, null=True, blank=True)
    username = models.CharField(max_length=250, null=True, blank=True)
    typeofuser = models.CharField(max_length=250, null=True, blank=True)
    officename = models.CharField(max_length=250, null=True, blank=True)
    nameenglish = models.CharField(max_length=250, null=True, blank=True)
    namemalayalam = models.CharField(max_length=250, null=True, blank=True)
    gender = models.CharField(max_length=250, null=True, blank=True)
    mobilenumber = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    phonenumber = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=250, null=True, blank=True)
    pannumber = models.CharField(max_length=250, null=True, blank=True)
    profession = models.IntegerField(null=True, blank=True)
    gstnumber = models.CharField(max_length=250, null=True, blank=True)
    comaddressline1 = models.CharField(max_length=250, null=True, blank=True)
    comaddressline2 = models.CharField(max_length=250, null=True, blank=True)
    comaddressline3 = models.CharField(max_length=250, null=True, blank=True)
    comaddressstate = models.CharField(max_length=250, null=True, blank=True)
    comaddressdistrict = models.ForeignKey(
        District, related_name='comdis', on_delete=models.CASCADE, null=True)
    comaddressspincode = models.CharField(
        max_length=250, null=True, blank=True)
    peraddressline1 = models.CharField(max_length=250, null=True, blank=True)
    peraddressline2 = models.CharField(max_length=250, null=True, blank=True)
    peraddressline3 = models.CharField(max_length=250, null=True, blank=True)
    peraddressstate = models.CharField(max_length=250, null=True, blank=True)
    peraddressdistrict = models.ForeignKey(
        District, related_name='perdis', on_delete=models.CASCADE, null=True)
    peraddressspincode = models.CharField(
        max_length=250, null=True, blank=True)
    landownership = models.CharField(max_length=250, null=True, blank=True)
    mineral = models.IntegerField(null=True, blank=True)
    royaltytype = models.IntegerField(null=True, blank=True)
    quantitytobeextracted = models.IntegerField(null=True, blank=True)
    unit = models.IntegerField(null=True, blank=True)
    utilizationmanner = models.CharField(max_length=250, null=True, blank=True)
    requestedperiodofpermityear = models.IntegerField(null=True, blank=True)
    requestedperiodofpermitmonth = models.IntegerField(null=True, blank=True)
    requestedperiodofpermitday = models.IntegerField(null=True, blank=True)
    majorlandmark = models.CharField(max_length=250, null=True, blank=True)
    locationname = models.CharField(max_length=250, null=True, blank=True)
    policestation = models.CharField(max_length=250, null=True, blank=True)
    financialresouces = models.CharField(max_length=250, null=True, blank=True)
    shortestroutetoquarry = models.CharField(
        max_length=250, null=True, blank=True)
    applicationstatus = models.CharField(max_length=250, null=True, blank=True)
    docrevenuedept = models.CharField(max_length=250, null=True, blank=True)
    docrmcu = models.CharField(max_length=250, null=True, blank=True)
    docshowingloc = models.CharField(max_length=250, null=True, blank=True)
    docminingplan = models.CharField(max_length=250, null=True, blank=True)
    docclearance = models.CharField(max_length=250, null=True, blank=True)


class Boundingsurvey(models.Model):

    frn = models.ForeignKey(Proponent, on_delete=models.CASCADE, null=True)
    ploteastdistrict = models.ForeignKey(
        District, related_name='eastdistrict', on_delete=models.CASCADE, null=True)
    ploteasttaluk = models.ForeignKey(
        Taluka, related_name='easttaluka', on_delete=models.CASCADE, null=True)
    ploteastvillage = models.ForeignKey(
        Village, related_name='eastvillage', on_delete=models.CASCADE, null=True)
    ploteastsurveyno = models.CharField(max_length=250, null=True, blank=True)
    ploteastresurveyno = models.CharField(
        max_length=250, null=True, blank=True)
    ploteastblockno = models.CharField(max_length=250, null=True, blank=True)
    plotnorthdistrict = models.ForeignKey(
        District, related_name='northdistrict', on_delete=models.CASCADE, null=True)
    plotnorthtaluk = models.ForeignKey(
        Taluka, related_name='northtaluka', on_delete=models.CASCADE, null=True)
    plotnorthvillage = models.ForeignKey(
        Village, related_name='northvillage', on_delete=models.CASCADE, null=True)
    plotnorthsurveyno = models.CharField(max_length=250, null=True, blank=True)
    plotnorthresurveyno = models.CharField(
        max_length=250, null=True, blank=True)
    plotnorthblockno = models.CharField(max_length=250, null=True, blank=True)
    plotsouthdistrict = models.ForeignKey(
        District, related_name='southdistrict', on_delete=models.CASCADE, null=True)
    plotsouthtaluk = models.ForeignKey(
        Taluka, related_name='southtaluka', on_delete=models.CASCADE, null=True)
    plotsouthvillage = models.ForeignKey(
        Village, related_name='southvillage', on_delete=models.CASCADE, null=True)
    plotsouthsurveyno = models.CharField(max_length=250, null=True, blank=True)
    plotsouthresurveyno = models.CharField(
        max_length=250, null=True, blank=True)
    plotsouthblockno = models.CharField(max_length=250, null=True, blank=True)
    plotwestdistrict = models.ForeignKey(
        District, related_name='westdistrict', on_delete=models.CASCADE, null=True)
    plotwesttaluk = models.ForeignKey(
        Taluka, related_name='westtaluka', on_delete=models.CASCADE, null=True)
    plotwestvillage = models.ForeignKey(
        Village, related_name='westvillage', on_delete=models.CASCADE, null=True)
    plotwestsurveyno = models.CharField(max_length=250, null=True, blank=True)
    plotwestresurveyno = models.CharField(
        max_length=250, null=True, blank=True)
    plotwestblockno = models.CharField(max_length=250, null=True, blank=True)


class Plotlocalbody(models.Model):

    frn = models.ForeignKey(Proponent, on_delete=models.CASCADE, null=True)
    localbodydistrict = models.ForeignKey(
        District, on_delete=models.CASCADE, null=True)
    localbodytype = models.CharField(max_length=250, null=True, blank=True)
    localbody = models.IntegerField(null=True, blank=True)
    localbodyblock = models.CharField(max_length=250, null=True, blank=True)


class Plotsurveynumloc(models.Model):

    frn = models.ForeignKey(
        Proponent, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, null=True)
    taluk = models.ForeignKey(Taluka, on_delete=models.CASCADE, null=True)
    village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True)
    surveyno = models.CharField(max_length=250, null=True, blank=True)
    resurveyno = models.CharField(max_length=250, null=True, blank=True)
    blockno = models.CharField(max_length=250, null=True, blank=True)
    miningarea = models.CharField(max_length=250, null=True, blank=True)
    tenureofland = models.CharField(max_length=250, null=True, blank=True)
    ownername = models.CharField(max_length=250, null=True, blank=True)
    owneraddress = models.CharField(max_length=250, null=True, blank=True)


class Document(models.Model):

    frn = models.ForeignKey(
        Proponent, on_delete=models.CASCADE, null=True)
    documentname = models.CharField(max_length=250, null=True, blank=True)
    documentlink = models.CharField(max_length=250, null=True, blank=True)


class Fieldinspection(models.Model):

    frn = models.ForeignKey(
        Proponent, on_delete=models.CASCADE, null=True)
    lat = models.FloatField(max_length=250, blank=True, null=True)
    log = models.FloatField(max_length=250, blank=True, null=True)
    coments = models.CharField(max_length=250, null=True, blank=True)


class Dronesurveydetails(models.Model):

    frn = models.ForeignKey(
        Proponent, on_delete=models.CASCADE, null=True)
    date = models.CharField(max_length=250, blank=True, null=True)
    teamid = models.IntegerField(blank=True, null=True)


class Quantification(models.Model):

    frn = models.ForeignKey(
        Proponent, on_delete=models.CASCADE, null=True)
    dronsurvey = models.ForeignKey(
        Dronesurveydetails, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(blank=True, null=True)


class Payment(models.Model):

    frn = models.ForeignKey(
        Proponent, on_delete=models.CASCADE, null=True)
    dronsurvey = models.ForeignKey(
        Dronesurveydetails, on_delete=models.CASCADE, null=True)
    gateway = models.CharField(max_length=250, blank=True, null=True)
    amount = models.FloatField(max_length=250, null=True, blank=True)

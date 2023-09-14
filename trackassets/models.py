from django.db import models
from django.contrib.auth.models import User


class Asset(models.Model):
    '''
    this is the assets table (Database model classs)
    '''
    assetsName = models.CharField(max_length=255)

    def __str__(self):
        return self.assetsName


class Company(models.Model):
    '''
    company table for storing company information
    '''
    owner = models.OneToOneField(User, related_name='company', on_delete=models.CASCADE, default=None)
    companyName = models.CharField(max_length=255, unique=True, db_index=True)
    address = models.CharField(max_length=255, blank=False)
    employee = models.ManyToManyField(User, related_name="employees")
    asset = models.ManyToManyField(Asset)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.companyName.title()


class EmployeeAssets(models.Model):
    employee = models.ForeignKey(User, related_name='employeeasset', on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    provideDate = models.DateField(auto_now_add=True)
    qualityWhenProvided = models.CharField(max_length=255, blank=False)
    returnDate = models.DateField(blank=False)
    qualityWhenReturn = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return '{}, {}, {}, {}'.format(self.employee, self.asset, self.provideDate, self.returnDate)


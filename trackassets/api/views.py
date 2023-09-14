from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    CompanySerializer, UserSerializer, 
    ProvideAssetsSerializer, ReturAssetsToCompanySerializer, 
    EmployeeAssetsDetailsSerializer
)
from . permissions import IsCompanyOwner

from .. models import Asset, EmployeeAssets


class CompanyCreateApiView(generics.CreateAPIView):

    '''
    Craete Company 
    '''

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    serializer_class = CompanySerializer


class UserCreateApiView(generics.CreateAPIView):
    '''
    craete User
    '''
    serializer_class = UserSerializer


class HireEmployeeApiView(APIView):

    '''
    Hire employee for company, this work done by the company owner with authentication
    '''

    permission_classes = [IsAuthenticated, IsCompanyOwner]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request):
        employeeIdList = request.data.get('employee', None)

        if employeeIdList is None or type(employeeIdList) is not list:
            return Response({'employee': '[List of employee id is required.]'}, status=status.HTTP_400_BAD_REQUEST)
        company = self.request.user.company

        for employeeId in employeeIdList:
            company.employee.add(employeeId)
        return Response({'success': True}, status=status.HTTP_200_OK)


class AddCompanyAsset(HireEmployeeApiView):
    
    '''
    add new assets in a company, also this work done by the company owner
    '''

    def post(self, request):
        employeeIdList = request.data.get('assetsName', None)

        if employeeIdList is None or type(employeeIdList) is not list:
            return Response({'assetsName': '[List of assets name is required.]'}, status=status.HTTP_400_BAD_REQUEST)
        
        company = self.request.user.company
        for assetName in employeeIdList:
            asset = Asset.objects.create(assetsName=assetName)
            company.asset.add(asset.pk)
        return Response({'success': True}, status=status.HTTP_200_OK)


class ProvideAssetToEmployee(CompanyCreateApiView):


    '''
    provide the the assests for each company erployee, with the assets quality
    '''
    permission_classes = [IsAuthenticated, IsCompanyOwner]
    serializer_class = ProvideAssetsSerializer



class ReturnAssetToCompany(APIView):

    '''
    return the assets from the employee to the company with  the assets Quality
    '''

    permission_classes = [IsAuthenticated, IsCompanyOwner]
    authentication_classes = [TokenAuthentication, ]
    serializer_class = ReturAssetsToCompanySerializer

    def patch(self, request, *args, **kwargs):
        asset = EmployeeAssets.objects.get(pk=kwargs['id'])
       
        serializer = ReturAssetsToCompanySerializer(instance=asset, data=request.data)
        if serializer.is_valid(raise_exception=True):
            asset.qualityWhenReturn = serializer.validated_data['qualityWhenReturn']
            asset.save()
            serializer = ProvideAssetsSerializer(instance=asset)
            return Response(serializer.data, status=status.HTTP_200_OK)
          
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AssetTrackingApiView(generics.ListAPIView):

    ''''
    tracking the assets based on the company, each company only show owne assets
    '''

    permission_classes = [IsAuthenticated, IsCompanyOwner]
    authentication_classes = [TokenAuthentication, ]

    serializer_class = EmployeeAssetsDetailsSerializer

    def get_queryset(self):
        company = self.request.user.company
        return EmployeeAssets.objects.filter(employee__company__companyName=company)


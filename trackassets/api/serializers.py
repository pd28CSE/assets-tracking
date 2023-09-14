from django.contrib.auth.models import User

from rest_framework import serializers

from ..models import Company, EmployeeAssets, Asset

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ['asset', 'employee', ]


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        exclude = ['last_login', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions']


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user



class ProvideAssetsSerializer(serializers.ModelSerializer):
    returnDate = serializers.DateField()
    
    class Meta:
        model = EmployeeAssets
        fields = '__all__'



class ReturAssetsToCompanySerializer(serializers.Serializer):
    
    qualityWhenReturn = serializers.CharField(max_length=255)



class EmployeeAssetsDetailsSerializer(serializers.ModelSerializer):
    asset = AssetSerializer()
    employee = UserSerializer()
    class Meta:
        model = EmployeeAssets
        fields = '__all__'
from django.urls import path

from rest_framework.authtoken import views as AuthTokenView

from . import views

urlpatterns = [
    path('user-login/', AuthTokenView.obtain_auth_token),
    path('create-company/', views.CompanyCreateApiView.as_view()),
    path('create-user/', views.UserCreateApiView.as_view()),
    path('hire-employee/', views.HireEmployeeApiView.as_view()),
    path('add-asset/', views.AddCompanyAsset.as_view()),
    path('provide-asset-to-employee/', views.ProvideAssetToEmployee.as_view()),
    path('returned-asset-to-company/<int:id>/', views.ReturnAssetToCompany.as_view()),
    path('assest-tarcking/', views.AssetTrackingApiView.as_view()),
]

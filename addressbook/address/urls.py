from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.generics import GenericAPIView

schema_view = get_schema_view(
   openapi.Info(
      title="API Docs",
      default_version='Address Book',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router=DefaultRouter()
router.register('alladdress',views.AddressViewset,basename="address")

urlpatterns = [
   path('addaddress/', views.addAddress, name="addaddress"),
   path('address_view_by_user/',views.address_view_by_user,name='turf_view_by_user'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]+router.urls 
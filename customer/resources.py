from tastypie.resources import ModelResource
from customer.models import CustomerInfo
from tastypie.authorization import Authorization

class CustomerInfoResource(ModelResource):
    class Meta:
        queryset = CustomerInfo.objects.all()
        resource_name = 'CustomerInfo'
        authorization = Authorization()
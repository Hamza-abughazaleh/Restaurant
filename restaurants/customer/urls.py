from django.urls import path

from customer import views


urlpatterns = [
    # Your URLs...
    path(r'<customers_number>', views.CustomerViewSet.as_view({'get': 'list'}),
         name='customers')
]

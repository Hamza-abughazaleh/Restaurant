from customer.serializer import CustomerTableSerializer
from django.conf import settings
from django.db.models import Func, F
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from table.models import Table


class CustomerViewSet(viewsets.ModelViewSet):
    """ViewSet for the PartnerProgram class"""
    serializer_class = CustomerTableSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        customers_number = self.kwargs.get('customers_number')
        closest_table = Table.objects.annotate(
            abs_diff=Func(F('seats_number') - int(customers_number), function='ABS')
        ).order_by('abs_diff').first()
        return Table.objects.filter(
            seats_number=closest_table.seats_number
        ).all()

    def list(self, request, *args, **kwargs):
        customers_number = int(self.kwargs.get('customers_number'))
        if isinstance(customers_number, int):
            if customers_number > settings.MAXIMUM_TABLE_SEATS_SIZE:
                return Response({'error_message': 'Our tables only serve 12 people'},
                                status=status.HTTP_406_NOT_ACCEPTABLE)
            return super(CustomerViewSet, self).list(request, *args, **kwargs)
        else:
            return Response({'error_message': 'Please add only digits'},
                            status=status.HTTP_406_NOT_ACCEPTABLE)

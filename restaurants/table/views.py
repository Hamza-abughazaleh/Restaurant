from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from table.models import Table
from table.serializer import TableSerializer


class TableViewSet(viewsets.ModelViewSet):
    """ViewSet for the PartnerProgram class"""
    queryset = Table.objects.all().order_by('-id')
    serializer_class = TableSerializer
    permission_classes = (IsAdminUser,)
    lookup_url_kwarg = "table_id"

    def list(self, request, *args, **kwargs):
        return super(TableViewSet, self).list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        table = self.get_object()
        if table.table_reservation.all():
            return Response({'error_message': 'Cannot delete table has reservations.'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            return super(TableViewSet, self).destroy(request, *args, **kwargs)

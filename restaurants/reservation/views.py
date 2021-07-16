from datetime import date

from reservation.models import Reservation
from reservation.serializer import ReservationSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ReservationViewSet(viewsets.ModelViewSet):
    """ViewSet for the PartnerProgram class"""
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = "reservations_id"

    def get_queryset(self):
        if 'reservations_id' in self.kwargs:
            return Reservation.objects.all()
        elif self.request.user.is_superuser:
            if self.request.GET.get('table_id'):
                return Reservation.objects.filter(tableid=self.request.GET.get('table_id')).all()
            if self.request.GET.get('date_start') and self.request.GET.get('date_end'):
                return Reservation.objects.filter(date__gte=self.request.GET.get('date_start'),
                                                  date__lte=self.request.GET.get('date_end')).all()
            if self.request.GET.get('date_start'):
                return Reservation.objects.filter(date__gte=self.request.GET.get('date_start')).all()
            if self.request.GET.get('date_end'):
                return Reservation.objects.filter(date__lte=self.request.GET.get('date_end')).all()
            return Reservation.objects.all().order_by('-id')
        else:
            if self.request.GET.get('sort_by') == 'asc':
                Reservation.objects.filter(date=date.today()).order_by('id')
            return Reservation.objects.filter(date=date.today()).order_by('-id')

    def list(self, request, *args, **kwargs):
        return super(ReservationViewSet, self).list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        reservation = self.get_object()
        if reservation.date != date.today():
            return Response({'error_message': 'Cannot delete reservation in the past.'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            return super(ReservationViewSet, self).destroy(request, *args, **kwargs)

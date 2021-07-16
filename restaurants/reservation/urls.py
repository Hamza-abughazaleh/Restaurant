from django.urls import path

from reservation import views

actions_url = {'actions': {'get': 'list', 'post': 'create'}}
actions_obj = {'actions': {'delete': 'destroy'}}

urlpatterns = [
    # Your URLs...
    path('', views.ReservationViewSet.as_view(**actions_url), name='reservations'),
    path(r'<reservations_id>', views.ReservationViewSet.as_view(**actions_obj), name='reservations'),
]

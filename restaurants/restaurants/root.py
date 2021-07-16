import collections

from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


def PUBLIC_APIS(r, f):
    return [
        ('login', reverse('api-login', request=r, format=f)),
        ('login-refresh', reverse('api-login-refresh', request=r, format=f))
    ]


def ADMIN_APIS(r, f):
    return [
        ('tables', reverse('tables', request=r, format=f)),
        ('employees-registration', reverse('employees-registration', request=r, format=f))
    ]


def PROTECTED_APIS(r, f):
    return [
        ('reservations', reverse('reservations', request=r, format=f)),
        ('customers', reverse('customers', args=[1], request=r, format=f)),
    ]


@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    """
    GET:
    Display all available urls.
    Since some urls have specific permissions, you might not be able to access
    them all.
    """
    apis = PUBLIC_APIS(request, format)
    if request.user.is_superuser:
        apis += ADMIN_APIS(request, format)
    if request.user.is_authenticated:
        apis += PROTECTED_APIS(request, format)

    return Response(collections.OrderedDict(apis))

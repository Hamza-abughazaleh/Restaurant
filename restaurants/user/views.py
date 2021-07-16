from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser

from user.serializer import UsersSerializer


class CandidatesCreateAPIView(generics.CreateAPIView):
    serializer_class = UsersSerializer
    permission_classes = (IsAdminUser,)

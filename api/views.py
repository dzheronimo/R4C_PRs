from rest_framework.permissions import IsAdminUser
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from robots.models import Robot
from .serializers import NewRobotSerializer


class NewRobot(CreateModelMixin, GenericViewSet):
    queryset = Robot.objects.all()
    serializer_class = NewRobotSerializer
    permission_classes = [IsAdminUser]

    class Meta:
        model = Robot

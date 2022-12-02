from rest_framework.generics import CreateAPIView

from .models import Movement
from .serializers import MovementSerializer


class PostMovementView(CreateAPIView):

    serializer_class = MovementSerializer
    queryset = Movement.objects

    
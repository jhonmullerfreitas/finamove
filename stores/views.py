from rest_framework.generics import ListAPIView

from .models import Store
from .serializers import StoreSerializer

class ListStoreView(ListAPIView):

    serializer_class = StoreSerializer
    queryset = Store.objects
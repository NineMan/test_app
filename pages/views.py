from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Page
from .serializers import PageDetailSerializer
from .serializers import PageListSerializer
from .utils import increment


class PageListView(ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageListSerializer


class PageDetailView(APIView):

    def get(self, request, pk, *args, **kwargs):
        page = Page.objects.get(pk=pk)
        serializer = PageDetailSerializer(page)
        for content in page.content.all():
            increment(content.pk)
        return Response([serializer.data][0])

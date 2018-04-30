from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator
from .models import Manga
from .serializer import MangaSerializer
from rest_framework import status


class MangaList(APIView):
    def get(self, request, format=None):
        manga_list = Manga.objects.get_queryset().order_by('id')
        paginator = Paginator(manga_list, 15)

        page = request.GET.get('page')
        mangas = paginator.get_page(page)
        serializer = MangaSerializer(mangas, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
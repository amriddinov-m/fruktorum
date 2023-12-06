from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Bookmark, Collection
from .serializers import BookmarkSerializer, CollectionSerializer


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    http_method_names = ['get', 'post', 'delete']

    @swagger_auto_schema(
        operation_summary="Список закладок",
        operation_description="Получите список всех закладок",
        responses={200: BookmarkSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Создать закладку",
        operation_description="Создайте новую закладку с предоставленными данными",
        responses={201: BookmarkSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Детали закладки",
        operation_description="Получить подробную информацию о конкретной закладке.",
        responses={200: BookmarkSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Удалить закладку",
        operation_description="Удалить существующую закладку.",
        responses={204: "Закладка успешно удалена"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    @swagger_auto_schema(
        operation_summary="Добавьте закладку в коллекцию.",
        operation_description="Параметры:\n- pk: идентификатор закладки\n- collection_pk: идентификатор коллекции",
        responses={200: "закладка успешно добавлена в коллекцию."}
    )
    def add_to_collection(self, request, pk=None, collection_pk=None):
        bookmark = self.get_object()
        collection = Collection.objects.get(pk=collection_pk)
        collection.bookmarks.add(bookmark)
        collection.save()
        return Response(status=status.HTTP_200_OK)


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    http_method_names = ['get', 'put', 'post', 'delete']

    @swagger_auto_schema(
        operation_summary="Список коллекций",
        operation_description="Получите список всех коллекций",
        responses={200: CollectionSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Создать коллекцию",
        operation_description="Создайте новую коллекцию с предоставленными данными",
        responses={201: CollectionSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Детали коллекций",
        operation_description="Получить подробную информацию о конкретной коллекции.",
        responses={200: CollectionSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Изменить коллекцию",
        operation_description="Обновите существующую коллекцию предоставленными данными.",
        responses={200: CollectionSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Удалить коллекцию",
        operation_description="Удалить существующую коллекцию.",
        responses={204: "Коллекция успешно удалена"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

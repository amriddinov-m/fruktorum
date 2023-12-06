from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import BookmarkViewSet, CollectionViewSet

router = DefaultRouter()
router.register('bookmarks', BookmarkViewSet)
router.register('collections', CollectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('bookmarks/<int:pk>/add_to_collection/<int:collection_pk>/',
         BookmarkViewSet.as_view({'post': 'add_to_collection'}))
]

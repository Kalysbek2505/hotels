from rest_framework.routers import DefaultRouter
from django.urls import path, include


from .views import CommentViewSet, RoomViewSet, add_rating, toggle_like, status

from .views import BookingViewSet, CommentViewSet, RoomViewSet, add_rating, toggle_like, FavoriteViewSet

router = DefaultRouter()
router.register('rooms', RoomViewSet)
router.register('comments', CommentViewSet)
router.register('bookings', BookingViewSet)
router.register('favorites', FavoriteViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('rooms/toggle_like/<int:p_id>/', toggle_like),
    path('rooms/add_rating/<int:p_id>/', add_rating),
    path('status/<int:p_id>/', status)

]
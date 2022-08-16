from rest_framework.routers import DefaultRouter
from django.urls import path, include

<<<<<<< HEAD
from .views import BookingViewSet, CommentViewSet, RoomViewSet, add_rating, toggle_like, FavoriteViewSet, add_to_favorite
=======

from .views import CommentViewSet, RoomViewSet, add_rating, toggle_like, status

from .views import BookingViewSet, CommentViewSet, RoomViewSet, add_rating, toggle_like, FavoriteViewSet
>>>>>>> e43e764881aebe0932e35f9adab9a8dd8ab7dc12

router = DefaultRouter()
router.register('rooms', RoomViewSet)
router.register('comments', CommentViewSet)
router.register('bookings', BookingViewSet)
router.register('favorites', FavoriteViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('rooms/toggle_like/<int:p_id>/', toggle_like),
    path('rooms/add_rating/<int:p_id>/', add_rating),
<<<<<<< HEAD
    path('rooms/add_to_favorite/<int:p_id>/', add_to_favorite),
=======
    path('status/<int:p_id>/', status)

>>>>>>> e43e764881aebe0932e35f9adab9a8dd8ab7dc12
]
from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import api_view, action
from .models import Booking, Room, Comment, Like, Rating
from .serializers import RoomSerializer, CommentSerializer
from .models import Room, Comment, Like, Rating, Favorite, Booking, Chat
from .serializers import FavoriteSerializer, RoomSerializer, CommentSerializer, BookingSerializer, ChatSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsAuthor
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    orfering_fields = ['title', 'price', 'average_rating'] 


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


    @swagger_auto_schema(manual_parameters=[openapi.Parameter("title", openapi.IN_QUERY, "search rooms by title", type=openapi.TYPE_STRING)])
    @action(methods=["GET"], detail=False)
    def search(self, request):
        title = request.query_params.get("title")
        queryset = self.get_queryset()
        if title:
            queryset = queryset.filter(title__icontains=title)
        serializer = RoomSerializer(queryset, many=True, context={"request":request})
        return Response(serializer.data, 200)


    @action(methods=["GET"], detail=False)
    def order_by_rating(self, request):
        rating = request.query_params.get("rating")
        queryset =self.get_queryset()

        queryset = sorted(queryset, key=lambda room: room.average_rating, reverse=True)
        serializer = RoomSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)
    

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

class ChatViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context
       
@api_view(["GET"])
def toggle_like(request, p_id):
    user = request.user
    room = get_object_or_404(Room, id=p_id)
    
    if Like.objects.filter(user=user, room=room).exists():
        Like.objects.filter(user=user, room=room).delete()
    else:
        Like.objects.create(user=user, room=room)
    return Response("Like toggled", 200)

@api_view(["POST"])
def add_rating(request, p_id):
    user = request.user
    room = get_object_or_404(Room, id=p_id)
    value = request.POST.get("value")

    if not user.is_authenticated:
        raise ValueError("authentication credentials are not provided")

    if not value:
        raise ValueError("value is required")
    
    if Rating.objects.filter(user=user, room=room).exists():
        rating = Rating.objects.get(user=user, room=room)
        rating.value=value
        rating.save()
    else:
        Rating.objects.create(user=user, room=room, value=value)
    return Response("rating created", 201)

    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


class FavoriteViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


@api_view(["GET"])
def add_to_favorite(request, p_id):
    user = request.user
    room = get_object_or_404(Room, id=p_id)
    
    if Favorite.objects.filter(user=user, room=room).exists():
        Favorite.objects.filter(user=user, room=room).delete()
    else:
        Favorite.objects.create(user=user, room=room)
    return Response("Favorite toggled", 200)

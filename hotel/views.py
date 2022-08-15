from django.shortcuts import get_object_or_404
from rest_framework import mixins, filters
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import api_view, action
from .models import Product, Category, Comment, Like
from .serializers import ProductSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsAuthor
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    orfering_fields = ['title', 'price', 'average_rating'] 


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    @swagger_auto_schema(manual_parameters=[openapi.Parameter("title", openapi.IN_QUERY, "search products by title", type=openapi.TYPE_STRING)])
    @action(methods=["GET"], detail=False)
    def search(self, request):
        title = request.query_params.get("title")
        queryset = self.get_queryset()
        if title:
            queryset = queryset.filter(title__icontains=title)
        serializer = ProductSerializer(queryset, many=True, context={"request":request})
        return Response(serializer.data, 200)

    @action(methods=["GET"], detail=False)
    def order_by_rating(self, request):
        rating = request.query_params.get("rating")
        queryset =self.get_queryset()

        queryset = sorted(queryset, key=lambda product: product.average_rating, reverse=True)
        serializer = ProductSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

class CommentViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


        
@api_view(["GET"])
def toggle_like(request, p_id):
    user = request.user
    product = get_object_or_404(Product, id=p_id)
    
    if Like.objects.filter(user=user, product=product).exists():
        Like.objects.filter(user=user, product=product).delete()
    else:
        Like.objects.create(user=user, product=product)
    return Response("Like toggled", 200)

@api_view(["POST"])
def add_rating(request, p_id):
    user = request.user
    product = get_object_or_404(Product, id=p_id)
    value = request.POST.get("value")

    if not user.is_authenticated:
        raise ValueError("authentication credentials are not provided")

    if not value:
        raise ValueError("value is required")
    
    if Rating.objects.filter(user=user, product=product).exists():
        rating = Rating.objects.get(user=user, product=product)
        rating.value=value
        rating.save()
    else:
        Rating.objects.create(user=user, product=product, value=value)
    return Response("rating created", 201)
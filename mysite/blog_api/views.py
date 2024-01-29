from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAuthorOrReadOnly
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 10


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["author"]
    search_fields = ["body", "author__profile__bio"]
    ordering_fields = ["author_id", "publish"]
    ordering = ["body"]
    pagination_class = StandardResultsSetPagination


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

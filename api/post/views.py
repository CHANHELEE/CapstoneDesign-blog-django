from rest_framework.generics import CreateAPIView, UpdateAPIView ,DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import viewsets, generics
from .models import Post
from .serializers import PostSerializer



# Create your views here.

class PostListView(generics.ListCreateAPIView) :
    serializer_class = PostSerializer

    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.set_filters(self.get_queryset(), request)

        self.paginator.page_size_query_param = "page_size"
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def set_filters(self, queryset, request):
        title = request.query_params.get('title', None)
        content = request.query_params.get('content', None)
        created_at = request.query_params.get('created_at', None)

        if title is not None:
            queryset = queryset.filter(title__contains=title)

        if content is not None:
            queryset = queryset.filter(content__contains=content)

        if created_at is not None:
            queryset = queryset.filter(created_at__contains=created_at)

        return queryset


class CreatePostView(CreateAPIView):

    model = Post
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UpdatePostView(UpdateAPIView) :
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'


class DeletePostView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

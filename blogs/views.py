from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.serializers import UserSerializer
from .models import Post
from .serializers import PostSerializer
class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# @api_view(['GET'])
# def view_all(request):
#     permission_classes = (IsAuthenticated,)
#     if request.method == 'GET':
#         snippets = Post.objects.all()
#         serializer = PostSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(['DELETE'])
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return Response(
            {'message': "you do not have permission to do this action"},
            status=status.HTTP_403_FORBIDDEN)

    post.delete()
    return JsonResponse({'message': 'DELETED SUCCESSFULLY'}, status=status.HTTP_200_OK)
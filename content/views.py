from rest_framework import mixins, generics

from content.models import Blog
from content.serializer import BlogSerializer


# Create your views here.

class BlogView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_queryset(self):
        query = {}
        if "auther" in self.request.GET:
            query["auther"] = int(self.request.GET.get("auther"))
        elif "created" in self.request.GET:
            query["created"] = self.request.GET.get("created")
        return self.queryset.filter(**query)

    def get(self, request, *args, **kwargs):
        if "pk" in kwargs:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

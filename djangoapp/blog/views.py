from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from blog.models import Post, Page
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404, HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect

PER_PAGE = 9


# CLASS BASED VIEWS


class PostListView(ListView):
    model = Post
    template_name = "blog/pages/index.html"
    context_object_name = "posts"
    ordering = "-pk"
    paginate_by = PER_PAGE
    queryset = Post.objects.get_published()

    # THIS FUNCTION MANIPULATES THE QUERYSET
    # def get_queryset(self):
    #     return Post.objects.get_published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Home"
        return context


class CreatedByListView(PostListView):

    # THIS FUNCTION MANIPULATES THE QUERYSET
    def get_queryset(self):
        return super().get_queryset().filter(created_by__pk=self.kwargs["author_id"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        author_id = self.kwargs["author_id"]

        user = User.objects.filter(pk=author_id).first()

        if user is None:
            raise Http404("User does not exist")

        context["page_title"] = (
            User.objects.filter(pk=author_id).first().first_name + "'s" + " Posts"
        )

        return context


class CategoryListView(PostListView):
    allow_empty = False

    def get_queryset(self):
        return super().get_queryset().filter(categories__slug=self.kwargs.get("slug"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = str(
            Post.objects.get_published()
            .filter(categories__slug=self.kwargs["slug"])
            .first()
            .categories
        )

        return context


class TagListView(PostListView):
    allow_empty = False

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(tags__slug=self.kwargs.get("slug"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["page_title"] = str(
            Post.objects.get_published()
            .filter(tags__slug=self.kwargs["slug"])
            .first()
            .tags.filter(slug=self.kwargs["slug"])
            .first()
        )

        return context


class SearchListView(PostListView):
    def get_queryset(self) -> QuerySet[Any]:
        search = self.request.GET.get("search").strip()
        return (
            super()
            .get_queryset()
            .filter(
                Q(title__icontains=search)
                | Q(content__icontains=search)
                | Q(excerpt__icontains=search)
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get("search").strip()
        context["page_title"] = "Search Results for " + search
        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.GET.get("search") == "":
            return redirect("blog:index")

        return super().get(request, *args, **kwargs)


class PageDetailView(DetailView):
    model = Page
    template_name = "blog/pages/page.html"
    slug_field = "slug"
    context_object_name = "page"

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.object.title
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/pages/post.html"
    slug_field = "slug"
    context_object_name = "post"

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.object.title
        return context


# FUNCTION BASE VIEWS


# def index(request):
#     posts = Post.objects.get_published()

#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     return render(
#         request,
#         "blog/pages/index.html",
#         {
#             "page_title": "Home",
#             "page_obj": page_obj,
#         },
#     )


# def created_by(request, author_id: int):
#     posts = Post.objects.get_published().filter(created_by__pk=author_id)
#     user = User.objects.get(pk=author_id)

#     if user is None:
#         raise Http404("User does not exist")

#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     return render(
#         request,
#         "blog/pages/index.html",
#         {
#             "page_title": user.first_name + "'s" + " Posts",
#             "page_obj": page_obj,
#         },
#     )


# def category(request, slug):
#     posts = Post.objects.get_published().filter(categories__slug=slug)

#     if len(posts) == 0:
#         raise Http404("Category does not exist")

#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     return render(
#         request,
#         "blog/pages/index.html",
#         {
#             "page_title": str(posts.first().categories) + " category -",
#             "page_obj": page_obj,
#         },
#     )


# def tag(request, slug):
#     posts = Post.objects.get_published().filter(tags__slug=slug)

#     if len(posts) == 0:
#         raise Http404("Tag does not exist")

#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     return render(
#         request,
#         "blog/pages/index.html",
#         {
#             "page_title": str(posts.first().tags.filter(slug=slug).first()) + " tag -",
#             "page_obj": page_obj,
#         },
#     )


# def search(request):
#     search = request.GET.get("search").strip()
#     posts = Post.objects.get_published().filter(
#         Q(title__icontains=search)
#         | Q(content__icontains=search)
#         | Q(excerpt__icontains=search)
#     )[:PER_PAGE]

#     return render(
#         request,
#         "blog/pages/index.html",
#         {
#             "page_title": "Search Results for " + search,
#             "page_obj": posts,
#         },
#     )


# def page(request, slug):
#     page = Page.objects.get_published().filter(slug=slug).first()

#     if page is None:
#         raise Http404("Page does not exist")

#     return render(
#         request,
#         "blog/pages/page.html",
#         {
#             "page_title": page.title,
#             "page": page,
#         },
#     )


# def post(request, slug):
#     post = Post.objects.get_published().filter(slug=slug).first()

#     if post is None:
#         raise Http404("Post does not exist")

#     return render(
#         request,
#         "blog/pages/post.html",
#         {
#             "page_title": post.title,
#             "post": post,
#         },
#     )

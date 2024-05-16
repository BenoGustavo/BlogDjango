from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models import Post, Page, User
from django.db.models import Q
from django.http import Http404

PER_PAGE = 9


def index(request):
    posts = Post.objects.get_published()

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/pages/index.html",
        {
            "page_title": "Home",
            "page_obj": page_obj,
        },
    )


def created_by(request, author_id: int):
    posts = Post.objects.get_published().filter(created_by__pk=author_id)
    user = User.objects.get(pk=author_id)

    if user is None:
        raise Http404("User does not exist")

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/pages/index.html",
        {
            "page_title": user.first_name + "'s" + " Posts",
            "page_obj": page_obj,
        },
    )


def category(request, slug):
    posts = Post.objects.get_published().filter(categories__slug=slug)

    if len(posts) == 0:
        raise Http404("Category does not exist")

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/pages/index.html",
        {
            "page_title": str(posts.first().categories) + " category -",
            "page_obj": page_obj,
        },
    )


def tag(request, slug):
    posts = Post.objects.get_published().filter(tags__slug=slug)

    if len(posts) == 0:
        raise Http404("Tag does not exist")

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/pages/index.html",
        {
            "page_title": str(posts.first().tags.filter(slug=slug).first()) + " tag -",
            "page_obj": page_obj,
        },
    )


def search(request):
    search = request.GET.get("search").strip()
    posts = Post.objects.get_published().filter(
        Q(title__icontains=search)
        | Q(content__icontains=search)
        | Q(excerpt__icontains=search)
    )[:PER_PAGE]

    return render(
        request,
        "blog/pages/index.html",
        {
            "page_title": "Search Results for " + search,
            "page_obj": posts,
        },
    )


def page(request, slug):
    page = Page.objects.get_published().filter(slug=slug).first()

    if page is None:
        raise Http404("Page does not exist")

    return render(
        request,
        "blog/pages/page.html",
        {
            "page_title": page.title,
            "page": page,
        },
    )


def post(request, slug):
    post = Post.objects.get_published().filter(slug=slug).first()

    if post is None:
        raise Http404("Post does not exist")

    return render(
        request,
        "blog/pages/post.html",
        {
            "page_title": post.title,
            "post": post,
        },
    )

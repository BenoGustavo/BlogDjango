from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models import Post, Page
from django.db.models import Q

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
            "page_obj": page_obj,
        },
    )


def created_by(request, author_id: int):
    posts = Post.objects.get_published().filter(created_by__pk=author_id)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/pages/index.html",
        {
            "page_obj": page_obj,
        },
    )


def category(request, slug):
    posts = Post.objects.get_published().filter(categories__slug=slug)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/pages/index.html",
        {
            "page_obj": page_obj,
        },
    )


def tag(request, slug):
    posts = Post.objects.get_published().filter(tags__slug=slug)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/pages/index.html",
        {
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
            "page_obj": posts,
        },
    )


def page(request, slug):
    page = Page.objects.get_published().filter(slug=slug).first()
    return render(
        request,
        "blog/pages/page.html",
        {
            "page": page,
        },
    )


def post(request, slug):
    post = Post.objects.get_published().filter(slug=slug).first()

    return render(
        request,
        "blog/pages/post.html",
        {
            "post": post,
        },
    )

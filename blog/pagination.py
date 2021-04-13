from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def pagination(request, post, post_per_page):
    if request.user_agent.is_mobile:
        return post

    paginator = Paginator(post, post_per_page)
    page = request.GET.get('page', 1)

    try:
        post = paginator.get_page(page)
    except PageNotAnInteger:
        post = Paginator.get_page(1)
    except EmptyPage:
        post = Paginator.get_page(paginator.num_pages)

    return post
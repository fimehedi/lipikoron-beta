import json
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.hashers import check_password

# For hit count
# from hitcount.utils import get_hitcount_model
# from hitcount.views import HitCountMixin

from . forms import createForm, commentForm, ReportForm, WithdrawForm
from . models import category, article, comment, Withdraw
from . pagination import pagination
from notifications.models import Notification


# Create your views here.
def index(request):
    post = article.objects.all().order_by('-id')
    cat = category.objects.all()

    context = {
        "post": pagination(request, post, 15),
        "category": cat
    }
    return render(request, "index.html", context)


def getSearch(request):
    try:
        search = request.GET.get("search").strip()
    except:
        search = False

    if search:
        post = article.objects.filter(
                Q(title__icontains = search)|
                Q(body__icontains = search)
            ).order_by('-id')

        context = {
            "post": pagination(request, post, 1),
            "search": search
        }

        return render(request, 'search.html', context)

    return redirect('/')


def notFound(request, exception):
    return render(request, '404.html')


def getAuthor(request, name):
    authorData = get_object_or_404(get_user_model(), username=name)
    post = article.objects.filter(author__username = authorData).order_by('-id')

    total_views = 0
    total_likes = 0

    for p in post:
        total_views += p.views
        total_likes += p.likes.count()

    authorData.views = total_views
    authorData.likes = total_likes
    authorData.save()

    context = {
        "author" : authorData,
        "post": pagination(request, post, 15),
    }
    return render(request, "profile.html", context)


def getSingle(request, id):
    post = get_object_or_404(article, pk = id)
    commentData = comment.objects.filter(post = id)
    form = commentForm(request.POST or None)
    context = {}
    post_author = post.author

    if form.is_valid():
        isinstance = form.save(commit = False)
        isinstance.post = post
        isinstance.user = request.user
        isinstance.save()
        if post_author != request.user:
            notify = Notification(post=post, user=post_author, sender=request.user, notification_type=2)
            notify.save()
        return redirect(reverse('single_post', args=[post.id]))

    liked = False

    if post.likes.filter(id=request.user.id).exists():
        liked = True

    # Count Visitor
    post.views += 1
    post.save()

    # Count visitor old code
    '''
    hit_count = get_hitcount_model().objects.get_for_object(post)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'id': hit_count.id}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)

    if hit_count_response.hit_counted:
        hits = hits + 1
        post.views = hits
        post.save()

        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits
    '''

    context = {
        "post":post,
        "form":form,
        "comment":commentData,
        "liked": liked
    }
    return render(request, "single.html", context)


def getCategory(request, name):
    cat = get_object_or_404(category, name = name)
    post = article.objects.filter(category = cat.id).order_by('-id')

    return render(request, "category.html", {
        "post": pagination(request, post, 15),
        "category":cat,
    })


@login_required
@csrf_exempt
def getCreate(request):
    user = get_object_or_404(get_user_model(), username = request.user)
    form = createForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        isinstance = form.save(commit = False)
        isinstance.author = user
        isinstance.save()
        user.articles = article.objects.filter(author=user).count()
        user.save()
        messages.success(request, 'আপনার লিপিটি প্রকাশ করা হয়েছে!')
        return redirect("dashboard")
    return render(request, "create.html", {"form" : form})


@login_required
@csrf_exempt
def getUpdate(request, id):
    user = get_object_or_404(get_user_model(), username = request.user)
    post = get_object_or_404(article, id = id)
    form = createForm(request.POST or None, request.FILES or None, instance=post)

    if form.is_valid():
        isinstance = form.save(commit = False)
        isinstance.author = user
        isinstance.save()
        messages.info(request, 'আপনার লিপিটি আপডেট করা হয়েছে!')
        return redirect("dashboard")
    return render(request, "create.html", {"form" : form})


@login_required
def getDelete(request, id):
    post = get_object_or_404(article, id = id)
    post.delete()
    post_author = get_object_or_404(get_user_model(), username=request.user)
    post_author.articles = article.objects.filter(author=post_author).count()
    post_author.save()
    messages.warning(request, 'আপনার লিপিটি অপসারণ করা হয়েছে!')
    return redirect("dashboard")


@login_required
def getDashboard(request):
    user = get_object_or_404(get_user_model(), username=request.user)
    post = article.objects.filter(author = request.user).order_by('-id')
    return render(request, "dashboard.html", {"post" : pagination(request, post, 15)})


@login_required
def like(request):
    print(request.user)
    if request.method == "POST":
        if request.POST.get('operation') == 'like' and request.is_ajax():
            post_id = request.POST.get('post_id', None)
            post    = get_object_or_404(article, id=post_id)
            sender  = request.user
            user    = post.author

            if post.likes.filter(id=request.user.id).exists():
                post.likes.remove(request.user)
                liked = False

                notify = Notification.objects.filter(post=post, sender=sender, notification_type=1)
                notify.delete()

            else:
                post.likes.add(request.user)
                liked = True

                if user != sender:
                    notify = Notification(post=post, user=user, sender=sender, notification_type=1)
                    notify.save()

            ctx = {'total_like': post.likes.count(), 'liked': liked, 'post_id': post_id}
            return HttpResponse(json.dumps(ctx), content_type='application/json')

    return render(request, '404.html')


@login_required
def report(request, post_id):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid ():
            post = get_object_or_404(article, id=post_id)
            cd = form.cleaned_data
            isinstance = form.save(commit=False)
            isinstance.user = request.user
            isinstance.post_id = post
            isinstance.save()
            messages.info(request, "রিপোর্ট করা হয়েছে!")
            return redirect(reverse('single_post', args=[post_id]))
    else:
        form = ReportForm()

    return render(request, "report.html", {
        "form": form,
        "post_id": post_id,
    })


@login_required
def bookmark(request):
    if request.method == 'POST':
        if request.POST.get('operation') == 'bookmark' and request.is_ajax():
            post_id = request.POST.get('post_id', None)
            post    = get_object_or_404(article, id=post_id)

            if post.bookmark.filter(id=request.user.id).exists():
                post.bookmark.remove(request.user)
                is_bookmark = False
            else:
                post.bookmark.add(request.user)
                is_bookmark = True

            ctx = {'is_bookmark': is_bookmark, 'post_id': post_id}
            return HttpResponse(json.dumps(ctx), content_type='application/json')

    post = request.user.bookmark.all().order_by('id')
    return render(request, 'bookmarks.html', {
        "post": pagination(request, post, 15),
    })


@login_required
def getBalance(request):
    return render(request, 'reward.html')


@login_required
def getWithdraw(request):
    user = get_object_or_404(get_user_model(), id=request.user.id)
    balance = user.balance

    withdraw_req = Withdraw.objects.filter(user=user)

    form = WithdrawForm(request.POST or None)

    if form.is_valid():
        isinstance = form.save(commit = False)
        isinstance.user = request.user
        password = request.POST.get('password')

        if isinstance.withdraw_amount >= 100 and isinstance.withdraw_amount <= balance and check_password(password, user.password):
            user.balance = balance - isinstance.withdraw_amount
            user.save()
            isinstance.save()
            messages.success(request, 'পেমেন্টের জন্য আবেদন করা হয়েছে!')
        else:
            messages.error(request, 'আবেদন সম্পন্ন হয়নি!')

        return redirect(reverse('withdraw'))

    return render(request, "withdraw.html", {"form" : form, 'req': withdraw_req})


def leaderboard(request):
    best_lipikar = get_user_model().objects.order_by('-likes', '-articles', '-views')

    return render(request, 'leaderboard.html', {
        'best_lipikar': best_lipikar[:25],
    })

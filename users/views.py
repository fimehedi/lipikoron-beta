from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView


from .forms import CustomUserCreationForm, SettingsForm


@csrf_protect
def getRegister(request):
    form = CustomUserCreationForm(request.POST or None)

    if form.is_valid():
        isinstance = form.save(commit = False)
        isinstance.save()
        messages.success(request, "রেজিস্ট্রেশন সফল হয়েছে!")
        return redirect("login")

    if form.errors:
        messages.error(request, "রেজিস্ট্রেশন সফল হয়নি!")

    return render(request, "register.html", {"form" : form})


def getLogin(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == "POST":
            user = request.POST.get("user")
            password = request.POST.get("password")
            auth = authenticate(request, username = user, password = password)

            if auth is not None:
                login(request, auth)
                return redirect("index")
            else:
                messages.add_message(request, messages.ERROR, 'ইউজারনেম অথবা পাসওয়ার্ড ভুল হয়েছে!')
                return render(request, "login.html")
    return render(request, "login.html")

def getLogout(request):
    logout(request)
    return redirect("index")

@login_required
def settings(request):
    current_user = get_object_or_404(get_user_model(), username=request.user)


    if request.method == 'POST':
        form = SettingsForm(request.POST, request.FILES, instance=current_user)

        if form.is_valid():
            isinstance = form.save(commit = False)
            if isinstance.first_name and isinstance.last_name and isinstance.email:
                form.save()
                messages.success(request, "আপডেট সম্পন্ন হয়েছে!")
            else:
                messages.error(request, "সঠিক তথ্য প্রদান করুন!")
            return redirect('settings')

    else:
        form = SettingsForm(instance=current_user)


    return render(request, "settings.html", context={
        'form' : form
    })


# @login_required
# def becomeLipikar(request):
#     user = get_object_or_404(get_user_model(), id=request.user.id)
#     if user.is_lipikar:
#         return redirect("create")
#     else:
#         form = AuthorForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             isinstance = form.save(commit=False)
#             isinstance.name = user
#             isinstance.save()
#             messages.success(request, "অভিনন্দন, আপনি লিপিকার হয়েছেন!")
#             return redirect("create")
#         return render(request, "lipikar-form.html", {"form":form})


@login_required
def account_delete(request):
    user = get_object_or_404(get_user_model(), id=request.user.id)

    if request.method == 'POST':
        password = request.POST.get('password')
        if check_password(password, user.password):
            try:
                user.delete()
                return HttpResponseRedirect(reverse('index'))
            except:
                messages.warning(request, "একাউন্ট ডিলিট হয়নি!")
        else:
            messages.error(request, "পাসওয়ার্ড ভুল!")

    return render(request, 'account-delete.html')




class UserPasswordChangeView(PasswordChangeView):
    template_name = 'change-password.html'
    success_url   = '/'


class UserPasswordResetView(PasswordResetView):
    template_name = 'password-reset.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password-reset-confirm.html'
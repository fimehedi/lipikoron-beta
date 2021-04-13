from django import forms
from . models import article, comment, Report, Withdraw

class createForm(forms.ModelForm):
    class Meta:
        model = article
        fields = [
            "title",
            "body",
            "category",
            "thumbnail"
        ]


class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = [
            "post_comment",
        ]


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            "report"
        ]


class WithdrawForm(forms.ModelForm):
    class Meta:
        model = Withdraw
        fields = [
            "withdraw_amount",
            "withdraw_method",
            "account_number"
        ]

from collections import OrderedDict
from django import forms
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from pretix.base.forms import SecretKeySettingsField
from pretix.base.signals import register_global_settings, register_payment_providers

@receiver(register_global_settings, dispatch_uid="payment_airtelmoney_global_settings")
def register_global_settings(sender, **kwargs):
    return OrderedDict(
        [
            (
                "payment_airtelmoney_client_id",
                forms.CharField(
                    label=_("AirtelMoney: Client ID"),
                    required=True,
                ),
            ),
            (
                "payment_airtelmoney_client_secret",
                SecretKeySettingsField(
                    label=_("AirtelMoney: Client Secret"),
                    required=True,
                ),
            ),
            (
                "payment_airtelmoney_baseurl",
                forms.ChoiceField(
                    label=_("AirtelMoney: URL"),
                    initial="STAGING",
                    choices=(
                        ("https://openapiuat.airtel.africa/", "STAGING"),
                        ("https://openapi.airtel.africa/", "PRODUCTION"),
                    ),
                ),
            ),
        ]
    )

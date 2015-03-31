# -*- coding: utf-8 -*-
from django import forms
from django.db import transaction
from django.utils.translation import ugettext_lazy as _
from .models import Invitation, InvitationUsage


class InvitationUsageForm(forms.Form):
    code = forms.CharField(max_length=255, required=True,)
    session_key = forms.CharField(max_length=40, required=True, widget=forms.HiddenInput(),)

    def clean_code(self):
        try:
            invitation = Invitation.objects.get(code=self.cleaned_data['code'])
            if invitation.is_valid():
                return self.cleaned_data['code']
            else:
                # TODO: This event should be logged.
                raise Exception(_('Invitation is not valid.'))
        except Invitation.DoesNotExist:
            raise forms.ValidationError(_('Invitation does not exist! Please check your invitation code.'))
        except:
            raise forms.ValidationError(_('An error occurred! Please try again.'))

    def save(self):
        with transaction.atomic():
            try:
                invitation = Invitation.objects.get(code=self.cleaned_data['code'])

                try:
                    invitation_usage = InvitationUsage.objects.get(
                        invitation=invitation,
                        session_key=self.cleaned_data['session_key'],
                    )
                except InvitationUsage.DoesNotExist as e:
                    # Save the invitation usage action.
                    invitation_usage = InvitationUsage()
                    invitation_usage.invitation = invitation
                    invitation_usage.session_key = self.cleaned_data['session_key']
                invitation_usage.save()

                # Update invitation accordingly.
                invitation.update_status()
            except Exception as e:
                # TODO: Log exception
                pass


class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['code', 'sent_by']
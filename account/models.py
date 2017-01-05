import simplejson as json
import decimal
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from event.models import Event


class Account(models.Model):
    balance = models.DecimalField(max_digits=19, decimal_places=6, default=decimal.Decimal(0))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='account')

    def make_deposit(self, amount):
        """Deposit money into account"""
        Event.objects.create(
            content_object=self,
            time_created=timezone.now(),
            body=json.dumps({
                'type': 'made_deposit',
                'amount': amount,
            })
        )
        self.balance += amount
        self.save()

    def make_withdrawal(self, amount):
        """Withdraw money from account"""
        Event.objects.create(
            content_object=self,
            time_created=timezone.now(),
            body=json.dumps({
                'type': 'made_withdrawal',
                'amount': -amount,  # withdraw = negative amount
            })
        )
        self.balance -= amount
        self.save()

    @classmethod
    def create_account(cls, owner):
        """Create an account"""
        account = cls.objects.create(owner=owner, balance=0)
        Event.objects.create(
            content_object=account,
            time_created=timezone.now(),
            body=json.dumps({
                'type': 'created_account',
                'id': account.id,
                'owner_id': owner.id
            })
        )
        return account

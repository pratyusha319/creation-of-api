from rest_framework import serializers
from bank.models import *

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['name','id']

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"

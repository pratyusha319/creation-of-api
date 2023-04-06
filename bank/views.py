from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from bank.models import *
from bank.serializers import *

class bank_list(APIView):
        
    def get(self,request):
       
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)
    def post(self,request):
        data=request.data
        serializer = BankSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def put(self,request):
       
        data=request.data
        serializer = BankSerializer(data=data)
    
        return Response(serializer.data,)
    def patch(self,request):
        data=request.data
        banks = Bank.objects.get(id=data['id'])
        serializer = BankSerializer(banks, data=data,partial=True)
    
        return Response(serializer.data,)
    def delete(self,request):
        data=request.data
        banks = Bank.objects.get(id=data['id'])
        banks.delete()
        
        return Response({'message':'bankdetails deleted'})
class branch_details(APIView):
    def get(self,request):
       
        branches =Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)
    def post(self,request):
       
        data=request.data
        serializer = BranchSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
       
        data=request.data
        serializer = BranchSerializer(data=data)
        serializer.save()
        return Response(serializer.data,)
    def patch(self,request):
        data=request.data
        branches = Branch.objects.get(id=data['id'])
        serializer = BranchSerializer(branches, data=data,partial=True)
        serializer.save()
        return Response(serializer.data,)
    def delete(self,request):
        data=request.data
        branches = Branch.objects.get(id=data['id'])
        branches.delete()
        
        return Response({'message':'bankdetails deleted'})
  
from django.http import HttpResponse
from django.shortcuts import render

from expenses.models import Expense

def index(request):
  expense_list = Expense.objects.order_by('-date')
  context = { 'expense_list': expense_list }
  return render(request, 'expenses/index.html', context)
def new(request):
  context = { 'expense': null }#Change when you figure out how
  return render(request, 'expenses/new.html')
def create(request):
  return HttpResponse("This should be a POST that redirects to index.")

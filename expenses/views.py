from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import date
from expenses.models import Expense
from django.core.exceptions import ValidationError

def index(request):
  expense_list = Expense.objects.order_by('-date')
  context = { 'expense_list': expense_list }
  return render(request, 'expenses/index.html', context)
def new(request):
  context = { 'expense': None }#Change when you figure out how
  return render(request, 'expenses/new.html')
def create(request):
  form_data = request.POST
  try:
    Expense.objects.create(name=form_data['name'],
      source=form_data['source'],
      amount=form_data['amount'],
      date=date.today()
    )
  except ValidationError as e:
    return HttpResponse(e.message_dict.values)
  else:
    return redirect(index)

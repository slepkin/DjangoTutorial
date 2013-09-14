from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import date
from expenses.models import Expense
from django.core.exceptions import ValidationError
from django.contrib import messages #FLASH! AH ahhhhhhh...

def index(request):
  expense_list = Expense.objects.order_by('-date')
  context = { 'expense_list': expense_list }
  return render(request, 'expenses/index.html', context)

def new(request):
  context = {
    'expense': Expense(),
    'F_checked': None,
    'C_checked': None,
    'H_checked': None,
    'messages': False
  }
  return render(request, 'expenses/new.html', context)

def create(request):
  form_data = request.POST
  expense = Expense(name=form_data['name'],
    # Different syntax below, in case none selected
    source=form_data.get('source',None),
    amount=form_data['amount'],
    date=date.today()
  )
  try:
    expense.save()
  except ValidationError as e:
    messages.add_message(request, messages.ERROR, e)
    context = {
    'expense': expense,
    'F_checked': 'checked' if expense.source=="F" else None,
    'C_checked': 'checked' if expense.source=="C" else None,
    'H_checked': 'checked' if expense.source=="H" else None,
    'messages': e.messages
    }
    return render(request, 'expenses/new.html', context)
  else:
    return redirect(index)

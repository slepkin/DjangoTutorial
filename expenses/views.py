from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import date
from expenses.models import Expense
from django.core.exceptions import ValidationError
from django.contrib import messages #FLASH! AH ahhhhhhh...
from django.template import RequestContext

def index(request):
  expense_list = Expense.objects.order_by('-date')
  context = { 'expense_list': expense_list }
  return render(request, 'expenses/index.html', context)

def new(request):
  context = RequestContext(request, {
    'expense': Expense(),
    'F_checked': None,
    'C_checked': None,
    'H_checked': None
  })
  return render(request, 'expenses/new.html', context)

def create(request):
  post_data = request.POST
  if not post_data:
    return redirect(new)


  expense = Expense(name=post_data['name'],
    source=post_data.get('source', None),
    amount=post_data['amount'],
    date=post_data['date']
  )
  try:
    expense.full_clean()
  except ValidationError as e:

    for message in e.messages:
      messages.error(request, message)

    context = RequestContext(request, {
    'expense': expense,
    'F_checked': 'checked' if expense.source=="F" else None,
    'C_checked': 'checked' if expense.source=="C" else None,
    'H_checked': 'checked' if expense.source=="H" else None
    })
    return render(request, 'expenses/new.html', context)

  else:
    expense.save()
    return redirect(index)

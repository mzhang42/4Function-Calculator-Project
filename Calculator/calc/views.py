from django.shortcuts import render, redirect
from .form import CalculationForm
from .models import Calculation
from django.core.exceptions import ValidationError

# Create your views here.

def calculate(request):
   print(request.POST)
   if request.method == 'POST' and ('button' in request.POST):
       form = CalculationForm(request.POST)
       operator = request.POST.get('calculation_type')
       num_one = request.POST.get('num_one')
       num_two = request.POST.get('num_two')
       if form.is_valid():
           if(operator == '0'):
               result = int(num_one) + int(num_two)
               operator = '+'
           elif(operator == '1'):
               result = int(num_one) - int(num_two)
               operator = '-'
           elif(operator == '2'):
               result = int(num_one) * int(num_two)
               operator = '*'
           else:
               result = int(num_one) / int(num_two)
               operator = '/'
           calculation = form.save(commit=False)
           calculation.operator = operator
           calculation.result = result
           calculation.save()
           print(result)
           return render(request, 'home.html', {'form':form, 'resultdict':result})
   elif("switch" in request.POST):
       return redirect('results')
   else:
       form = CalculationForm()
   return render(request, 'home.html', {'form':form})

def results(request):
   past = Calculation.objects.all()
   if "goBack" in request.POST:
       return redirect(calculate)
   if "wipe" in request.POST:
       Calculation.objects.all().delete() 
   for expression in past:
        print(expression.operator) 
   return render(request, 'results.html', {'past':past})


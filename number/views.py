from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from .forms import NumberForm
from django.urls import reverse_lazy
from django.http import request


class NumberView(FormView):
    template_name = 'number/number.html'
    form_class = NumberForm
    success_url = reverse_lazy('number:success')

    def form_valid(self, form):
        form.send()
        return super().form_valid(form)

        if request.method =='POST':
           form = NumberForm(request.POST)
           if form.is_valid():
                form.send()
                return redirect('number:success')
        else:
            form = NumberForm()

class NumberSuccessView(TemplateView):
    template_name = 'number/success.html'          
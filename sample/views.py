from django.shortcuts import render,redirect
from .forms import SampleForm
from django.urls import reverse
from django.views import View

class SampleFormView(View):
    template_name = 'form.html'
    form_class = SampleForm
    success_url = reverse('sample:index')

    # Create your views here.
    def get(self, request, *args, **kwargs):
        context = {
            'form': SampleForm()
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = SampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)

        context = {
            'form': form
        }
        return render(request, self.success_url, context=context)


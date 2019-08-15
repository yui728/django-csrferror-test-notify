from django.shortcuts import render,redirect
from .forms import SampleForm
from django.urls import reverse
from django.views import View

class SampleFormView(View):

    # Create your views here.
    def get(self, request, *args, **kwargs):
        context = {
            'form': SampleForm()
        }
        return render(request, 'sample/index.html', context)

    def post(self, request, *args, **kwargs):
        form = SampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('sample:index'))

        context = {
            'form': form
        }
        return render(request, 'sample/index.html', context)

sampleFromView = SampleFormView.as_view()
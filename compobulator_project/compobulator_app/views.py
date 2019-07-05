from django.shortcuts import render
from compobulator_app.forms import mp_archetype_model_form, mp_element_model_form
from django.views.generic import TemplateView, CreateView, ListView, DetailView  # For the cbv's
from compobulator_app import models

class IndexView(TemplateView):
    template_name = 'compobulator_app/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectMeId'] = "Here's some text for injection!"
        return context

class ArchetypeListView(ListView):
    context_object_name = 'alvcon_list'
    model = models.Mp_archetype
    template_name = 'compobulator_app/mp_archetype_list.html'

class ArchetypeDetailView(DetailView):
    context_object_name = 'advcon_details'
    model = models.Mp_archetype
    template_name = 'compobulator_app/mp_archetype_detail.html'

class ElementListView(ListView):
    context_object_name = 'elvcon_list'
    model = models.Mp_element
    template_name = 'compobulator_app/mp_element_list.html'

class ElementDetailView(DetailView):
    context_object_name = 'edvcon_details'
    model = models.Mp_element
    template_name = 'compobulator_app/mp_element_detail.html'

def index(request):
    return render(request, 'compobulator_app/index.html')

def mp_archetype_form_view(request):
    form = mp_archetype_model_form()

    if request.method == 'POST':
        form = mp_archetype_model_form(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error: mp_archetype_model_form is invalid!')
    return render(request, 'compobulator_app/mp_archetype_form.html', {'form': form})

def mp_element_form_view(request):
    form = mp_element_model_form()

    if request.method == 'POST':
        form = mp_element_model_form(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error: mp_element_model_form is invalid!')
    return render(request, 'compobulator_app/mp_element_form.html', {'form': form})

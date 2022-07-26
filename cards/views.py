from django.views.generic import ListView, CreateView, UpdateView
from .models import Card
from django.urls import reverse_lazy
import random

class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by('box', '-date_created')


class CardCreateView(CreateView):
    model = Card
    fields = ('question', 'answer', 'box',)
    success_url = reverse_lazy('card-create')


class CardUpdateView(CardCreateView,UpdateView):
    success_url = reverse_lazy('card-list')


class CardBoxView(CardListView):
    template_name = "cards/box.html"
    
    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs['box_num'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['box_number'] = self.kwargs['box_num']
        return context     
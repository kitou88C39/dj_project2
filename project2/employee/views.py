from django.views import generic
from .forms import SearchForm
from .models import Employee

class IndexView(generic.ListView):
    model=Employee



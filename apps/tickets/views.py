from django.views.generic import ListView
from apps.tickets.models import Ticket


class TicketListView(ListView):
    model = Ticket
    template_name = 'tickets/list.tpl'

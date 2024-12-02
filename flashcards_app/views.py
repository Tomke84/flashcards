from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)
from django.shortcuts import get_object_or_404, redirect
from .models import Card
from .forms import CardCheckForm
import random

class CardListView(ListView):
    model = Card
    # you want your database to return all items ordered by
    # their box in ascending order, then by date_created in descending order
    queryset = Card.objects.all().order_by("box", "-date_created")

class BoxView(CardListView):
    # To avoid Django would serve card_list.html (default template for ListView), you have to define its template-name.
    template_name = "flashcards_app/box.html"
    form_class = CardCheckForm

    # Because you don't want to list all you cards
    def get_queryset(self):
        # you only return the cards where the box number matches the box_num value
        # by passing in the value of box_num as a keyword argument in your GET request.
        return Card.objects.filter(box=self.kwargs["box_num"])

    # To use the box number in your template, you use .get_context_data()
    # and add box_num as box_number (= variable) to your view's context.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        # This is to show a random card in the BoxView.
        # First you check if there is a card
        # Then you use random.choise() to pick one card
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context

    # define the .post() method to handle incoming POST requests
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        # Usually, your browser checks if all required fields of your form are filled out.
        # But it’s good practice to check your forms in the back end in any case.
        if form.is_valid():
            # If your form is valid, then you’re trying to get the Card object from the database by its card_id value.
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            # And call .move() with solved, which is either True or False.
            card.move(form.cleaned_data["solved"])

        # finally you redirect the request to the same page from which you posted the request.
        # In this case , the HTTP_REFERER is the URL of the box for your current check session.
        return redirect(request.META.get("HTTP_REFERER"))

class CardCreateView(CreateView):
    model = Card
    fields = ["NL", "FR", "box"]
    success_url = reverse_lazy("card-create")

class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("card-list")
# During a check session, you want to tell your flashcards app if you knew the answer or not.
# You’ll do this by sending a POST request that contains a form to your back end.
# Notice that the structure of a Django form is similar to a Django model.

from django import forms

class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    solved = forms.BooleanField(required=False)
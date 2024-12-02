# Don't understand how this works, but it's to create a dictionary so the templates know how many boxes exist.
# You do this with a custom inclusion tag, with which you can return a template that contains the context data that a function provides

from django import template

from flashcards_app.models import BOXES, Card

register = template.Library()

@register.inclusion_tag("flashcards_app/box_links.html")
def boxes_as_links():
    boxes = []
    for box_num in BOXES:
        card_count = Card.objects.filter(box=box_num).count()
        boxes.append({
            "number": box_num,
            "card_count": card_count,
        })

    return {"boxes": boxes}
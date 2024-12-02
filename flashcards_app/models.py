from django.db import models

# Basically you're saying there are 5 boxes and
# the BOXES variable has a range from 1 to 6.
# That way you can loop through your boxes with a user-friendly numbering from 1 to 5
# instead of the zero-based numbering that the range would have otherwise defaulted to.
NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

class Card(models.Model):
    NL = models.CharField(max_length=200)
    FR = models.CharField(max_length=200)
    # The box field is to keep track where your card sits
    box = models.IntegerField(
        # By default you create your flashcard in the first box
        # With choises you make sure that the models.IntegerFiels must contain a number that's within you BOXES range
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    date_created = models.DateTimeField(auto_now_add=True)

    # To control the string representation of your Card objects, you define .__str__().
    # When you return the question string of your card instance, then you can conveniently spot wich card you're working with.
    def __str__(self):
        return self.NL

    # This is a function to move your card in the next box
    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]

        # This is to avoid you put a card in box nbr 6
        if new_box in BOXES:
            self.box = new_box
            self.save()

        return self

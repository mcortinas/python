# Form for Comment
# Form for ClientMessage

from django.forms import ModelForm
from contingut import models

class CommentForm(ModelForm):
    class Meta:
        model = models.Comment
        exclude = ("article", "timestamp")

class ClientMessageForm(ModelForm):
    class Meta:
        model = models.ClientMessage
        exclude = ("timestamp",)

from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from apps.Yugioh_Database import models


class HomeView(TemplateView):
    def get(self, request):
        list_of_cards = models.Card.objects.all()
        """
        for monsters it would be models.MonsterCard.objects.all()
        for spells it would be models.SpellCard.objects.all()
        for trap it would be models.TrapCard.objects.all()
        afterwards add them to the dictionary below with appropriate key names
        """
        my_data = {
            "cards_from_db": list_of_cards,
        }
        return render(request, "home.html", context=my_data)


def get_cards(request):
    list_of_cards = models.Card.objects.all()
    text = "<h1>List of cards</h1>"
    for card in list_of_cards:
        text += "A card was found"

    return HttpResponse("HI I HOPE THIS BLOODY WORKS NOW")

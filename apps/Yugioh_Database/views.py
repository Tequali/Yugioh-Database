from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from apps.Yugioh_Database import models


class HomeView(TemplateView):
    def get(self, request):
        list_of_monsters = models.Monster_Card.objects.all()
        list_of_spells = models.Spell_Card.objects.all()
        list_of_traps = models.Trap_Card.objects.all()
        """
        for monsters it would be models.MonsterCard.objects.all()
        for spells it would be models.SpellCard.objects.all()
        for trap it would be models.TrapCard.objects.all()
        afterwards add them to the dictionary below with appropriate key names
        """
        list_of_all_cards = (
            list(list_of_monsters) + list(list_of_spells) + list(list_of_traps)
        )
        my_data = {
            "all_cards_from_db": list_of_all_cards,
        }
        return render(request, "home.html", context=my_data)


def redirect_home(request):
    return redirect("home")

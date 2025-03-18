from django.db import models
from apps.Yugioh_Database.enums import (
    CardTypeOptions,
    MonsterAttributeOptions,
    MonsterTypeOptions,
    MonsterCardTypeOptions,
    SpellCardTypeOptions,
    TrapCardTypeOptions,
    EffectTypeOptions,
)


def maximum_level_rank_pendscale(value):
    if value > 13:
        value = 13
    return value


def maximum_link_rating(value):
    if value > 8:
        value = 8
    return value


def maximum_battle_value(value):
    if value > 5000:
        value = 5000
    return value


class Effect(models.Model):
    # this will serve like an enum
    effect_type = models.CharField(
        max_length=500,
        choices=EffectTypeOptions.options(),
        default=EffectTypeOptions.default(),
    )

    def __str__(self):
        return self.effect_type

    class Meta:
        verbose_name = "Effect"
        verbose_name_plural = "Effects"


class Precise_Effect(models.Model):
    # this will serve like an enum
    effect_category = models.ManyToManyField(Effect, related_name="Precise_Effect")
    effect_type = models.CharField(max_length=100)

    def __str__(self):
        return self.effect_type

    class Meta:
        verbose_name = "Precise Effect"
        verbose_name_plural = "Precise Effects"


class Archetype(models.Model):
    archetype_name = models.CharField(max_length=200)

    def __str__(self):
        return self.archetype_name

    class Meta:
        verbose_name = "Archetype"
        verbose_name_plural = "Archetypes"


# Create your models here.
class Card_Description(models.Model):
    description = models.TextField(default="", null=True, blank=True)
    effects = models.ManyToManyField(Effect)
    precise_effects = models.ManyToManyField(Precise_Effect)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Card Description"
        verbose_name_plural = "Card Descriptions"


class Card(Card_Description):
    name = models.CharField(max_length=100)
    archetypes = models.ManyToManyField(Archetype)
    card_type = models.CharField(
        max_length=50,
        choices=CardTypeOptions.options(),
        default=CardTypeOptions.default(),
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"


class Monster_Card(Card):
    card_id = models.ForeignKey(
        Card, related_name="Monster_Card", on_delete=models.CASCADE
    )
    card_name = Card.name
    archetypes = Card.archetypes
    card_type = Card.card_type
    attribute = models.CharField(
        max_length=50,
        choices=MonsterAttributeOptions.options(),
        default=MonsterAttributeOptions.default(),
    )
    monster_card_type = models.CharField(
        max_length=100,
        choices=MonsterCardTypeOptions.options(),
        default=MonsterCardTypeOptions.default(),
    )
    monster_type = models.CharField(
        max_length=50,
        choices=MonsterTypeOptions.options(),
        default=MonsterTypeOptions.default(),
    )
    level_rank = models.PositiveSmallIntegerField(
        default=0, validators=[maximum_level_rank_pendscale]
    )
    pendulum_scale = models.PositiveSmallIntegerField(
        default=0, validators=[maximum_level_rank_pendscale]
    )
    link_rating = models.PositiveSmallIntegerField(
        default=0, validators=[maximum_link_rating]
    )
    attack = models.PositiveSmallIntegerField(
        default=0, validators=[maximum_battle_value]
    )
    defense = models.PositiveSmallIntegerField(
        default=0, validators=[maximum_battle_value]
    )

    def __str__(self):
        return self.card_name

    class Meta:
        verbose_name = "Monster Card"
        verbose_name_plural = "Monster Cards"


class Spell_Card(Card):
    card_id = models.ForeignKey(
        Card, related_name="Spell_Card", on_delete=models.CASCADE
    )
    card_name = models.CharField(max_length=100)
    archetypes = Card.archetypes
    card_type = Card.card_type
    type = models.CharField(
        max_length=50,
        choices=SpellCardTypeOptions.options(),
        default=SpellCardTypeOptions.default(),
    )

    def __str__(self):
        return self.card_name

    class Meta:
        verbose_name = "Spell Card"
        verbose_name_plural = "Spell Cards"


class Trap_Card(Card):
    card_id = models.ForeignKey(
        Card, related_name="Trap_Card", on_delete=models.CASCADE
    )
    card_name = models.CharField(max_length=100)
    archetypes = Card.archetypes
    card_type = Card.card_type
    type = models.CharField(
        max_length=50,
        choices=TrapCardTypeOptions.options(),
        default=TrapCardTypeOptions.default(),
    )

    def __str__(self):
        return self.card_name

    class Meta:
        verbose_name = "Trap Card"
        verbose_name_plural = "Trap Cards"

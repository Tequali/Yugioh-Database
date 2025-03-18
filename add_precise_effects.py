from apps.Yugioh_Database import models


def add_activation_condition_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="ACTIVATION CONDITION"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_activation_upon_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="ACTIVATION UPON"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_activation_when_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="ACTIVATION WHEN"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_activation_others_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="ACTIVATION OTHERS"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_add_card_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="ADD CARD"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_monster_modifier_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="MONSTER STAT MODIFIERS"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_no_effect_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="NORMAL"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_allow_activation_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="ALLOW ACTIVATIONS"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_alter_summon_condition_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="ALTER SUMMON CONDITION"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_apply_effect_when_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="APPLY EFFECT WHEN"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_monster_modifier_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="MONSTER STAT MODIFIERS"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_add_card_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="ADD CARD"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_activation_others_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="ACTIVATION OTHERS"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_activation_when_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="ACTIVATION WHEN"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_apply_effect_if_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="APPLY EFFECT IF"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_attach_xyz_material_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="ATTACH XYZ MATERIAL"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_banish_shifts_location_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="BANISH SHIFTS LOCATION"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_banish_fusion_materials_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(
            effect_type="BANISH FUSION MATERIALS"
        ),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_banish_for_cost_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="BANISH FOR COST"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_banish_for_ritual_summon_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(
            effect_type="BANISH FOR RITUAL SUMMON"
        ),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_battle_related_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="BATTLE RELATED"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_external_special_summon_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(
            effect_type="EXTERNAL SPECIAL SUMMON"
        ),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_quick_effect_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="QUICK EFFECT"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_external_revive_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="EXTERNAL REVIVE"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_alternative_fusion_summon_possible_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(
            effect_type="ALTERNATIVE FUSION SUMMON POSSIBLE"
        ),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_easier_ritual_summon_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="EASIER RITUAL SUMMON"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_restriction_type_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="RESTRICTION TYPE"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_chain_effect_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="CHAIN EFFECT"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_activated_by_either_player_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(
            effect_type="ACTIVAED BY EITHER PLAYER"
        ),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


precise_effects: dict = {
    "ACTIVATION_CONDITION": [
        "Activates if destroyed while Set",
        "Activates if detached from Xyz Monster to activate its effect",
        "Activates if other Pendulum Zone is occupied",
        "Activates if other Pendulum Zone is occupied by specific card",
        "Activates if other Pendulum Zone is unoccupied",
        "Activates if returned from the field to the hand",
        "Activates if sent to the Graveyard",
        "Activates if targeted by card effect",
        "Activates if Tributed",
        "Activates if used as Fusion Material",
        "Activates if used as Link Material",
        "Activates if used as Synchro Material",
        "Activates if you gain LP",
        "Activates if you take battle damage",
        "Activates if you take effect damage",
        "Activates if your opponent draws a card",
        "Activates if your opponent gains LP",
    ],
    "ACTIVATION_UPON": [
        "Activates upon attack declaration",
        "Activates upon being flipped face-up",
        "Activates upon Flip Summon",
        "Activates upon Fusion Summon",
        "Activates upon Link Summon",
        "Activates upon Normal Summon",
        "Activates upon Pendulum Summon",
        "Activates upon Ritual Summon",
        "Activates upon Special Summon",
        "Activates upon Synchro Summon",
        "Activates upon Tribute Summon",
        "Activates upon Xyz Summon",
    ],
    "ACTIVATION_WHEN": [
        "Activates when it destroys a monster by battle",
        "Activates when it inflicts battle damage",
        "Activates when it inflicts effect damage",
        "Activates when it leaves the field",
    ],
    "ACTIVATION_OTHERS": [
        "Activates while banished",
        "Activation cannot be negated",
    ],
    "ADD_CARD": [
        "Adds banished cards to the hand",
        "Adds copies of itself to hand",
        "Adds excavated cards to the hand",
        "Adds from Deck to Extra Deck",
        "Adds from Deck to hand",
        "Adds from Extra Deck to hand",
        "Adds from Graveyard to Extra Deck",
        "Adds from Graveyard to hand",
        "Adds from hand to Extra Deck",
        "Adds from your opponent's Deck to your opponent's hand",
        "Adds Xyz Materials to the hand",
    ],
    "MONSTER_STAT_MODIFIERS": [
        "All monsters gain ATK",
        "All monsters gain DEF",
        "All monsters gain Levels",
        "All monsters lose ATK",
        "All monsters lose DEF",
        "All monsters lose Levels",
        "Changes ATK value",
        "Changes ATK value of equipped",
        "Changes Attribute",
    ],
    
}

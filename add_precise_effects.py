from apps.Yugioh_Database import models


def add_precise_effects(func, list: list):
    for entry in list:
        func()
        print(f"{entry} inserted.")
    print(f"{func.__name__} is done!")


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


def add_allow_faceup_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="ALLOW FACE UP IN DECK"),
        effect_type=list_entry,
    )
    print(f"Effect No. {index} is created!")
    return


def add_allow_multiple_summons_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="ALLOW MULTIPLE SUMMONS"),
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


def add_battle_related_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="BATTLE RELATED"),
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


def add_banish_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="BANISH"),
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


def add_banish_negated_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(effect_type="BANISH NEGATED"),
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


def add_activated_by_either_player_cards(list_entry, index):
    models.Precise_Effect.objects.create(
        effect_category=models.Effect.objects.get(
            effect_type="ACTIVAED BY EITHER PLAYER"
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
    "ALLOW_ACTIVATIONS": [
        "Allows activation of Quick-Play Spell Cards the turn they were Set",
        "Allows activation of Spell Cards from the player's hand during the opponent's turn",
        "Allows activation of Trap Cards from your hand",
        "Allows activation of Trap Cards the turn they were Set",
    ],
    "ALLOW_FACE_UP_IN_DECK": [
        "Allows face-up cards in Main Deck",
    ],
    "ALLOW_MULTIPLE_SUMMONS": [
        "Allows multiple Normal Summons",
        "Allows multiple Pendulum Summons",
        "Allows multiple Tribute Summons",
    ],
    "ALTER_SUMMON_CONDITION": [
        "Alters Summoning conditions",
    ],
    "APPLY_EFFECT_WHEN": [
        "Applies effect when Tributed for Tribute Summon",
        "Applies effect when used as Fusion Material",
        "Applies effect when used as Link Material",
        "Applies effect when used as Synchro Material",
        "Applies effect when used as Xyz Material",
        "Applies effect when used for a Ritual Summon",
    ],
    "APPLY_EFFECT_IF": [
        "Applies effect if other Pendulum Zone is not occupied by specific card",
        "Applies effect if other Pendulum Zone is unoccupied",
        "Applies effects if Link Summoned using specific Link Material",
        "Applies effects if specific Xyz Material is attached",
        "Applies effects if Xyz Material is attached",
        "Applies effects if Xyz Summoned using specific Xyz Material",
    ],
    "ATTACH_XYZ_MATERIAL": [
        "Attaches as Xyz Material",
        "Attaches from your Deck as Xyz Material",
        "Attaches from your Extra Deck as Xyz Material",
        "Attaches from your field as Xyz Material",
        "Attaches from your Graveyard as Xyz Material",
        "Attaches from your hand as Xyz Material",
        "Attaches from your opponent's Extra Deck as Xyz Material",
        "Attaches from your opponent's field as Xyz Material",
        "Attaches from your opponent's Graveyard as Xyz Material",
        "Attaches itself as Xyz Material",
        "Attaches itself from your field as Xyz Material",
        "Attaches itself from your Graveyard as Xyz Material",
        "Attaches itself from your hand as Xyz Material",
        "Attaches itself from your Pendulum Zone as Xyz Material",
        "Attaches your opponent's banished cards as Xyz Material",
    ],
    "BATTLE_RELATED": [
        "Applies DEF for damage calculation",
        "Allows direct attacks",
        "Allows multiple attacks",
        "Allows multiple attacks on monsters",
        "Banishes battling monster after damage calculation",
        "Banishes battling monster at the end of the Damage Step",
        "Banishes battling monster at the start of the Damage Step",
        "Battle damage treated as effect damage",
        "Can make multiple attacks on monsters",
    ],
    "BANISH_SHIFTS_LOCATION": [
        "Banishes cards that would be returned to the Deck",
        "Banishes cards that would be returned to the hand",
        "Banishes cards that would be sent to the Graveyard",
        "Banishes cards when it leaves the field",
        "Banishes itself when it leaves the field",
        "Banishes itself while as an Xyz Material",
    ],
    "BANISH": [
        "Banishes equipped",
        "Banishes excavated cards",
        "Banishes face-down",
        "Banishes from Deck",
        "Banishes from Extra Deck",
        "Banishes from field",
        "Banishes from field for Summon",
        "Banishes from Graveyard",
        "Banishes from Graveyard for Summon",
        "Banishes from hand",
        "Banishes from hand for Summon",
        "Banishes from the top of your Deck",
        "Banishes from the top of your opponent's Deck",
        "Banishes from your Deck",
        "Banishes from your Extra Deck",
        "Banishes from your field",
        "Banishes from your Graveyard",
        "Banishes from your hand",
        "Banishes from your opponent's Deck",
        "Banishes from your opponent's Extra Deck",
        "Banishes from your opponent's field",
        "Banishes from your opponent's Graveyard",
        "Banishes from your opponent's hand",
        "Banishes itself from field",
        "Banishes itself from Deck",
        "Banishes itself from Graveyard",
        "Banishes itself from hand",
        "Banishes itself from Pendulum Zone",
        "Banishes Xyz Materials",
    ],
    "BANISH_FUSION_MATERIALS": [
        "Banishes Fusion Materials for Contact Fusion",
        "Banishes Fusion Materials used in a Fusion Summon",
    ],
    "BANISH_FOR_COST": [
        "Banishes for cost",
        "Banishes from Deck for cost",
        "Banishes from field for cost",
        "Banishes from Graveyard for cost",
        "Banishes from hand for cost",
        "Banishes itself from field for cost",
        "Banishes itself from Graveyard for cost",
        "Banishes itself from hand for cost",
    ],
    "BANISH_FOR_RITUAL_SUMMON": [
        "Banishes monsters from Graveyard for Ritual Summon",
    ],
    "BANISH_NEGATED": [
        "Banishes negated activations",
        "Banishes negated Summons",
    ],
    "EXTERNAL_SPECIAL_SUMMON": [
        "Can always be Special Summoned",
    ],
    "ACTIVATED_BY_EITHER_PLAYER": [
        "Can be activated by either player",
    ],
    "QUICK_EFFECT": [
        "Can be activated during either player's turn",
    ],
    "EXTERNAL_REVIVE": [
        "Can be Special Summoned",
    ],
    "ALTERNATIVE_FUSION_SUMMON_POSSIBLE": [
        "Can be Special Summoned either by Fusion Summon or Contact Fusion",
    ],
    "EASIER_RITUAL_SUMMON": [
        "Can be used as entire Ritual Summon requirement",
    ],
    "RESTRICTION_TYPE": [
        "Cannot attack",
        "Cannot attack directly",
        "Cannot attack the turn it is Summoned",
        "Cannot be activated",
        "Cannot be banished",
        "Cannot be destroyed by battle",
        "Cannot be destroyed by card effects",
        "Cannot be Flip Summoned",
        "Cannot be Fusion Summoned",
        "Cannot be Link Summoned",
        "Cannot be Normal Set",
        "Cannot be Normal Summoned",
        "Cannot be Pendulum Summoned",
        "Cannot be Special Summoned",
        "Cannot be Special Summoned except by a specific method",
        "Cannot be Special Summoned from the Deck",
        "Cannot be Special Summoned from the Extra Deck",
        "Cannot be Special Summoned from the Graveyard",
        "Cannot be Special Summoned from the hand",
        "Cannot be Special Summoned while banished",
        "Cannot be Synchro Summoned",
        "Cannot be targeted by card effects",
        "Cannot be Tributed",
        "Cannot be Tributed for a Tribute Summon",
        "Cannot be used as a Fusion Material",
        "Cannot be used as a Link Material",
        "Cannot be used as a Synchro Material",
        "Cannot be used as an Xyz Material",
        "Cannot be Xyz Summoned",
        "Cannot change control",
        "Cannot conduct Battle Phase",
        "Cannot destroy by battle",
    ],
    "CHAIN_EFFECT": [
        "Chain Effects",
    ],
}

for key in precise_effects:
    if key == "ACTIVATION_CONDITION":
        add_precise_effects(add_activation_condition_cards, precise_effects[key])
    elif key == "ACTIVATION_UPON":
        add_precise_effects(add_activation_upon_cards, precise_effects[key])
    elif key == "ACTIVATION_WHEN":
        add_precise_effects(add_activation_when_cards, precise_effects[key])
    elif key == "ACTIVATION_OTHERS":
        add_precise_effects(add_activation_others_cards, precise_effects[key])
    elif key == "ADD_CARD":
        add_precise_effects(add_add_card_cards, precise_effects[key])
    elif key == "MONSTER_STAT_MODIFIERS":
        add_precise_effects(add_monster_modifier_cards, precise_effects[key])
    elif key == "ALLOW_ACTIVATIONS":
        add_precise_effects(add_allow_activation_cards, precise_effects[key])
    elif key == "ALLOW_FACE_UP_IN_DECK":
        add_precise_effects(add_allow_faceup_cards, precise_effects[key])
    elif key == "ALLOW_MULTIPLE_SUMMONS":
        add_precise_effects(add_allow_multiple_summons_cards, precise_effects[key])
    elif key == "ALTER_SUMMON_CONDITION":
        add_precise_effects(add_alter_summon_condition_cards, precise_effects[key])
    elif key == "APPLY_EFFECT_WHEN":
        add_precise_effects(add_apply_effect_when_cards, precise_effects[key])
    elif key == "APPLY_EFFECT_IF":  #
        add_precise_effects(add_apply_effect_if_cards, precise_effects[key])
    elif key == "ATTACH_XYZ_MATERIAL":  #
        add_precise_effects(add_attach_xyz_material_cards, precise_effects[key])
    elif key == "BATTLE_RELATED":  #
        add_precise_effects(add_battle_related_cards, precise_effects[key])
    elif key == "BANISH_SHIFTS_LOCATION":  #
        add_precise_effects(add_banish_shifts_location_cards, precise_effects[key])
    elif key == "BANISH":  #
        add_precise_effects(add_banish_cards, precise_effects[key])
    elif key == "BANISH_FUSION_MATERIALS":  #
        add_precise_effects(add_banish_fusion_materials_cards, precise_effects[key])
    elif key == "BANISH_FOR_COST":  #
        add_precise_effects(add_banish_for_cost_cards, precise_effects[key])
    elif key == "BANISH_FOR_RITUAL_SUMMON":  #
        add_precise_effects(add_banish_for_ritual_summon_cards, precise_effects[key])
    elif key == "BANISH_NEGATED":  #
        add_precise_effects(add_banish_negated_cards, precise_effects[key])
    elif key == "EXTERNAL_SPECIAL_SUMMON":  #
        add_precise_effects(add_external_special_summon_cards, precise_effects[key])
    elif key == "ACTIVATED_BY_EITHER_PLAYER":  #
        add_precise_effects(add_activated_by_either_player_cards, precise_effects[key])
    elif key == "QUICK_EFFECT":  #
        add_precise_effects(add_quick_effect_cards, precise_effects[key])
    elif key == "EXTERNAL_REVIVE":  #
        add_precise_effects(add_external_revive_cards, precise_effects[key])
    elif key == "ALTERNATIVE_FUSION_SUMMON_POSSIBLE":  #
        add_precise_effects(add_alternative_fusion_summon_possible_cards, precise_effects[key])
    elif key == "EASIER_RITUAL_SUMMON":  #
        add_precise_effects(add_easier_ritual_summon_cards, precise_effects[key])
    elif key == "RESTRICTION_TYPE":  #
        add_precise_effects(add_restriction_type_cards, precise_effects[key])
    elif key == "CHAIN_EFFECT":  #
        add_precise_effects(add_chain_effect_cards, precise_effects[key])
    elif key == "NORMAL":  #
        add_precise_effects(add_no_effect_cards, precise_effects[key])
    else:
        print(f"the key: {key} did not fit into any of the categories")

from abc import ABC, abstractmethod


class Options(ABC):
    @abstractmethod
    def options(cls):
        pass

    @abstractmethod
    def default(cls):
        pass


# region cards
class CardTypeOptions(Options):
    monster = "MONSTER"
    spell = "SPELL"
    trap = "TRAP"

    @classmethod
    def options(cls):
        return [
            (cls.monster, "MONSTER"),
            (cls.spell, "SPELL"),
            (cls.trap, "TRAP"),
        ]

    @classmethod
    def default(cls):
        return cls.monster


class MonsterAttributeOptions(Options):
    light = "LIGHT"
    dark = "DARK"
    earth = "EARTH"
    water = "WATER"
    wind = "WIND"
    fire = "FIRE"
    divinity = "DIVINITY"

    @classmethod
    def options(cls):
        return [
            (cls.light, "LIGHT"),
            (cls.dark, "DARK"),
            (cls.earth, "EARTH"),
            (cls.water, "WATER"),
            (cls.wind, "WIND"),
            (cls.fire, "FIRE"),
            (cls.divinity, "DIVINITY"),
        ]

    @classmethod
    def default(cls):
        return cls.light


class MonsterTypeOptions(Options):
    aqua = "AQUA"
    beast = "BEAST"
    beast_Warrior = "BEAST_WARRIOR"
    cyberse = "CYBERSE"
    dinosaur = "DINOSAUR"
    divine_Beast = "DIVINE_BEAST"
    dragon = "DRAGON"
    fairy = "FAIRY"
    fiend = "FIEND"
    fish = "FISH"
    illusion = "ILLUSION"
    insect = "INSECT"
    machine = "MACHINE"
    plant = "PLANT"
    psychic = "PSYCHIC"
    pyro = "PYRO"
    reptile = "REPTILE"
    rock = "ROCK"
    sea_Serpent = "SEA_SERPENT"
    spellcaster = "SPELLCASTER"
    thunder = "THUNDER"
    warrior = "WARRIOR"
    winged_Beast = "WINGED_BEAST"
    wyrm = "WYRM"
    zombie = "ZOMBIE"

    @classmethod
    def options(cls):
        return [
            (cls.aqua, "AQUA"),
            (cls.beast, "BEAST"),
            (cls.beast_Warrior, "BEAST-WARRIOR"),
            (cls.cyberse, "CYBERSE"),
            (cls.dinosaur, "DINOSAUR"),
            (cls.divine_Beast, "DIVINE BEAST"),
            (cls.dragon, "DRAGON"),
            (cls.fairy, "FAIRY"),
            (cls.fiend, "FIEND"),
            (cls.fish, "FISH"),
            (cls.illusion, "ILLUSION"),
            (cls.insect, "INSECT"),
            (cls.machine, "MACHINE"),
            (cls.plant, "PLANT"),
            (cls.psychic, "PSYCHIC"),
            (cls.pyro, "PYRO"),
            (cls.reptile, "REPTILE"),
            (cls.rock, "ROCK"),
            (cls.sea_Serpent, "SEA SERPENT"),
            (cls.spellcaster, "SPELLCASTER"),
            (cls.thunder, "THUNDER"),
            (cls.warrior, "WARRIOR"),
            (cls.winged_Beast, "WINGED BEAST"),
            (cls.wyrm, "WYRM"),
            (cls.zombie, "ZOMBIE"),
        ]

    @classmethod
    def default(cls):
        return cls.aqua


class MonsterCardTypeOptions(Options):
    normal = "NORMAL"
    effect = "EFFECT"
    ritual = "RITUAL"
    fusion = "FUSION"
    synchro = "SYNCHRO"
    xyz = "XYZ"
    toon = "TOON"
    spirit = "SPIRIT"
    union = "UNION"
    gemini = "GEMINI"
    tuner = "TUNER"
    flip = "FLIP"
    pendulum = "PENDULUM"
    link = "LINK"

    @classmethod
    def options(cls):
        return [
            (cls.normal, "NORMAL"),
            (cls.effect, "EFFECT"),
            (cls.ritual, "RITUAL"),
            (cls.fusion, "FUSION"),
            (cls.synchro, "SYNCHRO"),
            (cls.xyz, "XYZ"),
            (cls.toon, "TOON"),
            (cls.spirit, "SPIRIT"),
            (cls.union, "UNION"),
            (cls.gemini, "GEMINI"),
            (cls.tuner, "TUNER"),
            (cls.flip, "FLIP"),
            (cls.pendulum, "PENDULUM"),
            (cls.link, "LINK"),
        ]

    @classmethod
    def default(cls):
        return cls.normal


class SpellCardTypeOptions(Options):
    quick_play = "QUICK_PLAY"
    field = "FIELD"
    continuous = "CONTINUOUS"
    equip = "EQUIP"
    ritual = "RITUAL"
    field_Spell = "FIELD SPELL"
    normal = "NORMAL"

    @classmethod
    def options(cls):
        return [
            (cls.quick_play, "QUICK PLAY"),
            (cls.field, "FIELD"),
            (cls.continuous, "CONTINUOUS"),
            (cls.equip, "EQUIP"),
            (cls.ritual, "RITUAL"),
            (cls.field_Spell, "FIELD SPELL"),
            (cls.normal, "NORMAL"),
        ]

    @classmethod
    def default(cls):
        return cls.normal


class TrapCardTypeOptions(Options):
    normal = "NORMAL"
    continuous = "CONTINUOUS"
    counter = "COUNTER"

    @classmethod
    def options(cls):
        return [
            (cls.normal, "NORMAL"),
            (cls.continuous, "CONTINUOUS"),
            (cls.counter, "COUNTER"),
        ]

    @classmethod
    def default(cls):
        return cls.normal


# endregion


class EffectTypeOptions(Options):
    activation_condition = "ACTIVATION CONDITION"
    activation_upon = "ACTIVATION UPON"
    activation_when = "ACTIVATION WHEN"
    activation_others = "ACTIVATION OTHERS"
    add_card = "ADD CARD"
    monster_stat_modifiers = "MONSTER STAT MODIFIERS"
    allow_activations = "ALLOW ACTIVATIONS"
    alter_summon_condition = "ALTER SUMMON CONDITION"
    apply_effect_when = "APPLY EFFECT WHEN"
    apply_effect_if = "APPLY EFFECT IF"
    attach_xyz_material = "ATTACH XYZ MATERIAL"
    banish = "BANISH"
    banish_shifts_location = "BANISH SHIFTS LOCATION"
    banish_fusion_materials = "BANISH FUSION MATERIALS"
    banish_for_cost = "BANISH FOR COST"
    banish_for_ritual_summon = "BANISH FOR RITUAL SUMMON"
    battle_related = "BATTLE RELATED"
    external_special_summon = "EXTERNAL SPECIAL SUMMON"
    activated_by_either_player = "ACTIVATED BY EITHER PLAYER"
    quick_effect = "QUICK EFFECT"
    external_revive = "EXTERNAL REVIVE"
    alternative_fusion_summon_possible = "ALTERNATIVE FUSION SUMMON POSSIBLE"
    easier_ritual_summon = "EASIER RITUAL SUMMON"
    restriction_type = "RESTRICTION TYPE"
    chain_effect = "CHAIN EFFECT"
    normal = "NORMAL"


    @classmethod
    def options(cls):
        return [
            (cls.activation_condition, "ACTIVATION CONDITION"),
            (cls.activation_upon, "ACTIVATION UPON"),
            (cls.activation_when, "ACTIVATION WHEN"),
            (cls.activation_others, "ACTIVATION OTHERS"),
            (cls.add_card, "ADD CARD"),
            (cls.monster_stat_modifiers, "MONSTER STAT MODIFIERS"),
            (cls.allow_activations, "ALLOW ACTIVATIONS"),
            (cls.alter_summon_condition, "ALTER SUMMON CONDITION"),
            (cls.apply_effect_when, "APPLY EFFECT WHEN"),
            (cls.apply_effect_if, "APPLY EFFECT IF"),
            (cls.attach_xyz_material, "ATTACH XYZ MATERIAL"),
            (cls.banish, "BANISH"),
            (cls.banish_shifts_location, "BANISH SHIFTS LOCATION"),
            (cls.banish_fusion_materials, "BANISH FUSION MATERIALS"),
            (cls.banish_for_cost, "BANISH FOR COST"),
            (cls.banish_for_ritual_summon, "BANISH FOR RITUAL SUMMON"),
            (cls.battle_related, "BATTLE RELATED"),
            (cls.external_special_summon, "EXTERNAL SPECIAL SUMMON"),
            (cls.activated_by_either_player, "ACTIVATED BY EITHER PLAYER"),
            (cls.quick_effect, "QUICK EFFECT"),
            (cls.external_revive, "EXTERNAL REVIVE"),
            (
                cls.alternative_fusion_summon_possible,
                "ALTERNATIVE FUSION SUMMON POSSIBLE",
            ),
            (cls.easier_ritual_summon, "EASIER RITUAL SUMMON"),
            (cls.restriction_type, "RESTRICTION TYPE"),
            (cls.chain_effect, "CHAIN EFFECT"),
            (cls.normal, "NORMAL"),
        ]

    @classmethod
    def default(cls):
        return cls.normal

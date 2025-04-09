from django.contrib import admin
from apps.Yugioh_Database import models


# region custom_action
@admin.action(description="Set Effect Category to ALTER SUMMON CONDITION")
def set_effect_category_to_allow_face_up_in_deck(modeladmin, request, queryset):
    queryset.update(effect_category=31)


@admin.action(description="Set Effect Category to BANISH NEGATED")
def set_effect_category_to_banish_negated(modeladmin, request, queryset):
    queryset.update(effect_category=30)


@admin.action(description="Set Effect Category to BANISH")
def set_effect_category_to_banish(modeladmin, request, queryset):
    queryset.update(effect_category=29)


@admin.action(description="Set Effect Category to NORMAL")
def set_effect_category_to_normal(modeladmin, request, queryset):
    queryset.update(effect_category=28)


@admin.action(description="Set Effect Category to ACTIVATION AREA")
def set_effect_category_to_activation_area(modeladmin, request, queryset):
    queryset.update(effect_category=27)


@admin.action(description="Set Effect Category to ACTIVATION CONDITION")
def set_effect_category_to_activation_condition(modeladmin, request, queryset):
    queryset.update(effect_category=26)


@admin.action(description="Set Effect Category to ACTIVATION UPON")
def set_effect_category_to_activation_upon(modeladmin, request, queryset):
    queryset.update(effect_category=25)


@admin.action(description="Set Effect Category to ACTIVATION WHEN")
def set_effect_category_to_activation_when(modeladmin, request, queryset):
    queryset.update(effect_category=24)


@admin.action(description="Set Effect Category to ACTIVATION OTHERS")
def set_effect_category_to_activation_others(modeladmin, request, queryset):
    queryset.update(effect_category=23)


@admin.action(description="Set Effect Category to ADD CARD")
def set_effect_category_to_add_card(modeladmin, request, queryset):
    queryset.update(effect_category=22)


@admin.action(description="Set Effect Category to MONSTER STAT MODIFIERS")
def set_effect_category_to_monster_stat_modifiers(modeladmin, request, queryset):
    queryset.update(effect_category=21)


@admin.action(description="Set Effect Category to ALLOW ACTIVATION")
def set_effect_category_to_allow_activations(modeladmin, request, queryset):
    queryset.update(effect_category=20)


@admin.action(description="Set Effect Category to ALTER SUMMON CONDITION")
def set_effect_category_to_alter_summon_condition(modeladmin, request, queryset):
    queryset.update(effect_category=19)


@admin.action(description="Set Effect Category to APPLY EFFECT WHEN")
def set_effect_category_to_apply_effect_when(modeladmin, request, queryset):
    queryset.update(effect_category=18)


@admin.action(description="Set Effect Category to APPLY EFFECT IF")
def set_effect_category_to_apply_effect_if(modeladmin, request, queryset):
    queryset.update(effect_category=17)


@admin.action(description="Set Effect Category to ATTACH XYZ MATERIAL")
def set_effect_category_to_attach_xyz_material(modeladmin, request, queryset):
    queryset.update(effect_category=16)


@admin.action(description="Set Effect Category to BANISH SHIFTS LOCATION")
def set_effect_category_to_banish_shifts_location(modeladmin, request, queryset):
    queryset.update(effect_category=15)


@admin.action(description="Set Effect Category to BANISH FUSION MATERIALS")
def set_effect_category_to_banish_fusion_materials(modeladmin, request, queryset):
    queryset.update(effect_category=14)


@admin.action(description="Set Effect Category to BANISH FOR COST")
def set_effect_category_to_banish_for_cost(modeladmin, request, queryset):
    queryset.update(effect_category=13)


@admin.action(description="Set Effect Category to BANISH FOR RITUAL SUMMON")
def set_effect_category_to_banish_for_ritual_summon(modeladmin, request, queryset):
    queryset.update(effect_category=12)


@admin.action(description="Set Effect Category to BATTLE RELATED")
def set_effect_category_to_battle_related(modeladmin, request, queryset):
    queryset.update(effect_category=11)


@admin.action(description="Set Effect Category to EXTERNAL SPECIAL SUMMON")
def set_effect_category_to_external_special_summon(modeladmin, request, queryset):
    queryset.update(effect_category=10)


@admin.action(description="Set Effect Category to QUICK EFFECT")
def set_effect_category_to_quick_effect(modeladmin, request, queryset):
    queryset.update(effect_category=9)


@admin.action(description="Set Effect Category to EXTERNAL REVIVE")
def set_effect_category_to_external_revive(modeladmin, request, queryset):
    queryset.update(effect_category=8)


@admin.action(description="Set Effect Category to ALTERNATIVE FUSION SUMMON POSSIBLE")
def set_effect_category_to_alternative_fusion_summon_possible(
    modeladmin, request, queryset
):
    queryset.update(effect_category=7)


@admin.action(description="Set Effect Category to EASIER RITUAL SUMMON")
def set_effect_category_to_easier_ritual_summon(modeladmin, request, queryset):
    queryset.update(effect_category=6)


@admin.action(description="Set Effect Category to RESTRICTION TYPE")
def set_effect_category_to_restriction_type(modeladmin, request, queryset):
    queryset.update(effect_category=5)


@admin.action(description="Set Effect Category to CHAIN EFFECT")
def set_effect_category_to_chain_effect(modeladmin, request, queryset):
    queryset.update(effect_category=4)


@admin.action(description="Set Effect Category to ACTIVATED BY EITHER PLAYER")
def set_effect_category_to_activated_by_either_player(modeladmin, request, queryset):
    queryset.update(effect_category=3)


# endregion


class ArchetypeFilter(admin.SimpleListFilter):
    # create filter
    title = "Archetype"
    parameter_name = "archetype"

    def lookups(self, request, model_admin):
        """
        returns a list of tuples
        """
        return [
            ("A", "Archetype A"),
            ("B", "Archetype B"),
            ("C", "Archetype C"),
            ("D", "Archetype D"),
            ("E", "Archetype E"),
            ("F", "Archetype F"),
            ("G", "Archetype G"),
            ("H", "Archetype H"),
            ("I", "Archetype I"),
            ("J", "Archetype J"),  # 10
            ("K", "Archetype K"),
            ("L", "Archetype L"),
            ("M", "Archetype M"),
            ("N", "Archetype N"),
            ("O", "Archetype O"),
            ("P", "Archetype P"),
            ("Q", "Archetype Q"),
            ("R", "Archetype R"),
            ("S", "Archetype S"),
            ("T", "Archetype T"),  # 20
            ("U", "Archetype U"),
            ("W", "Archetype W"),
            ("V", "Archetype V"),
            ("X", "Archetype X"),
            ("Y", "Archetype Y"),
            ("Z", "Archetype Z"),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(archetype_name__startswith=self.value())
        else:
            return queryset


class ArchetypeDashboardAdmin(admin.ModelAdmin):
    # purely visual
    ordering = ("archetype_name",)
    list_display = ("archetype_name",)

    search_fields = ("archetype_name",)

    list_filter = (ArchetypeFilter,)  # add filter here after comma

    prepopulated_fields = {"archetype_name": ("archetype_name",)}

    fieldsets = (
        (
            "Archetype",
            {
                "fields": ("archetype_name",),
            },
        ),
    )
    ordering = ("archetype_name",)


class MonsterCardAdmin(admin.ModelAdmin):
    # purely visual
    ordering = ("name",)
    list_display = ("name",)

    # to search for strings, it needs to be the original name of the field
    # contained in the highest instance of inheritance
    # while any FK field needs to be searched by table_name__field_name
    search_fields = (
        "name",
        "description",
        "archetypes__archetype_name",
    )

    filter_horizontal = (
        "effects",
        "precise_effects",
        "archetypes",
        "monster_card_type",
    )


class EffectDashboardAdmin(admin.ModelAdmin):
    # purely visual
    list_filter = ("effect_category",)
    list_editable = ("effect_category",)
    list_display = ("effect_type", "effect_category")
    search_fields = ("effect_type",)

    actions = [
        set_effect_category_to_activation_condition,
        set_effect_category_to_activation_area,
        set_effect_category_to_activation_upon,
        set_effect_category_to_activation_when,
        set_effect_category_to_activation_others,
        set_effect_category_to_add_card,
        set_effect_category_to_monster_stat_modifiers,
        set_effect_category_to_allow_activations,
        set_effect_category_to_allow_face_up_in_deck,
        set_effect_category_to_alter_summon_condition,
        set_effect_category_to_apply_effect_when,
        set_effect_category_to_apply_effect_if,
        set_effect_category_to_attach_xyz_material,
        set_effect_category_to_battle_related,
        set_effect_category_to_banish,
        set_effect_category_to_banish_negated,
        set_effect_category_to_banish_for_cost,
        set_effect_category_to_banish_shifts_location,
        set_effect_category_to_banish_fusion_materials,
        set_effect_category_to_banish_for_ritual_summon,
        set_effect_category_to_external_special_summon,
        set_effect_category_to_activated_by_either_player,
        set_effect_category_to_quick_effect,
        set_effect_category_to_external_revive,
        set_effect_category_to_alternative_fusion_summon_possible,
        set_effect_category_to_easier_ritual_summon,
        set_effect_category_to_restriction_type,
        set_effect_category_to_chain_effect,
        set_effect_category_to_normal,
    ]


class CardDescriptionAdmin(admin.ModelAdmin):
    # purely visual

    filter_horizontal = (
        "effects",
        "precise_effects",
    )


class CardAdmin(admin.ModelAdmin):
    # purely visual

    filter_horizontal = (
        "effects",
        "precise_effects",
        "archetypes",
    )
    # search_fields = ("name",)


admin.site.register(models.Card, CardAdmin)
# admin.site.register(models.Effect)
# admin.site.register(models.Precise_Effect, EffectDashboardAdmin)
admin.site.register(models.Archetype, ArchetypeDashboardAdmin)
admin.site.register(models.MonsterCardType)
admin.site.register(models.Monster_Card, MonsterCardAdmin)
admin.site.register(models.Spell_Card, CardAdmin)
admin.site.register(models.Trap_Card, CardAdmin)

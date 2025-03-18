from django.contrib import admin
from apps.Yugioh_Database import models


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
    # filter_horizontal = ("archetype_options",)


admin.site.register(models.Archetype, ArchetypeDashboardAdmin)


class CardDescriptionAdmin(admin.ModelAdmin):
    # purely visual

    filter_horizontal = (
        "effects",
        "precise_effects",
    )


admin.site.register(models.Card_Description, CardDescriptionAdmin)


class CardAdmin(admin.ModelAdmin):
    # purely visual

    filter_horizontal = (
        "effects",
        "precise_effects",
        "archetypes",
    )


admin.site.register(models.Card, CardAdmin)
# Register your models here.
admin.site.register(
    models.Effect,
)
admin.site.register(models.Precise_Effect)
admin.site.register(models.Monster_Card, CardAdmin)
admin.site.register(models.Spell_Card, CardAdmin)
admin.site.register(models.Trap_Card, CardAdmin)

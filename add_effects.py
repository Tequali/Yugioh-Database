from apps.Yugioh_Database.models import Effect


def add_effects():
    for i in range(0, 28):
        effect = Effect.objects.create()
        print(f"Effect No. {i} is created!")

    return

add_effects()
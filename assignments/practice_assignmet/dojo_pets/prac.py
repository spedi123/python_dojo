import ninja
import pet


peter = ninja.Ninja("peter", "an", pet.Pet(
    "joon", "maltese", "sit & down"), "bacon", "salmon")

peter.walk().feed().bathe()
print(f"energy:{peter.pet.energy} health:{peter.pet.health}")

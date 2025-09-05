from business_object.pokemon.abstract_pokemon import AbstractPokemon

from .abstract_attack import AbstractAttack


class FixedDamageAttack(AbstractAttack):
    def compute_damage(self, APkmatk: AbstractPokemon, APkmdef: AbstractPokemon) -> int:
        return self._power

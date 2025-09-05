from business_object.attack.fixed_damage_attack import FixedDamageAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon


class MockAbstractPokemon(AbstractPokemon):
    def get_pokemon_attack_coef(self):
        return 0


class TestFixedDamageAttack:
    def test_compute_damage(self):
        # GIVEN
        sonicboom = FixedDamageAttack(power=20)
        squirtle = AbstractPokemon(level=5)
        pikachu = AbstractPokemon(level=5)

        # WHEN
        damage = sonicboom.compute_damage(squirtle, pikachu)

        # THEN
        assert damage == 20


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])

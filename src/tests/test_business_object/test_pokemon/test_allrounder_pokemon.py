from business_object.pokemon.allrounder_pokemon import AllRounderPokemon
from business_object.statistic import Statistic


class TestAllRounderPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        charizard = AllRounderPokemon(stat_current=Statistic(sp_atk=100, sp_def=100))

        # WHEN
        multiplier = charizard.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 2


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])

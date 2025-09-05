from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.statistic import Statistic


class TestAttackerPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        garchomp = AttackerPokemon(stat_current=Statistic(speed=100, attack=100))
        pikachu = AttackerPokemon(stat_current=Statistic(speed=500))

        # WHEN
        garchompmultiplier = garchomp.get_pokemon_attack_coef()
        pikachumultiplier = pikachu.get_pokemon_attack_coef()

        # THEN
        assert garchompmultiplier == 2
        assert pikachumultiplier == 3.50


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])

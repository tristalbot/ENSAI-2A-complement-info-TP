from business_object.pokemon.abstract_pokemon import AbstractPokemon


class MockAbstractPokemon(AbstractPokemon):
    def get_pokemon_attack_coef(self):
        return 0


class TestAbstractPokemonDirectly:
    def test_level_up_increases_level_by_1(self):
        squirtle = AbstractPokemon(level=5)

        squirtle.level_up()

        assert squirtle.level == 6

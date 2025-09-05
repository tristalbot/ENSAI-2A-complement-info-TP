from abc import abstractmethod

from ..pokemon.abstract_pokemon import AbstractPokemon


class AbstractAttack:
    """
    An attack
    """

    # -------------------------------------------------------------------------
    # Constructor
    # -------------------------------------------------------------------------

    def __init__(self, power=0, name=None, description=None):
        # -----------------------------
        # Attributes
        # -----------------------------
        self._power: int = power
        self._name: str = name
        self._description: str = description

    @abstractmethod
    def compute_damage(self, APkmatk: AbstractPokemon, APkmdef: AbstractPokemon) -> int:
        pass

    @property
    def power(self):
        return self._power

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description


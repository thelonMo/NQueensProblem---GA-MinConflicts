from Utilities.board_utils import to_binary_string, count_bits_set
from Utilities.lookup_tables import ATTACK_LUT, bit_length


class Genome:

    def __init__(self, chromosome, size):
        self._chromosome = chromosome
        self._size = size
        self._fitness = size * (size - 1) // 2
        self.eval_fitness()

    def __repr__(self) -> str:
        return 'Genome(chromosome: {} - fitness: {})'\
            .format(to_binary_string(self._chromosome, self._size), self._fitness)

    def __lt__(self, other) -> bool:
        return self._fitness < other.fitness

    @property
    def fitness(self) -> int:
        return self._fitness

    @property
    def size(self) -> int:
        return self._size

    @property
    def chromosome(self) -> int:
        return self._chromosome

    @chromosome.setter
    def chromosome(self, value) -> None:
        self._chromosome = value

    def eval_fitness(self) -> None:
        attacks = 0
        squares = bit_length(self._chromosome)
        for square in squares:
            attack_bb = ATTACK_LUT[square]
            attacks  += count_bits_set(attack_bb & self._chromosome)
        self._fitness -= attacks // 2

import random

from .exceptions import UnableToBreedException


class Gender:
    """
    An enum for defining genders.
    """

    # NOTE: I really don't care about political correctness for
    # this algorithm. Numerical values only serve a logical purpose.
    # Undefined only means unspecified.
    MALE = 0x2
    FEMALE = 0x1
    UNDEFINED = 0x0

    CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNDEFINED, 'Undefined')
    )

    @classmethod
    def get_keys(cls):
        """
        Returns all the choices as a raw value.
        """
        return [key for key, value in cls.CHOICES if key != cls.UNDEFINED]

    @classmethod
    def get_random_gender(cls):
        """
        Returns a random gender.
        """
        keys = cls.get_keys()
        index = random.randrange(0, len(keys))
        return keys[index]

    @classmethod
    def is_valid(cls, gender):
        """
        Returns wheter the gender is valid and defined.
        """
        if gender == cls.UNDEFINED:
            return False
        return gender in [cls.MALE, cls.FEMALE]

    @classmethod
    def can_mate(cls, gender_x, gender_y):
        """
        Returns whether the two genders can mate.
        """
        if not all([cls.is_valid(gender_x), cls.is_valid(gender_y)]):
            return False
        return gender_x != gender_y


class Panthera:
    """
    A Panthera hybrid is a crossbreed between any of four
    species—tiger, lion, jaguar and leopard—in captivity.

    Source: https://en.wikipedia.org/wiki/Panthera_hybrid
    """

    male_prefix = ''
    male_suffix = ''
    female_prefix = ''
    female_suffix = ''
    generation = 0
    gender = Gender.UNDEFINED
    parent = None
    children = []

    def __init__(self, mother=None, father=None, children=[]):
        if mother:
            if not issubclass(mother.__class__, Panthera):
                raise ValueError('mother must be an instance of Panthera')
        if father:
            if not issubclass(father.__class__, Panthera):
                raise ValueError('father must be an instance of Panthera')
        if len(children) > 0:
            for i, child in enumerate(children):
                if not issubclass(child.__class__, Panthera):
                    raise ValueError(
                        f'All children passed must be an instance of '
                        f'Panthera. Recieved {child} in index {i}.'
                    )
        self.gender = Gender.get_random_gender()
        self.mother = mother
        self.father = father
        self.children = children

    def __gt__(self, other):
        try:
            return self.generation > other.generation
        except (AttributeError, TypeError):
            return False

    def __gte__(self, other):
        try:
            return self.generation >= other.generation
        except (AttributeError, TypeError):
            return False

    def __lt__(self, other):
        try:
            return self.generation < other.generation
        except (AttributeError, TypeError):
            return False

    def __lte__(self, other):
        try:
            return self.generation <= other.generation
        except (AttributeError, TypeError):
            return False

    def __eq__(self, other):
        try:
            return self.generation == other.generation
        except (AttributeError, ValueError):
            return False

    def __str__(self):
        return self.name

    @property
    def name(self):
        """
        Returns the proper name of the panthera
        based on its gender.
        """
        mapping = {
            Gender.MALE: f'{self.male_prefix}{self.male_suffix}',
            Gender.FEMALE: f'{self.female_prefix}{self.female_suffix}'
        }
        return mapping[self.gender]

    def _add_child(self, child):
        """
        Receives another panthera then identifies it
        as the child of the instance.
        """
        self.children.append(child)

    def get_name_fragments(self, partner):
        """
        A virtual method called when breeding to determine
        the amalgamation of the offspring's name based on
        the parent's panthera.
        """
        # NOTE: Notice that the argument `partner` is
        # unused by default. This is intended to be used
        # by any possible overrides.
        mapping = {
            Gender.MALE: (self.male_prefix, self.male_suffix),
            Gender.FEMALE: (self.female_prefix, self.female_suffix)
        }
        prefix, suffix = mapping[self.gender]
        return {
            'prefix': prefix,
            'suffix': suffix
        }

    @classmethod
    def breed(cls, panthera_x, panthera_y):
        """
        Breeds two panthera together, then returns the offspring.
        """
        if not issubclass(panthera_x.__class__, Panthera):
            raise ValueError('panthera_x must be an instance of Panthera')
        if not issubclass(panthera_y.__class__, Panthera):
            raise ValueError('panthera_y must be an instance of Panthera')
        if not Gender.can_mate(panthera_x.gender, panthera_y.gender):
            raise UnableToBreedException(
                f'A {panthera_x.name} is unable to breed '
                f'with a {panthera_y.name}.'
            )
        parents = [panthera_x, panthera_y]
        male = max(parents, key=lambda panthera: panthera.gender)
        female = min(parents, key=lambda panthera: panthera.gender)
        male_fragments = male.get_name_fragments(female)
        female_fragments = female.get_name_fragments(male)
        offspring = Panthera(
            mother=female,
            father=male,
        )
        offspring.male_prefix = male_fragments['prefix']
        offspring.male_suffix = male_fragments['suffix']
        offspring.female_prefix = female_fragments['prefix']
        offspring.female_suffix = female_fragments['suffix']
        male._add_child(offspring)
        female._add_child(offspring)
        return offspring

    def breed_with(self, partner):
        """
        Breeds this panthera to another one of its species.
        """
        if not issubclass(partner.__class__, Panthera):
            raise ValueError('partner must be an instance of Panthera')
        return self.breed(self, partner)

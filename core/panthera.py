from .mixins import NameMapperMixin
from .panthera_core import Gender
from .panthera_core import Panthera


class Tiger(NameMapperMixin, Panthera):
    """
    """

    male_prefix = 'Ti'
    male_suffix = 'ger'
    female_prefix = 'Ti'
    female_suffix = 'gress'

    self_with_male_map = {
        'Lion': {
            'prefix': 'Li',
            'suffix': 'ger'
        },
        'Jaguar': {
            'prefix': 'Jag',
            'suffix': 'gress'
        },
        'Leopard': {
            'prefix': 'Leo',
            'suffix': 'gress'
        },
    }
    self_with_female_map = {
        'Lioness': {
            'prefix': 'Ti',
            'suffix': 'goness'
        },
        'Jaguaress': {
            'prefix': 'Ti',
            'suffix': 'guar'
        },
        'Leopardess': {
            'prefix': 'Ti',
            'suffix': 'gard'
        },
    }


class Lion(NameMapperMixin, Panthera):
    """
    """

    male_prefix = 'Li'
    male_suffix = 'on'
    female_prefix = 'Li'
    female_suffix = 'oness'

    self_with_male_map = {
        'Tiger': {
            'prefix': 'Ti',
            'suffix': 'gon'
        },
        'Jaguar': {
            'prefix': 'Jag',
            'suffix': 'lioness'
        },
        'Leopard': {
            'prefix': 'Leo',
            'suffix': 'pon'
        },
    }
    self_with_female_map = {
        'Tigress': {
            'prefix': 'Li',
            'suffix': 'gress'
        },
        'Jaguaress': {
            'prefix': 'Li',
            'suffix': 'guar'
        },
        'Leopardess': {
            'prefix': 'Li',
            'suffix': 'pard'
        },
    }


class Jaguar(NameMapperMixin, Panthera):
    """
    """

    male_prefix = 'Jag'
    male_suffix = 'uar'
    female_prefix = 'Ja'
    female_suffix = 'guaress'

    self_with_male_map = {
        'Tiger': {
            'prefix': 'Jag',
            'suffix': 'ger'
        },
        'Lion': {
            'prefix': 'Li',
            'suffix': 'guaress'
        },
        'Leopard': {
            'prefix': 'Le',
            'suffix': 'guaress'
        },
    }
    self_with_female_map = {
        'Tigress': {
            'prefix': 'Ti',
            'suffix': 'guaress'
        },
        'Leopardess': {
            'prefix': 'Ja',
            'suffix': 'gupard'
        },
        'Lioness': {
            'prefix': 'Jag',
            'suffix': 'lion'
        },
    }


class Leopard(NameMapperMixin, Panthera):
    """
    """

    male_prefix = 'Leo'
    male_suffix = 'pard'
    female_prefix = 'Leo'
    female_suffix = 'pardess'

    self_with_male_map = {
        'Tiger': {
            'prefix': 'Ti',
            'suffix': 'gardess'
        },
        'Jaguar': {
            'prefix': 'Ja',
            'suffix': 'gupardess'
        },
        'Lion': {
            'prefix': 'Li',
            'suffix': 'pardess'
        }
    }
    self_with_female_map = {
        'Tigress': {
            'prefix': 'Leo',
            'suffix': 'ger'
        },
        'Jaguaress': {
            'prefix': 'Le',
            'suffix': 'guar'
        },
        'Lioness': {
            'prefix': 'Leo',
            'suffix': 'poness'
        }
    }

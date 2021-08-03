from core import Gender
from core import Leopard
from core import Lion
from core import Jaguar
from core import Panthera
from core import Tiger


def get_defined_panthera():
    """
    Returns an assorted data set of panthera.
    """
    return {
        'leopard': {
            'male': Leopard(gender=Gender.MALE),
            'female': Leopard(gender=Gender.FEMALE)
        },
        'lion': {
            'male': Lion(gender=Gender.MALE),
            'female': Lion(gender=Gender.FEMALE)
        },
        'jaguar': {
            'male': Jaguar(gender=Gender.MALE),
            'female': Jaguar(gender=Gender.FEMALE)
        },
        'tiger': {
            'male': Tiger(gender=Gender.MALE),
            'female': Tiger(gender=Gender.FEMALE)
        }
    }


def test_breeding():
    """
    Test breeding process.
    """
    panthera_data = get_defined_panthera()
    offsprings = [
        # Leopard
        {
            'child': Panthera.breed(
                panthera_data['leopard']['male'],
                panthera_data['leopard']['female']
            ),
            'assertion': ['Leopard', 'Leopardess']
        },

        # Leopard to female of different breed
        {
            'child': Panthera.breed(
                panthera_data['leopard']['male'],
                panthera_data['lion']['female']
            ),
            'assertion': ['Leopon', 'Leoponess']
        },
        {
            'child': Panthera.breed(
                panthera_data['leopard']['male'],
                panthera_data['jaguar']['female']
            ),
            'assertion': ['Leguar', 'Leguaress']
        },
        {
            'child': Panthera.breed(
                panthera_data['leopard']['male'],
                panthera_data['tiger']['female']
            ),
            'assertion': ['Leoger', 'Leogress']
        },

        # Leopardess to male of different breed
        {
            'child': Panthera.breed(
                panthera_data['leopard']['female'],
                panthera_data['lion']['male']
            ),
            'assertion': ['Lipard', 'Lipardess']
        },
        {
            'child': Panthera.breed(
                panthera_data['leopard']['female'],
                panthera_data['jaguar']['male']
            ),
            'assertion': ['Jagupard', 'Jagupardess']
        },
        {
            'child': Panthera.breed(
                panthera_data['leopard']['female'],
                panthera_data['tiger']['male']
            ),
            'assertion': ['Tigard', 'Tigardess']
        },

        # Jaguar
        {
            'child': Panthera.breed(
                panthera_data['jaguar']['male'],
                panthera_data['jaguar']['female']
            ),
            'assertion': ['Jaguar', 'Jaguaress']
        },

        # Jaguar to female of other breed
        {
            'child': Panthera.breed(
                panthera_data['jaguar']['male'],
                panthera_data['tiger']['female']
            ),
            'assertion': ['Jagger', 'Jaggress']
        },
        {
            'child': Panthera.breed(
                panthera_data['jaguar']['male'],
                panthera_data['lion']['female']
            ),
            'assertion': ['Jaglion', 'Jaglioness']
        },

        # Jaguaress to male of other breed
        {
            'child': Panthera.breed(
                panthera_data['jaguar']['female'],
                panthera_data['tiger']['male']
            ),
            'assertion': ['Tiguar', 'Tiguaress']
        },
        {
            'child': Panthera.breed(
                panthera_data['jaguar']['female'],
                panthera_data['lion']['male']
            ),
            'assertion': ['Liguar', 'Liguaress']
        },

        # Lion
        {
            'child': Panthera.breed(
                panthera_data['lion']['male'],
                panthera_data['lion']['female']
            ),
            'assertion': ['Lion', 'Lioness']
        },

        # Lion to tiger
        {
            'child': Panthera.breed(
                panthera_data['lion']['male'],
                panthera_data['tiger']['female']
            ),
            'assertion': ['Liger', 'Ligress']
        },
        {
            'child': Panthera.breed(
                panthera_data['tiger']['male'],
                panthera_data['lion']['female']
            ),
            'assertion': ['Tigon', 'Tigoness']
        },

        # Tiger
        {
            'child': Panthera.breed(
                panthera_data['tiger']['male'],
                panthera_data['tiger']['female']
            ),
            'assertion': ['Tiger', 'Tigress']
        },
    ]

    for offspring in offsprings:
        assert offspring['child'].name in offspring['assertion']

    return panthera_data


if __name__ == '__main__':
    try:
        test_breeding()
        print('Test succeeded! :)')
    except AssertionError:
        print('Test Failed :(')

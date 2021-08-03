from core.panthera import Leopard
from core.panthera import Lion
from core.panthera import Jaguar
from core.panthera import Tiger
from core.panthera_core import Gender


count_per_specie = 10

leopards = []
lions = []
jaguars = []
tigers = []

for i in range(count_per_specie):
    leopards.append(Leopard())
    lions.append(Lion())
    jaguars.append(Jaguar())
    tigers.append(Tiger())


female_tigers = [tiger for tiger in tigers if tiger.gender == Gender.FEMALE]
male_tigers = [tiger for tiger in tigers if tiger.gender == Gender.MALE]

female_lions = [lion for lion in lions if lion.gender == Gender.FEMALE]
male_lions = [lion for lion in lions if lion.gender == Gender.MALE]

child = female_lions[0].breed_with(male_tigers[0])


import pdb; pdb.set_trace()

from core.panthera import Leopard
from core.panthera import Lion
from core.panthera import Jaguar
from core.panthera import Tiger


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


import pdb; pdb.set_trace()

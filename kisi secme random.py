import random

lst = ["sam", "dean", "jo", "sarah", "jones", "matthew", "samuel", "ted", "barney", "robin", "marshall", "lily", "joanna"]

while lst:
    chosen = random.sample(lst,2)
    print(chosen)
    
    for item in chosen:
        lst.remove(item)
    if len(lst) % 2 == 1:
        lst.append("   ")
    



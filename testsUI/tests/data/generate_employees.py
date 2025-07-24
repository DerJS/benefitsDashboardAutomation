import random
import string

def generate_random_employee():
    def random_text(max_characters):
        lenght=random.randint(3,max_characters)
        return ''.join(random.choices(string.ascii_letters, k=lenght)).capitalize()

    first_name=random_text(50)[:50]
    last_name=random_text(50)[:50]
    dependents=random.randint(0, 32)

    return{
    "first_name": first_name,
    "last_name": last_name,
    "dependents": dependents
    }
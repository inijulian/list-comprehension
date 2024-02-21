# Import library external
import random

# Membuat daftar yang berisi hanya bilangan genap dari daftar bilangan acak
random_numbers = [random.randint(1, 100) for _ in range(10)]
even_numbers = [num for num in random_numbers if num % 2 == 0]

print("Random Numbers:", random_numbers)
print("Even Numbers:", even_numbers)
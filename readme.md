# LIST COMPREHENSION

## Definisi 
List comprehensions adalah cara ringkas untuk membuat list di Python yang memungkinkan kita untuk membuat list dengan sintaks yang lebih sederhana dan mudah dibaca.
List comprehensions menyediakan cara ringkas untuk membuat daftar baru berdasarkan nilai daftar yang sudah ada dan cara untuk menulis loop `for` lebih jelas.
    
Nama 'list comprehension' bisa sedikit membingungkan karena seakan hanya bekerja untuk list saja. Pada kenyataannya, kata 'list' pada list comprehension digunakan untuk menunjukkan bahwa kita bisa membuat loop untuk semua iterable dalam Python dan hasil akhirnya berupa list.

## Kelebihan
- List comprehension menyederhanakan sintaks dan membuat kode lebih ringkas dan mudah dipahami. Ini dapat mengurangi jumlah baris kode yang diperlukan untuk membuat list.
- List comprehension dieksekusi lebih cepat daripada pendekatan tradisional yang menggunakan loop for karena implementasinya di dalam interpreter Python. 

## Kekurangan
- Keterbatasan saat Debugging
- Kemungkinan overuse jika digunakan berlebihan atau tidak tepat.

## Cara Kerja
![cara kerja](https://www.programiz.com/sites/tutorial2program/files/python-working-of-list-comprehension.png)

## Syntax
Karena list comprehension juga ternary operator, maka dibutuhkan 3 operand dan 2 operator.
```python
<variable-target> = [<kembalian> for <item> in <iterable> if <kondisi>]
```

## Parameter
**variable-target** : variable untuk menampung list yang telah dibuat
**kembalian**       : nilai yang akan dikembalikan sebagai elemen list. Dapat berupa nilai tetap, variable, maupun ekspresi untuk memproses nilai item
**item**            : penampung nilai dari iterable pada tiap iterasi, nilai ini dapat digunakan sebagai ekspresi dalam kembalian
**iterable**        : variable yang berisi kumpulan nilai (list, string, tuple, dll)

## [Contoh Penggunaan](./list_comprehension,py)
```python
# Tanpa list comprehension
squares = []
for x in range(10):
    squares.append(x**2)

# Dengan list comprehension
squares = [x**2 for x in range(10)]
```

## Referensi
https://www.geeksforgeeks.org/python-list-comprehension/
https://www.programiz.com/python-programming/list-comprehension
https://www.invasikode.com/list-comprehension-pada-pyhton
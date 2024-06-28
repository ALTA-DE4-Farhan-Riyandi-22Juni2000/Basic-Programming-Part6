def caesar(offset,input_str):
  hasil = ""
  # traverse text
  for i in range(len(input_str)):
    karakter = input_str[i]

    if (karakter.isupper()):
      hasil += chr((ord(karakter) + offset-65) % 26 + 65)
		# Untuk karakter huruf besar
    # ord() digunakan untuk mengembalikan nilai ASCII dari karakter char. Misalnya, ord('A') akan mengembalikan nilai 65, ord('B') akan mengembalikan nilai 66, dan seterusnya.
    # modulo % 26 untuk memastikan hasil pergeseran tetap dalam rentang 0 sampai 25.
    # Fungsi chr() digunakan untuk mengonversi nilai ASCII kembali menjadi karakter. Misalnya, chr(65) menghasilkan karakter 'A', chr(66) menghasilkan karakter 'B', dan seterusnya.
    else:
      hasil += chr((ord(karakter) + offset-97) % 26 + 97)
		# untuk karakter huruf kecil
    # ord() digunakan untuk mengembalikan nilai ASCII dari karakter char. Misalnya, ord('a') akan mengembalikan nilai 97, ord('b') akan mengembalikan nilai 98, dan seterusnya.
    # modulo % 26 untuk memastikan hasil pergeseran tetap dalam rentang 0 sampai 25.
    # Fungsi chr() digunakan untuk mengonversi nilai ASCII kembali menjadi karakter. Misalnya, chr(97) menghasilkan karakter 'a', chr(98) menghasilkan karakter 'b', dan seterusnya.
  return hasil

if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl
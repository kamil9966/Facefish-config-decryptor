import sys
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad

def read_hex_file(file_path, offset, length):
    with open(file_path, 'rb') as f:
        f.seek(offset)
        data = f.read(length)
        hex_data = data.hex()
        print()
        print("Facefish ROOTKIT config extractor (v1.2) /by Tat@r1in\ - my github projects https://github.com/kamil9966 ")
        print()
        print("Исходная часть конфига в файле")
        print()
        for i in range(0, len(hex_data), 2):
            print(hex_data[i:i+2], end=' ')
            if (i // 2) % 16 == 15:
                print()

        #блок дешифровки бловфиша
        key = b'builbuil' # ключ
        iv = b'\x00\x00\x00\x00\x00\x00\x00\x00'# вектор
        cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(data)
        pad_size = decrypted_data[-1]
        if pad_size > 0 and pad_size <= 8:
            decrypted_data = decrypted_data[:-pad_size]

        print("\nДешифрованный конфиг в хексе:")
        decrypted_hex_data = decrypted_data.hex()
        for i in range(0, len(decrypted_hex_data), 2):
            print(decrypted_hex_data[i:i+2], end=' ')
            if (i // 2) % 16 == 15:
                print()

        print("\nДешифрованный конфиг в аски:")
        ascii_data = decrypted_data.decode('utf-8', errors='replace')
        for i in range(0, len(ascii_data)):
            print(ascii_data[i], end='')
            if (i + 1) % 16 == 0:
                print()
            elif ascii_data[i] == '\n':
                print()
            else:
                print(' ', end='')

if __name__ == '__main__':
    if len(sys.argv)!= 2:
        print("Введи путь до файла через TAB")
        sys.exit(1)

    file_path = sys.argv[1] # если отработал без успех, открыть файл руткта в hxd самом низу полседние последние 10 строк - это конфиг, соответсвенно подставить смещения и длинну относительно адресов из вашего семпла
    offset = 0x1CCD0  # смещение в hex
    length = 0x90  # длина относительно последнего значния оффсета

    read_hex_file(file_path, offset, length)
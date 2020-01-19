# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'

mac = mac.replace(":","")
mac_decimal = int(mac,16)
mac_binary = bin(mac_decimal)
mac_str = str(mac_binary).replace("0b","")

print(mac_str)

#done
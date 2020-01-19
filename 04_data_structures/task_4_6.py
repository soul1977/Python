# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

tmp = ospf_route.replace(",", "")
tmp = tmp.split()
protocol = tmp[0]
protocol = protocol.replace("O", "OSPF")
prefix = tmp[1]
metric = tmp[2].strip("[]")
next_hop = tmp[4]
update = tmp[5]
interface = tmp[6]

print(f'''
Protocol:              {protocol}
Prefix:                {prefix}
AD/Metric:             {metric}
Next-Hop:              {next_hop}
Last update:           {update}
Outbound Interface:    {interface}
''')

# done
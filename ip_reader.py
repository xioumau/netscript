#!/usr/bin/env python
import os
import csv

tll = 10
awk = "awk -F '(' '{ print $2 }' | awk -F ')' '{ print $1 }' | awk 'NF'"
save_to = "awk '!seen[$0]++' rota_temp.csv > rota.csv"
remove = "rm -Rf rota_temp.csv"
scan = "nmap -sT -O -oN scan.csv -iL rota.csv -p 20,21,22,23,25,26,35,37,38,39,41,42,43,49,53,57,67,68,69,70,79,80,81,82,88,101,102,107,109,110,111,113,115,117,118,119,123,135,137,138,139,143,152,153,156,158,161,162,170,179,194,201,209,213,218,220,259,264,311,318,323,383,366,369,371,384,387,389,401,411,412,427,443,444,445,464,465,500,502,512,513,514,515,517,518,520,524,525,530,531,532,533,540,542,543,544,546,547,548,550,554,556,560,561,563,587,591,593,604,631,639,646,647,648,652,654,665,666,674,691,692,694,695,698,699,700,701,702,706,711,712,720,749,750,782,829,860,873,901,902,904,981,989,990,991,992,993,995,1001,1059,1080,1099,1109,1167,1176,1182,1194,1198,1200,1214,1223,1234,1241,1248,1270,1311,1313,1337,1344,1352,1387,1414,1431,1433,1434,1494,1512,1514,1521,1522,1524,1526,1533,1547,1550,1581,1589,1627,1677,1701,1716,1723,1725,1755,1761,1762-1768,1812,1813,1863,1883,1900,1935,1970,1971,1972,1975-1977,1984,1985,2000,2002,2030,2031,2049,2053,2056,2074,2082,2083,2086,2087,2095,2096,2161,2181,2200,2219,2220,2222,2301,2302,2303,2305,2369,2370,2381,2400,2404,2447,2483,2484,2546,2593,2598,2612,2710,2735,2809,2944,2945,2948,2949,2967,3000,3001,3002,3003,3004,3006,3007,3050,3074,3128,3260,3305,3306,3333,3389,3396,3689,3690,3784,3785,3872,3900,3945,4000,4007,4089,4093,4096,4100,4111,4226,4224,4569,4662,4664,4672,4894,4899,5000,5001,5003,5004,5005,5050,5051,5060,5061,5093,5104,5121,5190,5222,5223,5269,5351,5353,5402,5405,5432,5445,5495,5498,5499,5500,5501,5517,5555,5556,5631,5666,5667,5800,5814,5900,5938,6000,6001,6005,6050,6051,6112,6129,6257,6346,6347,6502,6522,6543,6566,6619,6665-6669,6679,6697,6699,6881-6999,7000,7001,7002,7005,7006,7010,7171,7312,7707,8000,8002,8008,8010,8074,8080,8086,8087,8090,8118,8200,8220,8222,8291,8294,8330,8331,8332,8333,8400,8443,8500,8767,8880,8888,9000,9001,9009,9043,9060,9100,9101,9102,9103,9200,9535,9800,9999,10000,10008,10050,10051,10113,10114,10115,10116,10480,11235,11294,11371,11576,12345,12975,13720,13721,13724,13782,13783,14567,15000,15567,15345,16384,16567,19226,19813,20000,20720,22347,22350,24800,24842,25565,25575,25999,26000,27000,27010,27015,27374,27500,27888,27900,27901,27960,28910,28960,29900,29920,30000,30564,31337,31415,31456-31458,32245,32400,33434,37777,36963,40000,43594,43595,47808 "

menu = int(input('Escolha uma opção:\n[1]Scanner de rede interna\n[2]Trace uma rota\n[3].....  '))
if menu == 1:
    ip_number = str(input('Digite o endereço: '))
    internal_scan = f'nmap -A -T4 {ip_number}'
    os.system(internal_scan)

if menu == 2:
    host = str(input('Digite o destino: '))
    print('Aguarde...\nA operação pode demorar alguns minutos.')
    os.system('echo > rota_temp.csv')
    while True:
        ping = f'ping -c 1 -t {tll} {host} | {awk} >> rota_temp.csv'
        os.system(ping)
        tll -= 1
        if tll == 0:
            break
    os.system(save_to)
    os.system(remove)
    os.system(scan)

"""filename = 'rota.csv'
with open(filename) as f:
    reader = csv.reader(f)
    ip = []
    for row in reader:
        ip.append(row)
    print(ip)
"""
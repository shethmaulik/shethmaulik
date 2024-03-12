from csv import reader
from pprint import pprint
import paramiko
import time

conf_dict = {}



with open('01_config_in_row.csv') as csv_data:
    csv_content = reader(csv_data)
    #print (dir(csv_content))
    for device in csv_content:
        print(device)
        ip = device[0]
        print(ip)
        if not ip:
            continue
        #print (ip)
        #print(device[1:])
        final_conf = []  
        for conf in device[1:]:
            if not conf:
                continue
        conf_dict[ip] = final_conf

pprint(conf_dict)


# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vordynsk <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/12 17:13:51 by vordynsk          #+#    #+#              #
#    Updated: 2020/01/15 20:41:38 by vordynsk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests 
#import tkinter

url_locate = "https://cisco-cmx.unit.ua/"
login_locate = "RO"
password_locate = "just4reading"

url_presence = "https://cisco-presence.unit.ua"
login_presence = "RO"
password_presence = "Passw0rd"

all_clients = "api/location/v2/clients"

try:  
    r = requests.request("GET", url_locate + all_clients, auth=(login_locate, password_locate), verify=False) 
except:
    print("error occured\nexiting...")
    exit()
data = r.json()
print( data[0] )
print( len(data) )
#tkinter._test()

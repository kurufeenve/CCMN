# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Locate.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vordynsk <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 21:01:31 by vordynsk          #+#    #+#              #
#    Updated: 2020/01/16 21:26:57 by vordynsk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
from Request import *

class   Locate(Request):

    '''class to access "Locate" Cisco API'''

    clients = "api/location/v2/clients"
    all_maps = "api/config/v1/maps"
    #https://cisco-cmx.unit.ua/api/config/v1/maps/imagesource/domain_4_1511041548007.png?login=%22RO%22password=%22just4reading%22verify=False

    def __init__(self):
        super().__init__("https://cisco-cmx.unit.ua/", "RO", "just4reading")

    def get_number_of_clients(self):
        return len(self.get_request(self.clients))

    def get_all_maps(self):
        try:
            os.mkdir("./maps")
        except OSError as e:
            pass
        return self.get_request(self.all_maps)

if __name__ == '__main__':
    L = Locate()
    print (L.get_number_of_clients())
    print (L.get_all_maps())

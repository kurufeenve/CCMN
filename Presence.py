# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Presence.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vordynsk <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/21 20:39:17 by vordynsk          #+#    #+#              #
#    Updated: 2020/01/21 21:04:21 by vordynsk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import json
from Request import *

class   Presence(Request):

    '''class to access "Presence" Cisco API'''

    site_id = "api/config/v1/sites"

    def __init__(self):
        super().__init__("https://cisco-presence.unit.ua/", "RO", "Passw0rd")

    def get_site_id(self):
        r = self.get_request(self.site_id, None)
        return r

if __name__ == '__main__':
    P = Presence()
    print (P.get_site_id())

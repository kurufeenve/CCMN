# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Locate.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vordynsk <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 21:01:31 by vordynsk          #+#    #+#              #
#    Updated: 2020/01/15 21:49:08 by vordynsk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Request import *

class   Locate(Request):

    '''class to access "Locate" Cisco API'''

    def __init__(self):
        super().__init__("https://cisco-cmx.unit.ua/", "RO", "just4reading")

    def get_number_of_clients(self):
        return len(self.get_request("api/location/v2/clients"))

    

if __name__ == '__main__':
    L = Locate()
    print (L.get_number_of_clients())

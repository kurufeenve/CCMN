# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Locate.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vordynsk <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 21:01:31 by vordynsk          #+#    #+#              #
#    Updated: 2020/01/18 17:41:55 by vordynsk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
from Request import *


class   Locate(Request):

    '''class to access "Locate" Cisco API'''

    clients = "api/location/v2/clients"
    all_maps = "api/config/v1/maps"
    map_image = "api/config/v1/maps/imagesource/"
    map_names = {}
    path_to_maps = "./maps/"

    def __init__(self):
        super().__init__("https://cisco-cmx.unit.ua/", "RO", "just4reading")

    def get_number_of_clients(self):
        return len(self.get_request(self.clients, None))

    def get_all_maps(self): 
        maps_json =  self.get_request(self.all_maps, None)
        for campus in maps_json['campuses']:
            for building in campus['buildingList']:
                for floor in building['floorList']:
                    self.map_names[floor['name']] = floor['image']['imageName']
        return self.map_names

    def get_map_images(self):
        try:
            os.mkdir(self.path_to_maps)
        except OSError as e:
            pass
        for floor_name in self.map_names:
            r = self.get_request(self.map_image + self.map_names[floor_name], 'image')
            if r.status_code == 200:
                with open(self.path_to_maps + floor_name, 'wb') as f:
                    for chunk in r.iter_content(1024):
                        f.write(chunk)

if __name__ == '__main__':
    L = Locate()
    print (L.get_number_of_clients())
    print (L.get_all_maps())
    print (L.get_map_images())

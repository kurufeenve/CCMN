# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Locate.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vordynsk <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 21:01:31 by vordynsk          #+#    #+#              #
#    Updated: 2020/01/20 21:26:54 by vordynsk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import json
import os
from Request import *


class   Locate(Request):

    '''class to access "Locate" Cisco API'''

    clients = "api/location/v2/clients"
    all_maps = "api/config/v1/maps"
    map_image = "api/config/v1/maps/imagesource/"
    map_names = {}
    path_to_maps = "./maps/"
    old_clients = {}
    new_clients = {}

    def __init__(self):
        super().__init__("https://cisco-cmx.unit.ua/", "RO", "just4reading")

    def get_number_of_clients(self):
        r = self.get_request(self.clients, None)
        try:
            if r['error'] != 200:
                return r            
        except:
            pass
        return len(r)

    def get_clients(self):
        for key in self.new_clients:
            if key in self.old_clients:
                self.old_clients[key]['userName'] = self.new_clients[key]['userName']
                self.old_clients[key]['floorName'] = self.new_clients[key]['floorName']
                self.old_clients[key]['x'] = self.new_clients[key]['mapCoordinate']['x']
                self.old_clients[key]['y'] = self.new_clients[key]['mapCoordinate']['y']
                self.old_clients[key]['z'] = self.new_clients[key]['mapCoordinate']['z']
            else:

        self.old_clients = self.new_clients.copy()
        self.new_clients.clear()
        r = self.get_request(self.clients, None)
        try:
            if r['error'] != 200:
                return r            
        except:
            pass
        cl = {}
        for client in r:
            if client['macAddress'] in self.old_clients:
                self.old_clients[client['macAddress']]['userName'] = client['userName']
                self.old_clients[client['macAddress']]['floorName'] = client['mapInfo']['mapHierarchyString'][27:36]
                self.old_clients[client['macAddress']]['x'] = client['mapCoordinate']['x']
                self.old_clients[client['macAddress']]['y'] = client['mapCoordinate']['y']
                self.old_clients[client['macAddress']]['z'] = client['mapCoordinate']['z']
            else:
                cl['userName'] = client['userName']
                cl['floorName'] = client['mapInfo']['mapHierarchyString'][27:36]
                cl['x'] = client['mapCoordinate']['x']
                cl['y'] = client['mapCoordinate']['y']
                cl['z'] = client['mapCoordinate']['z']
                self.new_clients[client['macAddress']] = cl

    def get_all_maps(self): 
        maps_json =  self.get_request(self.all_maps, None)
        try:
            if maps_json['error'] != 200:
                return maps_json            
        except:
            pass
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
        self.get_all_maps()
        for floor_name in self.map_names:
            r = self.get_request(self.map_image + self.map_names[floor_name], 'image')
            if r.status_code == 200:
                with open(self.path_to_maps + floor_name, 'wb') as f:
                    for chunk in r.iter_content(1024):
                        f.write(chunk)

    def get_old_clients(self):
        return json.dumps(self.old_clients)

    def get_new_clients(self):
        return json.dumps(self.new_clients)

if __name__ == '__main__':
    L = Locate()
    print (L.get_number_of_clients())
    print (L.get_all_maps())
    print (L.get_map_images())
    print (L.get_clients())
    print (L.get_old_clients())
    print ("------------------------------------------------")
    print (L.get_new_clients())
    print ("================================================")
    print (L.get_clients())
    print (L.get_old_clients())
    print ("------------------------------------------------")
    print (L.get_new_clients())

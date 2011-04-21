#!/usr/bin/python
# coding: utf-8
# Copyright (C) 2011 Lucas Alvares Gomes <lucasagomes@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import tibiadevel.offset.entity
from tibiadevel.object.client import Client
from tibiadevel.utils import *

class Entity:
    """  """

    def __init__(self, address):
        self.client = Client()
        self.address = address

    @property
    def id(self):
        return self.client.read_memory(self.address + \
                                        tibiadevel.offset.entity.id, "I")[0]
   
    @property
    def type(self):
        return self.client.read_memory(self.address + \
                                      tibiadevel.offset.entity.type, "B")[0]

    @property
    def name(self):
        return strncpy(self.client.read_memory(self.address + \
                                   tibiadevel.offset.entity.name, "32s")[0])

    @property
    def x(self):
        return self.client.read_memory(self.address + \
                                         tibiadevel.offset.entity.x, "i")[0]
    
    @property
    def y(self):
        return self.client.read_memory(self.address + \
                                         tibiadevel.offset.entity.y, "i")[0]
    
    @property
    def z(self):
        return self.client.read_memory(self.address + \
                                         tibiadevel.offset.entity.z, "i")[0]

    @property
    def horizontal_offset(self):
        return self.client.read_memory(self.address + \
                         tibiadevel.offset.entity.horizontal_offset, "i")[0]

    @property
    def vertical_offset(self):
        return self.client.read_memory(self.address + \
                           tibiadevel.offset.entity.vertical_offset, "i")[0]

    @property
    def is_walking(self):
        return self.client.read_memory(self.address + \
                                tibiadevel.offset.entity.is_walking, "i")[0]
    
    @property
    def direction(self):
        return self.client.read_memory(self.address + \
                                 tibiadevel.offset.entity.direction, "i")[0]

    @property
    def is_visible(self):
        return self.client.read_memory(self.address + \
                                tibiadevel.offset.entity.is_visible, "i")[0]

    @property
    def light(self):
        return self.client.read_memory(self.address + \
                                     tibiadevel.offset.entity.light, "i")[0]
    
    @property
    def light_color(self):
        return self.client.read_memory(self.address + \
                               tibiadevel.offset.entity.light_color, "i")[0]

    @property
    def hp_bar(self):
        return self.client.read_memory(self.address + \
                                  tibiadevel.offset.entity.hitpoint, "i")[0]
    
    @property
    def black_square(self):
        return self.client.read_memory(self.address + \
                              tibiadevel.offset.entity.black_square, "i")[0]
    
    @property
    def skull_icon(self):
        return self.client.read_memory(self.address + \
                                tibiadevel.offset.entity.skull_icon, "i")[0]
   
    @property
    def party_icon(self):
        return self.client.read_memory(self.address + \
                                tibiadevel.offset.entity.party_icon, "i")[0]

    @property
    def war_icon(self):
        return self.client.read_memory(self.address + \
                                  tibiadevel.offset.entity.war_icon, "i")[0]

    @property
    def is_blocking(self):
        return self.client.read_memory(self.address + \
                               tibiadevel.offset.entity.is_blocking, "i")[0]
    
    @property
    def outfit(self):
        return self.client.read_memory(self.address + \
                                    tibiadevel.offset.entity.outfit, "i")[0]
    
    @property
    def head_color(self):
        return self.client.read_memory(self.address + \
                                tibiadevel.offset.entity.head_color, "i")[0]
    
    @property
    def body_color(self):
        return self.client.read_memory(self.address + \
                                tibiadevel.offset.entity.body_color, "i")[0]

    @property
    def legs_color(self):
        return self.client.read_memory(self.address + \
                                tibiadevel.offset.entity.legs_color, "i")[0]

    @property
    def feet_color(self):
        return self.client.read_memory(self.address + \
                                tibiadevel.offset.entity.feet_color, "i")[0]

    @property
    def addon(self):
        return self.client.read_memory(self.address + \
                                     tibiadevel.offset.entity.addon, "i")[0]

    def get_location(self):
        # TODO: Retornar um objeto
        return (self.x, self.y, self.z)

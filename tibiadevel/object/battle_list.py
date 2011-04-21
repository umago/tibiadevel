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


import tibiadevel.offset.battle_list
from tibiadevel.object.entity import Entity
from tibiadevel.utils import *

@singleton
class BattleList:
    """  """

    def get_entities(self):
        """ """
        entity_list = list()
        for addr in range(tibiadevel.offset.battle_list.start,
                          tibiadevel.offset.battle_list.end,
                          tibiadevel.offset.battle_list.entity_struct_size):
            entity = Entity(addr)
            if entity.id and entity.is_visible:
                entity_list.append(entity)

        return entity_list


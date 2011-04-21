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

from tibiadevel.utils import *

@singleton
class Client:
    """ """

    def __init__(self):
        self.pid = get_process_pid("Tibia")
        self.wm_id = get_xwindow_id("Tibia Player Linux")

    def read_memory(self, address, fmt):
        """Read memory from tibia client process
        
        @address = Memory address
        @fmt = struct format
        """

        data = read_process_memory(self.pid, address, struct.calcsize(fmt))
        try:
            return struct.unpack(fmt, data)
        except struct.error:
            return ''

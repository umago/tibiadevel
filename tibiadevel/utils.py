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

import errno
import subprocess
import struct

from tibiadevel.ptrace import Ptrace
from tibiadevel.exceptions import *

_PTRACE = Ptrace()

def singleton(cls):
    """A singleton decorator"""

    instance_container = []
    def getinstance():
        if not len(instance_container):
            instance_container.append(cls())
        return instance_container[0]
    return getinstance

def strncpy(buf, n=None):
    if n == None:
        n = len(buf)
    nullpos = buf.find("\0", 0, n)
    assert nullpos < n
    return buf[:(n if nullpos == -1 else nullpos)]

def get_process_pid(process):
    """Get the pid of the process

    @process = process name
    """

    ch = subprocess.Popen(["pidof", process], stdout=subprocess.PIPE)
    pid = ch.communicate()[0]
    if len(pid) == 0:
            raise PidNotFound
    return int(pid)

def get_xwindow_id(wm_title):
    """Get the X Window id

    @wm_title = The window title
    """
    return 0

def read_process_memory(pid, address, size):
    """Read memory region
    
    @pid = process id
    @address = memory address
    @size = how much bytes you want to read
    """

    _PTRACE.attach(pid)
    try:
        _PTRACE.wait(pid)
        with open("/proc/{0}/mem".format(pid)) as memfile:
	    memfile.seek(address)
	    return memfile.read(size)
    finally:
        try:
            _PTRACE.detach(pid)
	except OSError, e:
	    if e.errno != errno.ESRCH:
	        raise ReadingMemoryError


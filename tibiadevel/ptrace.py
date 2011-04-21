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

# Based on the anacrolix ptrace: http://code.google.com/p/anacrolix

import ctypes
import os
from ctypes.util import find_library
from signal import SIGSTOP

class Ptrace:

    def __init__(self):
        libc = ctypes.CDLL(find_library('c'), use_errno=True)
        func = ("ptrace", libc)
        prototype = ctypes.CFUNCTYPE(ctypes.c_long, ctypes.c_int, ctypes.c_int,
                                     ctypes.c_void_p, ctypes.c_void_p,
                                     use_errno=True)
        flags = (1, "request"), (1, "pid"), (1, "addr", None), (1, "data", 0)
        self._ptrace = prototype(func, flags)
        self._ptrace.errcheck = self._check_err
    
    def _check_err(self, result, func, args):
        if result != 0:
            errno = ctypes.get_errno()
            raise OSError(errno, os.strerror(errno))

    def attach(self, pid):
        self._ptrace(pid=pid, request=16)

    def detach(self, pid):
        self._ptrace(pid=pid, request=17)

    def cont(self, pid, signum=0):
        self._ptrace(pid=pid, request=7, data=signum)

    def wait(self, pid):
        while True:
            proc_pid, status = os.waitpid(pid, 0)
            if proc_pid == pid:
                if os.WIFSTOPPED(status):
                    signum = os.WSTOPSIG(status)
                    if signum == SIGSTOP:
                        break
                    else:
                        cont(pid, signum)

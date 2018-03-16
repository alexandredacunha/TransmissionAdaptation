#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  messages.py
#  
#  Copyright 2018 cunha <dacunha.alexandre@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

class messageBase(object):
    def __init__(self):
        self._msg_id = None
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, msg_id):
        self._msg_id = msg_id
        

class DataPacketMsg(messageBase):
    def __init__(self):
        self._msg_id = 0x01
        self._payload_size = 0
        self._discard = False
    
    @property
    def payload_size(self):
        return self._payload_size

    @payload_size.setter
    def payload_size(self, size):
        self._payload_size = size

    @property
    def discard(self):
        return self._discard

    @discard.setter
    def discard(self, discard):
        self._discard = discard

        
class AckNackMsg(messageBase):
    def __init__(self):
        self._msg_id = 0x02
        self._acknack = None
    
    @property
    def acknack(self):
        return self._acknack

    @acknack.setter
    def acknack(self, acknack):
        self._acknack = acknack

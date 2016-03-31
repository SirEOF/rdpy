#
# Copyright (c) 2014-2015 Sylvain Peyrefitte
#
# This file is part of rdpy.
#
# rdpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

"""
Basic virtual scancode mapping
"""

_SCANCODE_QWERTY_ = {
    0x01 : "<esc>",
    0x1c : "<enter>",
    0x0e : "<del>",
    0x0f : "<tab>",
    0x36 : "<shift>",
    0x2a : "<shift>",
    0x39 : "<space>",
    0x38 : "<alt>",
    0x3c : "f2",
    0x40 : "f6",
    0x58 : "f2",
    0x02 : "1",
    0x03 : "2",
    0x04 : "3",
    0x05 : "4",
    0x06 : "5",
    0x07 : "6",
    0x08 : "7",
    0x09 : "8",
    0x0a : "9",
    0x0b : "0", 
    0x0c : "-",
    0x28 : "'",
    0x34 : ".",
    0x10 : "q",
    0x11 : "w",
    0x12 : "e",
    0x13 : "r",
    0x14 : "t",
    0x15 : "y",
    0x16 : "u",
    0x17 : "i",
    0x18 : "o",
    0x19 : "p",
    0x1e : "a",
    0x1f : "s",
    0x20 : "d",
    0x21 : "f",
    0x22 : "g",
    0x23 : "h",
    0x24 : "j",
    0x25 : "k",
    0x26 : "l",
    0x2c : "z",
    0x2d : "x",
    0x2e : "c",
    0x2f : "v",
    0x30 : "b",
    0x31 : "n",
    0x32 : "m"
}
        
def scancodeToChar(code):
    """
    @summary: try to convert native code to char code
    @return: char
    """
    if not _SCANCODE_QWERTY_.has_key(code):
        return "<unknown scancode %x>"%code
    return _SCANCODE_QWERTY_[code];

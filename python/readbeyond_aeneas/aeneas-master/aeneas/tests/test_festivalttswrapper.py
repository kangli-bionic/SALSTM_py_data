#!/usr/bin/env python
# coding=utf-8

# aeneas is a Python/C library and a set of tools
# to automagically synchronize audio and text (aka forced alignment)
#
# Copyright (C) 2012-2013, Alberto Pettarin (www.albertopettarin.it)
# Copyright (C) 2013-2015, ReadBeyond Srl   (www.readbeyond.it)
# Copyright (C) 2015-2016, Alberto Pettarin (www.albertopettarin.it)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest

from aeneas.tests.base_ttswrapper import TestBaseTTSWrapper
from aeneas.ttswrappers.festivalttswrapper import FESTIVALTTSWrapper


class TestFESTIVALTTSWrapper(TestBaseTTSWrapper):

    TTS = u"festival"
    TTS_PATH = u"/usr/bin/text2wave"
    TTS_CLASS = FESTIVALTTSWrapper
    TTS_LANGUAGE = FESTIVALTTSWrapper.ENG
    TTS_LANGUAGE_VARIATION = FESTIVALTTSWrapper.ENG_GBR


if __name__ == "__main__":
    unittest.main()

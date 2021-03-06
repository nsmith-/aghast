#!/usr/bin/env python

# Copyright (c) 2019, IRIS-HEP
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import unittest

import numpy

from aghast import *
import aghast.connect.numpy as connect_numpy

class Test(unittest.TestCase):
    def runTest(self):
        pass

    def test_numpy1d(self):
        before = numpy.histogram(numpy.random.normal(0, 1, int(1e6)), bins=100, range=(-5, 5))
        after = connect_numpy.tonumpy(connect_numpy.fromnumpy(before))
        assert numpy.array_equal(before[0], after[0])
        assert numpy.array_equal(before[1], after[1])

    def test_numpy2d(self):
        before = numpy.histogram2d(x=numpy.random.normal(0, 1, int(1e6)), y=numpy.random.normal(0, 1, int(1e6)), bins=(10, 10), range=((-5, 5), (-5, 5)))
        after = connect_numpy.tonumpy(connect_numpy.fromnumpy(before))
        assert numpy.array_equal(before[0], after[0])
        assert numpy.array_equal(before[1], after[1])
        assert numpy.array_equal(before[2], after[2])

    def test_numpydd(self):
        before = numpy.histogramdd((numpy.random.normal(0, 1, int(1e6)), numpy.random.normal(0, 1, int(1e6)), numpy.random.normal(0, 1, int(1e6))), bins=(5, 5, 5), range=((-5, 5), (-5, 5), (-5, 5)))
        after = connect_numpy.tonumpy(connect_numpy.fromnumpy(before))
        assert numpy.array_equal(before[0], after[0])
        assert numpy.array_equal(before[1][0], after[1][0])
        assert numpy.array_equal(before[1][1], after[1][1])
        assert numpy.array_equal(before[1][2], after[1][2])

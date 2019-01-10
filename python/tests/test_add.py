#!/usr/bin/env python

# Copyright (c) 2018, DIANA-HEP
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

from stagg import *

class Test(unittest.TestCase):
    def runTest(self):
        pass

    def test_add_twodim_same_same(self):
        a = Histogram([Axis(IntegerBinning(1, 2)), Axis(IntegerBinning(10, 19))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.arange(20))))
        b = Histogram([Axis(IntegerBinning(1, 2)), Axis(IntegerBinning(10, 19))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.full(20, 100))))
        assert a.counts.counts.array.tolist() == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
        assert b.counts.counts.array.tolist() == [[100, 100, 100, 100, 100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]]
        assert (a + b).counts.counts.array.tolist() == [[100, 101, 102, 103, 104, 105, 106, 107, 108, 109], [110, 111, 112, 113, 114, 115, 116, 117, 118, 119]]
        assert a.counts.counts.array.tolist() == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
        assert b.counts.counts.array.tolist() == [[100, 100, 100, 100, 100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]]
        assert (b + a).counts.counts.array.tolist() == [[100, 101, 102, 103, 104, 105, 106, 107, 108, 109], [110, 111, 112, 113, 114, 115, 116, 117, 118, 119]]
        assert a.counts.counts.array.tolist() == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
        assert b.counts.counts.array.tolist() == [[100, 100, 100, 100, 100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]]

    def test_add_twodim_same_different(self):
        a = Histogram([Axis(IntegerBinning(1, 2)), Axis(IntegerBinning(9, 20))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.arange(2*12))))
        b = Histogram([Axis(IntegerBinning(1, 2)), Axis(IntegerBinning(10, 19))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.full(20, 100))))
        assert a.counts.counts.array.tolist() == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]]
        assert b.counts.counts.array.tolist() == [[100, 100, 100, 100, 100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]]
        assert (a + b).counts.counts.array.tolist() == [[0, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 11], [12, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 23]]
        assert a.counts.counts.array.tolist() == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]]
        assert b.counts.counts.array.tolist() == [[100, 100, 100, 100, 100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]]
        assert (b + a).counts.counts.array.tolist() == [[0, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 11], [12, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 23]]
        assert a.counts.counts.array.tolist() == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]]
        assert b.counts.counts.array.tolist() == [[100, 100, 100, 100, 100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]]

    def test_add_twodim_different_same(self):
        a = Histogram([Axis(IntegerBinning(0, 3)), Axis(IntegerBinning(10, 19))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.arange(4*10))))
        b = Histogram([Axis(IntegerBinning(1, 2)), Axis(IntegerBinning(10, 19))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.full(20, 100)))); 
        assert a.counts.counts.array.tolist() == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]]
        assert b.counts.counts.array.tolist() == [[100, 100, 100, 100, 100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]]
        assert (a + b).counts.counts.array.tolist() == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [110, 111, 112, 113, 114, 115, 116, 117, 118, 119], [120, 121, 122, 123, 124, 125, 126, 127, 128, 129], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]]

    def test_add_twodim_different_different(self):
        a = Histogram([Axis(IntegerBinning(0, 3)), Axis(IntegerBinning(9, 20))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.arange(4*12))))
        b = Histogram([Axis(IntegerBinning(1, 2)), Axis(IntegerBinning(10, 19))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.full(20, 100))))
        assert a.counts.counts.array.tolist() == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]]
        assert b.counts.counts.array.tolist() == [[100, 100, 100, 100, 100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]]
        assert (a + b).counts.counts.array.tolist() == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [12, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 23], [24, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 35], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]]
        assert a.counts.counts.array.tolist() == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]]
        assert b.counts.counts.array.tolist() == [[100, 100, 100, 100, 100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]]
        assert (b + a).counts.counts.array.tolist() == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [12, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 23], [24, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 35], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]]
        assert a.counts.counts.array.tolist() == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]]
        assert b.counts.counts.array.tolist() == [[100, 100, 100, 100, 100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]]

    def test_add_weighting(self):
        a = Histogram([Axis(IntegerBinning(10, 19))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.arange(10))))
        b = Histogram([Axis(IntegerBinning(10, 19))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.full(10, 100))))
        assert a.counts.counts.array.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert b.counts.counts.array.tolist() == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        assert (a + b).counts.counts.array.tolist() == [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
        assert a.counts.counts.array.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert b.counts.counts.array.tolist() == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        assert (b + a).counts.counts.array.tolist() == [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
        assert a.counts.counts.array.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert b.counts.counts.array.tolist() == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

        a = Histogram([Axis(IntegerBinning(10, 19))], WeightedCounts(InterpretedInlineBuffer.fromarray(numpy.arange(10))))
        b = Histogram([Axis(IntegerBinning(10, 19))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.full(10, 100))))
        assert a.counts.sumw.array.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert b.counts.counts.array.tolist() == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        ab = a + b
        assert isinstance(ab.counts, WeightedCounts)
        assert ab.counts.sumw.array.tolist() == [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
        assert ab.counts.sumw2 is None
        assert ab.counts.unweighted is None
        assert a.counts.sumw.array.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert b.counts.counts.array.tolist() == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        ab = b + a
        assert isinstance(ab.counts, WeightedCounts)
        assert ab.counts.sumw.array.tolist() == [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
        assert ab.counts.sumw2 is None
        assert ab.counts.unweighted is None
        assert a.counts.sumw.array.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert b.counts.counts.array.tolist() == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

        a = Histogram([Axis(IntegerBinning(10, 19))], WeightedCounts(InterpretedInlineBuffer.fromarray(numpy.arange(10)), InterpretedInlineBuffer.fromarray(numpy.arange(10, 20))))
        b = Histogram([Axis(IntegerBinning(10, 19))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.full(10, 100))))
        assert a.counts.sumw.array.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert a.counts.sumw2.array.tolist() == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        assert b.counts.counts.array.tolist() == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        ab = a + b
        assert isinstance(ab.counts, WeightedCounts)
        assert ab.counts.sumw.array.tolist() == [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
        assert ab.counts.sumw2 is None
        assert ab.counts.unweighted is None
        assert a.counts.sumw.array.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert a.counts.sumw2.array.tolist() == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        assert b.counts.counts.array.tolist() == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        ab = b + a
        assert isinstance(ab.counts, WeightedCounts)
        assert ab.counts.sumw.array.tolist() == [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
        assert ab.counts.sumw2 is None
        assert ab.counts.unweighted is None
        assert a.counts.sumw.array.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert a.counts.sumw2.array.tolist() == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        assert b.counts.counts.array.tolist() == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

        a = Histogram([Axis(IntegerBinning(10, 19))], WeightedCounts(InterpretedInlineBuffer.fromarray(numpy.arange(10)), InterpretedInlineBuffer.fromarray(numpy.arange(10, 20)), UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.arange(20, 30)))))
        b = Histogram([Axis(IntegerBinning(10, 19))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.full(10, 100))))
        assert a.counts.sumw.array.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert a.counts.sumw2.array.tolist() == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        assert a.counts.unweighted.counts.array.tolist() == [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        assert b.counts.counts.array.tolist() == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        ab = a + b
        assert isinstance(ab.counts, WeightedCounts)
        assert ab.counts.sumw.array.tolist() == [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
        assert ab.counts.sumw2 is None
        assert ab.counts.unweighted.counts.array.tolist() == [120, 121, 122, 123, 124, 125, 126, 127, 128, 129]
        assert a.counts.sumw.array.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert a.counts.sumw2.array.tolist() == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        assert a.counts.unweighted.counts.array.tolist() == [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        assert b.counts.counts.array.tolist() == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        ab = b + a
        assert isinstance(ab.counts, WeightedCounts)
        assert ab.counts.sumw.array.tolist() == [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
        assert ab.counts.sumw2 is None
        assert ab.counts.unweighted.counts.array.tolist() == [120, 121, 122, 123, 124, 125, 126, 127, 128, 129]
        assert a.counts.sumw.array.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert a.counts.sumw2.array.tolist() == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        assert a.counts.unweighted.counts.array.tolist() == [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        assert b.counts.counts.array.tolist() == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

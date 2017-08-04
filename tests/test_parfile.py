#! /usr/bin/env python
import sys,os
import pint.models as tm

from pinttestdata import testdir, datadir
datadir = os.path.join(testdir,'datafile')
parfile = os.path.join(datadir,'J1744-1134.basic.par')

m = tm.get_model(parfile)

print("model.param_help():")
m.param_help()
print()

print("calling model.read_parfile():")
m.read_parfile(parfile)
print()

print("print model:")
print(m)
print()

print("model.as_parfile():")
print(m.as_parfile())
print()

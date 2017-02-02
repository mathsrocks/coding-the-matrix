# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return [dct[k] for (i, k) in enumerate(keylist) if k in dct]

def list2dict(L, keylist): return {k:v for (k, v) in zip(keylist, L)}

def listrange2dict(L): return {i:v for (i, v) in enumerate(L)}
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re



# blocks_re = re.compile(r'(\(.*\))*(\([^\)]*){1}$')
blocks_re = re.compile(r'(.*)(\([^\)]*){1}$')

def replace_unclosed_blocks(s):
#    m = blocks_re.match(s)
#    if m:
#        print m.groups()

    return blocks_re.sub(r'\1', s)



# (“asdfd((asdf)(asdf”->”“asdfd((asdf)”
s = "(asdfd((asdf)(asdf"
s1 = "(+++((+++)(----"
s2 = "(+++((+++)(+++  (+++++)"
s3 = "()()("
s4 = "+++++++(---------"

print replace_unclosed_blocks(s)
print replace_unclosed_blocks(s1)
print replace_unclosed_blocks(s2)
print replace_unclosed_blocks(s3)
print replace_unclosed_blocks(s4)

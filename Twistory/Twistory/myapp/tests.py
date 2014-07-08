#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

"""
To test the program:
% coverage3 run --branch tests.py

To obtain coverage of the test:
% coverage3 report -m
"""

# -------
# imports
# -------

from unittest import main, TestCase
from models import Handle, Hashtag, Cluster

# -----------
# test
# -----------

class Test (TestCase) :
    # ----
    # Handle Model
    # ----

    def handle_test(self):
    	handle = Handle(username = "@LadyGaga", name = "Stephanie", bio = "Mother monster, \
    		popstar, popular twitter person.", tweets = "QUEEN OF THE WORLD!")
    	self.assertEquals(str(handle), "");
    
# ----
# main
# ----

main()
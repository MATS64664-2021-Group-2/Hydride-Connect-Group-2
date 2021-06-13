#!/usr/bin/env python
# coding: utf-8

import pytest
import sys, os

sys.path.append("./Workflow/packages")

import Workflow.packages.connectivity

strips_num = 25

def test_otsu():
    assert Workflow.packages.connectivity.otsu(strips_num)


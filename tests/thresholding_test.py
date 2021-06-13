#!/usr/bin/env python
# coding: utf-8

import pytest
import sys, os

sys.path.append("./Workflow/packages")

import Workflow.packages.connectivity

def test_otsu():
    assert connectivity.otsu()


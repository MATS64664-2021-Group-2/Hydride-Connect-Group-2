#!/usr/bin/env python
# coding: utf-8

import pytest
from hydride_package import connectivity

def test_otsu():
    assert connectivity.otsu()


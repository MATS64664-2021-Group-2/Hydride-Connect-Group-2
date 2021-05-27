#!/usr/bin/env python
# coding: utf-8
import pytest 
import parameters 
import numpy as np 
import cv2

def test_HCC2():
       assert parameters.HCC2(7) == 127


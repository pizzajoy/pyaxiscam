#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:26:50 2020

@author: letiziamoro
"""


import pyaxiscam
cam = pyaxiscam.AxisCam('host', 'username', 'password')
status, image = cam.get_live_image()
status,image = cam.display_live_image()

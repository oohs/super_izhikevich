#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:17:51 2021

@author: lyl
"""

import izhikevich_cells as izh


class cCell(izh.izhCell):
    def __init__(self, stimVal):
        super().__init__(stimVal)
        # Define Neuron Parameters
        self.celltype='Chattering' # Regular spiking
        self.C=50
        self.vr=-60
        self.vt=-40
        self.k=1.5
        self.a=0.03
        self.b=1
        self.c=-40
        self.d=150
        self.vpeak=25

myCell = cCell(stimVal = 4000)
myCell.simulate()
izh.plotMyData(myCell)
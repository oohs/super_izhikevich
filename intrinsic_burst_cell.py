#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:16:33 2021

@author: lyl
"""

import izhikevich_cells as izh


class ibCell(izh.izhCell):
    def __init__(self, stimVal):
        super().__init__(stimVal)
        # Define Neuron Parameters
        self.celltype='Intrinsic Burst' # Regular spiking
        self.C=150
        self.vr=-75
        self.vt=-45
        self.k=1.2
        self.a=0.01
        self.b=5
        self.c=-56
        self.d=130
        self.vpeak=50

myCell = ibCell(stimVal = 4000)
myCell.simulate()
izh.plotMyData(myCell)
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:38:48 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time,random

pos = mc.player.getPos()
while True:
    x = pos.x+random.uniform(-20,20)
    z = pos.z+random.uniform(-20,20)
    y = pos.y+30
    mc.spawnEntity(x,y,z,13)
    time.sleep(0.5)
"""
File name : TilesAsset.py
Function : Collect all the tiles assets and make them become global variable
"""
import pygame, sys, os
from pygame.locals import *
from os import listdir
from os.path import isfile, join

CurrentWorkingDirectory = os.getcwd()
TilesDirectory = CurrentWorkingDirectory + '/asset/Tiles'
AssetFiles = [ f for f in listdir(TilesDirectory) if isfile(join(TilesDirectory,f)) ]

#dirtImage = pygame.image.load('asset/Tiles/dirt.png')
AssetFilesDictionary = {}
for i, elem in enumerate(AssetFiles):
	AssetFilesDictionary[AssetFiles[i]]=TilesDirectory + AssetFiles[i]


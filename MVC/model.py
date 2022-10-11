import os
import re

from PyQt6.QtCore import QThread

from .image_operations import ImageWorker


class Model:
    def __init__(self):
        self.targetPath = ''
        self.files = []
        self.rename = False
        self.prefix = 'IMG_'
        self.nextIndex = None
        self.rotate = False
        self.rotateValues = (90, 180, 270)
        self.rotateIndex = 0
        self.resolution = False
        self.resolutions = (1280, 1920, 2560, 3840)
        self.resolutionIndex = 0

    def checkExistingPrefixes(self) -> int:
        samePrefixFiles = []
        for file in os.listdir(self.targetPath):
            check = re.fullmatch(fr"{self.prefix}\d{{5}}\.(jpg|JPG)", file)
            if check:
                samePrefixFiles.append(file)

        samePrefixFiles.sort()
        try:
            lastIndex = samePrefixFiles[-1]
        except IndexError:
            return 0
        else:
            return int(lastIndex.split(self.prefix)[-1].split('.')[0])

    def runOperations(self):
        if not isinstance(self.nextIndex, int) and self.rename:
            self.nextIndex = self.checkExistingPrefixes()

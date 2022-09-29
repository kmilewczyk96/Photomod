import os
import re

from PIL import Image, ImageFile
from .utils.shorten_path import getShortenedPath


class Model:
    def __init__(self):
        self.targetPath = ''
        self.files = []
        self.rename = False
        self.prefix = 'IMG_'
        self.firstIndex = None
        self.rotate = False
        self.rotateValues = [90, 180, 270]
        self.rotateIndex = 0
        self.resolution = False
        self.resolutions = [1280, 1920, 2560, 3840]
        self.resolutionIndex = 0

    def checkExistingPrefixes(self):
        samePrefixFiles = []
        for file in os.listdir(self.targetPath):
            check = re.fullmatch(fr"{self.prefix}\d{{5}}\.(jpg|JPG)", file)
            if check:
                samePrefixFiles.append(file)

        samePrefixFiles.sort()
        try:
            lastIndex = samePrefixFiles[-1]
        except IndexError:
            print('Brak plików z tym prefixem')
            return 0
        else:
            print(f'Ostatni plik z tym prefixem: {lastIndex}')
            return lastIndex.split(self.prefix)[-1].split('.')[0]

    def runOperations(self):
        print('Rozpoczynam pracę...')
        if not isinstance(self.firstIndex, int) and self.rename:
            self.firstIndex = self.checkExistingPrefixes()

        ImageFile.LOAD_TRUNCATED_IMAGES = True
        for img in self.files:
            with Image.open(img) as original:
                original.load()

            if self.resolution:
                print('Zmieniam rozdzielczość...')
                max_ = self.resolutions[self.resolutionIndex]
                originalSize = max(original.size)
                if originalSize > max_:
                    original.thumbnail(size=(max_, max_), resample=Image.LANCZOS)

            if self.rotate:
                print('Obracam...')
                original = original.rotate(self.rotateValues[self.rotateIndex], expand=True)

            if self.rename:
                self.firstIndex += 1
                newName = self.prefix + str(self.firstIndex).zfill(5) + '.jpg'

            else:
                newName = os.path.basename(img)

            print('Zapisuję...')
            original.save(os.path.join(self.targetPath, newName), quality=95, subsampling=0)
            original.close()

        print('Zakończono =).')

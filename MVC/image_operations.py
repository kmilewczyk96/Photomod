import os

from PIL import Image, ImageFile
from PyQt6.QtCore import pyqtSignal, QObject


class ImageWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    currentOperation = pyqtSignal(str)

    def __init__(self, model):
        super().__init__()
        self.TARGET_PATH = model.targetPath
        self.FILES = model.files
        self.RENAME = model.rename
        self.PREFIX = model.prefix
        self.nextIndex = model.nextIndex
        self.ROTATE = model.rotate
        self.ROTATE_VALUES = model.rotateValues
        self.ROTATE_INDEX = model.rotateIndex
        self.RESOLUTION = model.resolution
        self.RESOLUTIONS = model.resolutions
        self.RESOLUTION_INDEX = model.resolutionIndex

    def run(self):
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        for finished, img in enumerate(self.FILES):
            with Image.open(img) as original:
                original.load()

            if self.RESOLUTION:
                self.currentOperation.emit('Zmieniam rozdzielczość...')
                max_ = self.RESOLUTIONS[self.RESOLUTION_INDEX]
                originalSize = max(original.size)
                if originalSize > max_:
                    original.thumbnail(size=(max_, max_), resample=Image.LANCZOS)

            if self.ROTATE:
                self.currentOperation.emit('Obracam obraz...')
                original = original.rotate(self.ROTATE_VALUES[self.ROTATE_INDEX], expand=True)

            if self.RENAME:
                self.nextIndex += 1
                newName = self.PREFIX + str(self.nextIndex).zfill(5) + '.jpg'

            else:
                newName = os.path.basename(img)

            self.currentOperation.emit('Zapisuję...')
            original.save(os.path.join(self.TARGET_PATH, newName), quality=95, subsampling=0)
            original.close()
            self.progress.emit(finished + 1)

        self.currentOperation.emit('Zakończono')
        self.finished.emit()

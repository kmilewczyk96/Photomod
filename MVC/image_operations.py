import os
import shutil

from PIL import Image, ImageFile
from PyQt6.QtCore import pyqtSignal, QObject


class ImageWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    currentOperation = pyqtSignal(str)
    filenamesError = pyqtSignal(list)

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

        self.pillowRequired = True if self.ROTATE or self.RESOLUTION else False
        self.errorsRaisedFlag = False

    def run(self):
        if not self.RENAME:
            collisions = self._checkForCollisions()
            if collisions:
                self.filenamesError.emit(collisions)
                self.finished.emit()
                return None

        if not self.pillowRequired:
            self._shutilOperations()

        else:
            ImageFile.LOAD_TRUNCATED_IMAGES = True
            for index, img in enumerate(self.FILES):
                if self.thread().isInterruptionRequested():
                    break
                with Image.open(img) as original:
                    original.load()

                if self.RESOLUTION:
                    max_ = self.RESOLUTIONS[self.RESOLUTION_INDEX]
                    originalSize = max(original.size)
                    if originalSize > max_:
                        original.thumbnail(size=(max_, max_), resample=Image.LANCZOS)

                if self.ROTATE:
                    original = original.rotate(self.ROTATE_VALUES[self.ROTATE_INDEX], expand=True)

                if self.RENAME:
                    newName = self._nextName()

                else:
                    newName = os.path.basename(img)

                original.save(os.path.join(self.TARGET_PATH, newName), quality=95, subsampling=0)
                original.close()
                self.progress.emit(index + 1)

        self.finished.emit()

    def _shutilOperations(self):
        """Executes built-in copy and rename if necessary."""
        for index, img in enumerate(self.FILES):
            newName = self._nextName() if self.RENAME else os.path.basename(img)
            output = os.path.join(self.TARGET_PATH, newName)
            shutil.copy(src=img, dst=output)
            self.progress.emit(index + 1)

    def _checkForCollisions(self) -> list:
        """
        Checks filename collisions when User won't pick RENAME option.
        Returns list of collisions if there are any.
        """
        collisions = []
        existingImages = os.listdir(self.TARGET_PATH)
        for img in self.FILES:
            img = os.path.basename(img)
            if img in existingImages:
                collisions.append(img)

        return collisions

    def _nextName(self):
        self.nextIndex += 1
        return self.PREFIX + str(self.nextIndex).zfill(5) + '.jpg'

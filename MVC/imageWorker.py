import os
import shutil

from PIL import Image, ImageFile
from PyQt6.QtCore import pyqtSignal, QObject


class ImageWorker(QObject):
    """Does all operations, sends signals to main thread with information about progress and potential errors."""
    finished = pyqtSignal(bool)
    progress = pyqtSignal(int)
    currentOperation = pyqtSignal(str)
    filenamesError = pyqtSignal(list)
    indexesError = pyqtSignal()

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

    def run(self) -> None:
        if self.RENAME:
            # Check if there are enough free indexes for operation:
            sufficientIndexes = self._checkForQuantity()
            if not sufficientIndexes:
                self.indexesError.emit()
                self.finished.emit(False)
                return

        else:
            # Check if there are no collisions with existing files in target dir:
            collisions = self._checkForCollisions()
            if collisions:
                self.filenamesError.emit(collisions)
                self.finished.emit(False)
                return

        # Prevent image from loading if no Pillow operations required:
        if not self.pillowRequired:
            self.finished.emit(self._shutilOperations())
            return

        # Execute Pillow operations:
        else:
            self.finished.emit(self._pillowOperations())
            return

    def _shutilOperations(self) -> bool:
        """Executes built-in copy and rename if necessary."""
        for index, img in enumerate(self.FILES):
            if self.thread().isInterruptionRequested():
                return False
            newName = self._nextName() if self.RENAME else os.path.basename(img)
            output = os.path.join(self.TARGET_PATH, newName)
            shutil.copy(src=img, dst=output)
            self.progress.emit(index + 1)

        return True

    def _pillowOperations(self) -> bool:
        """Executes Pillow operations and saves modified copy to designated folder."""
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        for index, img in enumerate(self.FILES):
            if self.thread().isInterruptionRequested():
                return False
            with Image.open(img) as original:
                original.load()

            exif = original.getexif()

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

            original.save(os.path.join(self.TARGET_PATH, newName), quality=95, subsampling=0, exif=exif)
            original.close()
            self.progress.emit(index + 1)

        return True

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

    def _checkForQuantity(self) -> bool:
        """
        Checks if there are enough free indexes to complete the task.
        """
        if 100000 - len(self.FILES) - self.nextIndex <= 0:
            return False

        return True

    def _nextName(self):
        self.nextIndex += 1
        return self.PREFIX + str(self.nextIndex).zfill(5) + '.jpg'

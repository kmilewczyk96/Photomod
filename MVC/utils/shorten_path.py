import sys


def getShortenedPath(path: str, limit: int) -> str:
    isWindows = sys.platform == 'win32'

    if not isWindows:
        path = '/'.join(path.split('/')[3::])
        if len(path) < limit:
            return path

    pathItems = path.split('/')
    first = pathItems.pop(0)
    pathLen = len(first) + 1

    shortenedPath = []
    while True:
        last = pathItems.pop()
        pathLen += len(last) + 1
        if pathLen >= limit:
            break
        shortenedPath.append(last)

    shortenedPath.append('...')
    shortenedPath.append(first)

    return '/'.join(shortenedPath[::-1])

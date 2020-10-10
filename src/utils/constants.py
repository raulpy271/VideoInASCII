tempDir = '.tmp/'
defaultPath = 'ballet.mp4'
videoResizedPath = tempDir + "videoResized.raw"
videoResizedFrameRate = 10
showAllErrorsFlag = '16'
screenBorder = 2
ffmpegGlobalArguments = ['-y', '-loglevel', showAllErrorsFlag]
ascii_chars = ('X', '#', '&', '^', '.', ' ')
keyToInterruptTheExecutation = ord('\n')
messageInTheEndOfScreen = 'Press ENTER to exit'


class VideoPath():
    def __init__(self, videoPath):
        self.videoPath = videoPath


    def getVideoPath(self):
        return self.videoPath


    def setVideoPath(self, videoPath):
        self.videoPath = videoPath


videoPath = VideoPath(defaultPath)


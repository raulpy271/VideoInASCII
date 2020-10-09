tempDir = '.tmp/'
defaultPath = 'ballet.mp4'
videoResizedPath = tempDir + "videoResized.raw"
videoResizedFrameRate = 10
showAllErrorsFlag = '16'
ffmpegGlobalArguments = ['-y', '-loglevel', showAllErrorsFlag]
ascii_chars = ('X', '#', '&', '^', '.', ' ')


class VideoPath():
    def __init__(self, videoPath):
        self.videoPath = videoPath


    def getVideoPath(self):
        return self.videoPath


    def setVideoPath(self, videoPath):
        self.videoPath = videoPath


videoPath = VideoPath(defaultPath)


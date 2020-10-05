tempDir = '.tmp/'
defaultPath = 'ballet.mp4'
videoResizedPath = tempDir + "videoResized.mp4"
videoResizedFrameRate = 5
ascii_chars = ('.', '^', '&', 'X', '#')
ffmpegGlobalArguments = ['-y', '-loglevel', '16']


class VideoPath():
    def __init__(self, videoPath):
        self.videoPath = videoPath


    def getVideoPath(self):
        return self.videoPath


    def setVideoPath(self, videoPath):
        self.videoPath = videoPath


videoPath = VideoPath(defaultPath)


# VideoInASCII

this program show a video in terminal with ascii-art style. Are used the ffmpeg library to resize the video automatically in the size of your terminal and numpy arrays to load pixels of the video.

## Example

![AsciiArt Example](/ballet.gif)

## How to setup

Fist of all, see the dependencies in the requirements file or type `pip install -r requirements.txt` to install the dependencies automatically.

After install all requiriments, put the video directory in the `src/utils/constants.py` file and type:

```
$ python main.py 
```

Or pass your path as a command line argument:

```
$ python main.py <path_of_your_video>
```

In the constants file you can change some settings, like video path, frame rate and chars used in ascii art.

To see more info view the help message:

```
$ python main.py --help
```

## TODO

 - Add support to specify the duration and period of the video.

 - Add colors in the ascii chars


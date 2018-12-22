from __future__ import print_function
import pychromecast

if __name__ == "__main__":
    chromecasts = pychromecast.get_chromecasts()
    print(chromecasts)
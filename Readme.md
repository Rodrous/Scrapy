# Scrapy

## Introduction

Scrapy is a threading based Wallpaper scraper, it goes to `[wallgaven.cc](http://wallgaven.cc)` to grab the images.

This is a three step process:

1. Going to the website
2. Finding the image source
3. Going to the source and downloading the image.

### Why threading?

Threading provide a way to improve application performance through parallelism.

As this piece of code is highly based on I/O functions threading is an ideal way to improve the performance.

### Usage

There are 2 basic ways to run the code:

1. No parameters ("It will grab images from First page of wallgaven")

    `python.exe Scrapy.py`

    ![Scrapy%207da08db858a840f6b4a86a631c16e3df/Without_Parameters.gif](Scrapy%207da08db858a840f6b4a86a631c16e3df/Without_Parameters.gif)

2. Parameters ("It will grab the page with respect to the parameter")

    `python.exe[Scrapy.py](http://scrapy.py) "pagenumber"`  

    ![Scrapy%207da08db858a840f6b4a86a631c16e3df/WithParameters.gif](Scrapy%207da08db858a840f6b4a86a631c16e3df/WithParameters.gif)

    If on Linux replace `python.exe` with `python`

In the end it will Display the number of images downloaded and the time taken to go through the whole process.

Thanks. :)

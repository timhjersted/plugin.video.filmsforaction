#!/usr/bin/env python
'''
This module contains unit tests and integration tests.
'''

import os
import sys
import unittest
# update path so we can import the lib files.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

import resources.lib.ffa_api as api

class ITTests(unittest.TestCase):

    def test_categories(self):
        category_list = api.get_categories()
        self.assertTrue(category_list is not None and len(category_list) > 20)

    def test_list_all_videos(self):
        url='http://www.filmsforaction.org/films/'
        video_items = api.get_videolist(url)
        self.assertTrue(len(video_items['video_list']) > 50)
        self.assertTrue(len(video_items['video_list'][0]['url']) > 30)
        self.assertTrue(len(video_items['video_list'][0]['thumbnail']) > 30)
        self.assertTrue(len(video_items['video_list'][0]['title']) > 1)

    def test_list_category(self):
        url='http://www.filmsforaction.org/watch_activism_videos/?p=2'
        video_items = api.get_videolist(url)
        self.assertTrue(len(video_items['video_list']) == 52)

    def test_vimeo_scraper(self):
        url='http://www.filmsforaction.org/watch/grasp-the-nettle-2013/'
        self.assertTrue(len(api.get_playable_url(url)) > 10)

    def test_archive_scraper(self):
        url='http://www.filmsforaction.org/watch/chasing-madoff-2010/'
        self.assertTrue(len(api.get_playable_url(url)) > 10)

    def test_kickstarter_scraper(self):
        url='http://www.filmsforaction.org/watch/inhabit-a-permaculture-perspective/'
        self.assertTrue(len(api.get_playable_url(url)) > 10)

    def test_dailymotion_scraper(self):
        url='http://www.filmsforaction.org/watch/plastic-paradise-the-great-pacific-garbage-patch-2013/'
        self.assertTrue(len(api.get_playable_url(url)) > 10)

    def test_tagtele_scraper(self):
        url='http://www.filmsforaction.org/watch/shop-til-you-drop-the-crisis-of-consumerism-2010/'
        self.assertTrue(len(api.get_playable_url(url)) > 10)


if __name__ == '__main__':
        unittest.main()

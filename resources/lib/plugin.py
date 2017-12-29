# -*- coding: utf-8 -*-

import routing
import logging
import xbmcaddon
import xbmc
import xbmcgui
import xbmcvfs
from resources.lib import kodiutils
from resources.lib import kodilogging
from xbmcgui import ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory, setResolvedUrl, setSetting,getSetting
import os


ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))
kodilogging.config()
plugin = routing.Plugin()


@plugin.route('/')
def index():
    addDirectoryItem(plugin.handle, plugin.url_for(prompt_and_play), ListItem("Play stream"), True)
    endOfDirectory(plugin.handle)


def make_item(stream_location, play=False):
    item = xbmcgui.ListItem(label=stream_location, path=stream_location)
    item.setInfo(type='audio', infoLabels={"Title": stream_location})

    if play:
        player = xbmc.Player()
        player.play(stream_location, item)
    return item

@plugin.route('/prompt_and_play')
@plugin.route('/')
def index()
    stream_location = get_input(heading=get_string("Stream URL"))

    if stream_location:
        item = make_item(stream_location, play=True)

        addDirectoryItem(plugin.handle, stream_location, item, isFolder=False)
        ddDirectoryItem(plugin.handle, plugin.url_for(), ListItem(get_string("Play other"), False)
        endOfDirectory(plugin.handle)

    return False

def get_input(heading=''):
    keyboard = xbmc.Keyboard(default='', heading=heading, hidden=False)
    keyboard.doModal(30*1000)
    return keyboard.getText() if keyboard.isConfirmed() else None

def run():
    plugin.run()

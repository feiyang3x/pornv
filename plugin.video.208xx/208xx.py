# -*-coding:utf-8 -*-
# 208xx.py
# 208xx video

import xbmcplugin, xbmcgui

url='http://mp4.123456mp4.com/new/om/2016-07/0709/%E5%A6%88%E5%A6%88%E4%BB%AC%E6%80%A7%E7%88%B1%E6%8C%87%E5%AF%BC.mp4'
handle=int(sys.argv[1])
listitem=xbmcgui.ListItem('妈妈们性爱指导')
xbmcplugin.addDirectoryItem(handle, url, listitem)
url='http://xia.auau99.com:888/%E4%BA%9A%E6%B4%B2/201607/09/[%E7%84%A1%E7%A2%BC]%E9%95%B7%E6%99%82%E9%96%93%E7%9A%84%E6%B2%89%E9%BB%98/[%E7%84%A1%E7%A2%BC]%E9%95%B7%E6%99%82%E9%96%93%E7%9A%84%E6%B2%89%E9%BB%98.rmvb'
handle=int(sys.argv[1])
listitem=xbmcgui.ListItem('长时间沉默')
xbmcplugin.addDirectoryItem(handle, url, listitem)
xbmcplugin.endOfDirectory(handle)

#######################################################################
#                                                                     #  
#  Author: Eugewx                                                     #
#  Desc: Have fun during working on Windows with Microsoft Teams      # 
#  Versions: 2.0                                                      #  
#                                                                     # 
#######################################################################

import time
import ctypes

def toggle_scroll_lock():
    dll = ctypes.WinDLL('User32.dll')
    VK_SCROLL = 0x91
    if not dll.GetKeyState(VK_SCROLL):
        dll.keybd_event(VK_SCROLL, 0X3a, 0X1, 0)
        dll.keybd_event(VK_SCROLL, 0X3a, 0X3, 0)
    else:
        dll.keybd_event(VK_SCROLL, 0X3a, 0X1, 1)
        dll.keybd_event(VK_SCROLL, 0X3a, 0X3, 1)

print('Running PyScrollToggler... CTRL+C twice to stop.')
while(True):
    toggle_scroll_lock()
    time.sleep(200)
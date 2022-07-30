from traceback import StackSummary
from django.shortcuts import render
from django.http import HttpResponse
import pyautogui
import time


# Create your views here.
def stay_on_page():
    print(f"\nCommand recieved at {time.ctime()}\n")
    return HttpResponse("""<html><script>window.location.replace('/Remote');</script></html>""")

def remote(request):
    return render(request, 'remotePage.html')

def play_pause(request):
    pyautogui.press('playpause')
    return stay_on_page()

def next_track(request):
    pyautogui.press('nexttrack')
    return stay_on_page()

def prev_track(request):
    pyautogui.press('prevtrack')
    return stay_on_page()

def vol_up(request):
    pyautogui.press('volumeup')
    return stay_on_page()

def vol_down(request):
    pyautogui.press('volumedown')
    return stay_on_page()

def mute(request):
    pyautogui.press('volumemute')
    return stay_on_page()

def toggle_fullscreen(request):
    pyautogui.press('f')
    return stay_on_page()

def toggle_caption(request):
    pyautogui.press('c')
    return stay_on_page()

def space(request):
    pyautogui.press('space')
    return stay_on_page()

def up(request):
    pyautogui.press('up')
    return stay_on_page()

def down(request):
    pyautogui.press('down')
    return stay_on_page()

def left(request):
    pyautogui.press('left')
    return stay_on_page()

def right(request):
    pyautogui.press('right')
    return stay_on_page()
    
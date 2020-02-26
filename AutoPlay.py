import pyautogui
from airtest.core.api import *
import uiautomation as auto
import subprocess
from MultiPlayNoxAuto import multiPlay,Nox

while 1:
    # multiPlay()
    # time.sleep(2)
    # Nox()
    # time.sleep(2)
    os.system('adb devices')
    connect_device('Android://127.0.0.1:5037/127.0.0.1:62001')
    time.sleep(2)
    tiaoguoyd = pyautogui.locateOnScreen(image='tiaoguoyd.png')
    print(tiaoguoyd)
    xt, yt = pyautogui.center(tiaoguoyd)
    print('tiaoguoyd()', xt, yt)
    pyautogui.click(x=xt, y=yt, clicks=1, button='left')
    time.sleep(5)

    os.system('adb install D:\\Downloads\\com.gamerry.gamerry-v2.0.0.apk')
    i=0
    while i <5 :
        i += 1
    # for i in range(1,8):
        try:
            connect_device('Android://127.0.0.1:5037/127.0.0.1:62001')
            os.system('adb shell am start -W -n com.gamerry.gamerry/.UnityPlayerActivity')

            time.sleep(75)
            #判定目标截图在系统上的位置
            closeA=pyautogui.locateOnScreen(image='xx.png')
            #输出坐标
            print(closeA)
            #利用center()函数获取目标图像在系统中的中心坐标位置
            x,y=pyautogui.center(closeA)
            print('closeA()',x,y)
            #对识别出的目标图像进行点击
            #参数x,y代表坐标位置，clicks代表点击次数,button可以设置为左键或者右键
            pyautogui.click(x=x,y=y,clicks=1,button='left')

            time.sleep(2)
            xrjiangli=pyautogui.locateOnScreen(image='xrjiangli.png')
            print(xrjiangli)
            if xrjiangli != None:
                xj,yj=pyautogui.center(xrjiangli)
                print('xrjiangli()',xj,yj)
                pyautogui.click(x=xj,y=yj,clicks=1,button='left')
                time.sleep(5)
                if xrjiangli != None:
                    os.system('adb shell am force-stop com.gamerry.gamerry')
                    continue
            else:
                pass

            time.sleep(8)
            lingq=pyautogui.locateOnScreen(image='firstd.png')
            print(lingq)
            if lingq != None:
                xl,yl=pyautogui.center(lingq)
                print('firstd()',xl,yl)
                pyautogui.click(x=xl,y=yl,clicks=1,button='left')
            else:
                pass

            time.sleep(3)
            gongxihd=pyautogui.locateOnScreen(image='gongxihd.png')
            print(gongxihd)
            if  gongxihd != None:
                xg,yg=pyautogui.center(gongxihd)
                print('gongxihd()',xg,yg)
                pyautogui.click(x=xg,y=yg,clicks=1,button='left')
            else:
                pass

            time.sleep(2)
            huoduoxx=pyautogui.locateOnScreen(image='huoduoxx.png')
            print(huoduoxx)
            if huoduoxx != None:
                xh,yh=pyautogui.center(huoduoxx)
                print('huoduoxx()',xh,yh)
                pyautogui.click(x=xh,y=yh,clicks=1,button='left')
            else:
                pass

            time.sleep(2)
            bd = 0
            while bd < 5:
                bangd=pyautogui.locateOnScreen(image='bangdsmall.png')
                bangdbig = pyautogui.locateOnScreen(image='bangdbig.png')
                if bangd != None:
                    print(bangd)
                    x1, y1 = pyautogui.center(bangd)
                    print('bangd()', x1, y1)
                    pyautogui.click(x=x1, y=y1, clicks=1, button='left')
                    break
                elif bangdbig != None:
                    print(bangdbig)
                    xb, yb = pyautogui.center(bangdbig)
                    print('bangdbig()', xb, yb)
                    pyautogui.click(x=xb, y=yb, clicks=1, button='left')
                    break
                else:
                    continue

            time.sleep(2)
            while 1:
                quxiaobd=pyautogui.locateOnScreen(image='quxiaobd.png')
                if quxiaobd != None:
                    print(quxiaobd)
                    xa, ya = pyautogui.center(quxiaobd)
                    print('quxiaobd()', xa, ya)
                    pyautogui.click(x=xa, y=ya, clicks=1, button='left')
                    break
                else:
                    continue

            time.sleep(3)
            play=pyautogui.locateOnScreen(image='paodek.png')
            print(play)
            x2,y2=pyautogui.center(play)
            print('play()',x2,y2)
            pyautogui.click(x=x2,y=y2,clicks=1,button='left')
            time.sleep(5)
            # if play != None:
            #     os.system('adb shell am force-stop com.gamerry.gamerry')
            #     continue
            # else:
            #     pass

            time.sleep(3)
            var =0
            #跑得快游戏玩3局
            while var < 3:
                var += 1
                while 1:
                    time.sleep(2)
                    playEnter = pyautogui.locateOnScreen(image='kuaisuyx.png')
                    print(playEnter)
                    if playEnter != None:
                        x3,y3=pyautogui.center(playEnter)
                        print('playEnter()',x3,y3)
                        pyautogui.click(x=x3,y=y3,clicks=1,button='left')
                        time.sleep(3)
                        jinbibz = pyautogui.locateOnScreen(image='jinbibzxx.png')
                        if jinbibz != None:
                            # os.system('adb shell am force-stop com.gamerry.gamerry')
                            print(jinbibz)
                            xjb,yjb = pyautogui.center(jinbibz)
                            print('jinbibz()',xjb,yjb)
                            pyautogui.click(x=xjb, y=yjb, clicks=1, button='left')
                            time.sleep(2)
                            break
                        else:
                            pass
                        #进入游戏，判断游戏是否可开始
                        time.sleep(5)
                        playkong = pyautogui.locateOnScreen(image='kong.png')
                        playkongs = pyautogui.locateOnScreen(image='kongs.png')
                        playkongx = pyautogui.locateOnScreen(image='kongx.png')
                        if playkong != None or playkongs != None or playkongx != None:
                            time.sleep(2)
                            back = pyautogui.locateOnScreen(image='fanh.png')
                            print(back)
                            x4,y4 = pyautogui.center(back)
                            print('back()',x4,y4)
                            pyautogui.click(x=x4, y=y4, clicks=1, button='left')
                            time.sleep(2)
                            continue
                        else:
                            time.sleep(10)
                            tg=pyautogui.locateOnScreen(image='tuog.png')
                            print(tg)
                            x5,y5=pyautogui.center(tg)
                            print('tg()',x5,y5)
                            pyautogui.click(x=x5,y=y5,clicks=1,button='left')

                            time.sleep(120)
                            goo=pyautogui.locateOnScreen(image='likaiqd.png')
                            print(goo)
                            x6,y6=pyautogui.center(goo)
                            print('goo()',x6,y6)
                            pyautogui.click(x=x6,y=y6,clicks=1,button='left')
                            if var == 3:
                                os.system('adb shell am force-stop com.gamerry.gamerry')
                            break
        except Exception as e:
            print(e)
            sleep(5)
            os.system('adb shell am force-stop com.gamerry.gamerry')
            # continue


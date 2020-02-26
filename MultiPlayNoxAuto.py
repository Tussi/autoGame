#-*- coding: utf-8 -*-
import subprocess
import uiautomation as auto
import time
import os
import pyautogui

def multiPlay():
    while 1:
        print(auto.GetRootControl())
        subprocess.Popen(r'D:\Program Files\Nox\bin\MultiPlayerManager.exe')
        time.sleep(2)
        ysWindow = auto.PaneControl(searchDepth=1, ClassName='Qt5QWindow')
        if not ysWindow.Exists(3, 1):
            print('Can not find Qt5QWindow')
            exit(0)
        # print(ysWindow)
        ysWindow.SetTopmost(True)
        childC = ysWindow.GetChildren()
        print(childC)

        allselect = ysWindow.CheckBoxControl(searchDepth=3, Name=r'全选')
        allselect.Click()
        time.sleep(1)
        customC = childC[6]
        # print(customC)
        ComboB = customC.GetChildren()
        ComboBC = ComboB[1]#.GetChildren()
        # print(ComboBC)
        ComboBC.Click()
        time.sleep(2)
        ListC = ComboBC.ListControl()
        time.sleep(2)
        ListItems = ListC.GetChildren()
        print(ListItems)
        listitem0 = ""
        listitem1 = ""
        listitem2 = ""
        listitem3 = ""
        if len(ListItems) == 5:
            listitem0 = ListItems[0]
            listitem1 = ListItems[1]
            listitem2 = ListItems[2]
            listitem3 = ListItems[3]

            break
        else:
            allselect.Click()
            continue
    # listitem0.Click()

    time.sleep(3)
    #关闭模拟器
    # ComboBC.Click()
    # time.sleep(1)
    listitem1.Click()
    time.sleep(4)
    SureClose = ysWindow.ButtonControl(searchDepth=4, Name=r"确认 Enter")
    SureClose.Click()

    time.sleep(3)

    #删除模拟器
    ComboBC.Click()
    time.sleep(1)
    listitem2.Click()
    time.sleep(3)
    SureDelete = ysWindow.ButtonControl(searchDepth=4,Name=r"确认 Enter")
    SureDelete.Click()

    time.sleep(3)
    #添加模拟器
    addandro = ysWindow.ButtonControl(searchDepth=4, Name=r'添加模拟器')
    addandro.Click()

    addan5 = ysWindow.ListItemControl(searchDepth=6, Name=r'Android7.1.2')
    addan5.Click()

    time.sleep(1)

    allselect.Click()
    time.sleep(1)
    allselect.Click()
    time.sleep(3)
    #启动模拟器
    ComboBC.Click()
    time.sleep(2)
    listitem0.Click()

    time.sleep(2)
    Btc = childC[5]
    print(Btc)
    closeB = Btc.GetChildren()
    clb = closeB[6]
    print(clb)
    clb.Click()


def Nox():
    subprocess.Popen(r'D:\Program Files\Nox\bin\Nox.exe')
    NoxWindow = auto.WindowControl(searchDepth=1, ClassName='Qt5QWindowIcon')
    if not NoxWindow.Exists(3, 1):
        print('Can not find NoxWindow')
        exit(0)
    print(NoxWindow)
    NoxWindow.SetTopmost(True)
    childC = NoxWindow.GetChildren()
    customCt = childC[1]
    print(customCt)
    ComboBt = customCt.GetChildren()
    ComboBCt = ComboBt[7]  # .GetChildren()
    print(ComboBCt)
    time.sleep(20)
    ComboBCt.Click()

    # childC = NoxWindow.GetChildren()[1]
    # print(childC)
    # closeC = childC.GetChildren()[8]
    # print(closeC)
    # closeC.Click()

if __name__=="__main__":
    yundaili()
    time.sleep(20)
    multiPlay()
    time.sleep(2)
    Nox()
    time.sleep(2)

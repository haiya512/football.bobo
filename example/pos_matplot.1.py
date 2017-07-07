# coding: utf-8
import random
import copy

birds = int(raw_input('Enter count of bird: '))
xcount = int(raw_input('Enter count of x: '))
pos = []
speed = []
bestpos = []
birdsbestpos = []
w = 0.8
c1 = 2
c2 = 2
r1 = 0.6
r2 = 0.3
for i in range(birds):
    pos.append([])
    speed.append([])
    bestpos.append([])


def GenerateRandVec(list):
    for i in range(xcount):
    list.append(random.randrange(1, 100))


def CalDis(list):
    dis = 0.0
    for i in list:
        dis += i ** 2
    return dis

for i in range(birds):  # initial all birds' pos,speed
    GenerateRandVec(pos[i])
    GenerateRandVec(speed[i])
    bestpos[i] = copy.deepcopy(pos[i])


def FindBirdsMostPos():
    best = CalDis(bestpos[0])
    index = 0
    for i in range(birds):
        temp = CalDis(bestpos[i])
        if temp < best:
            best = temp
        index = i
    return bestpos[index]

birdsbestpos = FindBirdsMostPos()  # initial birdsbestpos


def NumMulVec(num, list):  # result is in list
    for i in range(len(list)):
        list[i] *= num
    return list


def VecSubVec(list1, list2):  # result is in list1
    for i in range(len(list1)):
        list1[i] -= list2[i]
    return list1


def VecAddVec(list1, list2):  # result is in list1


    for i in range(len(list1)):
        list1[i] += list2[i]
    return list1


def UpdateSpeed():
    # global speed
    for i in range(birds):
        temp1 = NumMulVec(w, speed[i][:])
        temp2 = VecSubVec(bestpos[i][:], pos[i])
        temp2 = NumMulVec(c1 * r1, temp2[:])
        temp1 = VecAddVec(temp1[:], temp2)
        temp2 = VecSubVec(birdsbestpos[:], pos[i])
        temp2 = NumMulVec(c2 * r2, temp2[:])
        speed[i] = VecAddVec(temp1, temp2)


def UpdatePos():
    global bestpos, birdsbestpos
    for i in range(birds):
        VecAddVec(pos[i], speed[i])
    if CalDis(pos[i]) < CalDis(bestpos[i]):
        bestpos[i] = copy.deepcopy(pos[i])
    birdsbestpos = FindBirdsMostPos()

for i in range(100):
    # print birdsbestpos
    print CalDis(birdsbestpos)
    UpdateSpeed()
    UpdatePos()

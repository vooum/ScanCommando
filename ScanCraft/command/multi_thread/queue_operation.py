#! /usr/bin/env python3
import queue,copy

def FillQueue(q,mold,total_number=1e10,points=None):
    if points is None:
        points=1000
    while (not q.full()) and (q.qsize()<total_number) and (points>0):
        # print(q.full())
        point=copy.deepcopy(mold)
        point.Sample()
        q.put(point)
        points-=1
        # print(q.qsize())
    return q


def GenerateQueue(mold,lenth=None):
    if lenth==None:
        lenth=1000
    q=queue.Queue(lenth)
    FillQueue(q,mold,points=lenth)
    return q
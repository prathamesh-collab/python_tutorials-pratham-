#!/usr/bin/env pyhton3.7

#create module here to calculate area of the following shapes:
#use this module in (areaof_tri_rc_sq.py) this file 


def triangle(length,breath):
    length=float(input("enter lenght here :"))
    breath=float(input("enter breath here :"))

    area=length*breath/2
    print('area of triangle is ' , area )
    return

def rectangle(length,width):
    length=float(input("enter length of rectangle :"))
    width=float(input("enter width of rectangle :"))
    area=length*width
    print("area of rectangle is :",area)
    return

def polygon(side):
    s=float(input("enter side's of polygon :"))
    peri=6*s
    ap=s*1.73
    area=ap*peri*s/2
    print("area of polygon is :" , area)
    return

def hexagon(side):
    s=float(input("enter side of hexagon : "))
    area=3*1.73*s*s/2
    print("area of hexagon : " , area)
    return


def circle(radii,pi):
    radii=float(input("enter radius here :"))
    pi=float(input("enter pi vaalue here :"))
    area=radii*radii*2*3.14
    print(" area of circle is :" , area)
    return


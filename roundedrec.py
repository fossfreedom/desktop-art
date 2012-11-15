from __future__ import division

def roundedrec(cc, x, y, w, h, r):
    r = min(1,r)
    r = r * 0.7 * min(w, h)
    cc.move_to(x+r,y)
    cc.line_to(x+w-r,y)
    cc.curve_to(x+w,y,x+w,y,x+w,y+r)
    cc.line_to(x+w,y+h-r)
    cc.curve_to(x+w,y+h,x+w,y+h,x+w-r,y+h)
    cc.line_to(x+r,y+h)
    cc.curve_to(x,y+h,x,y+h,x,y+h-r)
    cc.line_to(x,y+r)
    cc.curve_to(x,y,x,y,x+r,y)

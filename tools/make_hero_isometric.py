#!/usr/bin/env python3
"""Generator for assets/hero-isometric.svg -- the pipe run in the hero.

The drawing is built from 3-D coordinates and projected, not drawn by hand:
an isometric elbow, a tube silhouette and a handwheel are all things you get
wrong by eye and right by arithmetic. iso() is the standard 30-degree
projection; tube() finds the two points of the end ring that are extreme
along the screen normal of the axis and joins them, which is what makes a
cylinder read as a cylinder; bend() sweeps those two silhouette points
around the arc rather than stacking rings, which is what the first attempt
did and it came out a scribble.

Run after changing the geometry:
    python3 tools/make_hero_isometric.py
"""
import math, re, os

C30 = math.cos(math.radians(30)); S30 = math.sin(math.radians(30))
def iso(p):
    x,y,z = p
    return ((x-y)*C30, (x+y)*S30 - z)
def sub(a,b): return (a[0]-b[0], a[1]-b[1], a[2]-b[2])
def add(a,b): return (a[0]+b[0], a[1]+b[1], a[2]+b[2])
def mul(a,k): return (a[0]*k, a[1]*k, a[2]*k)
def norm(a):
    L=math.sqrt(sum(c*c for c in a)) or 1.0; return mul(a,1.0/L)
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def basis(axis):
    a=norm(axis); t=(0,0,1) if abs(a[2])<0.9 else (1,0,0)
    u=norm(cross(a,t)); return u, norm(cross(a,u))
def ring(c, axis, r, n=32):
    u,v = basis(axis)
    return [add(c, add(mul(u, r*math.cos(2*math.pi*i/n)), mul(v, r*math.sin(2*math.pi*i/n)))) for i in range(n)]
def d_poly(pts, close=True):
    return "M" + " ".join("%.1f %.1f"%iso(p) for p in pts) + (" Z" if close else "")

def silhouette_idx(c, axis, r, n=32):
    """индексы двух крайних точек кольца по экранной нормали к оси"""
    R=ring(c,axis,r,n); s=[iso(p) for p in R]
    a1=iso(c); a2=iso(add(c, norm(axis)))
    ax=(a2[0]-a1[0], a2[1]-a1[1]); L=math.hypot(*ax) or 1
    nx,ny = -ax[1]/L, ax[0]/L
    pr=[(s[i][0]*nx+s[i][1]*ny, i) for i in range(n)]
    return max(pr)[1], min(pr)[1], R

def tube(p1, p2, r, cap1=True, cap2=True, n=32):
    ax=sub(p2,p1)
    i1,i2,R1 = silhouette_idx(p1, ax, r, n)
    _,_,R2 = silhouette_idx(p2, ax, r, n)
    out=[ "M%.1f %.1f L%.1f %.1f"%(*iso(R1[i1]), *iso(R2[i1])),
          "M%.1f %.1f L%.1f %.1f"%(*iso(R1[i2]), *iso(R2[i2])) ]
    if cap1: out.append(d_poly(R1))
    if cap2: out.append(d_poly(R2))
    return out

def bend(center, r_bend, a_from, a_to, r_pipe, steps=16, cap1=False, cap2=False):
    """колено: две силуэтные кривые + кольца по краям при необходимости"""
    outA=[]; outB=[]; ends=[]
    for i in range(steps+1):
        t=i/steps*math.pi/2
        d=add(mul(norm(a_from), math.cos(t)), mul(norm(a_to), math.sin(t)))
        c=add(center, mul(d, r_bend))
        tang=add(mul(norm(a_from), -math.sin(t)), mul(norm(a_to), math.cos(t)))
        i1,i2,R = silhouette_idx(c, tang, r_pipe, 32)
        outA.append(R[i1]); outB.append(R[i2])
        if i in (0,steps): ends.append(R)
    res=[d_poly(outA, False), d_poly(outB, False)]
    if cap1: res.append(d_poly(ends[0]))
    if cap2: res.append(d_poly(ends[1]))
    return res


# ================= сцена =================
R, RB = 15.0, 22.0            # труба и фланец
main, thin, dim = [], [], []

BEND_C = (-120, 0, 40)        # центр колена, радиус 40
RISER_TOP = (-160, 0, 130)
V  = (70, 0, 0)               # центр задвижки
END = (215, 0, 0)

# стояк: от верха до входа в колено (кольцо только на открытом торце)
main += tube(RISER_TOP, (-160, 0, 40), R, cap1=True, cap2=False)
# колено 90°: вниз-налево → вправо
main += bend(BEND_C, 40, (-1,0,0), (0,0,-1), R, steps=18)
# горизонталь от колена до фланца
main += tube((-120, 0, 0), (V[0]-52, 0, 0), R, cap1=False, cap2=False)
# горизонталь после задвижки до открытого торца
main += tube((V[0]+52, 0, 0), END, R, cap1=False, cap2=True)

# фланцы: короткие бочонки большего радиуса
for s in (-1, 1):
    a=(V[0]+s*52, 0, 0); b=(V[0]+s*42, 0, 0)
    main += tube(a, b, RB, cap1=True, cap2=True)

# корпус задвижки
# корпус — с торцевыми эллипсами, иначе теряется между фланцами
main += tube((V[0]-42, 0, 0), (V[0]+42, 0, 0), 27, cap1=True, cap2=True)
# бонет и шток
# бонет начинается от верха корпуса, а не изнутри трубы
main += tube((V[0], 0, 27), (V[0], 0, 62), 13, cap1=False, cap2=True)
thin += tube((V[0], 0, 62), (V[0], 0, 86), 3.5, cap1=False, cap2=False)
# маховик: обод + спицы
main.append(d_poly(ring((V[0],0,88), (0,0,1), 34)))
thin.append(d_poly(ring((V[0],0,88), (0,0,1), 24)))
for k in range(3):
    a=2*math.pi*k/3
    p=add((V[0],0,88), (34*math.cos(a), 34*math.sin(a), 0))
    thin.append("M%.1f %.1f L%.1f %.1f"%(*iso((V[0],0,88)), *iso(p)))

# опоры
for sx in (-45, 165):
    thin += tube((sx,0,-72), (sx,0,-R-2), 5, cap1=False, cap2=True)
    thin.append(d_poly([(sx-24,-16,-72),(sx+24,-16,-72),(sx+24,16,-72),(sx-24,16,-72)]))

# основание
GX0,GX1,GY0,GY1,GZ = -215, 250, -62, 62, -72
thin.append(d_poly([(GX0,GY0,GZ),(GX1,GY0,GZ),(GX1,GY1,GZ),(GX0,GY1,GZ)]))

# ---------- осевая линия трассы: путь для движущихся стрелок ----------
# Идёт по центру трубы: стояк сверху вниз, колено, горизонталь до открытого
# торца. Сама не рисуется -- она только задаёт траекторию.
centre = [RISER_TOP, (-160, 0, 40)]
for i in range(13):
    t = i/12*math.pi/2
    d = add(mul(norm((-1,0,0)), math.cos(t)), mul(norm((0,0,-1)), math.sin(t)))
    centre.append(add(BEND_C, mul(d, 40)))
centre.append((-120, 0, 0)); centre.append(END)
FLOW_D = "M" + " ".join("%.1f %.1f"%iso(q) for q in centre)

# размерные линии
def dimline(p1,p2,off):
    a,b=add(p1,off),add(p2,off)
    (ax,ay),(bx,by)=iso(a),iso(b); L=math.hypot(bx-ax,by-ay) or 1
    ux,uy=(bx-ax)/L,(by-ay)/L; k=8
    d=["M%.1f %.1f L%.1f %.1f"%(ax,ay,bx,by)]
    for (px,py),s in (((ax,ay),1),((bx,by),-1)):
        d.append("M%.1f %.1f L%.1f %.1f M%.1f %.1f L%.1f %.1f"%(
            px,py, px+s*ux*k-uy*k*.45, py+s*uy*k+ux*k*.45,
            px,py, px+s*ux*k+uy*k*.45, py+s*uy*k-ux*k*.45))
    for p,q in ((p1,a),(p2,b)):
        d.append("M%.1f %.1f L%.1f %.1f"%(*iso(p), *iso(q)))
    return d
dim += dimline((GX0,GY1,GZ),(GX1,GY1,GZ),(0,30,0))
dim += dimline((GX1,GY0,GZ),(GX1,GY1,GZ),(32,0,0))
dim += dimline((END[0],GY0,GZ),(END[0],GY0,0),(0,-30,0))

# ================= вывод =================
pts=[]
for g in (main,thin,dim):
    for d in g:
        pts += [(float(m.group(1)),float(m.group(2))) for m in re.finditer(r'(-?\d+\.?\d*) (-?\d+\.?\d*)', d)]
xs=[p[0] for p in pts]; ys=[p[1] for p in pts]; pad=16
vb=(min(xs)-pad, min(ys)-pad, max(xs)-min(xs)+2*pad, max(ys)-min(ys)+2*pad)
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="%.0f" height="%.0f" viewBox="%.1f %.1f %.1f %.1f" preserveAspectRatio="xMidYMid meet" role="presentation" aria-hidden="true" focusable="false">'%(vb[2],vb[3],*vb),
 '<g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">',
 '<g stroke-width="2.4">']+['<path d="%s"/>'%d for d in main]+['</g>',
 '<g stroke-width="1.5" opacity=".85">']+['<path d="%s"/>'%d for d in thin]+['</g>',
 '<g stroke-width="1" opacity=".45">']+['<path d="%s"/>'%d for d in dim]+['</g>']

# ---------- движущиеся стрелки потока ----------
# Шеврон едет по осевой линии. animateMotion с rotate="auto" разворачивает его
# по касательной, поэтому на колене он поворачивает вместе с трубой. Три штуки
# со сдвигом по фазе читаются как поток, одна -- как случайность.
CHEV = 'M-11 -8 L0 0 L-11 8'
svg.append('<g class="flow" stroke-width="2.6" opacity="1" stroke-linecap="round" stroke-linejoin="round">')
svg.append('<path id="flowline" d="%s" fill="none" stroke="none"/>'%FLOW_D)
for k in range(3):
    svg.append('<path d="%s" fill="none">'
               '<animateMotion dur="5.2s" begin="%.2fs" repeatCount="indefinite" rotate="auto" keyPoints="0;1" keyTimes="0;1" calcMode="linear">'
               '<mpath href="#flowline"/></animateMotion>'
               '<animate attributeName="opacity" dur="5.2s" begin="%.2fs" repeatCount="indefinite" '
               'values="0;1;1;0" keyTimes="0;0.12;0.86;1"/>'
               '</path>'%(CHEV, k*1.73, k*1.73))
svg.append('</g>')
svg.append('</g></svg>')
open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "hero-isometric.svg"), "w").write("\n".join(svg))
print("  %.0fx%.0f, %.1f КБ"%(vb[2],vb[3],os.path.getsize(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "hero-isometric.svg"))/1024))

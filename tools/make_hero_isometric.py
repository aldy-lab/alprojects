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


def flange(c, axis, r_out, r_in, bolts=12, thick=9.0):
    """Фланец: два кольца по торцам обечайки и болтовой ряд засечками.

    В референсе фланец читается именно болтовым рядом -- без него это просто
    утолщение. Засечки радиальные, длиной в треть кольца, как на чертеже."""
    a = norm(axis)
    c1, c2 = add(c, mul(a, -thick / 2)), add(c, mul(a, thick / 2))
    out = tube(c1, c2, r_out, cap1=True, cap2=True)
    out.append(d_poly(ring(c2, a, r_in)))
    u, v = basis(a)
    rb = (r_out + r_in) / 2.0
    for i in range(bolts):
        t = 2 * math.pi * i / bolts
        d = add(mul(u, math.cos(t)), mul(v, math.sin(t)))
        out.append("M%.1f %.1f L%.1f %.1f" % (
            *iso(add(c2, mul(d, r_in + 3))), *iso(add(c2, mul(d, r_out - 3)))))
    return out


def mitre(center, r_bend, a_from, a_to, r_pipe, pieces=3):
    """Сегментное колено со швами -- то, что в референсе делает колено коленом.

    Гладкая развёртка читается как шланг. Настоящее сварное колено собрано из
    сегментов, и видны кольцевые швы между ними; их и рисуем."""
    body, seams = [], []
    prev_c = prev_t = None
    for i in range(pieces + 1):
        t = i / float(pieces) * math.pi / 2
        d = add(mul(norm(a_from), math.cos(t)), mul(norm(a_to), math.sin(t)))
        c = add(center, mul(d, r_bend))
        tang = add(mul(norm(a_from), -math.sin(t)), mul(norm(a_to), math.cos(t)))
        if prev_c is not None:
            body += tube(prev_c, c, r_pipe, cap1=False, cap2=False)
        if 0 < i < pieces:
            seams.append(d_poly(ring(c, tang, r_pipe)))
        prev_c, prev_t = c, tang
    return body, seams


def box3(p0, p1, ribs=2):
    """Прямоугольный аппарат: двенадцать рёбер и пара внутренних перегородок."""
    (x0, y0, z0), (x1, y1, z1) = p0, p1
    V = [(x0,y0,z0),(x1,y0,z0),(x1,y1,z0),(x0,y1,z0),
         (x0,y0,z1),(x1,y0,z1),(x1,y1,z1),(x0,y1,z1)]
    E = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]
    out = ["M%.1f %.1f L%.1f %.1f" % (*iso(V[a]), *iso(V[b])) for a, b in E]
    for k in range(1, ribs + 1):
        x = x0 + (x1 - x0) * k / (ribs + 1.0)
        out.append("M%.1f %.1f L%.1f %.1f" % (*iso((x,y0,z1)), *iso((x,y1,z1))))
        out.append("M%.1f %.1f L%.1f %.1f" % (*iso((x,y0,z0)), *iso((x,y0,z1))))
    return out


# ================= сцена =================
# Толстая труба, сегментные колена, фланцы с болтовым рядом, аппарат и длинные
# построительные линии -- это и есть язык строительной изометрии. Точки трассы
# названы и стыки считаются, а не подбираются: первая версия развернула колено
# от (0,0,1) к (1,0,0) вокруг центра и продолжила горизонталь из центра, а не из
# выхода колена, и труба разошлась на 62 единицы.
R, RB = 32.0, 47.0
RBEND = 58.0
main, thin, dim = [], [], []

# --- аппарат, из которого выходит трасса ---
BOX0, BOX1 = (-330, -70, -30), (-205, 70, 118)
main += box3(BOX0, BOX1, ribs=2)

# --- горизонталь на верхней отметке ---
ZT = 44.0                       # ось верхней горизонтали
P_IN = (-205, 0, ZT)            # выход из аппарата
FLC  = (-70, 0, ZT)             # центр фланцевого стыка
BEND1 = (30.0, 0, ZT)           # ось трубы входит в колено здесь

main += tube(P_IN, add(FLC, (-26, 0, 0)), R)
main += flange(add(FLC, (-20, 0, 0)), (1, 0, 0), RB, R)
main += flange(add(FLC, ( 20, 0, 0)), (1, 0, 0), RB, R)
main += tube(add(FLC, (26, 0, 0)), BEND1, R)

# --- колено вниз: центр смещён на радиус вниз, выход считаем, а не гадаем ---
C1 = add(BEND1, (0, 0, -RBEND))                 # центр дуги
_b, _s = mitre(C1, RBEND, (0, 0, 1), (1, 0, 0), R, pieces=3)
main += _b; thin += _s
OUT1 = add(C1, (RBEND, 0, 0))                   # где колено кончается
ZB = OUT1[2]                                    # нижняя отметка

# --- нижняя горизонталь до открытого торца с фланцем ---
P_END = (300.0, 0, ZB)
main += tube(OUT1, add(P_END, (-24, 0, 0)), R)
main += flange(add(P_END, (-18, 0, 0)), (1, 0, 0), RB, R)

# --- опоры ---
SUPS = (-150.0, 210.0)
GZ = -150.0
for sx in SUPS:
    thin += tube((sx, 0, GZ), (sx, 0, ZB - R), 9, cap1=False, cap2=True)
    thin.append(d_poly([(sx-32,-24,GZ),(sx+32,-24,GZ),(sx+32,24,GZ),(sx-32,24,GZ)]))
# опора под верхней горизонталью, к аппарату
thin += tube((-150, 0, ZT - R), (-150, 0, ZB - R), 9, cap1=False, cap2=False)

# --- основание ---
GX0, GX1, GY0, GY1 = -350, 350, -95, 95
thin.append(d_poly([(GX0,GY0,GZ),(GX1,GY0,GZ),(GX1,GY1,GZ),(GX0,GY1,GZ)]))

# --- построительные линии: проекция вниз за пределы предмета ---
for pt in (BOX1, (BOX0[0], BOX1[1], BOX1[2]), FLC, BEND1, OUT1, P_END):
    x, y = iso(pt)
    dim.append("M%.1f %.1f L%.1f %.1f" % (x, y, x, y + 230))

END = P_END
V = FLC
RISER_TOP = P_IN

# ---------- осевая линия трассы: путь для движущихся стрелок ----------
# Идёт по центру трубы: стояк сверху вниз, колено, горизонталь до открытого
# торца. Сама не рисуется -- она только задаёт траекторию.
centre = [P_IN, BEND1]
for i in range(13):
    t = i / 12.0 * math.pi / 2
    d = add(mul(norm((0,0,1)), math.cos(t)), mul(norm((1,0,0)), math.sin(t)))
    centre.append(add(C1, mul(d, RBEND)))
centre.append(P_END)
FLOW_D = "M" + " ".join("%.1f %.1f"%iso(q) for q in centre)

# ---------- аннотации: то, что отличает чертёж от объёма ----------
# Изометрия трубы без размеров, отметок и швов -- это объём. Чертёж состоит
# ровно из этих подписей: размер по оси, EL на каждой смене уровня, точка на
# заводском шве и флаг на монтажном, номер линии, метка опоры, север и обрыв
# трассы. Текст здесь не язык, а обозначения -- он не переводится, как и
# 1200X1600 в остальной оснастке листа, и SVG всё равно вставляется скриптом,
# так что в собранный HTML он не попадает и i18n его не видит.
ANNO = []          # тексты; рисуются последним слоем

def label(pt, txt, dx=0.0, dy=0.0, anchor="middle", size=9.0, rot=None):
    x, y = iso(pt); x += dx; y += dy
    tr = ' transform="rotate(%.1f %.1f %.1f)"' % (rot, x, y) if rot else ""
    ANNO.append('<text x="%.1f" y="%.1f" text-anchor="%s" font-size="%.1f"%s>%s</text>'
                % (x, y, anchor, size, tr, txt))

def screen_angle(p1, p2):
    (ax, ay), (bx, by) = iso(p1), iso(p2)
    a = math.degrees(math.atan2(by - ay, bx - ax))
    return a + 180 if a > 90 or a < -90 else a      # цифра всегда читается

# размерные линии
def dimline(p1,p2,off,txt=None):
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
    if txt:
        mid = mul(add(a, b), 0.5)
        ang = screen_angle(a, b)
        # цифра стоит над линией по её нормали, как на настоящем листе
        rad = math.radians(ang)
        label(mid, txt, dx=math.sin(rad) * 7.5, dy=-math.cos(rad) * 7.5,
              size=8.5, rot=ang)
    return d


def weld(pt, field=False):
    """Заводской шов -- точка. Монтажный -- точка с флагом."""
    x, y = iso(pt)
    thin.append('M%.1f %.1f m-3 0 a3 3 0 1 0 6 0 a3 3 0 1 0 -6 0' % (x, y))
    if field:
        thin.append("M%.1f %.1f L%.1f %.1f L%.1f %.1f Z"
                    % (x, y, x, y - 15, x + 9, y - 11))


def leader(pt, dx, dy, txt, size=8.5, shelf=16.0):
    """Полка с выноской -- так на чертеже подписывают опору или линию."""
    x, y = iso(pt)
    dim.append("M%.1f %.1f L%.1f %.1f L%.1f %.1f"
               % (x, y, x + dx, y + dy, x + dx + shelf, y + dy))
    ANNO.append('<text x="%.1f" y="%.1f" text-anchor="start" font-size="%.1f">%s</text>'
                % (x + dx + 3, y + dy - 4, size, txt))


def elev(pt, txt, side=1):
    """Отметка уровня: короткая горизонталь и EL над ней."""
    x, y = iso(pt)
    dim.append("M%.1f %.1f L%.1f %.1f" % (x, y, x + side * 46, y))
    dim.append("M%.1f %.1f l%.1f -5 l%.1f 10 Z" % (x + side * 46, y, side * -9, side * 9))
    ANNO.append('<text x="%.1f" y="%.1f" text-anchor="%s" font-size="8.5">%s</text>'
                % (x + side * 50, y - 5, "start" if side > 0 else "end", txt))
# размеры по трём изометрическим осям -- как на листе
# Выносы размеров подобраны так, чтобы цифра не легла на трубу: при -110
# верхний размер шёл прямо по трассе, потому что -y в изометрии уходит
# вверх-вправо, то есть вдоль неё же.
dim += dimline(P_IN, BEND1, (0, -210, 0), "3450")          # верхняя горизонталь
dim += dimline(OUT1, P_END, (0, 150, 0), "2120")           # нижняя горизонталь
dim += dimline(BEND1, OUT1, (230, 0, 0), "580")            # высота колена
dim += dimline((GX0,GY1,GZ), (GX1,GY1,GZ), (0, 40, 0), "7000")

# отметки там, где меняется уровень
# EL у фланцевого стыка, а не у врезки в аппарат: там она ложилась на корпус.
elev(FLC, "EL +14300", -1)
elev(add(P_END, (-90,0,0)), "EL +13720", -1)

# швы: заводские на врезках в аппарат и на выходе колена, монтажные -- фланцы
weld(P_IN); weld(OUT1)
weld(add(FLC, (-20,0,0)), field=True); weld(add(FLC, (20,0,0)), field=True)

# номер линии и класс
leader(add(BEND1, (-90, 0, R)), 26, -104, "300-PG-1204-A1")
leader(add(BEND1, (-40, 0, R)), 34, -76, "DN 300 / SCH 40")

# метки опор
for sx, tag in zip(SUPS, ("SUP-0100", "SUP-0101")):
    leader((sx, 0, GZ), -52, 46, tag)

# север
NX, NY = iso((GX0 - 30, GY1 + 90, GZ))
dim.append("M%.1f %.1f L%.1f %.1f" % (NX, NY, NX+28, NY-16))
dim.append("M%.1f %.1f l-12 -1 l4 10 Z" % (NX+28, NY-16))
ANNO.append('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="9">N</text>'
            % (NX+33, NY-20))

# обрыв трассы
BX, BY = iso(P_END)
dim.append("M%.1f %.1f l11 -14 l7 28 l11 -14" % (BX+30, BY))
ANNO.append('<text x="%.1f" y="%.1f" text-anchor="start" font-size="8">CONT ON DRG 2</text>'
            % (BX+66, BY+3))

# ================= вывод =================
pts=[]
for g in (main,thin,dim):
    for d in g:
        pts += [(float(m.group(1)),float(m.group(2))) for m in re.finditer(r'(-?\d+\.?\d*) (-?\d+\.?\d*)', d)]
# подписи выходят за обводку -- их координаты тоже идут в рамку, иначе
# EL и CONT ON DRG 2 обрезаются по краю
for t in ANNO:
    m=re.search(r'x="(-?\d+\.?\d*)" y="(-?\d+\.?\d*)"', t)
    if m: pts.append((float(m.group(1)), float(m.group(2))))
xs=[p[0] for p in pts]; ys=[p[1] for p in pts]; pad=30
vb=(min(xs)-pad, min(ys)-pad, max(xs)-min(xs)+2*pad, max(ys)-min(ys)+2*pad)
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="%.0f" height="%.0f" viewBox="%.1f %.1f %.1f %.1f" preserveAspectRatio="xMidYMid meet" role="presentation" aria-hidden="true" focusable="false">'%(vb[2],vb[3],*vb),
 '<g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">',
 '<g stroke-width="2.4">']+['<path d="%s"/>'%d for d in main]+['</g>',
 '<g stroke-width="1.5" opacity=".85">']+['<path d="%s"/>'%d for d in thin]+['</g>',
 '<g stroke-width="1" opacity=".45">']+['<path d="%s"/>'%d for d in dim]+['</g>',
 # Текст -- отдельным слоем: он не обводка, у него своя заливка и гарнитура.
 # Montserrat через переменную сайта, потому что SVG вставляется в документ
 # скриптом и наследует его шрифты.
 '<g fill="currentColor" stroke="none" opacity=".6" letter-spacing="0.06em"'
 ' font-family="var(--font-display), Montserrat, sans-serif">']+ANNO+['</g>']

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

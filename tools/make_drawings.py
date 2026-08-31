#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build one animated technical drawing per service, plus Company and Projects.

Fourteen subjects, one drawing language. Every file is generated here rather
than drawn by hand so the weight of line, the greys, the sheet furniture and
the way motion is switched off are decided once and cannot drift apart across
fourteen assets.

Rules that apply to all of them, and the reasons:

  * No text. A word inside an SVG is a translation key that no build step can
    see, and this site publishes in four languages.
  * Outline only, two weights: `l` for the subject, `f` for construction lines,
    dimensions and anything the eye should read second.
  * The animation lives inside the file, so every drawing is referenced with a
    plain <img>: no JavaScript, cached like any other asset, and
    prefers-reduced-motion is answered by the file itself. The cost is that
    stroke colour is baked in rather than taken from currentColor -- acceptable
    on a site whose ground is dark on every page.
  * Each motion says what the service does. A rotor turns, a bead is laid, a
    probe sweeps, a tank goes up course by course. Decoration that could sit on
    any of the fourteen has no business on one of them.

    python3 tools/make_drawings.py          # writes assets/drawings/*.svg

The wind field on /sectors/renewables predates this module and stays in
tools/make_wind_turbine.py; it uses the same conventions.
"""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(ROOT, "assets", "drawings")

W, H = 1000, 620
INK = "185, 196, 216"

BASE = """
    path, circle, rect, ellipse, polygon, polyline, line {
      fill: none; stroke-width: 1.2; stroke-linecap: round; stroke-linejoin: round;
    }
    .l  { stroke: rgba(@INK@, 0.50); }
    .f  { stroke: rgba(@INK@, 0.22); }
    .ff { stroke: rgba(@INK@, 0.13); }
    .dash    { stroke-dasharray: 5 7; }
    .dashdot { stroke-dasharray: 14 5 2 5; }
    .fill  { fill: rgba(@INK@, 0.10); stroke: none; }
"""

# Every animated class is listed here so one media query stops all of them.
REDUCED = """
    @media (prefers-reduced-motion: reduce) {
      [class*="anim"] { animation: none !important; }
    }
"""


# ---------------------------------------------------------------- primitives
def L(x1, y1, x2, y2, c="l"):
    return '<path class="%s" d="M %.1f %.1f L %.1f %.1f"/>' % (c, x1, y1, x2, y2)


def P(d, c="l", extra=""):
    return '<path class="%s" d="%s"%s/>' % (c, d, extra)


def C(cx, cy, r, c="l", extra=""):
    return '<circle class="%s" cx="%.1f" cy="%.1f" r="%.1f"%s/>' % (c, cx, cy, r, extra)


def R(x, y, w, h, c="l", rx=0, extra=""):
    return ('<rect class="%s" x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f"%s/>'
            % (c, x, y, w, h, rx, extra))


def hatch(x, y, w, n=14, step=None, c="ff", drop=13):
    """Section hatching, the convention for cut material."""
    step = step or (w / float(n))
    return "\n  ".join(L(x + i * step, y, x + i * step - drop * 0.7, y + drop, c)
                       for i in range(n + 1))


def ground(y, x0=40, x1=W - 40, n=26):
    return L(x0, y, x1, y, "l") + "\n  " + hatch(x0, y, x1 - x0, n)


def crosshair(x, y, r=9, c="f"):
    return L(x - r, y, x + r, y, c) + "\n  " + L(x, y - r, x, y + r, c)


def dim_h(x0, x1, y, c="f", tick=7):
    """A horizontal dimension line with end ticks -- no figure, only the rule."""
    return "\n  ".join([L(x0, y, x1, y, c),
                        L(x0, y - tick, x0, y + tick, c),
                        L(x1, y - tick, x1, y + tick, c)])


def furniture(marks):
    return "\n  ".join(crosshair(x, y) for x, y in marks)


def draws_itself(name, dur, delay=0, hold=0.25):
    """CSS that makes a path with pathLength=1 draw itself, then hold and repeat."""
    on = round(100.0 * (1 - hold), 1)
    return ("""
    .@N@ { stroke-dasharray: 1; stroke-dashoffset: 1;
           animation: @N@-draw @D@s linear @DELAY@s infinite; }
    @keyframes @N@-draw {
      0% { stroke-dashoffset: 1; }
      @ON@% { stroke-dashoffset: 0; }
      100% { stroke-dashoffset: 0; }
    }"""
            .replace("@N@", name).replace("@D@", str(dur))
            .replace("@DELAY@", str(delay)).replace("@ON@", str(on)))


def svg(parts, css):
    body = "\n  ".join(p for p in parts if p)
    style = (BASE + "\n" + css + "\n" + REDUCED).replace("@INK@", INK)
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d"'
            ' width="%d" height="%d" role="img" aria-label="">\n'
            '  <style>%s  </style>\n  %s\n</svg>\n' % (W, H, W, H, style, body))


# ================================================================= subjects
def welding_services():
    """Two plates in section with a V prep. The torch travels the joint and the
    bead is laid behind it -- the one motion that is welding and nothing else."""
    y, x0, x1 = 400.0, 180.0, 820.0
    p = [ground(560),
         # plates in section, cut faces hatched, a V between them
         P("M %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f Z"
           % (x0 - 120, y, 480, y, 496, y + 46, x0 - 120, y + 46)),
         P("M %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f Z"
           % (520, y, x1 + 120, y, x1 + 120, y + 46, 504, y + 46)),
         hatch(x0 - 116, y + 4, 292, 10, drop=38),
         hatch(524, y + 4, 400, 14, drop=38),
         # the root gap, dimensioned
         dim_h(496, 504, y + 74),
         # supports
         L(x0 - 40, y + 46, x0 - 40, 560, "f"), L(x1 + 40, y + 46, x1 + 40, 560, "f"),
         # the bead: a single stroke along the joint that draws itself
         P("M %.1f %.1f L %.1f %.1f" % (x0, y - 2, x1, y - 2), "l",
           ' pathLength="1" class="l anim-bead"').replace('class="l" ', ""),
         # torch: a nozzle on the joint, travelling with the bead
         ('<g class="anim-torch">'
          + P("M %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f Z"
              % (x0 - 15, y - 150, x0 + 15, y - 150, x0 + 9, y - 34, x0 - 9, y - 34))
          + L(x0, y - 150, x0, y - 196)
          + C(x0, y - 20, 5, "f")
          + '</g>'),
         crosshair(140, 200), crosshair(880, 250)]
    css = (draws_itself("anim-bead", 7)
           + """
    .anim-torch { animation: torch-run 7s linear infinite; }
    @keyframes torch-run {
      0% { transform: translateX(0); }
      75% { transform: translateX(640px); }
      100% { transform: translateX(640px); }
    }""")
    return p, css


def pipe_fitting():
    """A flange seen face-on, bolted up in the order a fitter actually pulls it:
    across the circle, not round it. The spool it belongs to is in section
    beside it, so the face view is not floating.

    The first version put the face edge-on and laid the bolts across it as
    horizontal bars; at page size it read as a fence."""
    import math
    cx, cy, r = 620.0, 300.0, 165.0
    p = [ground(560),
         # spool in section, coming in from the left to the flange
         R(60, cy - 58, 300, 116, "l"),
         hatch(66, cy - 54, 288, 9, drop=108),
         R(360, cy - 165, 26, 330, "l"),
         L(386, cy, 452, cy, "f dashdot"),
         # the face
         C(cx, cy, r, "l"), C(cx, cy, r - 26, "f"), C(cx, cy, 92, "l"), C(cx, cy, 66, "ff"),
         C(cx, cy, r - 44, "f dash"),
         crosshair(cx, cy, r + 32, "f"),
         dim_h(cx - r, cx + r, cy + r + 62)]
    # The shorthand goes FIRST. `animation:` resets animation-delay, so with the
    # per-bolt delays written above it every bolt landed at once and the star
    # sequence -- the whole point of the drawing -- silently did not happen.
    css = ["""
    .anim-bolt { opacity: 0; animation: bolt-in 8s linear infinite; }
    @keyframes bolt-in {
      0%, 3% { opacity: 0; }
      9%, 92% { opacity: 1; }
      100% { opacity: 0; }
    }"""]
    order = [0, 4, 2, 6, 1, 5, 3, 7]     # the star sequence
    for step, k in enumerate(order):
        a = math.radians(k * 45.0 - 90.0)
        bx, by = cx + (r - 44) * math.cos(a), cy + (r - 44) * math.sin(a)
        p.append(C(bx, by, 13, "l anim-bolt b%d" % step))
        p.append(C(bx, by, 6, "f anim-bolt b%d" % step))
        css.append(".b%d { animation-delay: %.2fs; }" % (step, step * 0.6))
    return p, "\n    ".join(css)


def non_destructive_testing():
    """A probe sweeping a weld, and the trace it returns. The blip rises where
    the probe passes the flaw: the service is not the sweep, it is the reading.

    Drawn large. The first version put a thin plate at the top of the frame and
    two hairlines at the bottom, and at page size it read as three stripes."""
    x0, x1 = 130.0, 870.0
    top, th = 210.0, 96.0
    flaw = 640.0
    base = 470.0
    p = [# the plate in section, with the weld cap and the flaw inside it
         R(x0, top, x1 - x0, th, "l"),
         hatch(x0 + 8, top + 4, x1 - x0 - 16, 22, drop=th - 8),
         P("M 470 %.1f q 60 -34 120 0" % top, "l"),
         L(470, top, 590, top, "f dash"),
         P("M %.1f %.1f l 20 13 l -9 15" % (flaw - 10, top + 34), "l"),
         C(flaw + 2, top + 46, 30, "f dash"),
         # the probe, on the plate from the first frame
         ('<g class="anim-probe">' + R(x0 - 44, top - 62, 88, 58, "l", rx=5)
          + L(x0 - 44, top - 4, x0 + 44, top - 4, "l")
          + L(x0, top - 62, x0, top - 96, "f") + '</g>'),
         # the trace
         L(x0, base, x1, base, "l"),
         L(x0, base - 96, x1, base - 96, "ff dash"),
         L(x0, base + 34, x1, base + 34, "ff"),
         ('<g class="anim-blip">'
          + P("M %.1f %.1f l 12 -124 l 12 124" % (flaw - 12, base)) + '</g>'),
         dim_h(x0, x1, 545), crosshair(x0 - 70, 160), crosshair(x1 + 60, 300)]
    css = """
    .anim-probe { animation: probe-run 9s ease-in-out infinite; }
    @keyframes probe-run {
      0%   { transform: translateX(0); }
      45%  { transform: translateX(740px); }
      55%  { transform: translateX(740px); }
      100% { transform: translateX(0); }
    }
    .anim-blip { opacity: 0; animation: blip 9s ease-in-out infinite; }
    @keyframes blip {
      0%, 29% { opacity: 0; }
      33%, 37% { opacity: 1; }
      41%, 62% { opacity: 0; }
      66%, 70% { opacity: 1; }
      74%, 100% { opacity: 0; }
    }"""
    return p, css


def laser_scanning():
    """A scanner on its tripod in a plant, the head turning and the fan going
    round with it, and the cloud arriving where the beam has already been.

    The plan is drawn as an ellipse rather than a circle: the sweep is
    horizontal and a head-on circle read as a target rather than as a room."""
    import math
    cx, cy = 500.0, 300.0
    rx, ry = 400.0, 150.0
    p = [ground(560),
         # the room being scanned, in plan, with a few things standing in it
         '<ellipse class="ff dash" cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f"/>'
         % (cx, cy, rx, ry),
         '<ellipse class="ff" cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f"/>'
         % (cx, cy, rx * 0.62, ry * 0.62),
         R(170, 250, 90, 60, "f"), C(300, 200, 30, "f"), R(760, 300, 80, 70, "f"),
         C(660, 380, 26, "f"),
         # the sweep, a narrow sector turning about the head
         ('<g class="anim-sweep">'
          + P("M %.1f %.1f L %.1f %.1f A %.1f %.1f 0 0 1 %.1f %.1f Z"
              % (cx, cy, cx + rx, cy - 52, rx, rx, cx + rx, cy + 52), "f")
          + L(cx, cy, cx + rx, cy, "f")
          + '</g>'),
         # the instrument itself, over its own plan
         R(cx - 30, cy - 74, 60, 76, "l", rx=8),
         C(cx, cy - 36, 17, "f"), C(cx, cy - 36, 6, "ff"),
         L(cx, cy + 2, cx - 52, cy + 96, "l"), L(cx, cy + 2, cx + 52, cy + 96, "l"),
         L(cx, cy + 2, cx, cy + 96, "f"),
         crosshair(120, 170), crosshair(880, 430)]
    # the cloud, filling in behind the beam
    for i in range(52):
        a = math.radians(i * (360.0 / 52) - 90)
        k = 0.86 + (i % 4) * 0.05
        p.append(C(cx + rx * k * math.cos(a), cy + ry * k * math.sin(a), 2.4,
                   "l anim-pt p%d" % i))
    css = ["""
    .anim-sweep { transform-box: view-box; transform-origin: @CXpx @CYpx;
                  animation: sweep 12s linear infinite; }
    @keyframes sweep { to { transform: rotate(360deg); } }
    .anim-pt { opacity: 0; animation: pt 12s linear infinite; }
    @keyframes pt { 0%, 2% { opacity: 0; } 6%, 95% { opacity: 1; } 100% { opacity: 0; } }"""
           .replace("@CX", "%.1f" % cx).replace("@CY", "%.1f" % cy)]
    for i in range(52):
        css.append(".p%d { animation-delay: %.2fs; }" % (i, i * 12.0 / 52))
    return p, "\n    ".join(css)


def rope_access():
    """Two ropes off one edge and a technician going down them. The second rope
    is the point of the trade, so it is drawn at the same weight as the first."""
    ex, top = 300.0, 120.0
    p = [# the structure
         R(120, top, 180, 460, "l"), hatch(126, top + 4, 168, 6, drop=452),
         L(120, top, 860, top, "l"),
         # anchors
         C(ex + 40, top - 16, 9, "l"), C(ex + 96, top - 16, 9, "l"),
         L(ex + 40, top - 16, ex + 40, 540, "f"),
         L(ex + 96, top - 16, ex + 96, 540, "f"),
         # rope protection at the edge
         P("M %.1f %.1f q 16 -14 32 0" % (ex + 24, top), "l"),
         P("M %.1f %.1f q 16 -14 32 0" % (ex + 80, top), "l"),
         # the technician, as a harness glyph rather than a figure
         ('<g class="anim-desc">'
          + R(ex + 26, 190, 84, 12, "l", rx=6)
          + L(ex + 40, 202, ex + 40, 236) + L(ex + 96, 202, ex + 96, 236)
          + P("M %.1f %.1f l 26 44 l 26 -44" % (ex + 42, 236))
          + C(ex + 68, 176, 13, "l")
          + '</g>'),
         dim_h(ex + 40, ex + 96, 560), crosshair(760, 240), crosshair(830, 400)]
    css = """
    .anim-desc { animation: descend 12s ease-in-out infinite; }
    @keyframes descend {
      0%   { transform: translateY(0); }
      55%  { transform: translateY(250px); }
      70%  { transform: translateY(250px); }
      100% { transform: translateY(0); }
    }"""
    return p, css


def rigging():
    """A hook block, two legs at an angle, and the load coming up. The angle is
    dimensioned because it is what decides the leg tension."""
    cx, top = 500.0, 110.0
    p = [ground(560),
         L(200, top, 800, top, "l"), hatch(206, top - 26, 588, 18, drop=-26),
         L(cx, top, cx, 210, "l"),
         # hook block
         R(cx - 34, 210, 68, 44, "l", rx=6), C(cx, 232, 9, "f"),
         P("M %.1f %.1f q 0 40 -22 40 q -22 0 -22 -26" % (cx, 254), "l"),
         ('<g class="anim-load">'
          # slings
          + L(cx, 262, cx - 150, 400) + L(cx, 262, cx + 150, 400)
          + P("M %.1f %.1f A 70 70 0 0 1 %.1f %.1f" % (cx - 48, 310, cx + 48, 310), "f")
          # the load
          + R(cx - 170, 400, 340, 96, "l") + hatch(cx - 164, 404, 328, 12, drop=88)
          + '</g>'),
         crosshair(220, 300), crosshair(790, 330)]
    css = """
    .anim-load { animation: hoist 10s ease-in-out infinite; }
    @keyframes hoist {
      0%   { transform: translateY(60px); }
      45%  { transform: translateY(0); }
      60%  { transform: translateY(0); }
      100% { transform: translateY(60px); }
    }"""
    return p, css


def mechanical_contracting():
    """A machine set down on resilient mounts and levelled: the dial swings and
    a shim goes in under the low foot."""
    base, cx = 470.0, 500.0
    p = [ground(560), L(160, base, 840, base, "l"), hatch(166, base, 668, 22, drop=26),
         # machine body
         R(250, 250, 420, 150, "l", rx=6), R(300, 200, 150, 50, "l", rx=4),
         C(600, 325, 44, "f"), C(600, 325, 14, "ff"),
         # four mounts
         ] + [
        item for x in (300.0, 400.0, 560.0, 640.0) for item in (
            R(x - 22, 400, 44, 26, "l", rx=3),
            L(x, 426, x, base, "f"))
    ] + [
         # the shim, sliding under the low foot
         ('<g class="anim-shim">' + R(618, 448, 44, 10, "l") + '</g>'),
         # dial gauge on a stand, needle sweeping
         L(760, base, 760, 300, "f"), C(760, 270, 40, "l"), C(760, 270, 5, "f"),
         ('<g class="anim-needle">' + L(760, 270, 760, 238, "l") + '</g>'),
         dim_h(300, 640, 520), crosshair(200, 210)]
    css = """
    .anim-needle { transform-box: view-box; transform-origin: 760px 270px;
                   animation: needle 6s ease-in-out infinite; }
    @keyframes needle {
      0%, 100% { transform: rotate(-52deg); }
      45%, 62% { transform: rotate(18deg); }
    }
    .anim-shim { animation: shim 6s ease-in-out infinite; }
    @keyframes shim {
      0%, 20%  { transform: translateX(90px); opacity: 0; }
      34%, 100% { transform: translateX(0); opacity: 1; }
    }"""
    return p, css


def mobile_repair():
    """A spanner pulling a nut round, a flat at a time. Mobile teams arrive and
    turn things; the drawing is that and nothing more."""
    import math
    cx, cy, r = 500.0, 300.0, 96.0
    hexa = " ".join("%.1f,%.1f" % (cx + r * math.cos(math.radians(60 * i - 90)),
                                   cy + r * math.sin(math.radians(60 * i - 90)))
                    for i in range(6))
    p = [ground(560), L(cx, 396, cx, 560, "f"),
         C(cx, cy, r + 34, "ff dash"),
         ('<g class="anim-nut">' + '<polygon class="l" points="%s"/>' % hexa
          + C(cx, cy, 54, "f") + C(cx, cy, 26, "ff") + '</g>'),
         ('<g class="anim-spanner">'
          + P("M %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f"
              % (cx + 96, cy - 34, cx + 330, cy - 20, cx + 330, cy + 20, cx + 96, cy + 34))
          + P("M %.1f %.1f q -34 34 0 68" % (cx + 96, cy - 34), "l")
          + '</g>'),
         crosshair(200, 200), crosshair(820, 420)]
    css = """
    .anim-nut, .anim-spanner { transform-box: view-box; transform-origin: 500px 300px; }
    .anim-nut { animation: turn 5s cubic-bezier(.5,0,.2,1) infinite; }
    .anim-spanner { animation: turn-back 5s cubic-bezier(.5,0,.2,1) infinite; }
    @keyframes turn {
      0%, 12%  { transform: rotate(0deg); }
      52%, 100% { transform: rotate(60deg); }
    }
    @keyframes turn-back {
      0%, 12%  { transform: rotate(0deg); }
      52%      { transform: rotate(60deg); }
      70%, 100% { transform: rotate(0deg); }
    }"""
    return p, css


def heavy_relocation():
    """A load walked along skid beams on rollers. The rollers turn at the rate
    the load travels, because a drawing that gets that wrong is worse than none."""
    y = 430.0
    p = [ground(560), L(120, y, 880, y, "l"), L(120, y + 26, 880, y + 26, "l"),
         hatch(126, y + 26, 748, 20, drop=22),
         ('<g class="anim-skid">'
          + R(300, y - 150, 400, 138, "l") + hatch(306, y - 146, 388, 14, drop=130)
          + L(360, y - 150, 360, y - 178, "f") + L(640, y - 150, 640, y - 178, "f")
          + P("M %.1f %.1f L %.1f %.1f" % (360, y - 178, 640, y - 178), "f")
          + "".join(C(x, y - 6, 12, "l anim-roll") + C(x, y - 6, 4, "f anim-roll")
                    for x in (340.0, 420.0, 500.0, 580.0, 660.0))
          + '</g>'),
         dim_h(120, 880, 530), crosshair(180, 220), crosshair(820, 250)]
    css = """
    .anim-skid { animation: skid 12s ease-in-out infinite; }
    @keyframes skid {
      0%   { transform: translateX(-150px); }
      55%  { transform: translateX(150px); }
      70%  { transform: translateX(150px); }
      100% { transform: translateX(-150px); }
    }"""
    return p, css


def quality_control():
    """A dial indicator with a tolerance band on the face. The needle comes up,
    settles inside the band and stays there."""
    cx, cy, r = 500.0, 290.0, 170.0
    import math
    ticks = []
    for i in range(24):
        a = math.radians(i * 15 - 90)
        ticks.append(L(cx + (r - 16) * math.cos(a), cy + (r - 16) * math.sin(a),
                       cx + r * math.cos(a), cy + r * math.sin(a),
                       "f" if i % 3 else "l"))
    p = [ground(560), L(cx, cy + r, cx, 560, "f"), L(cx - 70, 560, cx + 70, 560, "l"),
         C(cx, cy, r, "l"), C(cx, cy, r - 30, "ff dash")] + ticks + [
         # the tolerance band, as an arc between two limits
         P("M %.1f %.1f A %.1f %.1f 0 0 1 %.1f %.1f"
           % (cx + (r - 8) * math.cos(math.radians(-36)),
              cy + (r - 8) * math.sin(math.radians(-36)), r - 8, r - 8,
              cx + (r - 8) * math.cos(math.radians(-6)),
              cy + (r - 8) * math.sin(math.radians(-6))), "l"),
         C(cx, cy, 9, "l"),
         ('<g class="anim-hand">' + L(cx, cy, cx, cy - r + 34, "l") + '</g>'),
         crosshair(200, 180), crosshair(810, 400)]
    css = """
    .anim-hand { transform-box: view-box; transform-origin: 500px 290px;
                 animation: gauge 7s cubic-bezier(.4,0,.2,1) infinite; }
    @keyframes gauge {
      0%, 8%   { transform: rotate(-96deg); }
      40%      { transform: rotate(74deg); }
      48%      { transform: rotate(58deg); }
      56%, 92% { transform: rotate(66deg); }
      100%     { transform: rotate(-96deg); }
    }"""
    return p, css


def ship_repair():
    """A hull section sat on keel blocks in dock, with the cropped plate going
    back in. Repair is a patch landing in a hole, so that is what moves."""
    p = [ground(560),
         # dock floor and blocks
         ] + [R(x, 470, 54, 60, "f") for x in (300.0, 420.0, 540.0, 660.0)] + [
         # hull section
         P("M 220 200 L 780 200 L 760 400 Q 500 500 240 400 Z", "l"),
         hatch(240, 206, 520, 18, drop=26),
         L(220, 250, 780, 250, "f"), L(240, 330, 760, 330, "f"),
         # the hole and the patch that fills it
         P("M 430 300 L 560 300 L 560 372 L 430 372 Z", "f dash"),
         ('<g class="anim-patch">' + R(430, 300, 130, 72, "l")
          + hatch(434, 304, 122, 6, drop=64) + '</g>'),
         dim_h(430, 560, 420), crosshair(180, 180), crosshair(840, 300)]
    css = """
    .anim-patch { animation: patch 9s ease-in-out infinite; }
    @keyframes patch {
      0%, 10%  { transform: translate(-190px, -120px); opacity: 0; }
      22%      { opacity: 1; }
      55%, 100% { transform: translate(0, 0); opacity: 1; }
    }"""
    return p, css


def shipbuilding():
    """Frames going up on a keel line, one after another, because that is the
    order a hull is assembled in.

    Six frames at even width read as a comb: they were 148 wide on a 110 pitch
    and touched. A hull narrows fore and aft, so the frames do too, and the
    pitch is wider than the widest of them."""
    keel, top = 500.0, 200.0
    p = [ground(560), L(120, keel, 880, keel, "l"), L(150, keel - 26, 850, keel - 26, "f")]
    frames = [(190.0, 40.0), (320.0, 64.0), (450.0, 76.0),
              (580.0, 76.0), (710.0, 62.0), (830.0, 38.0)]
    for i, (x, hw) in enumerate(frames):
        d = ("M %.1f %.1f L %.1f %.1f Q %.1f %.1f %.1f %.1f L %.1f %.1f"
             % (x - hw, top, x - hw * 0.86, keel - 40, x, keel, x + hw * 0.86, keel - 40,
                x + hw, top))
        p.append(P(d, "l anim-frame f%d" % i, ' pathLength="1"'))
        p.append(L(x, top, x, keel, "ff dashdot"))
    # the sheer line, drawn last, tying the frames into a hull
    p.append(P("M %.1f %.1f Q %.1f %.1f %.1f %.1f"
               % (150, top + 18, keel, top - 34, 870, top + 18),
               "f anim-frame f6", ' pathLength="1"'))
    p += [dim_h(190, 830, 545), crosshair(160, 260), crosshair(870, 300)]
    css = [draws_itself("anim-frame", 11, hold=0.4)]
    for i in range(7):
        css.append(".f%d { animation-delay: %.2fs; }" % (i, i * 0.7))
    return p, "\n    ".join(css)


def company():
    """A vernier caliper closing on a round section. The company page is about
    how the work is checked, and this is the instrument that says so without a
    word of copy."""
    y = 300.0
    p = [ground(560),
         # the workpiece
         C(520, y, 96, "l"), C(520, y, 62, "f"), crosshair(520, y, 120, "ff"),
         # beam and fixed jaw
         R(160, y - 12, 620, 24, "l"),
         P("M %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f Z"
           % (160, y - 12, 190, y - 12, 190, y - 150, 172, y - 150)),
         P("M %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f Z"
           % (160, y + 12, 190, y + 12, 190, y + 150, 172, y + 150)),
         # the graduations
         ] + [L(210 + i * 22, y - 12, 210 + i * 22, y - (26 if i % 5 else 36), "f")
              for i in range(24)] + [
         # sliding jaw
         ('<g class="anim-jaw">'
          + R(690, y - 40, 40, 80, "l", rx=3)
          + P("M %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f Z"
              % (690, y - 12, 660, y - 12, 660, y - 150, 678, y - 150))
          + P("M %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f Z"
              % (690, y + 12, 660, y + 12, 660, y + 150, 678, y + 150))
          + '</g>'),
         dim_h(190, 660, y + 200), crosshair(880, 190)]
    css = """
    .anim-jaw { animation: jaw 8s cubic-bezier(.4,0,.2,1) infinite; }
    @keyframes jaw {
      0%, 6%   { transform: translateX(80px); }
      40%, 60% { transform: translateX(-72px); }
      94%, 100% { transform: translateX(80px); }
    }"""
    return p, css


def projects():
    """A storage tank going up course by course, then the roof. Four of the five
    older cases on /projects are tank work, and this is how a tank is built:
    bottom course first, the next landed on top of it, the roof last.

    The first version drew each course as an open three-sided path and the
    result was a ladder of horizontal lines. A course is a closed ring of plate,
    so each one is a closed path now and traces its own perimeter."""
    x0, x1, base = 330.0, 690.0, 520.0
    cx = (x0 + x1) / 2
    ch, courses = 60.0, 5
    top = base - courses * ch
    p = [ground(560)]
    # a second tank standing off, to give the elevation a yard to stand in
    p += [R(760, 300, 160, 220, "ff"), P("M 760 300 Q 840 262 920 300", "ff"),
          L(760, 360, 920, 360, "ff"), L(760, 430, 920, 430, "ff")]
    for i in range(courses):
        yb = base - i * ch
        p.append(P("M %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f Z"
                   % (x0, yb, x0, yb - ch, x1, yb - ch, x1, yb),
                   "l anim-course c%d" % i, ' pathLength="1"'))
    # the roof, last as it is on site
    p.append(P("M %.1f %.1f Q %.1f %.1f %.1f %.1f" % (x0, top, cx, top - 74, x1, top),
               "l anim-course c5", ' pathLength="1"'))
    p += [# what makes it a tank rather than a box: a manway and a shell nozzle
          C(x0 + 66, base - 34, 22, "f"), C(x0 + 66, base - 34, 9, "ff"),
          R(x1, base - 130, 30, 26, "f"), L(x1 + 30, base - 130, x1 + 30, base - 104, "f"),
          L(cx, top - 74, cx, base, "ff dashdot"),
          dim_h(x0, x1, 552), crosshair(200, 220), crosshair(250, 330)]
    css = [draws_itself("anim-course", 12, hold=0.34)]
    for i in range(6):
        css.append(".c%d { animation-delay: %.2fs; }" % (i, i * 0.85))
    return p, "\n    ".join(css)



SUBJECTS = {
    "welding-services": welding_services,
    "pipe-fitting": pipe_fitting,
    "non-destructive-testing": non_destructive_testing,
    "3d-laser-scanning": laser_scanning,
    "rope-access-services": rope_access,
    "rigging-technical-support": rigging,
    "mechanical-contracting": mechanical_contracting,
    "mobile-repair-teams": mobile_repair,
    "heavy-equipment-relocation": heavy_relocation,
    "quality-control": quality_control,
    "ship-repair": ship_repair,
    "shipbuilding": shipbuilding,
    "company": company,
    "projects": projects,
}


def run(quiet=True):
    os.makedirs(OUTDIR, exist_ok=True)
    total = 0
    for slug, fn in sorted(SUBJECTS.items()):
        parts, css = fn()
        out = os.path.join(OUTDIR, slug + ".svg")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(svg(parts, css))
        total += os.path.getsize(out)
        if not quiet:
            print("  %-32s %5.1f KB" % (slug + ".svg", os.path.getsize(out) / 1024.0))
    return len(SUBJECTS), total


if __name__ == "__main__":
    n, total = run(quiet=False)
    print("  %d drawings, %.0f KB total" % (n, total / 1024.0))

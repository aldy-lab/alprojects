#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Draw the offshore wind field for /sectors/renewables.

Three machines standing in open water, in the same drawing language as the
hero's isometric pipe: outline only, one hairline weight, the cool grey-blue
the site already uses for its module, and no text -- text in an asset means a
translation key that no build step can see.

The rotors turn, each at its own rate: three locked in step read as a repeated
stamp, which is what they would be. The animation lives inside the file rather
than in the page, so the drawing can be referenced with a plain <img>: no
JavaScript, cached like any other asset, and `prefers-reduced-motion` is
honoured by the SVG's own media query rather than by anything the page has to
remember. The cost is the stroke colour, which has to be baked in instead of
taken from currentColor -- acceptable here, where the ground is dark on every
page.

One machine on its own measured 21% of the viewport at 1440 and read as a
small object adrift in a wide band. The horizontal element in this subject is
the sea, so the canvas is wide and the water runs the full width of it.

Everything is generated in one absolute coordinate space rather than by
nesting scale transforms. That is deliberate: the rotors spin with a CSS
transform about an explicit `transform-origin`, and an origin inside a
transformed group is the kind of thing that resolves differently between
engines. Python does the scaling; the SVG carries no transforms at all.

    python3 tools/make_wind_turbine.py      # writes assets/wind-turbine.svg
"""

import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "wind-turbine.svg")

W, H = 1000, 720
WATER_Y = 606.0
SEABED_Y = 686.0
STROKE = "185, 196, 216"        # the module's grey-blue; alpha is set per machine

# (centre x, scale, hub height above the water, seconds per revolution, alpha)
MACHINES = [
    (560.0, 1.00, 374.0, 26, 0.50),   # the near one
    (168.0, 0.46, 374.0, 34, 0.30),
    (854.0, 0.31, 374.0, 41, 0.22),
]

BLADE = [(-6.0, 16), (-9.0, 30), (-10.0, 45), (-9.5, 58), (-8.0, 100),
         (-5.0, 158), (-2.2, 186), (2.4, 186), (6.0, 158), (11.0, 100),
         (13.0, 58), (13.5, 45), (11.0, 30), (7.0, 16)]


def machine(cx, k, hub_h, idx):
    """One turbine in absolute coordinates, standing on the waterline.

    `k` scales the machine about its own waterline point, so each rotor sits at
    its own height and all three feet stay in the same sea.
    """
    hub_y = WATER_Y - hub_h * k
    r = 186.0 * k
    out = []
    add = out.append
    sx = lambda v: cx + v * k                       # noqa: E731
    sy = lambda v: WATER_Y + v * k                  # noqa: E731

    # swept circle and centreline
    add('<circle class="f%d dash" cx="%.1f" cy="%.1f" r="%.1f"/>' % (idx, cx, hub_y, r))
    add('<path class="f%d dashdot" d="M %.1f %.1f L %.1f %.1f"/>'
        % (idx, cx, hub_y - r - 26 * k, cx, sy(96)))

    # monopile, and the buried length drawn broken as on a section
    add('<path class="l%d" d="M %.1f %.1f L %.1f %.1f M %.1f %.1f L %.1f %.1f"/>'
        % (idx, sx(-24), sy(-34), sx(-24), sy(80), sx(24), sy(-34), sx(24), sy(80)))
    add('<path class="f%d dash" d="M %.1f %.1f L %.1f %.1f M %.1f %.1f L %.1f %.1f"/>'
        % (idx, sx(-24), sy(80), sx(-24), sy(106), sx(24), sy(80), sx(24), sy(106)))

    # transition piece, platform, railing, boat landing
    add('<rect class="l%d" x="%.1f" y="%.1f" width="%.1f" height="%.1f"/>'
        % (idx, sx(-34), sy(-58), 68 * k, 24 * k))
    add('<path class="l%d" d="M %.1f %.1f L %.1f %.1f"/>'
        % (idx, sx(-34), sy(-76), sx(34), sy(-76)))
    for i in range(5):
        add('<path class="f%d" d="M %.1f %.1f L %.1f %.1f"/>'
            % (idx, sx(-34 + i * 17), sy(-76), sx(-34 + i * 17), sy(-58)))
    for off in (38.0, 47.0):
        add('<path class="l%d" d="M %.1f %.1f L %.1f %.1f"/>'
            % (idx, sx(off), sy(-58), sx(off), sy(16)))
    for i in range(7):
        add('<path class="f%d" d="M %.1f %.1f L %.1f %.1f"/>'
            % (idx, sx(38), sy(-58 + i * 12), sx(47), sy(-58 + i * 12)))

    # tapered tower and the nacelle behind the hub
    add('<path class="l%d" d="M %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f"/>'
        % (idx, sx(-9.5), sy(-(hub_h - 16.0)), sx(-20), sy(-58),
           sx(20), sy(-58), sx(9.5), sy(-(hub_h - 16.0))))
    add('<rect class="l%d" x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f"/>'
        % (idx, cx - 25 * k, hub_y - 15 * k, 50 * k, 30 * k, 15 * k))

    # rotor
    spin = ['<g class="s%d">' % idx]
    for b in range(3):
        a = math.radians(b * 120.0)
        ca, sa = math.cos(a), math.sin(a)

        def place(off, rad, ca=ca, sa=sa):
            x, y = off * k, -rad * k
            return (cx + x * ca - y * sa, hub_y + x * sa + y * ca)

        xy = [place(o, rr) for o, rr in BLADE]
        d = "M %.1f %.1f " % xy[0]
        for i in range(1, len(xy) - 1, 2):
            d += "Q %.1f %.1f %.1f %.1f " % (xy[i] + xy[i + 1])
        d += "Q %.1f %.1f %.1f %.1f Z" % (xy[-1] + xy[0])
        spin.append('<path class="l%d" d="%s"/>' % (idx, d))
        spin.append('<path class="f%d" d="M %.1f %.1f L %.1f %.1f"/>'
                    % ((idx,) + place(0, 22) + place(0, 178)))
    spin.append("</g>")
    add("\n  ".join(spin))
    add('<circle class="l%d" cx="%.1f" cy="%.1f" r="%.1f"/>' % (idx, cx, hub_y, 13 * k))
    add('<circle class="f%d" cx="%.1f" cy="%.1f" r="%.1f"/>' % (idx, cx, hub_y, 5.5 * k))
    return "\n  ".join(out), hub_y


def build():
    parts, css = [], []

    # the sea first, so every machine stands in front of it
    parts.append('<path class="l0" d="M 6 %.1f L %d %.1f"/>' % (WATER_Y, W - 6, WATER_Y))
    for i in range(18):
        parts.append('<path class="f0" d="M %.1f %.1f q 9 -5 18 0"/>'
                     % (18 + i * 55, WATER_Y + 14))
    parts.append('<path class="f0 dash" d="M 6 %.1f L %d %.1f"/>'
                 % (SEABED_Y, W - 6, SEABED_Y))
    for i in range(30):
        parts.append('<path class="f0" d="M %.1f %.1f l -9 12"/>' % (14 + i * 33, SEABED_Y))
    css.append(".l0 { stroke: rgba(%s, 0.42); }\n    .f0 { stroke: rgba(%s, 0.18); }"
               % (STROKE, STROKE))

    # smallest first, so the near machine overlaps the ones standing off
    for idx, (cx, k, hub_h, turn, alpha) in enumerate(
            sorted(MACHINES, key=lambda m: m[1]), start=1):
        svg, hub_y = machine(cx, k, hub_h, idx)
        parts.append(svg)
        css.append(
            ".l%d { stroke: rgba(%s, %.2f); }\n    .f%d { stroke: rgba(%s, %.2f); }\n"
            "    .s%d { transform-box: view-box; transform-origin: %.1fpx %.1fpx;\n"
            "           animation: turbine-spin %ds linear infinite; }"
            % (idx, STROKE, alpha, idx, STROKE, alpha * 0.45, idx, cx, hub_y, turn))

    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d"
     width="%d" height="%d" role="img" aria-label="">
  <style>
    path, circle, rect { fill: none; stroke-width: 1.2;
                         stroke-linecap: round; stroke-linejoin: round; }
    .dash    { stroke-dasharray: 5 7; }
    .dashdot { stroke-dasharray: 14 5 2 5; }
    %s
    @keyframes turbine-spin { to { transform: rotate(360deg); } }
    @media (prefers-reduced-motion: reduce) {
      .s1, .s2, .s3 { animation: none; }
    }
  </style>
  %s
</svg>
''' % (W, H, W, H, "\n    ".join(css), "\n  ".join(parts))


if __name__ == "__main__":
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(build())
    print("  wrote %s (%.1f KB)"
          % (os.path.relpath(OUT, ROOT), os.path.getsize(OUT) / 1024.0))

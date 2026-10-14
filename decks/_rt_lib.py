# -*- coding: utf-8 -*-
# Библиотека деки «Маршрутизация»: изумрудно-золотой стиль, компоненты, генератор топологий, исполнитель сценариев.
import base64, io, json, math, pathlib, re, html, zipfile
from PIL import Image

HERE = pathlib.Path(__file__).parent
PPTX = pathlib.Path(r"C:/Users/anank/Downloads/2_4.pptx")
FONTS = HERE.parent / "шрифты" / "Кириллица"

# ---------------------------------------------------------------- assets
def _media(name):
    return Image.open(io.BytesIO(zipfile.ZipFile(PPTX).read("ppt/media/" + name))).convert("RGB")

def b64(im, q=80, fmt="WEBP"):
    b = io.BytesIO(); im.save(b, fmt, quality=q, method=6)
    return f"data:image/{fmt.lower()};base64," + base64.b64encode(b.getvalue()).decode()

def pic(name, box=None, w=1100, q=82):
    im = _media(name)
    if box: im = im.crop(box)
    if im.width > w: im = im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
    return b64(im, q)

def _font(fname):
    from fontTools import subset
    opts = subset.Options(); opts.flavor = "woff2"; opts.layout_features = ["kern", "liga"]
    f = subset.load_font(str(FONTS / fname), opts)
    s = subset.Subsetter(opts)
    s.populate(unicodes=list(range(0x20, 0x7F)) + list(range(0xA0, 0xBC)) + [0x401, 0x451, 0x2116, 0xD7, 0x2264, 0x2265]
               + list(range(0x410, 0x450)) + list(range(0x2010, 0x2027)))
    s.subset(f); b = io.BytesIO(); subset.save_font(f, b, opts)
    return base64.b64encode(b.getvalue()).decode()

def esc(s): return html.escape(s, quote=False)

def rich(s):
    """<g>..</g> золото, <t>..</t> бирюза, <c>..</c> моноширинный фрагмент, <w>..</w> белый жирный."""
    if s is None: return ""
    for a, b in (("g", '<b class="gd">'), ("t", '<b class="tl">'), ("w", '<b class="wh">')):
        s = s.replace(f"<{a}>", b).replace(f"</{a}>", "</b>")
    return s.replace("<c>", '<code class="c">').replace("</c>", "</code>")

# ---------------------------------------------------------------- icons (контурные, золото)
def _i(d, cls="ic"): return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{d}</svg>'
ICON = {
    "book": _i('<path d="M3 5.5C6 4 9 4 12 6c3-2 6-2 9-.5V19c-3-1.5-6-1.5-9 .5-3-2-6-2-9-.5z"/><path d="M12 6v13.5"/>'),
    "gear": _i('<circle cx="12" cy="12" r="3.2"/><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5.3 5.3l2.1 2.1M16.6 16.6l2.1 2.1M5.3 18.7l2.1-2.1M16.6 7.4l2.1-2.1"/>'),
    "tree": _i('<circle cx="12" cy="5" r="2.4"/><circle cx="5.5" cy="18.5" r="2.4"/><circle cx="18.5" cy="18.5" r="2.4"/><path d="M12 7.4v4.6M12 12l-5.3 4.3M12 12l5.3 4.3"/>'),
    "bars": _i('<path d="M5 20v-6M10 20V9M15 20v-8M20 20V5M3 20h19"/>'),
    "globe": _i('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>'),
    "doc": _i('<path d="M6 2.5h8l4.5 4.5v14.5H6z"/><path d="M14 2.5V7h4.5M9 11h6.5M9 14.5h6.5M9 18h4"/>'),
    "lamp": _i('<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.3 1 2.1h5c0-.8.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>'),
    "warn": _i('<path d="M12 3.5 2.5 20h19z"/><path d="M12 10v4.5M12 17.3v.2"/>'),
    "route": _i('<circle cx="5" cy="18" r="2.2"/><circle cx="19" cy="6" r="2.2"/><path d="M7 18h7a3.5 3.5 0 0 0 0-7h-4a3.5 3.5 0 0 1 0-7h7"/>'),
    "table": _i('<rect x="3" y="4" width="18" height="16" rx="1.5"/><path d="M3 9h18M3 14h18M9 9v11"/>'),
    "cpu": _i('<rect x="6" y="6" width="12" height="12" rx="1.5"/><rect x="9.5" y="9.5" width="5" height="5"/><path d="M9 2.5V6M15 2.5V6M9 18v3.5M15 18v3.5M2.5 9H6M2.5 15H6M18 9h3.5M18 15h3.5"/>'),
    "shield": _i('<path d="M12 2.5 4.5 5.5V11c0 5 3.2 8.6 7.5 10.5 4.3-1.9 7.5-5.5 7.5-10.5V5.5z"/><path d="m8.5 12 2.5 2.5 4.5-5"/>'),
    "clock": _i('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>'),
    "layers": _i('<path d="m12 3 9.5 5-9.5 5-9.5-5z"/><path d="m2.5 12.5 9.5 5 9.5-5M2.5 16.5l9.5 5 9.5-5"/>'),
    "split": _i('<path d="M3 12h6l4-6h8M13 18h8M9 12l4 6"/><path d="m18 3 3 3-3 3M18 15l3 3-3 3"/>'),
    "hop": _i('<circle cx="4.5" cy="12" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="19.5" cy="12" r="2"/><path d="M6.5 12h3.5M14 12h3.5"/>'),
    "speed": _i('<path d="M4 17a8 8 0 1 1 16 0"/><path d="m12 17 4-6"/><circle cx="12" cy="17" r="1.3"/>'),
    "check": _i('<circle cx="12" cy="12" r="9"/><path d="m7.5 12.5 3 3 6-6.5"/>'),
    "cross": _i('<circle cx="12" cy="12" r="9"/><path d="m8.5 8.5 7 7M15.5 8.5l-7 7"/>'),
    "link": _i('<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>'),
    "star": _i('<path d="m12 3 2.7 5.6 6.1.8-4.5 4.3 1.1 6.1L12 17l-5.4 2.8 1.1-6.1-4.5-4.3 6.1-.8z"/>'),
    "search": _i('<circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5"/>'),
    "term": _i('<rect x="2.5" y="4" width="19" height="16" rx="1.5"/><path d="m6.5 9 3.5 3-3.5 3M12 15.5h5"/>'),
    "drop": _i('<path d="M4 7h16M9 7V4.5h6V7M6 7l1 13.5h10L18 7"/><path d="M10 11v6M14 11v6"/>'),
    "loop": _i('<path d="M20 12a8 8 0 1 1-2.3-5.6"/><path d="M20 4v4.5h-4.5"/>'),
    "up": _i('<circle cx="12" cy="12" r="9"/><path d="M12 16.5v-9M8 11l4-4 4 4"/>'),
}

# ---------------------------------------------------------------- компоненты
def head(title, sub=None, left=False, small=False):
    cls = "sh" + (" l" if left else "") + (" s" if small else "")
    s = f'<p class="sub">{rich(sub)}</p>' if sub else ""
    return f'<header class="{cls}"><h2 class="gt">{title}</h2><div class="orn" aria-hidden="true"><i></i><b></b><i></i></div>{s}</header>'

def P(*paras, cls="p"):
    return "".join(f'<p class="{cls}" data-s="1">{rich(t)}</p>' for t in paras)

def bl(items, cls=""):
    return f'<ul class="bl {cls}">' + "".join(f'<li data-s="1">{rich(t)}</li>' for t in items) + '</ul>'

def ol(items, cls=""):
    return f'<ol class="ol {cls}">' + "".join(f'<li data-s="1"><span class="nc sm">{k+1}</span><div>{rich(t)}</div></li>' for k, t in enumerate(items)) + '</ol>'

def pn(body, cls="", title=None, icon=None):
    t = ""
    if title or icon:
        ic = f'<span class="ico">{ICON[icon]}</span>' if icon else ""
        t = f'<div class="ph">{ic}' + (f'<h3>{title}</h3>' if title else "") + '</div>'
    return f'<div class="pn {cls}" data-s="1">{t}{body}</div>'

def ncard(n, text, cls="", title=None):
    t = f'<h3>{title}</h3>' if title else ""
    return f'<div class="pn nk {cls}" data-s="1"><span class="nc">{n}</span><div>{t}<p>{rich(text)}</p></div></div>'

def icard(icon, text, title=None, teal=False, cls=""):
    t = f'<h3>{title}</h3>' if title else ""
    return (f'<div class="pn ik {"teal" if teal else ""} {cls}" data-s="1"><span class="ico big">{ICON[icon]}</span>'
            f'<div>{t}<p>{rich(text)}</p></div></div>')

def banner(text, icon="lamp"):
    return f'<div class="ban" data-s="1"><div class="bi"><span class="ico">{ICON[icon]}</span><span class="bt">{rich(text)}</span></div></div>'

def grid(*cells, cols=None, cls=""):
    st = f' style="grid-template-columns:{cols}"' if cols else ""
    return f'<div class="gr {cls}"{st}>' + "".join(cells) + '</div>'

def table(caption, header, rows, tid=None, hl=None, cls="", fx=()):
    """rows: список списков; строка '...' — многоточие на все колонки. fx — номера строк (с 1), скрытых до сценария."""
    idt = f' id="{tid}"' if tid else ""
    cap = f'<caption>{rich(caption)}</caption>' if caption else ""
    th = "".join(f'<th>{rich(h)}</th>' for h in header)
    body = []
    for k, r in enumerate(rows, 1):
        c = []
        if k == hl: c.append("hl")
        if k in fx: c.append("fx")
        ca = f' class="{" ".join(c)}"' if c else ""
        if r == "...":
            body.append(f'<tr data-r="{k}" class="dots{" fx" if k in fx else ""}"><td colspan="{len(header)}">. . .</td></tr>')
        else:
            body.append(f'<tr data-r="{k}"{ca}>' + "".join(f'<td>{rich(str(x))}</td>' for x in r) + '</tr>')
    return f'<div class="tw {cls}" data-s="1"><table class="rt"{idt}>{cap}<thead><tr>{th}</tr></thead><tbody>{"".join(body)}</tbody></table></div>'

_CODE = re.compile(r"^(\s*)([CSROBi]\*?|[CSROBi] \*|[CSROBi]\s+\*|O E1\*|O IA)(\s)")
def con(text, title=None, cls="", hl=()):
    """Консоль ESR/Windows. Строки с номерами из hl подсвечиваются золотом. Код источника маршрута — золотом."""
    out = []
    for k, ln in enumerate(text.strip("\n").split("\n"), 1):
        e = esc(ln)
        m = re.match(r"^(\S+[#>])(\s?)(.*)$", ln)
        if m and (m.group(1).endswith("#") or m.group(1).endswith(">")) and not ln.startswith(" "):
            e = f'<span class="cp">{esc(m.group(1))}</span>{m.group(2)}<span class="cc">{esc(m.group(3))}</span>'
        else:
            e = re.sub(r"^(\s*)([CSROBi])(\s+\*?\s)", lambda mm: f'{mm.group(1)}<b class="cd">{mm.group(2)}</b>{mm.group(3)}', e)
        out.append(f'<span class="cl{" h" if k in hl else ""}">{e}</span>')
    t = f'<div class="ct"><i></i><i></i><i></i><span>{esc(title)}</span></div>' if title else ""
    return f'<div class="con {cls}" data-s="1">{t}<pre>{"".join(out)}</pre></div>'

def photo(src, cap="", cls=""):
    c = f'<figcaption>{rich(cap)}</figcaption>' if cap else ""
    return f'<figure class="fig {cls}" data-s="1"><img src="{src}" alt="{esc(re.sub("<[^>]+>", "", cap))}" loading="lazy">{c}</figure>'

def qa(q, a):
    return (f'<div class="qa pn" data-s="1"><button type="button" class="qq"><span class="qn">?</span><span>{rich(q)}</span></button>'
            f'<div class="qans">{rich(a)}</div></div>')

# ---------------------------------------------------------------- топологии: данные для JS-генератора
TOPO = {}
def topo(tid, spec, cls=""):
    TOPO[tid] = spec
    return f'<div class="topo {cls}" data-s="1" data-topo="{tid}"></div>'

DEV = {}
def host(key, name, ip, mask, mac, gw, port="eth0", arp=(), kind="Компьютер"):
    net = ".".join(ip.split(".")[:3]) + ".0"
    DEV[key] = {"n": name, "k": kind, "if": [[port, f"{ip}/{mask}", mac, "up"]], "gw": gw,
                "arp": [list(a) for a in arp],
                "rt": [["0.0.0.0/0", gw, port], [f"{net}/{mask}", "on-link", port]]}
def rtr(key, name, ifs, arp=(), rt=(), kind="Маршрутизатор"):
    DEV[key] = {"n": name, "k": kind, "if": [list(i) for i in ifs], "arp": [list(a) for a in arp], "rt": [list(r) for r in rt]}
def swt(key, name, ports, mact, kind="Коммутатор (L2)"):
    DEV[key] = {"n": name, "k": kind, "if": [[p, "—", m, "up"] for p, m in ports], "mac": [list(x) for x in mact]}

def scn(body):
    """Контейнер, который сценарий возвращает в исходное состояние при каждом показе."""
    return f'<div class="scn">{body}</div>'

# ---------------------------------------------------------------- slides registry
S = []
def slide(label, body, cls="", tl=None):
    S.append((label, body, cls, tl))

# ---------------------------------------------------------------- CSS
CSS = r"""
@font-face{font-family:"PT Serif";src:url(data:font/woff2;base64,__F_REG__) format("woff2");font-weight:400;font-display:swap}
@font-face{font-family:"PT Serif";src:url(data:font/woff2;base64,__F_BOLD__) format("woff2");font-weight:700;font-display:swap}
:root{--emerald-2:#061a16;--emerald:#0a2620;--panel:rgba(8,38,32,.72);--gold:#e8c87a;--gold-2:#f5e3b0;--gold-dim:#a98b46;
  --teal:#4fd6c4;--ink:#f2ece0;--dim:#bcc9bf;--line:rgba(232,200,122,.62);
  --f:"PT Serif","Georgia","Times New Roman",serif;--mono:"Cascadia Mono","Consolas","DejaVu Sans Mono",ui-monospace,monospace;
  --ez:cubic-bezier(.22,.7,.3,1);color-scheme:dark}
*{box-sizing:border-box;margin:0;padding:0}
[hidden]{display:none!important}
html{font-size:clamp(15px,min(1.28vw,2.35vh),34px)}
html,body{height:100%;overflow:hidden;color:var(--ink);font-family:var(--f)}
body{background:radial-gradient(60% 55% at 72% 18%,#0f3a30 0%,rgba(15,58,48,0) 70%),radial-gradient(45% 45% at 12% 70%,#0b3029 0%,rgba(11,48,41,0) 70%),var(--emerald-2)}
b{font-weight:700}.gd{color:var(--gold)}.tl{color:var(--teal)}.wh{color:#fff}
code.c{font-family:var(--mono);font-size:.9em;color:var(--gold-2);background:rgba(232,200,122,.08);border:1px solid rgba(232,200,122,.22);border-radius:4px;padding:0 .3em;white-space:nowrap}
/* ---- фон ---- */
#deco{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
#deco .globe{position:absolute;right:-18vw;top:-40vh;width:78vw;height:78vw;border-radius:50%;
  background:radial-gradient(circle at 40% 35%,rgba(40,110,90,.35),rgba(10,40,34,.2) 55%,rgba(6,26,22,0) 70%);
  box-shadow:inset 0 0 0 1px rgba(232,200,122,.10),0 0 80px rgba(232,200,122,.05)}
#deco svg{position:absolute;inset:0;width:100%;height:100%}
#deco .th{fill:none;stroke-linecap:round}
#deco .sweep{fill:none;stroke-linecap:round;stroke:#fff6d8;opacity:.55;stroke-dasharray:140 2400;animation:swp 14s linear infinite}
@keyframes swp{from{stroke-dashoffset:2540}to{stroke-dashoffset:0}}
#deco .spk{animation:twk 6s ease-in-out infinite}
@keyframes twk{0%,100%{opacity:.25;transform:scale(.85)}50%{opacity:1;transform:scale(1.15)}}
#deco .aur{position:absolute;inset:-12%;filter:blur(2px)}
#deco .aur i{position:absolute;display:block;border-radius:50%;mix-blend-mode:screen;opacity:.5;animation:drift 38s ease-in-out infinite alternate}
#deco .aur i:nth-child(1){left:4%;top:8%;width:46vw;height:46vw;background:radial-gradient(circle,rgba(36,120,98,.5),rgba(36,120,98,0) 68%)}
#deco .aur i:nth-child(2){right:2%;bottom:4%;width:52vw;height:52vw;background:radial-gradient(circle,rgba(176,138,58,.3),rgba(176,138,58,0) 66%);animation-duration:52s;animation-delay:-8s}
#deco .aur i:nth-child(3){left:38%;top:44%;width:38vw;height:38vw;background:radial-gradient(circle,rgba(79,214,196,.18),rgba(79,214,196,0) 70%);animation-duration:64s;animation-delay:-20s}
@keyframes drift{from{transform:translate3d(0,0,0) scale(1)}to{transform:translate3d(5vw,-4vh,0) scale(1.12)}}
#deco .orna{position:absolute;inset:0;opacity:.07;
  background-image:repeating-linear-gradient(45deg,rgba(232,200,122,.8) 0 1px,transparent 1px 46px),repeating-linear-gradient(-45deg,rgba(232,200,122,.55) 0 1px,transparent 1px 46px);
  -webkit-mask-image:radial-gradient(130% 95% at 50% 40%,#000 18%,transparent 72%);mask-image:radial-gradient(130% 95% at 50% 40%,#000 18%,transparent 72%)}
#deco .vig{position:absolute;inset:0;background:radial-gradient(118% 88% at 50% 42%,rgba(0,0,0,0) 52%,rgba(2,12,10,.62) 100%)}
#deco .lay{position:absolute;inset:0;width:100%;height:100%}
#deco .leaves{display:none}
#deco .leaves svg{width:100%;height:100%;display:block}
#deco .lf{transform-box:fill-box;transform-origin:center;will-change:transform}
#deco .lf path{fill:rgba(118,194,152,.55);stroke:rgba(178,236,200,.5);stroke-width:.8}
#deco .lf.b path{fill:rgba(232,200,122,.42);stroke:rgba(245,227,176,.5)}
#deco .lf .vn{fill:none;stroke:rgba(10,38,32,.5);stroke-width:.9}
#deco .leaves svg>g{animation:fall var(--d,40s) linear var(--dl,0s) infinite}
@keyframes fall{
  from{transform:translate(var(--x),-240px) rotate(0deg) scale(var(--s))}
  50%{transform:translate(calc(var(--x) + var(--sw)),540px) rotate(200deg) scale(var(--s))}
  to{transform:translate(var(--x),1320px) rotate(420deg) scale(var(--s))}
}
#deco .mal,#deco .cont,#deco .rings,#deco .net,#deco .rays{display:none}
#deco .net .nl line{stroke:rgba(232,200,122,.4);stroke-width:1.2}
#deco .net .nd circle{fill:#f5e3b0;opacity:.75;animation:twk 7s ease-in-out infinite}
#deco .cont polyline{fill:none;stroke:rgba(149,226,196,.8);stroke-width:1.7}
#deco .rings .rg circle{fill:none;stroke:rgba(232,200,122,.62);stroke-width:1.1}
#deco .rings .ry line{stroke:rgba(232,200,122,.24);stroke-width:1}
#deco .rays{background:repeating-linear-gradient(104deg,rgba(232,200,122,.1) 0 2px,transparent 2px 13px,rgba(79,214,196,.07) 13px 15px,transparent 15px 54px);
  -webkit-mask-image:radial-gradient(120% 100% at 80% 0%,#000 10%,transparent 78%);mask-image:radial-gradient(120% 100% at 80% 0%,#000 10%,transparent 78%)}
#deco .ph{position:absolute;inset:0;background-size:cover;background-position:center;opacity:0;transition:opacity .6s var(--ez)}
/* 1 — чистое зелёное полотно с листопадом */
body[data-bg="1"] #deco .ph.pclean{opacity:1}
body[data-bg="1"] #deco .leaves{display:block}
body[data-bg="1"] #deco .globe{opacity:.35}
body[data-bg="1"] #deco .orna{opacity:.03}
/* 2 — звёздное небо с сетью и городами */
body[data-bg="2"] #deco .ph.psky{opacity:1}
body[data-bg="2"] #deco .globe,body[data-bg="2"] #deco .orna,body[data-bg="2"] #deco .aur{display:none}
/* 3 — чистое полотно с изолиниями */
body[data-bg="3"] #deco .ph.pclean{opacity:1}
body[data-bg="3"] #deco .cont{display:block;opacity:.6}
body[data-bg="3"] #deco .globe{opacity:.4;right:-16vw;top:auto;bottom:-56vh}
body[data-bg="3"] #deco .orna{display:none}
/* 4 — чистое полотно с гильошем */
body[data-bg="4"] #deco .ph.pclean{opacity:1}
body[data-bg="4"] #deco .rings{display:block;opacity:.8}
body[data-bg="4"] #deco .globe{display:none}
body[data-bg="4"] #deco .orna{opacity:.035;background-image:repeating-linear-gradient(0deg,rgba(232,200,122,.6) 0 1px,transparent 1px 58px)}
/* 5 — глобус и золотые потоки */
body[data-bg="5"] #deco .ph.pglobe{opacity:1}
body[data-bg="5"] #deco .globe,body[data-bg="5"] #deco .orna,body[data-bg="5"] #deco .aur{display:none}
/* 6 — малахитовые волны на чистом полотне */
body[data-bg="6"] #deco .ph.pclean{opacity:1}
body[data-bg="6"] #deco .mal{display:block;opacity:.6}
body[data-bg="6"] #deco .leaves{display:block;opacity:.45}
body[data-bg="6"] #deco .globe{opacity:.3;right:-34vw;top:10vh}
body[data-bg="6"] #deco .orna{display:none}
/* на фотоподложках приглушаем нарисованные нити и виньетку */
body[data-bg="2"] #deco .thr,body[data-bg="5"] #deco .thr{opacity:.35}
body[data-bg="2"] #deco .vig,body[data-bg="5"] #deco .vig{background:radial-gradient(120% 92% at 50% 42%,rgba(0,0,0,0) 40%,rgba(2,14,11,.72) 100%)}
@media (prefers-reduced-motion: reduce){#deco .aur i,#deco .spk,#deco .sweep,#deco .leaves svg>g{animation:none}}
#frame{position:fixed;inset:10px;z-index:20;pointer-events:none;border:1px solid rgba(232,200,122,.32);border-radius:4px}
#frame i{position:absolute;width:76px;height:76px;border:2px solid var(--gold);filter:drop-shadow(0 0 5px rgba(232,200,122,.5))}
#frame i:nth-child(1){left:-3px;top:-3px;border-right:0;border-bottom:0}
#frame i:nth-child(2){right:-3px;bottom:-3px;border-left:0;border-top:0}
#frame i::after{content:"";position:absolute;width:7px;height:7px;border:1px solid var(--gold);transform:rotate(45deg)}
#frame i:nth-child(1)::after{left:10px;top:10px}#frame i:nth-child(2)::after{right:10px;bottom:10px}
#prog{position:fixed;left:10px;right:10px;top:10px;height:2px;z-index:21;background:rgba(232,200,122,.1)}
#prog i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--gold-dim),var(--gold-2));transition:width .4s var(--ez)}
/* ---- слайды ---- */
main{position:fixed;inset:0;z-index:2}
.slide{position:absolute;inset:0;visibility:hidden;opacity:0;transition:opacity .45s var(--ez),visibility 0s .45s}
.slide.on{visibility:visible;opacity:1;transition:opacity .45s var(--ez)}
.sc{position:absolute;inset:0;overflow:auto;padding:1.4rem 2rem 4.4rem;scrollbar-width:thin;scrollbar-color:var(--gold-dim) transparent}
.wrap{max-width:min(2240px,99%);margin:0 auto;min-height:100%;display:flex;flex-direction:column;justify-content:center;gap:.85rem}
[data-s]{opacity:0;transform:translateY(9px);transition:opacity .3s var(--ez),transform .3s var(--ez);transition-delay:var(--dl,0ms)}
.slide.ni [data-s]{transition:none}
[data-s].in{opacity:1;transform:none}
/* ---- заголовок ---- */
.sh{text-align:center}
.gt{font-size:3.05rem;line-height:1.08;font-weight:700;text-transform:uppercase;letter-spacing:.005em;
  background:linear-gradient(180deg,#fff8e4 8%,#f5e3b0 36%,#e8c87a 62%,#9c7b36 100%);-webkit-background-clip:text;background-clip:text;color:transparent;
  filter:drop-shadow(0 2px 10px rgba(232,200,122,.28))}
.sh.s .gt{font-size:2.45rem}
.sh.l{text-align:left}.sh.l .orn{margin-left:0;width:min(46rem,70%)}
.orn{display:flex;align-items:center;gap:.7rem;width:min(62rem,72%);margin:.55rem auto 0}
.orn i{flex:1;height:1px;background:linear-gradient(90deg,rgba(232,200,122,0),var(--gold) 85%)}
.orn i:last-child{background:linear-gradient(270deg,rgba(232,200,122,0),var(--gold) 85%)}
.orn b{width:9px;height:9px;border:1px solid var(--gold);transform:rotate(45deg);position:relative;box-shadow:0 0 6px rgba(232,200,122,.5)}
.orn b::after{content:"";position:absolute;inset:2px;background:var(--gold);opacity:.55}
.sub{margin-top:.6rem;color:var(--dim);font-size:1.15rem;font-style:normal}
.orn.bot{width:min(40rem,60%);margin-top:.4rem}
/* ---- текст ---- */
.p{font-size:1.15rem;line-height:1.5;color:var(--ink);text-align:left;hyphens:auto}
.p+.p{margin-top:.55rem}
.pn .p{font-size:1.1rem}
.bl{list-style:none;display:grid;gap:.5rem}
.bl li{position:relative;padding-left:1.5rem;font-size:1.12rem;line-height:1.45}
.bl li::before{content:"";position:absolute;left:.2rem;top:.55em;width:7px;height:7px;border:1px solid var(--gold);transform:rotate(45deg);background:rgba(232,200,122,.35)}
.ol{list-style:none;display:grid;gap:.65rem}
.ol li{display:grid;grid-template-columns:auto 1fr;gap:.8rem;align-items:start;font-size:1.12rem;line-height:1.45}
/* ---- панели ---- */
.pn{position:relative;background:linear-gradient(180deg,rgba(11,46,39,.82),rgba(6,28,24,.82));border:1px solid var(--line);border-radius:12px;padding:.8rem 1.05rem;
  box-shadow:0 0 16px rgba(232,200,122,.10),inset 0 0 24px rgba(232,200,122,.06)}
.pn::before{content:"";position:absolute;inset:4px;border:1px solid rgba(232,200,122,.12);border-radius:9px;pointer-events:none}
.pn h3{font-size:1.28rem;color:var(--gold);margin-bottom:.35rem;line-height:1.2}
.pn p{font-size:1.08rem;line-height:1.45}
.ph{display:flex;align-items:center;gap:.7rem;margin-bottom:.5rem}.ph h3{margin:0}
.pn.teal{border-color:rgba(79,214,196,.7);box-shadow:0 0 16px rgba(79,214,196,.14),inset 0 0 24px rgba(79,214,196,.07)}
.pn.teal::before{border-color:rgba(79,214,196,.14)}.pn.teal h3{color:var(--teal)}
.pn.teal .ico{border-color:var(--teal);color:var(--teal)}
.nc{flex:none;display:inline-grid;place-items:center;width:2.7rem;height:2.7rem;border-radius:50%;border:1.5px solid var(--gold);color:var(--gold-2);
  font-weight:700;font-size:1.45rem;box-shadow:0 0 10px rgba(232,200,122,.35),inset 0 0 8px rgba(232,200,122,.18);background:rgba(6,26,22,.6)}
.nc.sm{width:2rem;height:2rem;font-size:1.05rem}
.nk{display:flex;gap:1rem;align-items:flex-start}
.ico{flex:none;display:inline-grid;place-items:center;width:2.6rem;height:2.6rem;border-radius:50%;border:1.3px solid var(--gold);color:var(--gold);box-shadow:0 0 8px rgba(232,200,122,.25)}
.ico.big{width:4.2rem;height:4.2rem}
.ic{width:56%;height:56%;fill:none;stroke:currentColor;stroke-width:1.4;stroke-linecap:round;stroke-linejoin:round}
.ik{display:flex;gap:1.1rem;align-items:center}
.gr{display:grid;gap:.85rem;grid-template-columns:repeat(auto-fit,minmax(18.5rem,1fr));align-items:stretch}
.two{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.35fr);gap:1.1rem;align-items:center}
.two.eq{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
.two.wide{grid-template-columns:minmax(0,1.5fr) minmax(0,1fr)}
.two.top{align-items:start}
.col{display:flex;flex-direction:column;gap:1rem}
/* ---- баннер ---- */
.ban{--c:polygon(1.6rem 0,calc(100% - 1.6rem) 0,100% 50%,calc(100% - 1.6rem) 100%,1.6rem 100%,0 50%);align-self:center;min-width:min(60rem,92%);
  padding:1.5px;background:linear-gradient(90deg,var(--gold-dim),var(--gold-2),var(--gold-dim));clip-path:var(--c);filter:drop-shadow(0 0 8px rgba(232,200,122,.35))}
.bi{clip-path:var(--c);background:linear-gradient(180deg,#0d3a31,#06201b);display:flex;align-items:center;justify-content:center;gap:1rem;padding:.55rem 3rem}
.bt{font-size:1.45rem;font-weight:700;background:linear-gradient(180deg,#fff8e4 10%,#f5e3b0 40%,#e8c87a 70%,#b08d44 100%);-webkit-background-clip:text;background-clip:text;color:transparent}
.ban .ico{width:2.6rem;height:2.6rem}
/* ---- таблица ---- */
.tw{background:linear-gradient(180deg,rgba(11,46,39,.85),rgba(6,28,24,.85));border:1px solid var(--line);border-radius:14px;padding:.7rem .8rem .9rem;
  box-shadow:0 0 18px rgba(232,200,122,.12),inset 0 0 24px rgba(232,200,122,.05);overflow-x:auto}
.rt{width:100%;border-collapse:collapse;font-size:1.14rem}
.rt caption{font-size:1.55rem;font-weight:700;padding:.2rem 0 .6rem;
  background:linear-gradient(180deg,#fff8e4 10%,#f5e3b0 40%,#e8c87a 72%,#a8853e 100%);-webkit-background-clip:text;background-clip:text;color:transparent}
.rt th,.rt td{border:1px solid rgba(232,200,122,.55);padding:.45rem .55rem;text-align:center;vertical-align:middle;line-height:1.25;overflow-wrap:anywhere}
.rt th{font-weight:400;color:var(--ink);background:rgba(232,200,122,.05)}
.rt td{color:var(--ink);transition:background .35s var(--ez),color .35s var(--ez),box-shadow .35s var(--ez),opacity .35s var(--ez)}
.rt tr.hl td{color:#fff;background:linear-gradient(90deg,rgba(232,200,122,.16),rgba(232,200,122,.42) 50%,rgba(232,200,122,.16));box-shadow:inset 0 0 18px rgba(232,200,122,.30)}
.rt tr.hl td:first-child{box-shadow:inset 0 0 18px rgba(232,200,122,.30),inset 3px 0 0 var(--gold-2)}
.rt tr.dots td{letter-spacing:.3em;color:var(--dim)}
.rt tr.fx{opacity:0;transform:translateY(-9px);transition:opacity .35s var(--ez),transform .35s var(--ez)}
.rt tr.fx.on{opacity:1;transform:none}
.rt tr.dim td{opacity:.32}
.rt tr.bad td{background:rgba(214,96,80,.2);box-shadow:inset 0 0 14px rgba(214,96,80,.35)}
.rt .col-on{background:rgba(232,200,122,.28)!important;color:#fff}
.tw.sm .rt{font-size:1.02rem}.tw.sm .rt caption{font-size:1.3rem}
.tw.left .rt td{text-align:left}
/* ---- консоль ---- */
.con{background:#03120e;border:1px solid rgba(232,200,122,.45);border-radius:10px;overflow:hidden;box-shadow:0 0 14px rgba(232,200,122,.08)}
.ct{display:flex;align-items:center;gap:.4rem;padding:.35rem .7rem;border-bottom:1px solid rgba(232,200,122,.25);background:rgba(232,200,122,.06);font-size:.85rem;color:var(--dim)}
.ct i{width:.55rem;height:.55rem;border-radius:50%;border:1px solid var(--gold-dim)}.ct span{margin-left:.4rem}
.con pre{font-family:var(--mono);font-size:.95rem;line-height:1.45;color:#d6e4da;padding:.7rem .9rem;overflow-x:auto;white-space:pre}
.cl{display:block;min-height:1.45em}.cl.h{background:rgba(232,200,122,.16);box-shadow:inset 3px 0 0 var(--gold);color:#fff}
.cp{color:var(--gold)}.cc{color:#fff;font-weight:700}.cd{color:var(--gold-2)}
/* ---- фото ---- */
.fig{border:1px solid var(--line);border-radius:12px;overflow:hidden;background:#fff;box-shadow:0 0 16px rgba(232,200,122,.12)}
.fig img{display:block;width:100%;height:auto}
.fig figcaption{background:#07211c;color:var(--dim);font-size:.9rem;padding:.4rem .8rem;border-top:1px solid rgba(232,200,122,.3)}
.fig.dark{background:#06201b}
/* ---- топология ---- */
.topo svg{display:block;width:100%;height:auto;overflow:visible;font-family:var(--f)}
.topo .fx{opacity:0;transition:opacity .45s var(--ez)}
.topo .fx.on{opacity:1}
.topo .dim{opacity:.22!important;transition:opacity .45s var(--ez)}
.topo .lk{stroke:rgba(232,200,122,.6);stroke-width:1.6;fill:none}
.topo .lk.d{stroke:rgba(232,200,122,.72);stroke-dasharray:7 6}
.topo .lk.w{stroke:rgba(236,244,240,.75);stroke-width:1.4}
.topo .lk.t{stroke:var(--teal);stroke-dasharray:9 7;stroke-width:2.4}
.topo .lk.r{stroke:#e0735f;stroke-dasharray:6 5}
.topo .lk.g{stroke:#f5d98a;stroke-width:3;filter:drop-shadow(0 0 4px rgba(245,217,138,.8))}
.topo .gp{fill:none;stroke:#f7dc8c;stroke-width:3.4;stroke-linecap:round;filter:drop-shadow(0 0 5px rgba(247,220,140,.95));opacity:0}
.topo .gp.t{stroke:var(--teal);filter:drop-shadow(0 0 4px rgba(79,214,196,.9))}
.topo .gp.r{stroke:#ef8c78;filter:drop-shadow(0 0 4px rgba(239,140,120,.8))}
.topo .ah{fill:#f7dc8c;opacity:0;transition:opacity .25s;filter:drop-shadow(0 0 4px rgba(247,220,140,.9))}
.topo .ah.t{fill:var(--teal)}.topo .ah.r{fill:#ef8c78}
.topo .ah.on{opacity:1}
.topo .tx{fill:var(--ink);font-size:16.5px}
.topo .tx.g{fill:var(--gold-2)}.topo .tx.t{fill:var(--teal)}.topo .tx.b{font-weight:700}.topo .tx.dm{fill:var(--dim)}.topo .tx.r{fill:#ef8c78}
.topo .tx.w{fill:#fff;font-weight:700}
.topo .lbl{fill:#fff;font-weight:700;font-size:18.5px}
.topo .cld path{fill:rgba(232,200,122,.10);stroke:var(--gold);stroke-width:1.3;filter:drop-shadow(0 0 6px rgba(232,200,122,.45))}
.topo .cld text{fill:#fff;font-weight:700;font-size:17px}
.topo .cld.hl path{fill:rgba(232,200,122,.28)}
.topo .area rect{fill:rgba(232,200,122,.035);stroke:rgba(232,200,122,.7);stroke-width:1.2}
.topo .area text{fill:var(--gold-2);font-weight:700;font-size:16px}
.topo .co rect{fill:rgba(6,30,25,.92);stroke:var(--gold);stroke-width:1.1}
.topo .co text{fill:#fff;font-size:15px}
.topo .co line{stroke:var(--gold);stroke-width:1}
.topo .tag polygon{fill:#f1c94b}.topo .tag text{fill:#10231e;font-weight:700;font-size:14px}
.topo .dot{fill:var(--gold);filter:drop-shadow(0 0 3px rgba(232,200,122,.9))}
.topo .dot.up{fill:#8fe07a;filter:drop-shadow(0 0 4px rgba(143,224,122,.9))}
.topo .ring{fill:rgba(143,224,122,.06);stroke:#8fe07a;stroke-width:1.6;filter:drop-shadow(0 0 5px rgba(143,224,122,.7))}
.topo .ring.g{fill:rgba(232,200,122,.08);stroke:var(--gold)}
.topo .ring.t{fill:rgba(79,214,196,.08);stroke:var(--teal)}
.topo .pkt{opacity:0;filter:drop-shadow(0 0 6px rgba(255,220,130,.95))}
.topo .pkt.on{opacity:1}
.topo .dev.hl .top{fill:#2a7a68}
.topo .dev.hl{filter:drop-shadow(0 0 10px rgba(247,220,140,.9))}
.topo .xx{stroke:#ef6b57;stroke-width:3;stroke-linecap:round}
.topo .bx rect{fill:rgba(6,30,25,.9);stroke:var(--line);stroke-width:1;rx:6}
/* ---- вопросы ---- */
.qa{padding:.75rem 1rem}
.qq{display:flex;gap:.8rem;align-items:center;width:100%;text-align:left;background:none;border:0;color:var(--ink);font:inherit;font-size:1.1rem;cursor:pointer}
.qn{flex:none;display:grid;place-items:center;width:2rem;height:2rem;border-radius:50%;border:1.3px solid var(--gold);color:var(--gold);font-weight:700}
.qans{max-height:0;overflow:hidden;opacity:0;transition:max-height .45s var(--ez),opacity .35s var(--ez),margin .35s;color:var(--gold-2);font-size:1.02rem;line-height:1.45;padding-left:2.8rem}
.qa.open .qans{max-height:20rem;opacity:1;margin-top:.5rem}
.qa.open .qn{background:var(--gold);color:#0a2620}
/* ---- титул ---- */
.title .wrap{align-items:center;text-align:center;gap:1.4rem}
.title .kick{font-size:1.1rem;letter-spacing:.32em;text-transform:uppercase;color:var(--gold)}
.title h1{font-size:5rem;line-height:1.05;font-weight:700;text-transform:uppercase;
  background:linear-gradient(180deg,#fff8e4 8%,#f5e3b0 36%,#e8c87a 62%,#9c7b36 100%);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 3px 14px rgba(232,200,122,.3))}
.title .au{display:flex;gap:2.2rem;justify-content:center;color:var(--dim);font-size:1.1rem;flex-wrap:wrap}
/* ---- навигация ---- */
#nav{position:fixed;z-index:25;left:50%;bottom:20px;transform:translateX(-50%);display:flex;align-items:center;gap:.35rem;padding:.3rem .45rem;
  background:rgba(6,26,22,.9);border:1px solid rgba(232,200,122,.45);border-radius:10px;box-shadow:0 0 14px rgba(0,0,0,.5)}
#nav button{display:inline-flex;align-items:center;gap:.4rem;background:none;border:1px solid transparent;color:var(--gold-2);font:inherit;font-size:.9rem;padding:.3rem .55rem;border-radius:7px;cursor:pointer}
#nav button:hover{border-color:rgba(232,200,122,.5);background:rgba(232,200,122,.08)}
#nav button:active{background:rgba(232,200,122,.18)}
#nav button:disabled{opacity:.3;cursor:default}
#nav svg{width:1.1rem;height:1.1rem;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
#nav .stp2{display:none}#nav.hs .stp2{display:inline-flex}#nav.hs span.stp2{display:inline-block}
#sind{font-family:var(--mono);font-size:.85rem;color:var(--gold-2);min-width:3.4rem;text-align:center}
#nav button:disabled{opacity:.35;cursor:default}
#ind{font-family:var(--mono);font-size:.85rem;color:var(--gold);min-width:5.6rem;text-align:center}
.nsep{width:1px;height:1.3rem;background:rgba(232,200,122,.3)}
button:focus-visible,a:focus-visible,input:focus-visible{outline:2px solid var(--gold-2);outline-offset:2px}
#ov{position:fixed;inset:0;z-index:40;background:rgba(4,18,15,.96);overflow:auto;padding:2.5rem 3rem}
#ov h2{font-size:2rem;color:var(--gold);text-transform:uppercase;text-align:center;margin-bottom:1.2rem}
.ovg{display:grid;grid-template-columns:repeat(auto-fill,minmax(15rem,1fr));gap:.5rem;max-width:1500px;margin:0 auto}
.ovi{display:flex;gap:.6rem;align-items:baseline;text-align:left;background:rgba(10,38,32,.8);border:1px solid rgba(232,200,122,.25);color:var(--ink);font:inherit;font-size:.95rem;padding:.5rem .7rem;border-radius:8px;cursor:pointer}
.ovi:hover,.ovi.cur{border-color:var(--gold);background:rgba(232,200,122,.12)}
.ovi .mono{font-family:var(--mono);color:var(--gold);font-size:.8rem;min-width:1.6rem}
#lb{position:fixed;inset:0;z-index:45;background:rgba(3,14,11,.95);display:grid;place-items:center;padding:2rem;cursor:zoom-out}
#lb img{max-width:100%;max-height:100%;background:#fff;border-radius:8px}
.fig img{cursor:zoom-in}
/* ---- карточка устройства ---- */
.topo .clk{cursor:pointer}.topo .clk:hover .dev,.topo .clk:focus-visible .dev{filter:drop-shadow(0 0 9px rgba(247,220,140,.95))}
.topo .clk:focus{outline:none}
.hint{margin-top:.3rem;text-align:center;font-size:.92rem;color:var(--dim);opacity:.85}
#dvc{position:fixed;z-index:36;right:26px;top:26px;bottom:78px;width:min(36rem,calc(100% - 52px));overflow:auto;padding:1rem 1.1rem;display:flex;flex-direction:column;gap:.7rem;
  background:linear-gradient(180deg,rgba(11,46,39,.97),rgba(5,24,20,.97));border:1px solid var(--gold);border-radius:12px;box-shadow:0 0 30px rgba(0,0,0,.6),0 0 18px rgba(232,200,122,.2)}
#dvc[hidden]{display:none}
.dvh{display:flex;justify-content:space-between;align-items:flex-start;gap:1rem}.dvh h3{font-size:1.6rem;color:var(--gold-2)}
.dvk{font-size:.85rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)}
.dvx{background:none;border:1px solid var(--gold-dim);color:var(--gold-2);border-radius:8px;width:2.2rem;height:2.2rem;cursor:pointer;font-size:1rem;flex:none}
.dvx:hover{background:rgba(232,200,122,.15)}
.dvg{font-size:.95rem;color:var(--dim)}.dvg b{color:var(--gold-2)}
#dvc .rt{font-size:.85rem}#dvc .rt td,#dvc .rt th{padding:.3rem .4rem}#dvc .rt caption{font-size:1.1rem}
/* ---- кадр/заголовки ---- */
.frm{display:flex;flex-wrap:wrap;justify-content:center;border:1px solid var(--gold);border-radius:8px;overflow:hidden;background:rgba(3,18,14,.7)}
.frm>div{padding:.35rem .7rem;border-right:1px solid rgba(232,200,122,.5);text-align:center;min-width:8.5rem}
.frm>div:last-child{border-right:0}
.frm small{display:block;font-size:.82rem;color:var(--dim);letter-spacing:.06em;text-transform:uppercase}
.frm b{font-family:var(--mono);font-weight:400;font-size:1.05rem;color:#fff;transition:color .3s,background .3s;padding:0 .2rem}
.frm .l2{background:rgba(79,214,196,.08)}.frm .l3{background:rgba(232,200,122,.08)}
.frm b.fl{color:#0a2620;background:var(--gold-2);border-radius:3px}
/* ---- тренажёр ---- */
.trn input{font:inherit;font-family:var(--mono);font-size:1.15rem;background:#03120e;color:#fff;border:1px solid var(--gold);border-radius:8px;padding:.4rem .7rem;width:12rem}
.trn .btn{font:inherit;font-size:1rem;background:rgba(232,200,122,.1);color:var(--gold-2);border:1px solid var(--gold);border-radius:8px;padding:.4rem .9rem;cursor:pointer}
.trn .btn:hover{background:rgba(232,200,122,.22)}.trn .btn.on{background:var(--gold);color:#0a2620}
.trn .row{display:flex;flex-wrap:wrap;gap:.6rem;align-items:center}
.trn .msg{min-height:3.2rem;font-size:1.05rem;line-height:1.45}
.trn .msg .ok{color:#9fe38c}.trn .msg .no{color:#ef8c78}
.trn .rt tbody tr{cursor:pointer}
.trn .rt tbody tr:hover td{background:rgba(232,200,122,.1)}
.bits{font-family:var(--mono);font-size:1rem;display:grid;gap:.3rem}
.bits .br{display:grid;grid-template-columns:11rem 1fr auto;gap:.8rem;align-items:center}
.bits .bn{letter-spacing:.06em;white-space:nowrap}
.bits .bn i{font-style:normal;transition:color .3s,background .3s,opacity .3s}
.bits.go .bn i.m{color:#0a2620;background:var(--gold-2)}
.bits.go .bn i.x{color:#fff;background:rgba(239,140,120,.7)}
.bits.go .bn i.o{opacity:.35}
.bits .bn i{transition-delay:var(--d)}
.bits .res{font-weight:400;color:var(--dim);opacity:0;transition:opacity .4s 1.2s;font-size:.9rem;font-family:var(--f)}
.bits.go .res{opacity:1}.bits .br.best .res{color:var(--gold-2)}.bits .br.no .res{color:#ef8c78}
.bits .br.dst .bl2{color:#fff}
.pn.act{border-color:var(--gold-2);box-shadow:0 0 22px rgba(247,220,140,.35),inset 0 0 26px rgba(232,200,122,.12);transition:box-shadow .5s,border-color .5s}
.topo .pkt.gone{opacity:0;transition:opacity .6s}
.rin .box0{fill:rgba(232,200,122,.04);stroke:var(--gold-dim)}
.rin .bx1{fill:rgba(79,214,196,.10);stroke:var(--teal)}.rin .bx2{fill:rgba(232,200,122,.07);stroke:var(--gold)}.rin .bx3{fill:rgba(20,82,74,.8);stroke:var(--gold-2)}
.rin .pp path{fill:none;stroke:rgba(242,236,224,.55);stroke-width:1.4}
.rin .pkt rect{fill:#f7dc8c}.rin .pkt{opacity:0;filter:drop-shadow(0 0 6px rgba(255,220,130,.95))}.rin .pkt.on{opacity:1}
.rf .fb.big rect{fill:rgba(232,200,122,.12)}.rf .fb.big text{font-size:22px;font-weight:700;fill:var(--gold-2)}
.rf .fb.t rect{fill:rgba(79,214,196,.12);stroke:var(--teal)}.rf .fb.t text{fill:var(--teal)}
.rf .tf path{fill:none;stroke:var(--teal);stroke-width:1.6}
.bits .bl2{color:var(--gold-2);font-weight:700}
.bits .br.dim{opacity:.35;transition:opacity .4s}
.bits .br.win .bl2{color:#fff}.bits .br.win{background:rgba(232,200,122,.12);border-radius:6px;box-shadow:inset 3px 0 0 var(--gold)}
.big-f{font-size:1.5rem;text-align:center;color:var(--gold-2);font-weight:700}
.chip{display:inline-block;border:1px solid var(--gold);border-radius:6px;padding:.05rem .45rem;color:var(--gold-2);font-size:.95em}
.chip.t{border-color:var(--teal);color:var(--teal)}
.fl{display:flex;align-items:center;gap:.6rem;flex-wrap:wrap;justify-content:center}
.arr{color:var(--gold);font-size:1.4rem}
@media (max-width:1279px){.two,.two.eq,.two.wide{grid-template-columns:minmax(0,1fr)}}
@media (max-width:767px){html{font-size:15px}.sc{padding:1.6rem 1.1rem 6.5rem}.gt{font-size:1.75rem!important}.title h1{font-size:2.4rem}
  #frame i{width:40px;height:40px}.p{text-align:left}.bt{font-size:1.1rem}.bi{padding:.5rem 2rem}.lbl2{display:none}.rt{font-size:.9rem}
  .con pre{font-size:.7rem}.bits .br{grid-template-columns:1fr}.tw .rt{min-width:30rem}}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{transition:none!important;animation:none!important}}
"""

def _net_layer():
    """Созвездие узлов: редкая сеть точек и связей — мотив главы."""
    import random
    rnd = random.Random(7)
    pts = []
    for i in range(70):
        x = 40 + (i * 311) % 1840
        y = 40 + (i * 677) % 1000
        x += rnd.randint(-28, 28); y += rnd.randint(-26, 26)
        pts.append((x, y))
    lines = []
    for i, (x1, y1) in enumerate(pts):
        for x2, y2 in pts[i + 1:]:
            d = math.hypot(x1 - x2, y1 - y2)
            if d < 290:
                lines.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="{2.2 + (i % 3) * .9:.1f}"'
                   f' style="animation-delay:-{i * .7:.1f}s;transform-origin:{x}px {y}px"/>' for i, (x, y) in enumerate(pts))
    return ('<svg class="lay net" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice">'
            f'<g class="nl">{"".join(lines)}</g><g class="nd">{dots}</g></svg>')


def _cont_layer():
    """Топографические изолинии: спокойный «карточный» фон."""
    out = []
    for k in range(11):
        pts = []
        for i in range(0, 41):
            x = i * 48
            y = 150 + k * 86 + 58 * math.sin(i / 5.2 + k * .72) + 26 * math.sin(i / 2.1 + k)
            pts.append(f'{x},{y:.0f}')
        out.append(f'<polyline points="{" ".join(pts)}" opacity="{.5 - abs(k - 5) * .055:.2f}"/>')
    return ('<svg class="lay cont" viewBox="0 0 1920 1080" preserveAspectRatio="none">'
            f'<g>{"".join(out)}</g></svg>')


def _rings_layer():
    """Гильош: концентрические окружности и радиальные лучи, как на гравюре."""
    cx, cy = 1430, 420
    rings = "".join(f'<circle cx="{cx}" cy="{cy}" r="{70 + k * 46}" opacity="{.42 - k * .022:.2f}"/>' for k in range(16))
    rays = "".join('<line x1="{:.0f}" y1="{:.0f}" x2="{:.0f}" y2="{:.0f}"/>'.format(
        cx + 80 * math.cos(a), cy + 80 * math.sin(a), cx + 820 * math.cos(a), cy + 820 * math.sin(a))
        for a in [i * math.pi / 14 for i in range(28)])
    return ('<svg class="lay rings" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice">'
            f'<g class="rg">{rings}</g><g class="ry">{rays}</g></svg>')


def _mal_layer():
    """Малахитовые волны: мягкие зелёные полосы разной плотности."""
    bands = []
    for k in range(7):
        top = -120 + k * 185
        pts = [f'{i * 64},{top + 70 * math.sin(i / 4.6 + k * 1.1):.0f}' for i in range(0, 31)]
        low = [f'{i * 64},{top + 108 + 70 * math.sin(i / 4.6 + k * 1.1):.0f}' for i in range(30, -1, -1)]
        bands.append(f'<polygon points="{" ".join(pts + low)}" opacity="{.5 if k % 2 else .32:.2f}"/>')
    return ('<svg class="lay mal" viewBox="0 0 1920 1080" preserveAspectRatio="none">'
            '<defs><linearGradient id="mlg" x1="0" x2="1"><stop offset="0" stop-color="#0d4034"/>'
            '<stop offset=".5" stop-color="#17614f"/><stop offset="1" stop-color="#0b3429"/></linearGradient></defs>'
            f'<g fill="url(#mlg)">{"".join(bands)}</g></svg>')


def _asset_b64(name):
    f = HERE / "_rt_assets" / name
    return "data:image/webp;base64," + base64.b64encode(f.read_bytes()).decode()


def _leaf_layer():
    """Летящие листья: лёгкий листопад поверх тёмно-зелёного фона."""
    import random
    rnd = random.Random(11)
    out = []
    for i in range(34):
        x = rnd.randint(-80, 1900)
        s = rnd.uniform(.65, 1.8)
        dur = rnd.uniform(22, 46)
        dl = -rnd.uniform(0, dur)
        sw = rnd.uniform(60, 190)
        hue = "a" if i % 3 else "b"
        out.append(f'<g class="lf {hue}" style="--x:{x}px;--s:{s:.2f};--d:{dur:.1f}s;--dl:{dl:.1f}s;--sw:{sw:.0f}px">'
                   '<path d="M0,-16 C9,-10 13,-2 11,7 C9,14 2,17 -3,14 C-10,10 -12,0 -8,-8 C-6,-12 -3,-14 0,-16 Z"/>'
                   '<path class="vn" d="M0,-15 C-1,-6 -1,4 -2,13"/></g>')
    return '<div class="lay leaves"><svg viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice">' + "".join(out) + '</svg></div>'


def deco():
    th = [
        ("M-50,820 C300,700 520,760 760,640 S1250,420 1700,520 S2050,300 2100,260", 2.2, .55),
        ("M-80,960 C260,820 700,900 980,760 S1500,640 2080,700", 1.4, .4),
        ("M1500,-40 C1580,160 1760,240 2000,300", 1.6, .45),
        ("M-40,120 C120,200 180,360 120,560", 1.2, .3),
    ]
    paths = "".join(f'<path class="th" d="{d}" stroke="url(#thg)" stroke-width="{w}" opacity="{o}"/>'
                    f'<path class="th" d="{d}" stroke="url(#thg)" stroke-width="{w*4}" opacity="{o*.18}" filter="url(#thb)"/>' for d, w, o in th)
    sp = [(6, 18), (14, 62), (27, 9), (38, 30), (55, 12), (63, 40), (71, 7), (82, 24), (90, 52), (95, 14), (47, 58), (33, 72)]
    sparks = "".join(f'<circle class="spk" cx="{x*19.2:.0f}" cy="{y*10.8:.0f}" r="{3 + (i % 3)}" fill="url(#spk)" opacity="{.5 + (i % 3) * .2:.1f}"'
                      f' style="animation-delay:-{i*0.8:.1f}s;transform-origin:{x*19.2:.0f}px {y*10.8:.0f}px"/>' for i, (x, y) in enumerate(sp))
    sweeps = "".join(f'<path class="sweep" d="{d}" stroke-width="{w*.9:.1f}" style="animation-delay:-{k*3.5:.1f}s"/>' for k, (d, w, o) in enumerate(th[:2]))
    ph = "".join(f'<div class="ph p{k}" style="background-image:url({_asset_b64(f"bg_{k}.webp")})"></div>'
                 for k in ("clean", "sky", "globe"))
    return ('<div id="deco" aria-hidden="true">' + ph + '<div class="aur"><i></i><i></i><i></i></div><div class="orna"></div><div class="globe"></div>'
            + _leaf_layer() + _mal_layer() + _cont_layer() + _rings_layer() + _net_layer() +
            '<div class="rays"></div>'
            '<svg class="lay thr" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice"><defs>'
            '<linearGradient id="thg" x1="0" x2="1"><stop offset="0" stop-color="#e8c87a" stop-opacity="0"/><stop offset=".5" stop-color="#f5e3b0"/><stop offset="1" stop-color="#e8c87a" stop-opacity="0"/></linearGradient>'
            '<radialGradient id="spk"><stop offset="0" stop-color="#fff6d8"/><stop offset=".4" stop-color="#e8c87a" stop-opacity=".8"/><stop offset="1" stop-color="#e8c87a" stop-opacity="0"/></radialGradient>'
            '<filter id="thb"><feGaussianBlur stdDeviation="5"/></filter></defs>'
            f'{paths}{sweeps}{sparks}</svg><div class="vig"></div></div><div id="frame" aria-hidden="true"><i></i><i></i></div>')


JS = r"""
(function(){
'use strict';
var $=function(s,r){return (r||document).querySelector(s)}, $$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
var RM=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var TOPO=__TOPO__, DEV=__DEV__;
/* ================= генератор устройств и топологий ================= */
var GOLD='#e8c87a';
function f(n){return Math.round(n*10)/10}
function router(x,y,s){ s=s||1;
  return '<g class="dev rt" transform="translate('+x+','+y+') scale('+s+')">'+
   '<ellipse cx="0" cy="12" rx="38" ry="13" fill="url(#rglow)"/>'+
   '<ellipse cx="0" cy="9" rx="31" ry="10.5" fill="#062420"/>'+
   '<path d="M-31,-9 L-31,9 A31,10.5 0 0 0 31,9 L31,-9 Z" fill="url(#rside)"/>'+
   '<path d="M-31,9 A31,10.5 0 0 0 31,9" fill="none" stroke="'+GOLD+'" stroke-width="1.3" opacity=".85"/>'+
   '<path d="M-31,-9 V9 M31,-9 V9" stroke="'+GOLD+'" stroke-width="1.1"/>'+
   '<ellipse class="top" cx="0" cy="-9" rx="31" ry="10.5" fill="#14524a" stroke="'+GOLD+'" stroke-width="1.2"/>'+
   '<g stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none">'+
   '<path d="M-19,-9 H19 M0,-17 V-1"/><path d="M-14.5,-12 L-19,-9 L-14.5,-6 M14.5,-12 L19,-9 L14.5,-6 M-3.2,-14 L0,-17 L3.2,-14 M-3.2,-4 L0,-1 L3.2,-4"/></g></g>';
}
function sw(x,y,s){ s=s||1;
  return '<g class="dev sw" transform="translate('+x+','+y+') scale('+s+')">'+
   '<path d="M-24,-6 L-16,-14 H28 L20,-6 Z" fill="#1f8fa6" stroke="#8fe9f7" stroke-width="1"/>'+
   '<path d="M-24,-6 H20 V10 H-24 Z" fill="#0d4f60" stroke="#8fe9f7" stroke-width="1"/><path d="M20,-6 L28,-14 V2 L20,10 Z" fill="#0a3c49" stroke="#8fe9f7" stroke-width="1"/>'+
   '<g stroke="#fff" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M-10,-12 H10 M6,-14 L10,-12 L6,-10 M14,-8.5 H-6 M-2,-10.5 L-6,-8.5 L-2,-6.5"/></g></g>';
}
function pc(x,y,s){ s=s||1;
  return '<g class="dev pc" transform="translate('+x+','+y+') scale('+s+')">'+
   '<rect x="-20" y="-19" width="40" height="28" rx="2.5" fill="url(#scr)" stroke="#9af0ff" stroke-width="1.2"/>'+
   '<path d="M-4,9 L-6,16 H6 L4,9 Z M-12,17 H12" fill="#1b7c93" stroke="#9af0ff" stroke-width="1.1"/></g>';
}
function lap(x,y,s){ s=s||1;
  return '<g class="dev lap" transform="translate('+x+','+y+') scale('+s+')">'+
   '<path d="M-15,-18 H17 L14,4 H-18 Z" fill="url(#scr)" stroke="#9af0ff" stroke-width="1.2"/>'+
   '<path d="M-21,6 H15 L24,14 H-14 Z" fill="#1b7c93" stroke="#9af0ff" stroke-width="1.1"/></g>';
}
function srv(x,y,s){ s=s||1;
  return '<g class="dev srv" transform="translate('+x+','+y+') scale('+s+')">'+
   '<path d="M-12,-20 L-4,-25 H18 L10,-20 Z" fill="#2aa4bd" stroke="#9af0ff" stroke-width="1"/>'+
   '<rect x="-12" y="-20" width="22" height="42" fill="#0e5a6c" stroke="#9af0ff" stroke-width="1.1"/><path d="M10,-20 L18,-25 V17 L10,22 Z" fill="#0a3f4c" stroke="#9af0ff" stroke-width="1"/>'+
   '<path d="M-8,-12 H6 M-8,-6 H6 M-8,0 H6" stroke="#9af0ff" stroke-width="1.2"/></g>';
}
function cloudPath(x,y,w,h){
  var l=x-w/2,r=x+w/2,b=y+h/2,t=y-h/2,r0=h*.32;
  return 'M'+f(l+r0)+','+f(b)+' A'+f(r0)+','+f(r0)+' 0 0 1 '+f(l+r0*.55)+','+f(y-h*.02)+
    ' A'+f(h*.34)+','+f(h*.34)+' 0 0 1 '+f(l+w*.3)+','+f(t+h*.2)+
    ' A'+f(h*.42)+','+f(h*.42)+' 0 0 1 '+f(l+w*.7)+','+f(t+h*.16)+
    ' A'+f(h*.34)+','+f(h*.34)+' 0 0 1 '+f(r-r0*.55)+','+f(y-h*.02)+
    ' A'+f(r0)+','+f(r0)+' 0 0 1 '+f(r-r0)+','+f(b)+' Z';
}
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;')}
function textEl(x,y,s,c,a,z,id,fx){
  var lines=String(s).split('\n'), out='';
  lines.forEach(function(ln,k){ out+='<tspan x="'+x+'" dy="'+(k?'1.2em':'0')+'">'+esc(ln)+'</tspan>'; });
  return '<text'+(id?' id="'+id+'"':'')+' class="tx '+(c||'')+(fx?' fx':'')+'" x="'+x+'" y="'+y+'" text-anchor="'+(a||'middle')+'"'+(z?' style="font-size:'+z+'px"':'')+'>'+out+'</text>';
}
var BOX={r:[36,19],sw:[31,17],pc:[24,22],lap:[26,20],srv:[20,27]};
function rad(n,ux,uy){
  var sc=n.s||(n.t==='r'?1.3:1.15), ab=n.t==='cloud'?[n.w/2*.92,n.h/2*.86]:(BOX[n.t]||[6,6]).map(function(v){return v*sc});
  return 1/Math.sqrt(Math.pow(ux/ab[0],2)+Math.pow(uy/ab[1],2))+5;
}
function pt(sp,p){ if(typeof p==='string'){ var n=sp.nm[p]; return {x:n.x,y:n.y,n:n}; } return {x:p[0],y:p[1],n:null}; }
function buildTopo(el){
  var sp=TOPO[el.dataset.topo]; if(!sp) return; sp.nm={}; (sp.n||[]).forEach(function(n){sp.nm[n.i]=n;});
  var W=sp.vb[0],H=sp.vb[1], o=[], uid=el.dataset.topo;
  o.push('<svg viewBox="0 0 '+W+' '+H+'" role="img" aria-label="'+esc(sp.al||'Схема сети')+'"><defs>'+
   '<linearGradient id="rside" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#14524a"/><stop offset="1" stop-color="#062420"/></linearGradient>'+
   '<radialGradient id="rglow"><stop offset="0" stop-color="#e8c87a" stop-opacity=".45"/><stop offset="1" stop-color="#e8c87a" stop-opacity="0"/></radialGradient>'+
   '<linearGradient id="scr" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5fe1f5"/><stop offset="1" stop-color="#0c6f8c"/></linearGradient></defs>');
  (sp.ar||[]).forEach(function(a){ o.push('<g class="area'+(a.fx?' fx':'')+'"'+(a.id?' id="'+a.id+'"':'')+'><rect x="'+a.x+'" y="'+a.y+'" width="'+a.w+'" height="'+a.h+'" rx="10"/>'+(a.l?'<text x="'+(a.x+a.w/2)+'" y="'+(a.y+24)+'" text-anchor="middle">'+esc(a.l)+'</text>':'')+'</g>'); });
  (sp.rg||[]).forEach(function(r){ o.push('<ellipse'+(r.id?' id="'+r.id+'"':'')+' class="ring '+(r.c||'')+(r.fx?' fx':'')+'" cx="'+r.x+'" cy="'+r.y+'" rx="'+r.rx+'" ry="'+r.ry+'" transform="rotate('+(r.r||0)+' '+r.x+' '+r.y+')"/>'); });
  (sp.e||[]).forEach(function(e){ var a=pt(sp,e.a), b=pt(sp,e.b);
    o.push('<line'+(e.id?' id="'+e.id+'"':'')+' class="lk '+(e.c||'')+(e.fx?' fx':'')+'" x1="'+a.x+'" y1="'+a.y+'" x2="'+b.x+'" y2="'+b.y+'"/>'); });
  (sp.p||[]).forEach(function(p){
    var pts=p.d.map(function(q){return pt(sp,q)}), full='M'+pts.map(function(q){return q.x+','+q.y}).join(' L');
    o.push('<path id="'+uid+'-'+p.id+'-f" d="'+full+'" fill="none" stroke="none"/>');
    for(var k=0;k<pts.length-1;k++){
      var A=pts[k],B=pts[k+1],dx=B.x-A.x,dy=B.y-A.y,L=Math.sqrt(dx*dx+dy*dy),ux=dx/L,uy=dy/L;
      var ta=A.n?rad(A.n,ux,uy):0, tb=B.n?rad(B.n,ux,uy):0; if(p.tr){ta=p.tr[0]!=null&&k===0?p.tr[0]:ta; tb=p.tr[1]!=null&&k===pts.length-2?p.tr[1]:tb;}
      var x1=A.x+ux*ta,y1=A.y+uy*ta,x2=B.x-ux*(tb+(p.na?0:4)),y2=B.y-uy*(tb+(p.na?0:4));
      o.push('<path class="gp '+(p.c||'')+'" data-seg="'+p.id+'" d="M'+f(x1)+','+f(y1)+' L'+f(x2)+','+f(y2)+'"/>');
      if(!p.na && (!p.last||k===pts.length-2)){ var hx=B.x-ux*tb,hy=B.y-uy*tb,s=11,px=-uy,py=ux;
        o.push('<polygon class="ah '+(p.c||'')+'" data-ah="'+p.id+'" data-k="'+k+'" points="'+f(hx)+','+f(hy)+' '+f(hx-ux*s*1.3+px*s*.62)+','+f(hy-uy*s*1.3+py*s*.62)+' '+f(hx-ux*s*1.3-px*s*.62)+','+f(hy-uy*s*1.3-py*s*.62)+'"/>'); }
    }
  });
  (sp.n||[]).forEach(function(n){
    var g='', s=n.s||(n.t==='r'?1.3:1.15), fx=n.fx?' fx':'', id=n.id?' id="'+n.id+'"':'';
    if(n.t==='cloud'){ g='<g class="cld'+fx+'"'+id+'><path d="'+cloudPath(n.x,n.y,n.w,n.h)+'"/>'+textEl(n.x,n.y+(n.l2?-3:6),n.l||'','w','middle',n.z||17)+(n.l2?textEl(n.x,n.y+18,n.l2,'w','middle',n.z2||14):'')+'</g>'; o.push(g); return; }
    var fn={r:router,sw:sw,pc:pc,lap:lap,srv:srv}[n.t]; if(!fn) return;
    g=fn(n.x,n.y,s);
    var lp=n.lp||(n.t==='r'?'r':'b'), L='';
    if(n.l){ var lx=n.x,ly=n.y,an='middle';
      if(lp==='r'){lx=n.x+38*s;ly=n.y+14*s;an='start';} else if(lp==='l'){lx=n.x-38*s;ly=n.y+14*s;an='end';}
      else if(lp==='t'){ly=n.y-30*s;} else if(lp==='b'){ly=n.y+(n.t==='r'?38:40)*s;}
      L='<text class="lbl" x="'+lx+'" y="'+ly+'" text-anchor="'+an+'"'+(n.z?' style="font-size:'+n.z+'px"':'')+'>'+esc(n.l)+'</text>'; }
    var ck=n.dv&&DEV[n.dv];
    o.push('<g class="nd'+fx+(ck?' clk':'')+'"'+id+(ck?' data-dv="'+n.dv+'" tabindex="0" role="button" aria-label="Карточка устройства '+esc(n.l||'')+'"':'')+'>'+g+L+'</g>');
  });
  (sp.dt||[]).forEach(function(d){ o.push('<circle'+(d.id?' id="'+d.id+'"':'')+' class="dot '+(d.c||'')+(d.fx?' fx':'')+'" cx="'+d.x+'" cy="'+d.y+'" r="'+(d.r||4.2)+'"/>'); });
  (sp.x||[]).forEach(function(x){ o.push('<g class="'+(x.fx?'fx':'')+'"'+(x.id?' id="'+x.id+'"':'')+'><path class="xx" d="M'+(x.x-8)+','+(x.y-8)+' L'+(x.x+8)+','+(x.y+8)+' M'+(x.x+8)+','+(x.y-8)+' L'+(x.x-8)+','+(x.y+8)+'"/></g>'); });
  (sp.co||[]).forEach(function(c){ var lines=c.t.split('\n'), w=c.w||Math.max.apply(null,lines.map(function(s){return s.length}))*7.4+18, h=lines.length*17+10;
    o.push('<g class="co'+(c.fx?' fx':'')+'"'+(c.id?' id="'+c.id+'"':'')+'>'+(c.to?'<line x1="'+c.x+'" y1="'+(c.y+h/2)+'" x2="'+c.to[0]+'" y2="'+c.to[1]+'"/>':'')+
      '<rect x="'+f(c.x-w/2)+'" y="'+c.y+'" width="'+f(w)+'" height="'+h+'" rx="6"/>'+textEl(c.x,c.y+18,c.t,'','middle',c.z)+'</g>'); });
  (sp.tg||[]).forEach(function(t){ o.push('<g class="tag'+(t.fx?' fx':'')+'"'+(t.id?' id="'+t.id+'"':'')+'><polygon points="'+(t.x-12)+','+(t.y+10)+' '+(t.x-4)+','+(t.y-10)+' '+(t.x+16)+','+(t.y-10)+' '+(t.x+8)+','+(t.y+10)+'"/><text x="'+(t.x+2)+'" y="'+(t.y+5)+'" text-anchor="middle">'+esc(t.n)+'</text></g>'); });
  (sp.tx||[]).forEach(function(t){ o.push(textEl(t.x,t.y,t.s,t.c,t.a,t.z,t.id,t.fx)); });
  (sp.cube||[]).forEach(function(c){ o.push('<g transform="translate('+c.x+','+c.y+') scale('+(c.s||4)+')" style="filter:drop-shadow(0 0 3px rgba(255,220,130,.9))"><polygon points="0,-9 9,-4.5 0,0 -9,-4.5" fill="#fff3c8"/><polygon points="-9,-4.5 0,0 0,10 -9,5.5" fill="#e8c87a"/><polygon points="9,-4.5 0,0 0,10 9,5.5" fill="#b08a3a"/>'+
    '<path d="M0,-9 9,-4.5 9,5.5 0,10 -9,5.5 -9,-4.5 Z M0,0 V10 M0,0 9,-4.5 M0,0 -9,-4.5 M-4.5,-6.75 V7.75 M4.5,-6.75 V7.75 M-9,.5 L0,5 9,.5" fill="none" stroke="#fff8e0" stroke-width=".35"/></g>'); });
  (sp.pk||[]).forEach(function(k){ o.push('<g class="pkt" id="'+uid+'-'+k+'"><g transform="scale(1.25)"><polygon points="0,-9 9,-4.5 0,0 -9,-4.5" fill="#fff3c8"/><polygon points="-9,-4.5 0,0 0,10 -9,5.5" fill="#e8c87a"/><polygon points="9,-4.5 0,0 0,10 9,5.5" fill="#b08a3a"/>'+
    '<path d="M0,-9 9,-4.5 9,5.5 0,10 -9,5.5 -9,-4.5 Z M0,0 V10 M0,0 9,-4.5 M0,0 -9,-4.5" fill="none" stroke="#fff8e0" stroke-width=".6"/></g></g>'); });
  o.push('</svg>'); el.innerHTML=o.join('');
  var sv=el.querySelector('svg'); if(sv&&sp.vb&&sp.vb[1]){ sv.style.maxWidth='calc(var(--tcap, 46vh) * '+(sp.vb[0]/sp.vb[1]).toFixed(3)+')'; sv.style.margin='0 auto'; }
  if(el.querySelector('.clk')&&!sp.nohint){ var hn=document.createElement('p'); hn.className='hint'; hn.textContent='Нажмите на устройство: откроются его порты, MAC и IP-адреса, ARP-таблица, таблица коммутации или маршрутизации'; el.appendChild(hn); }
}
$$('[data-topo]').forEach(buildTopo);
/* ================= сценарии ================= */
var timers=[], rafs=[], INST=false;
function later(fn,ms){ if(INST){ fn(); return; } timers.push(setTimeout(fn,RM?0:ms)); }
function stopAll(){ timers.forEach(clearTimeout); timers=[]; rafs.forEach(cancelAnimationFrame); rafs=[]; }
function Q(sl,s){ return $$(s,sl); }
function drawSeg(el,ms){ if(INST) ms=0; var L=el.getTotalLength(); el.style.transition='none'; el.style.strokeDasharray=L; el.style.strokeDashoffset=L; el.style.opacity=1;
  void el.getBoundingClientRect(); el.style.transition='stroke-dashoffset '+(RM?0:ms)+'ms cubic-bezier(.45,.1,.35,1)'; el.style.strokeDashoffset=0; }
function act(sl,a){
  var k=a[1];
  if(k==='on') Q(sl,a[2]).forEach(function(e){e.classList.add('on')});
  else if(k==='off') Q(sl,a[2]).forEach(function(e){e.classList.remove('on')});
  else if(k==='add') Q(sl,a[2]).forEach(function(e){e.classList.add(a[3])});
  else if(k==='rm') Q(sl,a[2]).forEach(function(e){e.classList.remove(a[3])});
  else if(k==='txt') Q(sl,a[2]).forEach(function(e){e.textContent=a[3]});
  else if(k==='hl'){ var t=$(a[2],sl); if(!t) return; $$('tr',t).forEach(function(r){r.classList.remove('hl')}); if(a[3]!=null){ var r=$('tr[data-r="'+a[3]+'"]',t); if(r) r.classList.add('hl'); } }
  else if(k==='scan'){ var tb=$(a[2],sl), st=a[4]||420; a[3].forEach(function(n,i){ later(function(){ act(sl,[0,'hl',a[2],n]); }, i*st); }); }
  else if(k==='draw'){ var ms=a[3]||800, pid=a[2], segs=Q(sl,'[data-seg="'+pid+'"]'), heads=Q(sl,'[data-ah="'+pid+'"]');
    segs.forEach(function(s,i){ later(function(){ drawSeg(s,ms); }, i*ms);
      var h=heads.filter(function(x){return +x.dataset.k===i})[0]; if(h) later(function(){ h.classList.add('on'); }, (i+1)*ms-60); }); }
  else if(k==='undraw'){ Q(sl,'[data-seg="'+a[2]+'"],[data-ah="'+a[2]+'"]').forEach(function(e){ e.style.opacity=0; e.classList.remove('on'); }); }
  else if(k==='pkt'){ var path=$(a[2],sl), pk=$(a[4],sl); if(!path||!pk) return; var L=path.getTotalLength(), ms=RM?1:(a[3]||1600), t0=null, from=a[5]||0, to=a[6]==null?1:a[6];
    pk.classList.add('on');
    if(INST){ var qe=path.getPointAtLength(L*to); pk.setAttribute('transform','translate('+qe.x+','+qe.y+')'); if(a[7]==='hide') pk.classList.remove('on'); return; }
    var step=function(ts){ if(!t0) t0=ts; var u=Math.min(1,(ts-t0)/ms), e=u<.5?2*u*u:1-Math.pow(-2*u+2,2)/2, q=path.getPointAtLength(L*(from+(to-from)*e));
      pk.setAttribute('transform','translate('+q.x+','+q.y+')'); if(u<1) rafs.push(requestAnimationFrame(step)); else if(a[7]==='hide') pk.classList.remove('on'); };
    rafs.push(requestAnimationFrame(step)); }
  else if(k==='fn'){ var fn=FN[a[2]]; if(fn) fn(sl,a); }
}
var FN={};
/* ================= карточка устройства ================= */
var dvc=document.getElementById('dvc');
function tb(cap,h,rows){ if(!rows||!rows.length) return ''; return '<div class="tw sm"><table class="rt"><caption>'+cap+'</caption><thead><tr>'+h.map(function(x){return '<th>'+x+'</th>'}).join('')+'</tr></thead><tbody>'+
  rows.map(function(r){return '<tr>'+r.map(function(c){return '<td>'+esc(c)+'</td>'}).join('')+'</tr>'}).join('')+'</tbody></table></div>'; }
function openDev(key,from){ var d=DEV[key]; if(!d) return;
  var ifh=d.mac?['Порт','IP','MAC порта','Состояние']:['Интерфейс','IP/маска','MAC','Состояние'], ifr=d.if.map(function(r){return d.mac?[r[0],'нет',r[2],r[3]]:r});
  var h='<div class="dvh"><div><span class="dvk">'+esc(d.k)+'</span><h3>'+esc(d.n)+'</h3></div><button type="button" class="dvx" aria-label="Закрыть">&#10005;</button></div>';
  if(d.gw) h+='<p class="dvg">Шлюз по умолчанию: <b>'+esc(d.gw)+'</b></p>';
  h+=tb(d.mac?'Порты':'Интерфейсы',ifh,ifr);
  if(d.mac) h+=tb('Таблица коммутации (MAC-таблица)',['MAC-адрес','Порт'],d.mac);
  if(d.arp&&d.arp.length) h+=tb('ARP-таблица',['IP-адрес','MAC-адрес','Интерфейс'],d.arp);
  else if(!d.mac) h+='<p class="dvg">ARP-таблица пока пустая: запись появится после первого ARP-обмена.</p>';
  if(d.rt&&d.rt.length) h+=tb('Таблица маршрутизации',d.rt[0].length===4?['Код','Сеть назначения','Следующий переход','Интерфейс']:['Сеть назначения','Шлюз','Интерфейс'],d.rt);
  if(d.mac) h+='<p class="dvg">Коммутатор работает на канальном уровне: IP-адресов на портах нет, решение принимается по MAC-адресу назначения кадра.</p>';
  dvc.innerHTML=h; dvc.hidden=false; dvc._from=from; var x=dvc.querySelector('.dvx'); x.onclick=closeDev; x.focus(); }
function closeDev(){ if(dvc&&!dvc.hidden){ dvc.hidden=true; if(dvc._from&&dvc._from.focus) dvc._from.focus(); } }
document.addEventListener('click',function(e){ var n=e.target.closest&&e.target.closest('.clk'); if(n){ openDev(n.dataset.dv,n); return; } if(!dvc.hidden&&!(e.target.closest&&e.target.closest('#dvc'))) closeDev(); });
document.addEventListener('keydown',function(e){ if((e.key==='Enter'||e.key===' ')&&e.target.classList&&e.target.classList.contains('clk')){ e.preventDefault(); e.stopPropagation(); openDev(e.target.dataset.dv,e.target); } },true);
function runTL(sl){ var tl=sl._tl; if(!tl) return; tl.forEach(function(a){ later(function(){ act(sl,a); }, a[0]); }); }
function mkSteps(tl){
  function mv(a){ return a[1]==='draw'||a[1]==='pkt'; }
  var mt=tl.filter(mv).map(function(a){ return a[0]; }).sort(function(x,y){return x-y}), cuts=[];
  mt.forEach(function(x){ if(!cuts.length||x-cuts[cuts.length-1]>150) cuts.push(x); });
  if(!cuts.length) return [tl.slice()];
  function norm(g,c){ return g.map(function(a){ return [Math.max(0,a[0]-c)].concat(a.slice(1)); }); }
  var c0=cuts[0], setup=tl.filter(function(a){ return a[0]<c0||(a[0]<=c0&&!mv(a)); }), steps=[];
  steps.push(norm(setup,0));
  cuts.forEach(function(c,i){
    var hi=i+1<cuts.length?cuts[i+1]:Infinity;
    var g=tl.filter(function(a){ return a[0]>=c&&a[0]<hi&&!(a[0]<=c0&&!mv(a)); });
    if(g.length) steps.push(norm(g,c));
  });
  return steps;
}
function showAll(sl){ $$('[data-s]',sl).forEach(function(e){ e.style.setProperty('--dl','0ms'); e.classList.add('in'); }); }
function runStep(sl,k){
  var st=sl._steps; if(!st||!st.length) return;
  k=Math.max(0,Math.min(st.length-1,k));
  clearTimeout(tm); stopAll(); reset(sl); showAll(sl);
  INST=true; for(var i=0;i<k;i++) st[i].forEach(function(a){ act(sl,a); }); INST=false;
  st[k].forEach(function(a){ later(function(){ act(sl,a); }, a[0]); });
  sl._step=k; updSteps();
}
function updSteps(){
  var sl=slides[cur], st=sl._steps, nav=$('#nav');
  if(!st||st.length<2){ nav.classList.remove('hs'); return; }
  nav.classList.add('hs');
  $('#sind').textContent=((sl._step==null?st.length:sl._step+1))+' / '+st.length;
  $('#b-sprev').disabled=(sl._step!=null&&sl._step<=0);
  $('#b-snext').disabled=(sl._step==null||sl._step>=st.length-1);
}
function stepGo(d){ var sl=slides[cur], st=sl._steps; if(!st) return;
  var k=sl._step==null?st.length-1:sl._step; runStep(sl,k+d); }
/* ================= движок слайдов ================= */
var slides=$$('.slide'), N=slides.length, cur=0, tm=null;
var BG={}; (function(){
  var hero=/^(В этой главе|Маршрутизация между VLAN|Три метода: сравнение|Задачи для самостоятельного решения|Задача 1: лучший маршрут|Тест по главе|Проверь себя: 1)$/;
  slides.forEach(function(s,i){ if(hero.test(s.dataset.label)) BG[i]=(i%2?2:5); });
  BG[0]=5; BG[N-1]=2;
})();
slides.forEach(function(sl){ sl._snap=$$('.scn',sl).map(function(s){return s.innerHTML}); if(sl.dataset.tl){ try{ sl._tl=JSON.parse(sl.dataset.tl); sl._steps=mkSteps(sl._tl); }catch(e){ sl._tl=null; } } });
function reset(sl){ $$('.scn',sl).forEach(function(s,i){ s.innerHTML=sl._snap[i]; }); }
function show(sl){
  stopAll(); reset(sl); conFit(sl); var els=$$('[data-s]',sl); els.forEach(function(e,i){ if(!e.style.getPropertyValue('--dl')) e.style.setProperty('--dl',Math.min((i+1)*60,720)+'ms'); });
  els.forEach(function(e){e.classList.remove('in')}); sl.classList.add('ni'); void sl.offsetWidth; sl.classList.remove('ni');
  sl._step=null;
  tm=setTimeout(function(){ els.forEach(function(e){e.classList.add('in')}); later(function(){ var st=sl._steps; if(st&&st.length>1){ sl._step=0; st[0].forEach(function(a){ later(function(){ act(sl,a); }, a[0]); }); updSteps(); } else runTL(sl); }, 420); if(sl._init) sl._init(sl); },40);
  updSteps();
}
function play(){ clearTimeout(tm); show(slides[cur]); }
function go(i){
  i=Math.max(0,Math.min(N-1,i)); clearTimeout(tm); stopAll(); closeDev();
  slides.forEach(function(s){s.classList.remove('on')}); cur=i; var sl=slides[cur]; sl.classList.add('on');
  var sc=$('.sc',sl); if(sc) sc.scrollTop=0;
  fit(sl); play();
  document.body.dataset.bg=BG[cur]||([1,3,4,6][Math.floor((cur-1)/7)%4]);
  try{ history.replaceState(null,'','#'+(cur+1)); }catch(e){}
  $('#ind').textContent=(cur+1)+' / '+N; $('#prog i').style.width=((cur+1)/N*100)+'%';
  $('#b-prev').disabled=cur===0; $('#b-next').disabled=cur===N-1;
}
function conFit(sl){
  $$('.con pre',sl).forEach(function(pr){
    pr.style.fontSize='';
    var fs=parseFloat(getComputedStyle(pr).fontSize);
    for(var k=0;k<7;k++){
      if(pr.scrollWidth<=pr.clientWidth+2||fs<9) break;
      fs=Math.max(9,fs*Math.max(.75,pr.clientWidth/pr.scrollWidth)*.99);
      pr.style.fontSize=fs.toFixed(2)+'px';
    }
  });
}
function fit(sl){
  var w=$('.wrap',sl), sc=$('.sc',sl); if(!w||!sc) return;
  w.style.zoom=''; w.style.width=''; w.style.minHeight=''; w.style.removeProperty('--tcap');
  if(window.innerWidth<900) return;
  var cs=getComputedStyle(sc), P=parseFloat(cs.paddingTop)+parseFloat(cs.paddingBottom), H=sc.clientHeight-P, z=1;
  conFit(sl);
  function nat(){ w.style.minHeight='0'; var C=w.scrollHeight; w.style.minHeight=''; return C; }
  function apply(v){ z=v; w.style.width=v>1?(100/v).toFixed(2)+'%':''; w.style.zoom=v.toFixed(3); }
  function solve(){
    for(var i=0;i<5;i++){
      var C=nat(); if(C<40) return;
      var z2=Math.max(.66,Math.min(1.3,H/C*.98));
      if(Math.abs(z2-z)<.012) break;
      apply(z2);
    }
    for(var j=0;j<3;j++){
      var C3=nat(); if(C3*z<=H+4||z<=.661) break;
      apply(Math.max(.66,z*(H/(C3*z))*.99));
    }
  }
  solve();
  if(sl.querySelector('.topo svg')){
    var f=z>=.85?.56:(z>=.78?.5:.44);
    w.style.setProperty('--tcap',Math.round(H*f/z)+'px');
    solve();
  }
}
var rzT=null; window.addEventListener('resize',function(){ clearTimeout(rzT); rzT=setTimeout(function(){ fit(slides[cur]); },120); });
function next(){ if(cur<N-1) go(cur+1); } function prev(){ if(cur>0) go(cur-1); }
$('#b-prev').onclick=prev; $('#b-next').onclick=next; $('#b-play').onclick=play;
$('#b-sprev').onclick=function(){ stepGo(-1); }; $('#b-snext').onclick=function(){ stepGo(1); };
var ov=$('#ov'), ovg=$('.ovg',ov);
slides.forEach(function(s,k){ var b=document.createElement('button'); b.className='ovi'; b.type='button';
  b.innerHTML='<span class="mono">'+(k+1)+'</span><span></span>'; b.lastChild.textContent=s.dataset.label;
  b.onclick=function(){ ov.hidden=true; go(k); }; ovg.appendChild(b); });
function openOv(){ ov.hidden=false; $$('.ovi',ov).forEach(function(b,k){b.classList.toggle('cur',k===cur)}); var c=$('.ovi.cur',ov); if(c)c.focus(); }
$('#b-ov').onclick=openOv;
var lb=$('#lb'); document.addEventListener('click',function(e){ var im=e.target.closest&&e.target.closest('.fig img'); if(im){ $('img',lb).src=im.src; lb.hidden=false; } });
lb.onclick=function(){ lb.hidden=true; };
document.addEventListener('click',function(e){ var q=e.target.closest&&e.target.closest('.qq'); if(q) q.parentNode.classList.toggle('open'); });
var dbuf='', dtm=null;
document.addEventListener('keydown',function(e){
  var t=e.target, tag=t.tagName;
  if(e.ctrlKey||e.metaKey||e.altKey) return;
  if(tag==='INPUT'&&t.type!=='checkbox'&&t.type!=='range') return;
  if(!lb.hidden){ if(e.key==='Escape'||e.key===' '||e.key==='Enter'){ e.preventDefault(); lb.hidden=true; } return; }
  if(e.key==='Escape'&&!dvc.hidden){ e.preventDefault(); closeDev(); return; }
  if(e.key==='Escape'){ e.preventDefault(); ov.hidden?openOv():(ov.hidden=true); return; }
  if(!ov.hidden) return;
  switch(e.key){
    case 'ArrowRight': case 'ArrowDown': case 'PageDown': e.preventDefault(); e.shiftKey?stepGo(1):next(); return;
    case 'ArrowLeft': case 'ArrowUp': case 'PageUp': e.preventDefault(); e.shiftKey?stepGo(-1):prev(); return;
    case '.': case 'ю': e.preventDefault(); stepGo(1); return;
    case ',': case 'б': e.preventDefault(); stepGo(-1); return;
    case ' ': if(tag==='BUTTON'||tag==='INPUT') return; e.preventDefault(); next(); return;
    case 'Home': e.preventDefault(); go(0); return;
    case 'End': e.preventDefault(); go(N-1); return;
  }
  var k=e.key.toLowerCase(); if(k==='r'||k==='к'){ play(); return; }
  if(/^[0-9]$/.test(e.key)){ dbuf+=e.key; clearTimeout(dtm); dtm=setTimeout(function(){ var n=parseInt(dbuf,10); dbuf=''; if(n>=1&&n<=N) go(n-1); },550); }
});
/* колесо мыши слайды не листает: прокрутка работает только внутри слайда */
var tx=0,ty=0,tt=0;
window.addEventListener('touchstart',function(e){ var p=e.changedTouches[0]; tx=p.clientX; ty=p.clientY; tt=Date.now(); },{passive:true});
window.addEventListener('touchend',function(e){ var p=e.changedTouches[0], dx=p.clientX-tx, dy=p.clientY-ty;
  if(Date.now()-tt>700||Math.abs(dx)<60||Math.abs(dx)<Math.abs(dy)*1.4) return; if(e.target.closest&&e.target.closest('.tw,.con,input')) return; dx<0?next():prev(); },{passive:true});
__EXTRA__
window.addEventListener('hashchange',function(){ var n=parseInt((location.hash||'').slice(1),10); if(n>=1&&n<=N&&n-1!==cur) go(n-1); });
var h=parseInt((location.hash||'').slice(1),10);
go(h>=1&&h<=N?h-1:0);
})();
"""

ICON_L = '<svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg>'
ICON_R = '<svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg>'

def _auto_dl(body):
    k = [0]
    def rep(m):
        k[0] += 1
        t = m.group(0)
        if "style=" in t: return t
        return t.replace('data-s="1"', f'data-s="1" style="--dl:{min(k[0]*60, 720)}ms"', 1)
    return re.sub(r'<[a-z0-9]+ [^>]*data-s="1"[^>]*>', rep, body)

def render(out_path, title, extra_js=""):
    css = CSS.replace("__F_REG__", _font("PT_Serif-Web-Regular.ttf")).replace("__F_BOLD__", _font("PT_Serif-Web-Bold.ttf"))
    css = re.sub(r"\n\s*", "", css)
    out = ['<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
           f'<title>{title}</title><style>' + css + '</style></head><body>' + deco() + '<div id="prog"><i></i></div><main>']
    for label, body, cls, tl in S:
        t = f" data-tl='{html.escape(json.dumps(tl, ensure_ascii=False), quote=True)}'" if tl else ""
        out.append(f'<section class="slide {cls}" data-label="{html.escape(label)}"{t}><div class="sc"><div class="wrap">{body}</div></div></section>')
    out.append('</main><nav id="nav" aria-label="Навигация">'
               f'<button id="b-prev" type="button" aria-label="Предыдущий слайд">{ICON_L}</button><span id="ind"></span>'
               f'<button id="b-next" type="button" aria-label="Следующий слайд">{ICON_R}</button>'
               '<span class="nsep stp2"></span>'
               f'<button id="b-sprev" class="stp2" type="button" title="Шаг назад (клавиша , или Shift+влево)">{ICON_L}</button>'
               '<span id="sind" class="stp2">1 / 1</span>'
               f'<button id="b-snext" class="stp2" type="button" title="Шаг вперёд (клавиша . или Shift+вправо)">{ICON_R}</button>'
               '<span class="nsep"></span>'
               '<button id="b-play" type="button" title="Клавиша R"><svg viewBox="0 0 24 24"><path d="M4 12a8 8 0 1 0 2.5-5.8M4 4v5h5"/></svg><span class="lbl2">Повторить анимацию</span></button>'
               '<button id="b-ov" type="button" title="Esc"><svg viewBox="0 0 24 24"><path d="M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h6v6h-6z"/></svg><span class="lbl2">Содержание</span></button></nav>'
               '<div id="lb" hidden role="dialog" aria-label="Изображение во весь экран"><img alt=""></div><div id="ov" hidden><h2>Содержание</h2><div class="ovg"></div></div><aside id="dvc" hidden aria-label="Карточка устройства"></aside>')
    topo_js = json.dumps(TOPO, ensure_ascii=False, separators=(",", ":"))
    extra_js = re.sub(r"\n\s+", "\n", extra_js)
    out.append('<script>' + re.sub(r"\n\s+", "\n", JS).replace("__TOPO__", topo_js).replace("__DEV__", json.dumps(DEV, ensure_ascii=False, separators=(",", ":"))).replace("__EXTRA__", extra_js) + '</script></body></html>')
    pathlib.Path(out_path).write_text("".join(out), encoding="utf-8")
    print(len(S), "slides", pathlib.Path(out_path).stat().st_size, "bytes")

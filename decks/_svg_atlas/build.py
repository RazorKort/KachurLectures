import json, re, pathlib, hashlib, html

CAP = pathlib.Path(__file__).parent / "cap"
OUT = pathlib.Path(r"D:\Преза лекций\decks\svg-atlas.html")

LECTURES = [
    ("glava1-networks-test", "Глава 1", "Основы сетевых технологий"),
    ("glava2-devices", "Глава 2", "Устройства, ПО и среда"),
    ("glava3-protokoly", "Глава 3", "Протоколы и модели"),
    ("glava4-adres", "Глава 4", "Адресация в многоуровневой модели"),
    ("glava5-ip", "Глава 5", "IP-адреса и адресация в сетях"),
    ("glava6-podseti-ip", "Глава 6", "Разбиение IP-сетей на подсети"),
    ("glava7-application", "Глава 7", "Уровень приложений"),
    ("glava8-transport", "Глава 8", "Транспортный уровень: TCP и UDP"),
    ("glava9-network", "Глава 9", "Сетевой уровень"),
    ("glava10-kanalnyi", "Глава 10", "Канальный уровень"),
    ("glava11-physical", "Глава 11", "Физический уровень"),
    ("routing", "Маршрутизация", "Типы маршрутизации, таблица, метрика"),
    ("marshrutizatory", "Маршрутизаторы 2.3", "Интерфейсы ESR, настройка, шлюз, ICMP, AAA"),
    ("linux-basics", "Linux", "Дистрибутивы и терминал"),
]

# (key, title, regex over text + title + ids). Order = order of sections.
TOPICS = [
    ("switch", "Коммутаторы", r"коммутатор|switch|\bs\d\b|\bsw[-\s]?\d|\bsw\b|концентратор|\bhub\b|mac[- ]таблиц|таблиц[аы] коммутац|#?\b(switch-l2|rp-switch|n_sw|h_sw\d*|sw)\b"),
    ("router", "Маршрутизаторы и шлюзы", r"маршрутизатор|router|\br\d\b|шлюз|gateway|маршрутизац|таблиц[аы] маршрут|next hop|\b(rt|rp-router|h_r\d+)\b"),
    ("hosts", "Компьютеры, серверы, клиенты", r"\bpc[-\s]?\w?|\bпк\b|компьютер|сервер|server|клиент|client|хост|host|ноутбук|смартфон|\b(rp-pc|rp-server|host-pc|laptop|srv|h_phone)\b"),
    ("osi", "Модели OSI / TCP-IP, инкапсуляция", r"\bosi\b|tcp/ip|уров(ень|ня|ни)|инкапсуляц|декапсуляц|\bpdu\b|стек"),
    ("ip", "IP-адресация, маски, подсети", r"\bipv[46]\b|ip-адрес|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|маск|подсет|subnet|/\d{2}\b|префикс|октет|широковещ|broadcast"),
    ("mac", "MAC, ARP, кадры Ethernet", r"\bmac\b|mac-адрес|([0-9a-f]{2}[-:]){5}[0-9a-f]{2}|\barp\b|кадр|frame|ethernet|преамбул|\bfcs\b|\bcrc\b"),
    ("transport", "Транспорт: TCP, UDP, порты", r"мультиплекс|mux|\btcp\b|\budp\b|порт|port|\bsyn\b|\back\b|рукопожат|handshake|сегмент|окно|window|сокет|socket"),
    ("packet", "IP-пакеты, TTL, ICMP, фрагментация", r"пакет|packet|\bttl\b|icmp|ping|traceroute|фрагмент|\bmtu\b|заголов|header"),
    ("app", "Приложения: DNS, HTTP, DHCP, почта, FTP", r"www|веб|интернет|internet|web|tftp|аренд|атомн|сеанс|\bdns\b|http|\bdhcp\b|smtp|pop3|imap|\bftp\b|\bntp\b|почт|браузер|домен|url|telnet|\bssh\b"),
    ("media", "Среда передачи: кабели, оптика, Wi-Fi, сигналы", r"модуляц|несущ|ам:|фм:|чм:|бит|экран|stp|одномод|многомод|базовая станция|wisp|ftt[xhbcn]|pon|dsl|модем|кабел|витая|оптик|волокн|коаксиал|wi-?fi|802\.11|беспровод|радио|антен|сигнал|частот|rj-?45|разъ[её]м|затухан|физическ"),
    ("access", "Доступ к среде, коллизии, топологии", r"опрос|флаг|поле длины|каждый с каждым|полносвязн|csma|коллизи|топологи|звезд|шина|кольц|mesh|дуплекс|полудуплекс|доступ к среде"),
    ("history", "История, организации, стандарты", r"isoc|ietf|ieee|iso|iab|стандарт|arpanet|rfc|19[6-9]\d|истори|временная линия"),
    ("linux", "Linux и терминал", r"linux|bash|\$ |sudo|chmod|каталог|директор|/home|/etc|терминал|ubuntu|debian|ядро|kernel|права"),
]
# topics that need the word in svg text/ids itself (not just the slide title) to avoid noise
STRICT = {"hosts"}


def load():
    decks = []
    for fname, chap, title in LECTURES:
        p = CAP / f"{fname}.json"
        if not p.exists():
            print("MISSING", fname); continue
        d = json.loads(p.read_text(encoding="utf-8"))
        seen = {}
        for it in d["items"]:
            svg = re.sub(r'\s(data-[\w-]+)="[^"]*"', "", it["svg"])
            shapes = len(re.findall(r"<(path|rect|circle|ellipse|line|polyline|polygon|text|image|use)", svg))
            if shapes <= 2 and not it["text"].strip() and max(it["w"], it["h"]) > 170:
                continue  # decorative blob / background shape
            h = hashlib.md5(svg.encode()).hexdigest()
            if h in seen:
                if it["slide"] + 1 not in seen[h]["slides"]:
                    seen[h]["slides"].append(it["slide"] + 1)
                continue
            seen[h] = {"svg": svg, "slides": [it["slide"] + 1], "title": it["title"], "bg": it["bg"],
                       "w": it["w"], "h": it["h"], "text": it["text"], "ids": it["ids"], "deck": fname}
        decks.append((fname, chap, title, list(seen.values())))
    return decks


def topics_for(it):
    refs = " ".join(re.findall(r'(?:id|href)="#?([A-Za-z][\w-]*)"', it["svg"]))
    words = " ".join(t.strip() for t in re.findall(r">([^<>]+)<", it["svg"]) if t.strip())
    own = (html.unescape(words) + " " + it["ids"] + " " + refs).lower()
    full = own + " " + it["title"].lower()
    res = ["linux"] if it.get("deck") == "linux-basics" else []
    for key, _, rx in TOPICS:
        hay = own if key in STRICT else full
        if key not in res and re.search(rx, hay, re.I):
            res.append(key)
    return res


def main():
    decks = load()
    items, lect = [], []
    for fname, chap, title, its in decks:
        ids = []
        for it in its:
            idx = len(items)
            items.append({"s": it["svg"], "d": fname, "c": chap, "sl": it["slides"], "t": it["title"],
                          "bg": it["bg"], "w": it["w"], "h": it["h"], "tp": topics_for(it),
                          "ic": 1 if max(it["w"], it["h"]) <= 170 else 0})
            ids.append(idx)
        lect.append({"id": fname, "chap": chap, "title": title, "items": ids})
    tops = []
    for key, name, _ in TOPICS:
        tops.append({"id": key, "title": name, "items": [i for i, x in enumerate(items) if key in x["tp"]]})
    tops.append({"id": "other", "title": "Прочее", "items": [i for i, x in enumerate(items) if not x["tp"]]})
    data = json.dumps({"items": items, "lect": lect, "tops": tops}, ensure_ascii=False, separators=(",", ":"))
    data = data.replace("</", "<\\/")
    tpl = (pathlib.Path(__file__).parent / "atlas_tpl.html").read_text(encoding="utf-8")
    OUT.write_text(tpl.replace("__DATA__", data), encoding="utf-8")
    print("items", len(items), "size MB", round(OUT.stat().st_size / 1e6, 2))
    for l in lect: print(" ", l["chap"], len(l["items"]))
    for t in tops: print(" ", t["title"], len(t["items"]))


main()

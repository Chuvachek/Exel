import re

# === Входные данные (вставьте сюда любое количество строк) ===
data = """
3M. GLE-RD-(P0-02-180)-N-LB 2600.001 (RU)_04_изм_3.pdf
4M. GLE-RD-(P0-71-020)-N-LB 2600.001 (RU)_05_изм_2.pdf
5M. GLE-RD-(P0-71-050)-N-LB 2600.001 (RU)_02_изм_1.pdf
6M. GLE‑RD‑(P0‑02‑170)‑N‑LB 2600.001 (RU)_04_изм_1.pdf
7M. GLE-RD-(P0-02-190)-N-LB 2600.001 (RU)_01_изм_2.pdf
8M. GLE-RD-(P0-02-200)-N-LB 2600.001 (RU)_03_изм_1.pdf
9M. GLE-RD-(P0-02-210)-N-LB 2600.001 (RU)_02_изм_2.pdf
10M. GLE-RD-(P0-02-220)-N-LB 2600.001 (RU)_01_изм_2.pdf
11M. GLE-RD-(P0-51-020)-N-LB 2600.001 (RU)_04_изм_2.pdf
12M. GLE-RD-(P0-71-010)-N-LB 2600.001 (RU)_05_изм_2.pdf
13M. GLE-RD-(P0-71-080)-N-LB 2600.001 (RU)_07_изм_1.pdf
14M. GLE‑RD‑(P0‑02‑010)‑N‑LB 2600.001 (RU)_02_изм_2.pdf
15M. GLE‑RD‑(P0‑02‑040)‑N‑LB 2600.001 (RU)_03_изм_2.pdf
16M. GLE‑RD‑(P0‑02‑070)‑N‑LB 2600.001 (RU)_03_изм_3.pdf
17M. GLE‑RD‑(P0‑02‑080)‑N‑LB 2600.001 (RU)_04_изм_2.pdf
18M. GLE‑RD‑(P0‑02‑090)‑N‑LB 2600.001 (RU)_05_изм_2.pdf
19M. GLE‑RD‑(P0‑02‑101)‑N‑LB 2600.001 (RU)_02_изм_2.pdf
20M. GLE‑RD‑(P0‑02‑102)‑N‑LB 2600.001 (RU)_05_изм_2.pdf
21M. GLE‑RD‑(P0‑02‑103)‑N‑LB 2600.001 (RU)_04_изм_3.pdf
22M. GLE‑RD‑(P0‑02‑104)‑N‑LB 2600.001 (RU)_05_изм_3.pdf
23M. GLE‑RD‑(P0‑02‑105)‑N‑LB 2600.001 (RU)_01_изм_2.pdf
24M. GLE‑RD‑(P0‑02‑111)‑N‑LB 2600.001 (RU)_02_изм_2.pdf
25M. GLE‑RD‑(

P0‑02‑113)‑N‑LB 2600.001 (RU)_03_изм_2.pdf
26M. GLE‑RD‑(P0‑02‑120)‑N‑LB 2600.001 (RU)_04_изм_2.pdf
27M. GLE‑RD‑(P0‑02‑131)‑N‑LB 2600.001 (RU)_03_изм_2.pdf
28M. GLE‑RD‑(P0‑02‑132)‑N‑LB 2600.001 (RU)_03_изм_3.pdf
29M. GLE‑RD‑(P0‑02‑141)‑N‑LB 2600.001 (RU)_03_изм_2.pdf
30M. GLE‑RD‑(P0‑02‑142)‑N‑LB 2600.001 (RU)_04_изм_2.pdf
31M. GLE‑RD‑(P0‑02‑150)‑N‑LB 2600.001 (RU)_03_изм_2.pdf
32M. GLE‑RD‑(P0‑02‑160)‑N‑LB 2600.001 (RU)_04_изм_2.pdf


""".strip().splitlines()

# Регулярка: 
#   ^\d+M?\.\s*   -> отсекаем "3M. " / "4M. " и т.п. в начале
#   (.+?)\s*      -> само имя (нежадно, до пробела перед (RU))
#   \(RU\)_(\d+)_изм_(\d+)\.pdf  -> код версии
pattern = re.compile(r'^\d+M?\.\s*(.+?)\s*\(RU\)_(\d+)_изм_(\d+)\.pdf\s*$')

names = []
codes = []

for line in data:
    line = line.strip()
    if not line:
        continue
    m = pattern.match(line)
    if not m:
        print(f"⚠ Не удалось распознать строку: {line}")
        continue
    name, num, izm = m.groups()
    names.append(name)
    codes.append(f"{num}_{izm.zfill(2)}")

# === Вывод в виде markdown-таблицы (одна колонка, имена сверху, коды снизу) ===
all_rows = names + codes
width = max(len(r) for r in all_rows)

print("| " + "Данные".ljust(width) + " |")
print("| " + "-" * width + " |")
for row in all_rows:
    print("| " + row.ljust(width) + " |")
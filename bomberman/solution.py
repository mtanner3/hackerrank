
rowcnt, colcnt, report_time = map(int, raw_input().strip().split())

rows = []

def print_board():
    for r in rows:
        for char in r:
            print char,
        print ""


for dummy in range(rowcnt):
    row = list(raw_input().strip())
    rows.append(row)

print_board()





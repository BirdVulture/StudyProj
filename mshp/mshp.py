#урок1

a = []
ok = 0
fail = 0
while a != 0:
    a = int(input())
    if a <= 180 and a > 0:
        ok = ok + 1
    if a > 180:
        fail = fail + a
print(f"Было поднято {ok} ящиков, но еще {fail} кг груза ожидают внизу." )
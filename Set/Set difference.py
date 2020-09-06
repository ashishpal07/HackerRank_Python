#Set .difference() operation

eng = int(input(""))
roll_eng = set(map(int, input().split(" ")))
fr = int(input(""))
roll_fr = set(map(int, input().split(" ")))
print(len(roll_eng-roll_fr))

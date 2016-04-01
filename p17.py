g1 = "onetwothreefourfivesixseveneightnine" # 1-9
g2 = "eleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen" # 11-19
g3 = "twentythirtyfortyfiftysixtyseventyeightyninety" # 20-90
g4 = "ten"

c1 = 100 * len(g1) # hundred place
c2 = 10 * (10 * len(g3) + len(g4)) # ten's place
c3 = 9 * len(g1) * 10 # the unit
c4 = 10 * len(g2) # 11-19
c5 = 7 * 900 # "hundred"s
c6 = 3 * 891 # "and"s
c7 = 11 # one thousand

s = c1+c2+c3+c4+c5+c6+c7
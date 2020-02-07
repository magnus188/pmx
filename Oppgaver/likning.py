anne = 0
berit = 0
celine = 0
dina = 0

anne_berit = 35
anne_celine = 27
berit_dina = 50
berit_celine = 38

a = 0

for anne in range(1, anne_berit+1):
    berit = anne_berit-anne
    celine = anne_celine-anne
    dina = berit_dina-berit

    if anne+berit == anne_berit and anne+celine == anne_celine and berit+dina == berit_dina and berit+celine == berit_celine and anne >0 and berit >0 and celine >0 and dina >0:
        a+=1
        print('Anne:', anne)
        print('Berit:', berit)
        print('Celine:', celine)
        print('Dina:', dina)


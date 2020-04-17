sub1 = [x for x in 'zchnixtuølwvdkjsopfåbearæmqgy']
sub2 = [x for x in 'abcdefghijklmnopqrstuvwxyzæøå']

kodetekst = """nikki xjpdik xjp wpæsåipøktfzvtjpøådi wzvvif xjp fbcfåøåbåøjk høsuipf sy iktivfw

szffjpniå xjp kifåi fåit ip iååipkzekiå åøv åjd

ubfw fåjp xjpcjwfåze
"""

dekryptert = []

for letter in kodetekst:
    if letter == ' ':
        dekryptert.append(' ')
    elif letter == '\n':
        dekryptert.append('\n')
    else:
        indx = sub1.index(letter)
        if letter != sub2[indx]:
            dekryptert.append(sub2[indx])
        else:
            dekryptert.append(letter)


print("".join(dekryptert))



# Halvorsrød

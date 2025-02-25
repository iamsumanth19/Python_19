def flames():
    p1_name=input('Enter fisrt name:').upper()
    p2_name=input('Enter second name:').upper()
    match_lettrs=0
    total_letters=len(p1_name)+len(p2_name)
    for i in p1_name:
        for j in p2_name:
            if i==j:
                match_lettrs+=1
    different_characters=total_letters-match_lettrs
    flames_letters=['F','L','A','M','E','S']




flames()
def score(text):
    result=list(map(lambda x: 4 if x=='A' else 3 if x=='B' else 2 if x=='C' else 1 ,text))
    return sum(result)

print(score('ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC'))
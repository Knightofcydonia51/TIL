i=0
stars="*******"
while i<5:
    blank=" "
    print('{}'.format(stars[:-2]))
    stars=stars[:-2]
    stars+=blank
    i+=1
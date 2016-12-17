def freq(s):
    alpha_count={}
    for alpha in s:
        alpha_count[alpha]=0
    for alpha in s:
        alpha_count[alpha]+=1
    return (alpha_count)   


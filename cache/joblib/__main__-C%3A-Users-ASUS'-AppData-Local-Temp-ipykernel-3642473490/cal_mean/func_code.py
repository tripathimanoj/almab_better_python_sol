# first line: 1
@mem.cache
def cal_mean(num):
    print('calculating mean')
    total=sum(num)
    return(total/len(num))

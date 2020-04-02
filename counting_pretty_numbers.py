#https://www.codechef.com/problems/NUM239
def pretty(l,r):
    pretty_count=0
    for i in range(l,r+1):
        if i%10 == 2 or i%10 == 3 or i%10 == 9:
            pretty_count+=1
    return pretty_count
if __name__ == "__main__":
    t=int(input())
    assert 1<=t<=100
    pretty_list=[]
    for i in range(t):
        l,r=list(map(int,input().split()))
        assert 1<=l<=r and 1<=r<=pow(10,5) 
        pretty_list.append(pretty(l,r))
    for i in pretty_list:
        print(i)

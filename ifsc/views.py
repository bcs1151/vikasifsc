from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    try:
        #if request.method=='GET':
        n1 = request.GET['if']
        if len(n1)>2:
            n1=request.GET['if']
        else:
            n1='PYTM0123456'
        print(n1)
        a = "https://ifsc.bankifsccode.com/" + n1
        print(a)
        #n1=request.GET['if']
        #a = "https://ifsc.bankifsccode.com/" + n1s
    except:
        print("expect wala chal gya")
        n1='PYTM0123456'


        a = "https://ifsc.bankifsccode.com/" +n1
    from bs4 import BeautifulSoup
    import requests as re
    import json
    #b = 'PUNB0394700'
    #a = "https://ifsc.bankifsccode.com/" + n1
    result = re.get(a)
    hc = result.content
    soup = BeautifulSoup(hc, "html.parser")
    f = soup.find_all(text=True)
    a = list(f)
    b = a[120:160]

    def Convert_dict(a):
        init = iter(a)
        res_dct = dict(zip(init, init))
        return res_dct

    c = Convert_dict(b)
    c
    add = c['Address:']
    # print(add)
    ifsc = list(c.keys())
    d = list(c.keys())
    mm = d[1:2]
    mn = str(mm)
    mn = mn.split(",")
    mb = mn[1:2]
    mb = str(mb)
    branch = mb
    ifsc = ifsc[1:]
    ifsc = ifsc[0:1]
    ifsc = str(ifsc)
    ifsc = ifsc[14:25]
    print('Bank code : ' + ifsc[5:])
    print("ifsc :" + ifsc)
    # print("address : "+add)
    print('Bank : ' + branch[3:-2])
    ac = d[1:2]
    ac = str(ac)
    ac = ac.split(",")
    ac = ac[-1]
    print('BRANCH :' + ac[1:-2])
    print("address : " + add)
    di = d[7:8]
    di = str(di)
    co = di.find("in \"")
    lo = di.find("\" D")
    print('District : ' + di[co + 4:lo])
    st = d[5:6]
    st = str(st)
    print('state : ' + st[2:-2])

    data={
        "d" : [ifsc[5:], ifsc, branch[3:-2], ac[1:-2], add, di[co + 4:lo], st[2:-2]]

    }



    return render(request,'base.html',data)


def base(request):
    pass

    #return render(request, 'base.html')


from sys import exit
from subprocess import call

pre = "petlja.org"
extstart = '<div class="cell border-box-sizing text_cell rendered"'
endkey = '<div class="cookie-modal" id="cookieModal"'

result = '<html> <head> <meta charset="utf-8" /> </head><body>'
src = open("links.txt", "r")
print("\n")
print(src)
print("\n")


def keypos(data, key):
    i = -1
    results = []
    while i < len(data):
        i = (i+1)
        d = ""
        for x in key:
            if len(data) > (i+len(d)):
                d = d + data[i+len(d)]
        if d == key:
            results.append(i)
    return results

def closerpos(data, o_key, c_key):
    divs = keypos(data, o_key)
    closers = keypos(data, c_key)
    print(closers)
    return closers[len(closers)-len(divs)+1]

def load(scheme, rurl):
    res = ""
    try:
        call("wget -e robots=off -r -U Mozilla --no-parent --no-verbose " + scheme + pre + rurl, shell=True)
    except:
        print("\n Wget call failure. Were the links right? \n")
        exit(1)

    rs = open(pre + rurl, "r")
    t = absolutesub(rs.read(), extstart, endkey)
    res = res + t
    rs.close()
    return res

def absolutesub(data, s, e):
    st = data[(keypos(data, s)[0]):]
    nd = keypos(st, e,)
    print(nd, len(st), len(data))
    return st[:(nd[0])]

lines = src.readlines()
for x in lines:
    print(x.strip())
    result = result + load("https://", x.strip())
    # break

resl = open("result.html", "w+")
resl.truncate()
resl.write(result + "</body></html>")
resl.close()

try:
    print("\nCoverting..\n")
    call("wkhtmltopdf result.html fk.pdf", shell=True)
except:
    print("Shell prompt failed. You still can do pdf convertion running: \n")
    print("   $ wkhtmltopdf result.html fk.pdf")
    print("\n")
    exit(1)




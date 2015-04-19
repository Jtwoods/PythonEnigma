from Tkinter import *

##These are the references for the "moving parts" of the Enigma
ref_spin3 = (1,3,5,7,9,11,2,15,17,19,23,21,25,13,24,4,8,22,6,0,10,12,20,18,16,14)
ref_spin2 = (0,9,3,10,18,8,17,20,23,1,11,7,22,19,12,2,16,6,25,13,15,24,5,21,14,4)
ref_spin1 = (4,10,12,5,11,6,3,16,21,25,13,19,14,22,24,7,23,20,18,15,0,8,1,17,2,9)
ref_rev_spin1 = (20,22,24,6,0,3,5,15,21,25,1,4,2,10,12,19,7,23,18,11,17,8,13,16,14,9)
ref_rev_spin2 = (0,9,15,2,25,22,17,11,5,1,3,10,14,19,24,20,16,6,4,13,7,23,12,8,21,18)
ref_rev_spin3 = (19,0,6,1,15,2,18,3,16,4,20,5,21,13,25,7,24,8,23,9,22,11,17,10,14,12)
##These are copies, so that they can be changed later without mixing them up
spin3 = ref_spin3[:]
spin2 = ref_spin2[:]
spin1 = ref_spin1[:]
rev_spin1 = ref_rev_spin1[:]
rev_spin2 = ref_rev_spin2[:]
rev_spin3 = ref_rev_spin3[:]

##This is the "reflector" for the Enigma machine abstraction
stator = (24,17,20,7,16,18,11,3,15,23,13,6,14,10,12,8,4,1,5,25,2,22,21,9,0,19)


##The following are the "movable spindles" for the Enigma abstraction 
def spindle_III(key,ref):
    key += ref
    if key > 25:
        key -= 26
    
    key = spin3 [key]
    
    key -= ref
    if key < 0:
        key += 26
        
    return key

def spindle_II(key,ref):
    key += ref
    if key > 25:
        key -= 26
       
    key = spin2 [key]
    
    key -= ref
    if key < 0:
        key += 26
        
    return key

def spindle_I(key,ref):
    key += ref
    if key > 25:
        key -= 26
        
    key = spin1 [key]
    
    key -= ref
    if key < 0:
        key += 26

    return key

def rev_spindle_I(key,ref):
    key += ref
    if key > 25:
        key -= 26

    key = rev_spin1 [key]
    
    key -= ref
    if key < 0:
        key += 26
        
    return key

def rev_spindle_II(key,ref):
    key += ref
    if key > 25:
        key -= 26
    
    key = rev_spin2 [key]
    
    key -= ref
    if key < 0:
        key += 26

    return key

def rev_spindle_III(key,ref):
    key += ref
    if key > 25:
        key -= 26
    
    key = rev_spin3 [key]
    
    key -= ref
    if key < 0:
        key += 26
    
    return key
    
def reflector(key):#Enigma reflector

    key = stator [key]
    
    return key


##The mechanism is the Enigma machine and construct the user interface as well
##as positioning the initial positions for the spindles and reflectors.
def mechanism (key, ref_I, ref_II, ref_III, purpose):
  
    key = spindle_III(conv.index(alph[key]),ref_III)
    key = spindle_II(key,ref_II)
    key = spindle_I(key,ref_I)
    key = reflector(key)
    key = rev_spindle_I(key,ref_I)
    key = rev_spindle_II(key,ref_II)
    key = rev_spindle_III(key,ref_III)
    if purpose == 1:
        if conv [key] == 'A':
            a.lighted()
        if conv [key] == 'B':
            b.lighted()
        if conv [key] == 'C':
            c.lighted()
        if conv [key] == 'D':
            d.lighted()
        if conv [key] == 'E':
            e.lighted()
        if conv [key] == 'F':
            f.lighted()
        if conv [key] == 'G':
            g.lighted()
        if conv [key] == 'H':
            h.lighted()
        if conv [key] == 'I':
            i.lighted()
        if conv [key] == 'J':
            j.lighted()
        if conv [key] == 'K':
            k.lighted()
        if conv [key] == 'L':
            l.lighted()
        if conv [key] == 'M':
            m.lighted()
        if conv [key] == 'N':
            n.lighted()
        if conv [key] == 'O':
            o.lighted()
        if conv [key] == 'P':
            p.lighted()
        if conv [key] == 'Q':
            q.lighted()
        if conv [key] == 'R':
            r.lighted()
        if conv [key] == 'S':
            s.lighted()
        if conv [key] == 'T':
            t.lighted()
        if conv [key] == 'U':
            u.lighted()
        if conv [key] == 'V':
            v.lighted()
        if conv [key] == 'W':
            w.lighted()
        if conv [key] == 'X':
            x.lighted()
        if conv [key] == 'Y':
            y.lighted()
        if conv [key] == 'Z':
            z.lighted()
    elif purpose == 2:
        return conv[key]

##This is the start of the tk classes and all custom classes,
##These provide custom buttons for use with this Enigma machine
##using the 64bit encoded images that were made using MS Paint.
master = Tk()
master.title("Enigma")

window = Canvas(master, width=452, height=612, bg = 'grey')

##embeded .GIF photos used by tkinter canvas widget

buttonDownImage = '''R0lGODlhJwA6AHAAACH5BAEAAPwALAAAAAAnADoAhwAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwAr
ZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCq
mQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMA
zDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA
/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YA
AGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaA
M2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/
Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplV
mZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnV
zJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr
/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zV
AMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8r
M/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+q
Zv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAA
AAj/AG/EEEhwoMGCCA8qTFhQTAyHEB9KjEhxosWKDBdqzMhRYcWPF0OClBjD4MaTHRlyuXFj5cCV
MAnGfNlSZk2aEhM61OmxZ8OFLm/e3IlTYESbB2caBfqzZlCDO2M+FcqlqNKkTjnChIq0q8WMEXPi
7EmUqM2gU6eShco2KkKlaN0yLSr2KN2ESetivUvSrUu7S/cuXWqWL8+hgtUCloq46VMZJSFLLikQ
xxYcKEtqFqg5chhgweCJhmdPXaQwkDvH2KI6xqRJmWC/RhN7EiZhoteJjrd7t71gsmO/CS4bjfFJ
aCSlQa57tD17YMAsin5vNGl1yiWhQc79eCM0aSSN/0kTercuSADSq1evCMw9daLVpRkjPnv4NNuV
p4EvGtj6/wACY49u8t1nnyTIpRFJecGoAOCD66kADDzxAJMdGt9tt91+vPkH4YfqTcgbftxxt19/
IKaYnjHwqLPOGBqGN8Yl8aloY3nwkJidaMHY6OOE8NiHRnMw+GgjDLwVKIkkpfVopI1ALqlgPPY8
aeR7wqAxhj3weGilimCUFh4866D3pYqQ8CYJblWeaSOXmACzTptupjghf2DUqWIYo8WjiJ4pQsIf
PHkC+mGY66gTj5mGPriIdYU2CiAYvAWjDp2SrjchMGDAc0+mAJZ2hiTwMQoqkvCEgQOXkYLaKTw4
jO6hiKegqsclMOPBIFqrjSrCm2uT4CCnPUVKagCXwcRwHAzIZqooPDDEhqAMlrbYKJDAyJCgJJkE
wGKXgKpgTzzqBJBJfuGhEUB56tQJzHv2BHAceMohp0V5wBRrJAxA2rPCdiUap5y6xpBrj5dgckmu
vMiJgdx2jYSHXADw8QbdnxDCECaF6vin4ST3PWxfJgfEIKJoB4OhiBntCUhhfzeskMlyHx9H4sdi
HLBFmLxZR1pz9uwSM83IHVj0fQ7ThlwMAcSwSGgKd6nIDU3fkIl2Mg78MMjaTaIcIyFnoirTAQRw
QAAy4ODwbAa2LUlAADs='''

enigmaImage = '''R0lGODlhxwFoAnAAACH5BAEAAPwALAAAAADHAWgChwAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwAr
ZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCq
mQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMA
zDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA
/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YA
AGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaA
M2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/
Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplV
mZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnV
zJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr
/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zV
AMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8r
M/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+q
Zv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAA
AAj/ACXtsiWQ4MCCCA8qNMgwYcOFDiNCnPiwokSLE3lJ1Jhx48WEHA2GFBiS1y5JJhmZRLlL5cmU
K2G+bBmT5kyXLHHKzFlTp02eN3sKDUqUJKNdHHkdTbrUKFKnTJ8ibTpVqlKrVK9G3QoVpFeFI6WK
/DoWLNmPFNFi5MVWIMpISd3ygktSLl2pb+O+vMsxb92Zev3iNRmY8F+Wgnku6gtzsVyajoNGRjyX
o8pabwlibmyZ1+K5mjN77rw5UmjQowWq/Gxa0mbIpDO7Vhy78lHabm3tPX3S1l2VvjvDHX0bNV3M
wUHLXRxcdWWNzY0LZ9t6d2Xnw6tLCm7rkkGVcAl6/xYG3lbn7d41bt4eHtNm8Ly+k38uNy9jvnbj
MpYEt7ewzwCyFeBoz7Em4IEEGkjgcAM6xiB1CD4oyYB0KRjZgXtBGFN25mX4nIembWjecB7ORJmJ
z5Fon4ofsqQhi9mxBaKMK9KYoo0xbqjhjDq2eGOPMMp4n5D5EQZfeHglV5V9ScaYXI5QtoVUdlaR
RGVSV1pJnVVUihReJFPG5+SYEOpmWmsmLUKeJMGoJKUkKLmoEpy9QQinRoZpdOFVd5KE53YvHcgf
dE/px1Zx6rWVKEqHBrpYS3mZWJxNjDyG2FE46UanTwZtathPO8H0W02dhgqqdqJ2tttj8DlHU3Uu
lf/nqqyUKlcrrKJ+l+ustsZaGVw6oVqaeihtNhkvw862663B+coegbeJt1S0KH0mq1bUvmQQXeK9
dJu2cFVoJ1u2uNeWLcGIFwlcn/nWUrgmbasaUrWwOy+Elc6E2buu9acaX/LONhC7kbg1cF/7WrYL
XSn911YtYsb3mFJtUmfeZs0hxZhNSoHmHkq66Qlduqq5FavDWqXWHa2SlPexVq4dWjHHjqHrkngx
b0dyb21qzMjMrgnTnM0aq9kUup3agnJL5D1Vi9DczqwUyi4aXdVKP3VYbaP4PhVybtet5zQmQ1fM
btPXjXfUSbWQ/Zhp7sF7UoaIuQv2b3MTG9OTB9X/+2bbCYdoMJ7n9gfddYUGWvCIK22WlG0wVUaQ
vx3q9TCj4WnpW5wDH4S1RnHKhdl2WoJ+0l0EKev4oMAi9hTDowdqYreD1u4ZZVhK/Hntyr5E50hz
uY7nIpR1WldM+eK5F8iHFU/XX5bl5zzCxb5VN+fVOhwn5b6zXX3ELnE0LLLHDzeWVnmjtNRL7wkD
MfOjLcSw7t0xdPnUmFWnOyP/zTdauRC7CgD/xBqIPc88dYmdeBaEoDg1JYAnYZSF4lOxkl2tLQoC
T04K9bvtVMZvLUlcXTTlOQamD2ud2oXXBhWy9GkKWX3xXMiC0585hdCD8ALZl3YXv5YlCSkBChNO
/1Z1tbkVhFtYY9RRgBUmMD0rNXla27OOY6Ot9SZcvfHdaMCEM+vUJ29OVM6BGCZFGiYqjPBJluPu
EinsBepbAgHWzgYFIcdQEDyUW0lebAgY06hwJQOE2MJkIqP6qZAkgUMWUsYWnM598EYHA+TcdBOm
fQ2kkA6rxSKXEgnHxWuSIQSNdxZJr6YxjoYhg2FKFsm4TE3JTIr8HMA01p+BpMsk/aHkXyq3PtSI
xWnCOEzI/AgoGWWqWElZxCuR4i5yOY0tEERfcDTpNY0ZUCrh05ifVMk2k2gMLIJkCZLipbzKfQ6a
2qRkfBbJKFhGMpqg2eQmCSNIMbGyIJWJ5DQNo//JRJWwYIQB4y7SQFA0EFQSaTBoQhOKUIOiYRIL
behCH7rQSShUEga1aEEjmlCIPlShGv3oRkUq0YkSNKQjTahIK+rQNKA0oxw9qEknGlKPpkGiLaWo
Qx1qUYUatKQEXShHc9pRn25Uo0HlaUtvStOcEvWmLX2pTNFAVZRi1KQ29alUjdrUmQ6Vpl3V6k6P
utSLYvWnJv0pV9FaVjTgtKAizShIJ7pTpOrUpUstaE9lWtS+vpWpKg2qlTRFEMIK5KaSsChCE/tQ
xlr0sW5l6mIhu1jJ4nWxk/0oZG+q2KJOorKVbSxoofrY0SJUo6a17GI169bRQva1kU0taB/L1Mb/
cvanip0tGhphW9mSFq0YbYRve3vbScAWtZMQw2Qx21G8Fre4sd1sZj+L2N8i17EkVS1nxSDZyDJC
tZplbmq/69vKMoKkx9VuQ5NL2dhK1qJjAO1H5ctYl672uOidb3UZm1gzzqVO4dHod1kLX9PG17K7
1S9CycvaA7OWt9T9qHBra1EISxi4IiWvZRn82QPf160e1u6Gf2th2Jb4wqrlrWTF8FrJjoG1Nw2x
JOIrYxobGLS8rbF82ctiil51vApOMGRVLN409Bi0Mo4xcG964grjNrJNFjJJZfzQHr/WylXuLJJN
S+AsoyETID6taqnMXh9n2cVdbvKPEbxZNSFw/4HwgkuX15vd0YZXs+r1LHF/DOMP4xe171Uwm2Pb
ZdjmGaOG9nOh3ctl/LJW0Z1dNKQfzVD1Ljm0qaU0Qg99201P2tL7pfCiNZ3nPXdXy3qWLnitW+dB
a3nRtN0xVBEN6y6z+s9GHMgbmflRL/+2vqH9bI/7et5eOxm2WBYwpZMdWc2S98WAnjGdIxztEHsX
zdLOrnsHnGRJiIGtC1braVvNYBcHW7uMFqlyZ+3Z2k5btn1ubHwJvO6G2vqm9a4thLd82xhj9L7f
5vRi533f84oawp6tN0n37GHUQru3Msbyhi8NVeDOW6PtxXdPqz3uMkc6t1CEi9/eEmumanja3P+9
qoRde/JVl1e1f272r1m92lTXOqFR3jd4Sztz6pa3zpeGLWY1/edz75i1A555x6WM5qKLGk6HjmvM
mRrtUFf2yEOV7otDe+tFzxvdlHXwq6de8w9POK4WfjmtNZvvgYN2NUID8MN44VA7j53RkM0ElhHq
hrSbXNRpaDlGPYzWtkMXsmK/sInrfOS7axQTD495gQ/e5cQvmNXWdvKYtZ1ogjf9o2CeMJ09j2iJ
YzfsO364uSns7dUOvLcPFbyRp53fDgdbt5enc+B/e+rYRv6jmZ/z7ker4YXzPNi1jjKqR+sesvlr
WrsQ2uEhLm2wC7qhmX7s3l2NYe1DttWTTi7/nVnbZ6ha2snjR+2o1f9a2Z+499r3s5XXTGsBF9Xt
tfX3aIlsa0JHGw2ER12MoH7dxX0ShXyFZnB2132MlnJR52+19nPHNWw/x1uw1whuQGDFV3XpBlvl
xwhkFFBvoRJqBVUqVn7YZ4KXlmQJloKKlmff9X3JxXpGFnMPlmbWR1nolnNpVme/52/3V2n1x2yA
RWcqpmrTVWgOWFk7p1OK1VhIWITD51eeRnU9eHxL+He3p12yp3sLWFk+l2fMtnFVVWUL6IHHVVNa
WGkAWH9UhXDIZ33fRR3hJBve1FEyBm8eZ3E3dn5AV2F9R2rTxWy0h4EahglSVnbq9WKrx3CN/4Z3
0aVgb4AGjKB3kgd+kvVh2YaGXSaIKPhcDRVl7CYJbzBjkIdpdLZgbyB7jCZwRXVx/kdvUfdqekZk
pdZZnYd8XUiDCrh6wNZtgcZb/IZ9dhJO0Uc8dLd8Nrd0x2d+H0ZqtbZ8mBhvl3Vq1teE0oWEISVf
FQdRtJeDn/iF3ehW4YhXLaaIw0WGOqhWqjZfJUd7tHWJ3ZiOZZhZroWC+jVfFPeIyniPtKdo8MhW
7EeP+OWG2BheyGg8uiEetXCQlrVu+XiOnLZ4Q8Z5i9ZpsOd9S+Zl+LWGxOeMtoVnzDiGYrCKXMhm
Kad4eAaHNud9WFd92HV0ojdmmfV1jvVdA/8WaScWbrRmYTToUU6WXYxgklc3gYW4aI0wYslGhOVW
erpoaTs5e6cmcZKmjHgmZLqXk7HlOnXyK2yhZyvWj3IldIB3dDr4bwInkPTnV6JGhvRFg0e3kZul
afn4lvYWhW5VWpRGlx+3cAd4jWfpjNyHVhGGjk24ZAUIdcDWWErleJ/IgH1JltnXbPKoj4lmfpfY
j/02bUP1iM4IjJgVMVsjEosAWbsogUpYmP5WY8aHdd4lfr5IWt/2bd5GVSxGmyr1Xdx1Xso1m7Y5
eJRYcZSIBtzVm7UZcN9GnLNnULO5e1QVbt9WbMQ5Y1RFVUZGnD/lm+s2m8V5nNP5YuTonb//OZvH
eZ3gGXjYGZ3VqVzzhp26WXfpOZxU9WIMxpy1KZXfpnWOaHMc9lMtp5WKxYIWdXIfBaBhVlQ6d1qE
+Hud1XY/SGsAR1m5113K14pvFzwRoxHak4yxiHoTZ4vQiISYGJAiql0WlQn1EA30sAz0EA31oAz1
AA3KsAzKQA/KEA01Cg3LoA87SqM4mqIwCg0xqgw1yqJCCg30cKTLoKP7kKP18KJD+qJHeqM2+qIz
2qI3CqVKCqNEaqP7YKM42qRNuqRUKqZUyqM8iqQqSqMs+qNB2qZBqgw8mqQ2CqYw2qRr2qJDugwx
SqZNyqUsugx4eqVTyqJduqReqgxglpn7/8hUbvBafMeo7FeOplWKXVd1mYaazah28Cd83AiTiAVD
j/EoR2GFHUWBn/mUGoaqsnd3thiKXheGHJYJRFqrxFCrXDqjuKoMt3qrNUqkvkoMmXCrNFqrxaoM
xcCrvwqsu6qrytqszeoO0GqjuUqkxUAPwuqr2KoM7gAKuHqryWqsvoqr1AqtvFqsbAqt44qrwzCs
5WquvEqtx2qsuEqj9OCNNShlHmdefjWDB7iH+GeE5Zh8fQaLGmmitgZaWVhlCEad6thjWlmh1DZf
74NPd7ILk4AU7AhsMGds0ZhudqlaAFlqKahZ0CCtzXqr5foOtWqjMqqttTqsmpAJNlqsvfYKrSi7
q8RQrvRwrTDbpSn7rPU6rrTarvNKrTv7rUJ7qOtaD736rjX6szu7rs86rMKqqztbrEj7rlNLrkRK
o76aCfaodOxIaGrmYILphoz6hQ93dC43ixbasGTmY5yWsEIIf7UjFRCzGZihkxf5jbTWqRhHYOjG
fb2He/g2DOkKtEpLr8j6tTNKDNBQDMOaDIrKrEXKuFaarlDbrMUarsd6rCv6q+G6q8OgCbc6CfLq
uLjKo7tqpV87rsd6rc1aujf6q4YKo7SqDKe7rPEaCjXrrLXrtV8LX+X3sR7oeoZGl/QFmq6YfWqL
qg/lvMPFqTFpbgz7j6n/8T4aYS4oAYCSyXuK6ZDIl1ysdZsn+ZGAu1AINwnQoLKsy7jT6rWZkAmT
0LK7eqzrirT2Wquwu6s2SrXQqg/jOrr1S6uim7+j66sv2rlQC7XzeqWY27iTUL/w2qzvyrPPaq+Y
ILjr5YC+hn1jIJEwiXgSZX/VRmmy13YcmWGJGYAtrK83CFvAuG2W5ZYbhiPAo0K/FY6NamBBFr5q
i7y99WqZYKhHi65fS61WGrzl2sD2yqZ1Crky+r9AG8VAG7z+C7QvqsS62r+Zu6yLm7u1KqPlWqz/
28BL/KtV6rs1qqLGmqRxLMU0CrtqPKOBqqujC8Yz+ll/27F1q45lWGhu/+h6fkiiIeqxYVjITWi4
EMqGHHhcn3pTwBIS6gIyY4mUIQmTl5aRdnt59IZ92Wlo53Vc9nvAvnDAk9Cu7Vq/q1zB9asJsJwJ
lHDArmzLqly/w0AJwwDLkzCzwpoJMzvLsjyz9UsMs0zLuNwL9tvKsGzMuazLsMzMzezKu3zKt5zN
tlzB0DzMuqzMp1zL7frLzDzL1JzM4ZwJ4/zN6FzBrJzJkklo1/e8IyyLQwyU2duSrXiDL7iW5Cdd
Xhah9AapimyRacdHbURCvHdyzquSSNi2a5jI7zjPBKYJTDzH8Yu/8gvGVpq11UqvGazRv0qzccy4
6PrEV0ykm+u1XkzGEv+8DDSrtV68uvWa0tDq0q/rufLbxBJcuobXioC2ji7okWQ7aIEmm6q2fTLs
Wy1nhggmsR+Lto9FoJ3Vhb0RM8oDJxBjjnsJaC1MoYk4Yj88heYlkrtXyh4rBkELwLe6uaPLrFp7
0zrrwI/ruES7DPA7u/Fa07/6tLiasxHMrQD8rPd6qITNrEmr0gIctcIbvx0tv7hqu84auop6Yd0W
1ghVYgEbhIY5jO6mz3YXuOU7hhYKmmhloFL2aMIYUdPLj26FJ/7CMXNxYWZJmcB1XG4woQHZhPdc
hq6IBvPrqxFcriqLo339xT9Lr4a62NqKxspwv7uas53L17aa0yJN3bX/qgk6DbmNa9MlrdItu7/c
Pd2YW8DAKl1ud2C4eH2NSY6Sun56SNE898dmXb4f64UIq5fsxoqKFTI10xZnYguU6m+KJYN/7Nqc
mYoNi24cprhtXKw4etGQ67JgG7xwnKNhfMe1+qdWCsWGXaOZ4KYzKqMgnbtvDajK0KQrKq9nXLMn
3sUtOgluzbgrrquuu7iZa8ctS6NCWq9aHMUubqhybMXhpWe9ZnI4OFqD1m1bp1+7GFlri6DsHWmi
bXxjjWiPaNvviJKfNT/B008sYXMQlp/aBoEhxd+whmUOTcSvFQO57MuzXMFxjs2qLOeu3M64fMro
rM16js2+nOdzjudz/07nyfzn0ZzN3LzndH7AvRzNdt7nhu7ogH7Ls1zLPdbJ+MqxxbfZUNefmgeq
VcdgPAiECXaQE+h9h3ZxFAh849aoVwbQh4YZEIOMjKLVvCC4sHZfHSXaIOl31stQEI3IN4UDrkuk
TeoOa0qkSJq7MB65QwreWCzGM+oOZLyiwv3WWBqoU9zhKH6lJw3eS6zEVerc4G3F1OriGy3dbOzF
4M6lyc6lo9vESBzGYyrBXboPMZBZV7mFS3Z3I2qGlvph7KaEOViUAz3PaPnrkunrUsl1kxZeiJNP
j/K9FSnIH6fUjVCKD5Z+CxrElOZ3B0prYmDiVEvt6yq51x3A6qy/Nv8LwResrItdqzmrs2ZsrrDs
u4u9DJZ7xWccvzRts9et0cZF0jrruTcL80jKujegZMZ1bZ9adh0fhqWusODFknN2c/JlgTWVhSfM
z91lmft8bHnJkQaJ1mV2UwiUMOsRLxgGjso4YJy+iCRViiwYlbv4WGHwvo3N3bj6olQbwDNKq8J6
7nxPruGK7hcc19Wdxdb63TDNq8NADDPtq8l64nhNrwJMo6UL+Hy8xtYKDdBNDNrN7i8PweNaDzfg
cyD86ljfXIspeYE4uI7GkmvplOfX28KmiDD26bVlsGY94KbFH1hxLz8Dt1oGmtJIsqd66n/o5O52
YDdgxQns83XtrL3/K6zzqrKBvdZOm/Q8LbxKTO3Ey6w2OqyXu9FuzNiDrcGCba7CfaviD79EWrm7
C7SJDcZTDPS+SsBBKgMAISmNQIID0Uw6mBAhwoFpGDUkiKYRGogDxxTEWFGSGIFoCj4s6DGNQpEg
GyY8uZAkQTEMGUq6iFKSxJkqHQ602TEiRJkWOyL8eZARL0m8ItmStIsoL6O8bPX8qdFgzpQUgwId
CVQlRpI8F1aUSXLSlmjKlLkzq4yeMmJpza5Nu8ztW7OZJmWKq9YtsbVy3y5rC7ftXLODlRXTS3eu
X7aM1WbCW5iwYsNm6xkORY+Y47ebLavlTNcvvWWQB8M1Kzcw4tSE/5fRgzY49rIwUgUCTShRLBqR
GWvuztm7ocqttjUCR141DfGEGKkSfA52UkuRWqHeXMlr19CkRGslZZTUIUqQVg+K4WncpG/pySMS
F3Od/Y19baEtNvtOslu4offmncwdxvx6rTDGiLkPtcnS4ou//UKTa622IExsQQEXnEtBBvHbz8H/
zELLLcbqUUafGF4yaCqpGBFrpKusyso8rG6jzjYY31OIo+OYK46gi6qaMb3dgpKEx4NCQmg940IC
TztewlOqO6aQW4i6gqpkzsffbHpIOKiQ8w3MNMKo575lSDxTGWhIu69MEtH8DLTX9CmwzL7WIjEa
0pQpMzV96NJzmf8/1wpUGbne5DNREvmERq7XHDUUGhJJo7TAQ9c0a59EQTN0U3r0VKYsZTQVtE7Q
+tKnGDrVhO1QvUijc8887xQ0UT0DRW3RfW7gkToU2QN2Ryqbi/GrjCDy9cYYtRzuRoW23A2nrtgr
KUVqJyoOOEmKCmYopZhapKlFlhTzRSNNYvErkGZED6Mfg0XyoEkO2Gg6j9DgaAzeWERDX3zr3TeN
+Gbyd6R24/t34PgYiQm9LhEew+GDZ8K34vj0FYgjjwbeaCZ+/eWtY97Q63ej8xC6dyOL4puIRY7i
Qy++kXjzd6OW9J0IYYERQpjffDfud+SgdWQJ30liGNak3qx61yf/ZZUU6CEdSZroI6h8PQnqnYlF
4yElz0up3Rv1DVJphLAdtsd2l2RkO6MkQSqSpWqZ8iVlg5rIq+vS9jJqYXtlTreXTjzIDWwhMhYn
26ZriJFJirzytkma5fG2IoFTfJKFYLryoDSGW26qyydfLqOcftwqyMk33xynhzKZ6sjSiQtdcxhb
f/xxi1DSPQauGjfOq7U/WrGis3eruthkY2cObSODzEjrr6fjCvqRnOft17R1xMSWbptSiu6i5NYo
JrtRVundYYF0r6IutYeo6fdi0DveeLPVvaORwLq3x/aYTxZuzlW//gnscziaUY7O5znPRWRaP6LI
xpiTIuHMZCbS/8pSsZ5lFfo552rH8w21dGItrkGLOAicVlUyQhIWGgleUpGJ+mZkPsEN60VtawpS
iLILScitbS5anEKs57ctES1aFyRie1SiNRQOJAZv4JxFVDKRRiBOPhrMH+JixL4j8c0lMFqfQJbj
kSwm0YxisdKyMEgs6DRwRwE82QjhRREWLUcMmYgBJpqWvSHp7Vc3oVblxqiSnlwnjTjiCfaax8c/
HvJkCkzhC4kUP0QWRRLfcZJTktKdveUNJUeMH1TkJz8NVq99V2nJG3x3HK7sZIXoWx8TVSQmkcio
NygSS9Qi+UmbrARIvxkjKcOEsiVZS4NA5KXsttTBZ7FvkAchm/+yKmicsMASehmUJBb7iEL/BSuM
KoRh3sw4kCcFAyk8RCcv6LaIybGEOOsxmy8DmZvKuedLEQmTJDpovLuN0jcoQ1t5sKmQqbRkalNU
ZrME9pvoaRBtzkMSMF/yHKyw8SQXtGIg3QcRIrYEmLcp3Cp9lKPf4ehyJqxlAvPnRd740Z56A1Ix
K3g3i/YGgtycJkoh4q1teWeTS9kFuZRY0yHCcKRGlR9BTTIdFGkuj9E0iDiV09CfuFKNNWkWSGjY
TjhmSXbtHKTMwpTME0YzSM3BGNkqEqPDbSshbRVeNkE6BixlryUxyIRMqEfJNVKFqXQEHtgyVqXG
vTUh69LRXwn/+dAjvct8VjKrYSc4UnPJzqKvhFEdmVTYgcjNFkrh4SV5ES7xxDNwuqtWM1t4WIig
bXSGdR4cwdmbOxqgnWRspm+22pw/Em+wLPNSN6VDtDHik3nQcuNr0zPHdmLTIe/R0TNxEzthYdaU
xEFa65zFP9v4S4+SgOK7FIm5oIBFWOg6SUUwAchSjqRLmagReqnKvroe73lp694mGSE37RTFKLYA
S3n99s0oepMhJLkjTQm7re4WBK9hoW9NowJKD6IPiCHhHyEndx4G3vavEeYZuzBbtaQ+k5rIsiZ7
X3m9zP6NjapkHEoFiUTRFRcs68Ws3ZYES2rheCCVrZ6L73vW7RzLBznIGYrcvhUephzFKNZLF7Bk
dEjmSbONvTWqZCsIxaz4DkXYCwrVSNoQyL7IIFTGCFfMSt0EQvCEhoVJSztn397ggEfH5Vpf0Rgy
GwnQaBQG0gFwLMwqK7Kr1BGzcYc5zYT+88hoM+pA3jA9etJ0vMmrKRXFPNmBROlJSrGFZy9hC17Y
8n58G6+GtynMFgVLoAehH00KzcakOtekYdOIr4ZXsoi4FqFlTEkpiSvLmtSGJdQdrGrvm5B2/Uiz
UmT2Fc2lz+BAb4+KleffGuJa4M0XRoh+CQ2r3Dro9lLG1KwrsGRY6UVuhdTb6f9WJOR2yaIElUYu
ddc4e8IibOnbf3uraIyNA4O8wjLAdoxOZSe4LjcQV4wv4jAY59lg6sK3yssd40FZSsNTY/uL3E42
gxetkhNdObleYeiFtyjClbc8xzKu5Xjb85DmgbRHMc+tjabKz8uqeBeRYIQwcOikTT6lqNFNVy2v
YkEYulTg84WW/W50tGK+NoPT7GoKb1DdbvOqabhMdbYHHAawdnxktkljLkGcG7H5+UW8okjLNjqT
vB3NDVxcIOUiOVRgrbCPgLYuxmlcTfKScNxir8qw0ODjJD+pv5+GPEuBFfDjSKsjIBdy1i+X3DG4
QaTCwrS5CM3GKU8iDGUGZ8b/ZnpfVyZk3TAxduwKTOb4UOUkrtWXQ3sehlZL9yBwn4QbGKKxep5o
kcmjtEaCIy1WFpR5ey0i6/mab6HSnWtPr3pUobl64ATQJz09yvdC+/j94RTLAnbz3rUMlB85PL2n
Xs/RuJwuI1JujVzhdg119xIcvBJrBIE7rigPqso9b+o/FtsKwJqJ2usf3HqcXBqxGkqDLTit4BKD
2GujAyq/4UCapbGJ5CEiywoxg2IW+vuKQzsr7BkI6pC533g1hCC013ok3KM+syuS8fAjKjsPjGgK
8IGb0SqKp3Cl3Vo0k0uSY5onLCMJx6k0qcoNwhGwMaqyqKAxnJKqy+ECMHrA/wySGecJtsFjHSoR
A/fDKvgAvv85oh1UIkbAAfLoNp6wsxbakowgOPaSCeGLIFuLsAeCFhjitM3qGpm6OjrTO+mTI5+4
KkaCpEFsDlILF8fTDv6KhKDyOF4aPWwDlqxLuOVSOyNEAzwyROrqOSSpkZIakxUcMidiBDzUDXix
GzTiCQZEKN9oOzizQ5sYsnuBo5B4KLgTxOyhtvWzORyRqvjjG5vroj5rND0bKuFaOpXbDfm4tp6A
j/frPYzgrx4aPx5yCl5QOUaYtKwwrkfSQ25ypPwzkvR6n6eZF+eaFtnpEkjrQ2i5iIUAvkLSiYPA
AfVwmoCDJoUTgzbEJe2Zjv8D9JrboZKo84qRuIE8I4jBY5noaQ6SyIQDULVw06lxqkI/pK51ZL/f
+Zry0aW6IiVYnL1Ta8HsM6k/XAlSkxtMcryf2w6zw8UAWp6LzLZj3Jp3gqmCwITPgxdnU8bsg5Eb
GLl/RAPe88M8FMp8oiCeeUg9Gz4MfKbckKPIckJsGUOXuJyGsLxTTKIGoqsAgoGB2jnksp4aIqre
iCIx4wnBab1c9EfzyylyuTk/+0McrMHxcQpMUCclg5JS+7dbkyNnIcS2zEVywbSy0TB6QUQt2SO6
hL6EHAgZkEXPgZox6KCb4ihkkz0phI6NyC7AWkRJwAGyIyHaYZYiw4itc6v/nRSLMDjAQ0w5kxjN
X1stkMIsP1IxghKj67sb3zMSwkOlZcPN6tGR9VCWlgCS5aG+CjqKoiAtpqg3uHmDZCmwyDI7FfNM
tOQtlkJCxMGr4dGgnOMjSVLDqjpNCrqupBTJ9hC5XMuWMYnBlJBN07GoeJpCDaSIVfrKgqCOC8y+
pnowubSassMgpxw5BSU8bVLJ4qnLlIoW5LhCaarAoqq3eduFXQiX73i3B40oZUQ1UEKzYnG1NMAE
i5QnCstLw5oqhji9MWoEnBKDG9CaGykIbZKsrGCEhrSRG8GB4eHMYmKizRGDLUAm4QpIA1NEfVoS
GpqIWoshCX04ZNLKJeKn/1TzmBiBGv1jGsQjnmqsrN0ht8IqDuz8H0ngDnWCxHmbt1Mrpl0zEhVM
wolkiBdUxIviQJosJHkEpMjsM9McmLWKsypxTTz7Iuv4uhWVgZMSiy3EFwyEs8n8SLesoBtoCUNc
T1p0LigMz1v7EiyboXj5ksNTuOB0tIRb0VBULiSqoVTdpZdAJ77cJHR6ioJaIM4xz/Nzn0fSPsSs
OkrFTjR4ItY6RI/APOVkUqUR0GqrtEb1UkTMqUfaCdvMnsc0GENNTD5NKJHYuoAhmDmrUS6hiPvC
o7fKGPYoRIMqDuV8HlfEHBScx+VkKC4xJlNatF1NiEwosRrUiCA8Cv5yCv8nIx8mhc83tKV0PBbr
S8yTQ5KjsTrdmL5I0833vApMbU/d6JqtO7AyjdghA9Da6JKfSCx8yQRMHUi+4ccb7FHHgSGX+T0y
pC2peDAXYSDCTBvluFE9hRY4Qjw0MhZlSR/kTFmBA1ow6jee7SObhL7G04794kai+KzlQ0+HUKkl
ZJ+jHK6MKiGIUNEeCbv7qp8l2dRmQRv4mhyjXEZbwkHTklCEgFYXIjNM/Tue7VVTSggZ2DTeeZm1
EY7hdCLIeabVtMtajErSY8LXgrS6Spso1NULRVVKCtVSFJZwIkcRFA6OIorA/C+5kZtyqQj32zdl
zLE3KinOQ8ajyas7Qo//rI2RhLUhP5oETFVamEGZGq0iF/wxbUpLBN2IQ8WImCGaJR231YyssOqt
2yQWjemIcW0Jd1WgGU2DWPuVpmEiyiVczB2DvAobLuOm+sosX/LNy73aXJQyZ0Sx4ATO44I37dCh
UGMKp7AWxwpBkBWyGGoltuo+GDw1gniDstwg/IFLfNsdTUMRX4kB1j2enYGZFYRWqRiIVNMbEEwI
G821FeQjjAUcnbyi0WQSfSGbgDQ2LTy8T/SymZqqtPrE7QFf3wrdFyHCmJg7nli3StQxlLwij3xb
XyK2ioiEIFwK6lSKcIkEOqOKU1Ijwgtbq9jEbKojqtus7SwILXW5iji9/5Xgo5IRGKN8v8M7K06D
wdpAMD5iYOJF08JUKe4ssM+jLfiirQMsX9jdp5M0Dtz8YsKbnKTjVYpp4t76O2tqMXxtMC2ktXC1
y2ntN1u4hKNAJ0lMCnsTPODEipFVY6jC27+apBGqNFO8HKAkYHeS2AvSYY81CNMku2+zl/F4GYFc
xhGKrprQY3is4PJYqBhp4PtknsPjp5RLuRtYszFkO3zB2Lk7NFBkKbeLHfEdItCdM0mOXAQqnoxs
St6lUIXAsUjCSnwEte4YinDhjlsFssesT1j9Yl3D0KYLpBjAw+c5Yy++Fz21qNmtxVvCF4FBgy0o
GfNYv7XcK2fRW8uZmP8zE1RSdKOvmQiHLb+LWCVmu13FGtfgtFuBeLCdkLClHFoifYMNnkKd3Mgq
7ehmcWH7aS/a3CK3hY/zmwQgDC1u7I6kSMVJAjxpUy9qvtMg+kP6wTY/jRcTa2bcFKcgJaKIwReE
gZlDZcLc/Rsd7JV7PLOhduorlluGqsduPaGGoF1HjTGLAWb71R99ClGaK2RqPt8GzaaiXZ/LCryc
NGJi6UyRZi7DFI79chIcohvP/ayrwmuJTBKcrJJFpKOCExxfWaG80Sw0hVhGU8EhEQr3OmSIWM8V
BmaDqj2OmM28xtYjYw6gHMPJ7hc9Il72eIhmIWRIPZ8TXhmYQW1hrsD/LrGidtQ8aGs3prmui8rq
8kCjyzPW8aCzh2IWiX1B53Sp7vuo1r6sjXtI/+Iv7nAbpeg2jAEkMA2bvFO1qa6yTxLkSVhH3Xyi
BeNhOsOqj+Ym6EDZ34AZ3hCaGLjHRM3TMMEehZjjivmzkanREe7nBdoctmVtBpuOb31AoeEZgxnX
kYSISTPiPHIppe1OdKtL4jDreSI8dotdudI+FTEJ4KZjIzu/73AbDfWv/cq+tZu1lxghufxOQCZI
tvZkluscK0qRfMFta7oBVu4SDmOEMRwTHIhl77SexVllMZ6EMbhOi6lxYdbE6rgXuDpJcYrZKons
fxlq2v3ZzGZJVY1j/6e5CCnVMDpGKVPS5d1Us+FWN6tKuVZ0XfQECqDqQaf4uf6Sqd/QaZcitty+
lmfeqIH4yYgG0Q00ufRQCdxl6HqOGXx5bOII4TIC1GhBCA3+l/Hwl80OUp08MDMn1kGlCPhqXpg5
zRkKCxzJBNtC5erwlR4+1bysiVGnc7lCHlH6Db+WpKmuNnYFTmBRp20Jl1CzBUyYzuqGPoTbpoNl
UjxupqmBl9sAYGfNTS2Omj90rjAgnKaOD96DGWb3qk30zZCwLC7YRw4j6vKu0V3EDjNiHOhtljGQ
Ta6yGaeuGFxuN+xYiKOp6hJ1vQEbzgp0wm9HtmgKaYRNt9Rz52zZaQgHr+r5Qpch8f8WIb71z5JO
XPJJzvzo1ULQ9FRwE+/1njiRiU2O4DBvBy3OGqWjg6E/8+72vr4t/tmYXpPtO0UDjA3EhAmxSD1A
v03LZ2M6HQbAl7lde9bqGIjDyorGkjNVp8uRM+sR6q5X3yxzPB/rI8ymY56mHi7V+5m+XRC6n/Ov
Wugeo4DkwGOPNOrSw4RzNcaiZHks4oCBcMzkn6+JyNCMTKBlLemJG+CCjVhdMXgDp5bsAKSmIkkN
YoCdMe1KqA4YrR6ZTF/G9BiGTNAEiRqWBD4zF2EZohnm61r1hRC0kbhEZn6mfiX1d1GsrWmaAD1O
l8Pektztl+Llz7zwgXK3JpnJSGT/ilsVddeV4E4cPcJlWGCfEVUK8xo2rLaAE7Poo7NhCR8tb5jl
duXtFcuojN5kvq6RAQse6gW0GIEpd+BkwkmYDOJwA+k5TbEq74rJgY0oW51KHCcl7bqMS1QVLkhi
qNwY27fmVe9OA8PpjbB7kSU+2F43s+7IxoEFCF6MdknihWbSQTGTFKJphEZSGogMEUKsiCZixDEW
IT5Mc7Djx4UIEWKsmIZRyYuSQrKMeFBSDI8US2JkKUnjRTSZoBFT5rOnMooMPa50iRDHFowMxYhB
I0ZSU6Y3SJps2DETPZ9as1ac6LQiwhtLPUZl+lWMWJMVx2Dy2CiTz2VZlykj1hEl/0eRH8VGjIrQ
bFOnYkeKkanSKBq8k2KsHInmYMqajieVZAiVqmHMatOc9FhyMkuqHzd3VFu48eHNHFVnTjhzpcaU
jmOrZhn7aeeKjHgVXMQrEi/ev4NLMulGNW3XoUtjRKkXoUPHam0algwRNE2SMSaRxoxSYabwmYaN
L8ZTqzJ64sNPEh86DA6mKx9HdZomakyIeNe314Reaz3rCRiSGDiEgdNKhTV1n1MFhkHTUo+hAZRW
QAWWE1TzkbQFDhL95VRiTDXFxVQhWSSdYW9sV9IYCH2UBmh6LRfjcifa5JhhVdG4o1eU2dgaTaTd
pOOL2OEVJJJHoqZZGpjYQlBwvv8RZAtvteySGWIIZdJSXtSVxtKMh9Uom0qJNRdkQ5nA8IZXrEEE
V1zK0JVVhXTJSYxcytRTl1UjiSWGG0wtBKJGUcFXVSZz/ofnf3KiR88ydjkGH30MMvIViGi1id6e
izaK3jLQ+NiXWA/VVx+bgp0mmVcwmhiDGyhKAt1DhTLp5nIZDQljq7RyJ9loZ3YX7K6q6cdil82B
VhthtwIr447E7iLQtJJMWyVwBhGGWkZh/ojrqMPGiNNk14lpo3avuUpjJnt2OpeectIDjbzK6BPq
Ty9CRKJEDCp0Kho4MDbaJOktI1eeeyLsKKT01GOnMiiZaqBIuAXW1BiqvigGgND/NGwnPdEYDGk9
Dfv0q3N/2jeWfE5x2OVk/24Wg74uIRnaUFUBi5dXHz2G3Vpu1jQd0D47+5CXQ5YZLdO4oRtmkBkX
xMgltgAnSS3D8Xblkkiullq3zXIJLNEdMVQzRybe7NCsMbwxXW6yKbMPAGGIEQbeed9tN957r+DT
MGCHcYPUUXmUaUPw0ZYGXMvAkDfkkUcOg3+SfhQDU2yeejFUaI20Uk/EiBWfiKUzFR/qktAlGhok
EtYgVA06RfFH0aGd22JMl6ZuQmqJvSNG6qK2tHK+2qaf2iwd2WOWuR5LZJs01YyXtzjqZi1xvNSC
/UCS2HIRjUjqtTiRnze/bdys/02E0+GO2Y7QGzA8Z5lLHjYehj756LM///rrM8/+/IcJuBBDNqVC
TVkEVZgbPKgoswoV/vgnwQlKMDx8qh1f5rO5p6jKJBxTRnjyQY98zOMZ88gHNE6oDBLmg4T62AK9
JjGSiJSKLCBqUKA0ksEvscZn+cHZsjjjplUtCWyjCVO0ikUgJOXMa2hDovNCU76f1c5bQFINQQiy
veBEghHC2B7XVrU7ljQiVrezEfuQIzRwhURJrWnEYt52vpZMYl74o0cy5qGMPCpjHnjURzLwOEJJ
aIIen+jRDZIior4gjT5365CrZpUVMQByHsnoIx8tiUdN5kMSiRpGSkolBtpI7f8+o9QUTXoyCWHQ
4xnzooc++piPFbYyK/q7wZ62tJY/rcQiGbuhpsw1Q6KBJQZbokrGrCdE6jRGMohhzfyOBrTWvAaK
TIuNFd2UsZsJD1hei8j7XjKlaV3NFsGwBSaythzbMbN5z4LMsS4lKy85hjlFfKZLtsSY4KWGfHAS
wywDSo8TptCVKgQgIesiG1Q+5lIrA9FCDlgYuNDjBvoYYSsBWMIRziOFgNSHJ/VhF5NgLjH0eYwp
AxUoA6XEJyHsoyX9OEs90nQeAAzDyWTyFIqJCHbyERF8/iKaOU7CDTHBy+K+NBP6QYZYYJti2aZj
u2/CjEBrsSeZEOMQa1olIjH/mkhk1HiS241mN1vzXnAY4T3gkA1Z6ZMejXpJFG8mS1zcJGNottPI
Xy2HEXCpB/5smsIU9jGjKZypJIYBDU005jQGcsqlmtKIsnROLNHxKl0CG8iO0lSgyfgfSD8pxPvY
zXA/zRRT7KaUSaiSlZwFZB4D2tFa6gOXQblJW9CAucAMalBMIctjZWhVYKlkMW76nULKprtqarNY
ZJoJVsX1kHr2llheSyZIbKdcHjpxIZuRJ163thusfRF72RrSGlOTEK/ilZ+jGiNotIum9AVLX2w5
wAy9S1fGycmitbTpCgG4WY999hKVe48MHnq4sjToBrKBxjLw91nOjpDAGRXk/wAXu6QbxIc+CULt
7Br4EWKIChPQEGEyRPg/WuYRkCIMA710Cc4aXuwiF2sK5laTHQJx5yLGhFpVnVlE5F7kSHEDyWym
+DvmQPG6mzlbErnZRImF0zFbgutTIxIJcw5EGLsBzpQikZmedVM19GMWPA+jJB5bRbk9CtYk5Fff
MheMHhIW8IoHbFNX6mNCytCEmTiiqfowosYgSmROtJQei+qRhCsMZIoHGmCQasIdypjIoGU3KMRp
qp49yYRrXfnZCf9Rk/mTgVxYZ6DSfag+DcLBNJ0LkUZgAr9UfNqJUDPVy7xZuKKJclTJ55axoRnY
7F2ueqmqq/VKN0bWKoj3nv/Ni0UUZFo1s+Zp4PxUtGFamUEWGhQzEZNY06RxjC4oHkWYD4Nm5YSJ
5QmCTfrhMdxYKiiDkZzwl8JSs1jAtRzgBSsiSpKUZSEiKhWtTpYJEQZ4k66c6f8+i9OgBO+RTgnU
SROIljBAkYrt2w5p3tcZzHTcRc7SsY18FjYqCm9x4DV5n5x3174Yjy1OO3YUvwoW5uBmNFTacjDA
GJxdmJWZsZFYtIyilqO/M4hupu6ciRdnbzNxGD4Jw0AxOuHCynaWnlxG4Gjyp9/+yykGf0PA8pNP
Pd3Ajw/vIyBHCPdAdjJRyWhRQlbdlEJz+nJtIvEqG/72jZYQ7hXdBwib4if/szgEMGWfHZlv3mPu
jOQAbJRVRPLSa5uweSFjBU8m2tOeXoinnkNra5eqrC82o4ncvIM6aIhNzSVKmzdX2x60t+fE+X63
Jk+EObLDt0ZSQkTtS7LYkiCFP1GLUMAzHTUs/Ww5wpSq7z69G3PqqAz/OvqgEE+xHwFuF52qDHGM
LEuJOIKn8HA2wLSkMIr1AWNiZGJWCRm7jc2eKYRs4QbpnY1OyJnnORdIbEZyAB+PdVcmgAKFhE5d
/IQDEkN7oEFSrZGTYZu3ARnNQU3SuVGuaY8kbNm1/IbVEETUiBWugRMSmZ7mxYyyBU1WVYQxbd4w
6YQyRINm4dGjDdRHcVbd/y1DMpwZhwGMSwCTwITLX1lUIJlQJf3RgI0QJkxCpEwXfeAA4uBEYZgU
KpnEyQjD/9TS1s0U81XUnlBGz8EHg2mQEa7KkYTE0IyE25xZFbnPaPRQ7N1hJjjgA+phMmhC6HxC
BCoDeZyG7rwIeEHEWMmKsPXQTViXmzUW1HmQt2nN1EAJlPDCfXzLFenK7GWgU2Wg9ahEKSFZmIgb
ln2Vf1QUnmkUi0WcH/WZ1VmOUqhWgiSIfNzHJMDHpeQFBGVU3Plgul0YwCmD5mHOpZiSI9lHiHla
UGBCRgleozUaPYzQB8kRHD7F5mwVvd0EA9lMbcDVPgkTV41WaryGQiCGGP/k4QMmQ08Mg3/AhSb0
IVDACTGAgiDu4QW5CNs0B5DJngMhRvHglWNIjAX+X2lIQvdkzdXsgi0UhJWcIlfhiCO6hnud2Vup
xnP4jKwpBAwck1LNWcFE2EU1Gt1dmCsFGCEtVhWlweAwWMZ8h33ARwMFT3oAlKSR0L6F4R8l1Ei5
BFqYEiaYSa2YyhbGBollgjOa5EDl5P8w4Q1ACkXcn1kUSk5wUIIE1UvkCCfu3I/xTl2VRK6NVWt4
0DDQRU9UDihY3QPiIwH9GTv+WV18Ql2cJbdIhEcCz/NwYsyII7jFDMxFxpFQzzApXXAIR7YIHXBA
kY2gXG6snl6YRl+qRPT/9JM4zkRb0IzYJKJXYAU0nJtMYZITcpQ+nEHoLIkkkE7pXBzAkEgVYQJd
eOb3xZ0J0RImqCWmqUxqOp7GOEZ6pMEwuBAmxZ0ImdAfVVQ00MNgUkpUxE5ZkBZLNeJMVNmq6FWM
eJXTvIg/DkVftKU7sqNcnqUyACIxACIoXBIxvGVPvGUsJgMDhk47CaZ6nVxo1M9YviB7RSZlWNdf
DMf2ZA0XRRsmfiOR7NqMENEyDWY2dSI9fURs5I4UjZZJwMU7MNpsutCE6aQk2CMoMUcY0AwwmUXn
PAQOEI5J1BkORNw0LqFMRWMrtUc+XkRLolZTxA6IcMFMOsWnOSP4DZTb/xXWbJ7QB2XC2WRawenf
b4kFI8jR04CGuF3bPsLTZ2QZs6ClWoYOAaGneoJnWjKghtpj6LBjewrpNGXTtZGcmRrRrukUTcDn
dnljQVzNcBAdcVgbLgJRmDgEYsyRkEjPCx4gFTXCkhoA7BlNSCgDNAQWLT1DH+2gisLin8Gg5zAY
xixnfHCcleXbcI5QpM3S1n0ULxAQgcRH5xhOgygQh1EEQihc89mLoqLYQX1UGKxOXkiCDHBcT20Q
GsjkN5WJjVBnO3EL0uVlVb3FOvYEl1ZpH/qEfzCgMjArMXzpsyorCMHleQJOdbBGG2ZgdMhaIt6I
1HHVdkFHboAg0UHJs/8p5OQZaES20bosxyK+REAuqRHVJ0xcWRvCjScVgz7gAIpx1H/lj9wBUCQc
mGTcgAxIqlm8Gq2WCKrOy1NqasC+X6QBkPgdEYfU2CO5yKCFwWR8Gis9HE19FL/pTwzEkphyBG6W
qqGNAVaiS4nmDGbSUZhYRfToyJUSQ+W8ZV0461tmqVyGp7FaXTx+6QP64VvqH66o3j5WhbxWRVbK
K3bgKdEoxHFkHpwGh9WAIAkeRlt4oFjKlUncq1ainMvV6cm94GRghK92E1LBCda5kqgFI6S91oTA
287djYLITmSdlMogxBgk4Yr1q0G130Z9nTJ0BGWIUqky51lwWJeQmG//xi3cqhAJjdpNrY5hNELK
mkWHJFA37ko0kaK4jcohop57/V4swuUe1eOn3eMwMCB5vm6ztmM7/sQDCu20mqezOuIo4qU3QmRn
ZCW2oVkjlk1ENOQugFG1FcTQucpCnW13fMsi4qIZxdd6+YzqDaBRpIEABiSK5OE+BNYX4mSj9Zs+
DCw9ANpk3ID/uRpgGJy9RWi+uRjcuV0tZWo+iF+2ocEWYMwNWeFSVCohPgYxIKczkq+k+dFr6VFt
ZYWMQQSN3RAj4ICQRsUNcAHUNd3lDNmMtN4cFkbBuOU81oXOsi4+hk6Vlid4jmc9knDo+OEePaCQ
ukqbtWt0WIaY/MrzDWxesxEblMLgdTDE1qD/U9ZWIiMkpnIU2+9Nj30uZp4yYvOsRsaMboEGCZyU
LKP+j0fRXSCF1qMiGVKQxa1yGlIk2kEsWvPRbz7kEfRFWnsAofs4Lt4irAVD0r+41MLZUqlBQ6TN
rfzJCWi8TFTgwAQn44EcCj7B52SsSHdw0FaVWZDY7s5GK1xqglq+7nmmpeoK6U8wKyD+BO5+8iUZ
beXcnIDOSJfkRayY8hgMG0LAZ7aOSRERCy8QcbZk0ZzG2tjEcljtassRCdQyRPZ2BKzoxXPZGFZE
WL+uMY/CVA9Cw8DuAyi9DxoCDGA4BXzcAKDiRLtcWg8uKgD9F8PlL6jWhN0gDsdibKf5zMkc/3Bs
0Z0e+WJA4UAZjsYYiBJgBEpqWfCCgFuQHEBbLOldkQTSeJUMC6IKI/Q9mvBc7uxbcvIw1G7rVs5a
4mx6rqVHkgm4HQu44hxh1EQvT9E7hSAJ/sZaCQdDKug8FZV8odkTU9X0QoUvzydM6HB3HQTgntD9
0hIK1RRIueeXoAXSNEWpDGHApFb2+UTb7aCFNp+K0sOnTiFq1CpZ3Ed8iMXY6WozleV4vN28cJLb
hSxORYP9+YjiYnNPeYSB1GrSlXVI/BBVMFW5DE0Qt2VbHvQkr26yJmtE/8QHUesnW90k2GMfquUo
12Nfa8JT6PKvKU+ZDHQOP+jOoSB7lURDcv9RLfOCnEKJzNmpBU7kJHhgZFcV1T1tEqcBzUA2qt7g
2wrS81WS++WDDVpOdFywypoOGg6OFV5qPfiXv20dMH6WJ/FJI5DKv9DxDaiKKYOCAd+kTcXS98ld
PnABNLgD2vVWSU3CVBTIadrN2GXQMSuN7awt+EgpdnFHK/eSC8OlOlYOXFjdDUTKerM3/aGBW+Kj
0OIUzkorzuqsDP8MDTIH0tl1xcQV790Mq0BvRJCTf0bCsxEd1pygVpWpmvWOuApoJsYgNjnd7xpN
k6zIJxZZRlCUZ3IW/C0lQpHY+HlQcvtLcg9yaaEFUp0xPQBU4O4gE0pj/moCvGHQxRiIyoz/nRjE
AMPiKAgd8B8pA3GK2ooBkG3NRETdKlYfnFR4zkcgnZTqhPGN1SlDl2NoaeqmJ1BYKRqAKVymriBK
X1waqzLo90ML4pgzKwFZT1LRyHkSQ+pGihsQy4YjGZkE5rJZj1ewDUMWBy77hmZby+mlHst5b0t8
idRS0+9ipCO+4EEMTChCXaJU1I1vVIrtUQ/OAxr4R9iBxQX/eKEJ+VXLwKyam3AqMBg+HyxJEmPV
xOZWOa7HB2KczDBMbtb9qGfVlqH6yEcIdS7mpnKnBUaoINOeSTgmk19Gtn6tBKmvZTy+owszqzLI
AD1oclwKiBiQBz2C0LPiQIV0skJbXVuu//iEKxMaDMMwTAJ5rDcxcMSuLYtyuJWSobLWIHr2eA/X
xDSaBE2Tfbbwibg/ChtCjBuPLWJIhoG/RfdMDdQzgFQsSo+mNIhy5qpTnEFqsddBQBArBtRmxR30
Zdj0tc6LS4XsnIqyW8X6IbmK+iA4608Y1DP1HQinCbnLQBIVQukPf3hjY2fQZKSWMLQ63nmzTvIl
JZ5L2bsblolOAMUNKOt5Dq16VvS0MtbMVgwhDUNtFu3s+kTZIN05OjFjQm1qyKmDC8S0Jbpme7Am
QnLX4wwQR+kvC4sRtU1QMhdRYBNnBhaL9nEL0RI9oMEngF3xMJBZlNbonE42b/nDu9hmTf+YQakb
QrWLR0IF/t3ABHt3lTMQrFlEO0dcU07jKvZrfN9WSaAmWrj+ynPYgyhJVKL3Py4GJjQovAJqE9cu
RYPpl6JltGKnTcssR5BHelI0s/rHtZ+wLAcJMQhDRKclO1odJnM9KPp5QWIZgxbHEMcpb2AN1kQ2
njoHdWiGn5aZdd0FBRokjTyyGKjIuqyKkSSKMuAAAG3xv0JaukkCQBBTpkyMpDSS0EzCEQbHJDE4
xIi5ERHNwohiwiREczCTMno39CWjp28eNHol59FLFpLeM3qYOhI7mDDNFhxoJD2MCBGNxIsTNxpE
IzCTMGXzQuY7+UxkvnlHoSENo09ZpoP/B8dsudGTa5iJE31GvDFpksagacpelVTWIAy1GtXGPYtG
YyZNyoglU6YpGTFQApPxFZhX4DCyCQ0KLetwMcJJVxPG3Kts2F69g/VW7tiXrmKNixEPy0SMsCRM
vCQTBB3XIKO3oBOn0ahYzOLasQ3W2iWJ125evBfx+s2L9WucM8s2+hwUruPPtcUUX7s8Le40rs3O
lD5JUgzrzkGX7UhvKr18+kYqPW9e33l9+iTFPCtJkkWuYnpivMEIokQcrhObRJl9QCLpvHnWaw89
pdrLJJN6PnFNNjQYYgS/C8PQ6aGeJoJtoEkwIcklldArqamj0LthGWXKOg4NsPK7kK6f/3yibrYx
YvsshkyWE2o7xHBMA6/JBMIrsCEF4kuZZHiULbzlMmnNrNUyqeyyv4gRbK8i/foQrYJkSwzHjYYp
UxlQhpEEL0nK/KsqG6tjDc7jcFvuOrWEk6QW3naxJZJdepNkN+nQotPJKZdTLrn55kxrTknGMDTA
R2VLw7vi6PxstGgCkOQMMc7IKCP8Rs0wEjFgGEgT59IYgyH8wJoohp4O2oqLrdhCa6AYGPmUwp4+
DRZUUBnZES+6JnHNphkzZGhUTDASIwYwDRKDmHreGIZB9thDSj0Fb6CnqtquehVWnWC8UKInGZuN
uhggY3c2ucoapjAj+bqLoI6qGkimt/+US6y2hAAAYKPGgpREuaG2zEwfIfPC65PBBMLJTtyGwWSw
KgfDxN6+rEIj4IThjGtg2+ilzg1GeIlkuEhs4S1mXvaUM1eRExr4LUJjA3Bn3OJESDnpEqXuIO4O
aPK7SNkaYzx/oV6Sy4Emo5qYz9a6gYuL8hsrBhzqEysi0Dpacciozz4blL4GOvnFrXnqL6z+gFIL
FMpuwOGGvfXOe9q8/bYoGnrCqzHGMGS46I0Mb5hWrSDtdCi2S6dTVCPLPVvszMq0HKxtNPx10MWh
c6y24B2bi3ejTOhxU5mDziRN4nsfk/cqYtpURhJiJtbd3r8ycc2NFp9c2CGcQbOxTtj/DgJ0T0D5
FJQRTGq5HNl5v7sq+VyFsg5OMDMlPnXsgj5UqEwoR25Ofqluv8j2qaZnRWiujlQoib6iCKP8Yhh1
VrUE5BGruY9+8FsGPaKBF9A0Ym9h4dBFwsIQ7sykSAeshwX1UQx91EMZ9YDGOzbYQao9JjaIy9BP
OMS4nYRBfQfJHJRgsL3lfOZOiUHDaM7mF6KcTRNieJPlileXghUMWW7jDpAwMaSx4KVI/KqMmy4E
Gp+hwV5M1B1ePHaXynCvUPJiXvZeuBq2+Ik3MAOUywRFs0M95mQ/U5/PwGicRXlRez1ykhElFaQY
tKtQQPzMJHCniWFoAncDMRvURjPI/yppIkrhiVVBeALBR4rphqSxCzFwCD9/2WuRilzO39SVs3M9
ZCKx8SE03AEN+L1Pk6pUxgF5ZLGHvGoraLCQunhikzh67zF7nM8dj8hFgwRwGH+5zJEIg5dhiIFH
XqTOEAHgy5sZRH1+CUORiuk5HQ4pSqojW9XukolJiOZ91ltgo1poQ3adzDFltMVvdrMLRuwmZrvo
Ik6YZyPIZYJaRIsTosREG+4djDr9hJQ6Y4AJ46hPShthjg8HIi5lpJIY0bGY5Ap6gzA4xCLR2QrX
brVGrlisJ69k5ec0UpAphSUnX3lgRE44FqPRZC2aFMhiFIWQIDUCLRqF4E1iNBEV5v/IdriZ1QQn
tRp12vINpLlbYdzEOx3q5WeIQk4MoAkAcWJNpBRU1UA60pG7BAZkzizLkCqjTcqwiFE3SxlDRzYT
zF0lOolhGfRqIRzhuGw34JmLF60jTLpKkWfqyxUcMcXFzxzANk+6Ux2P6CQBHTIaxGBVbFQ3kUh+
hYWv4tAWuJicoyVEGSYphggfk7pJ9WQhkfLJZjfilbq6jRG5CqABhaJaOn1tVLKiCFhWqBZF1RV7
iEnaRlzDCOY41jFpqMxasyk1fx0pPIM1miSyCgD8eKYRfiUtIfvyvsJMzY45M0hM0EQkNC2jmZ4B
oDmPM8XqNAqfCWFEMCQxM5e5LDj/vAjOPQu3vOsJNmdmvdhCe5ayxRQHE4y9LNF6ptQsDYN0j9MI
gHIGXODWSJI0Zaj5JiFIgiDnNgm7o4YvkqFZSRI/tiPeMA64IsuOll1YOWEaWBxKsZAwTKwZw4IT
sseAJRYnQdJcNqOKl7/0rmI5o5MXsZrdw6zGbYq6kjI391R9iU+YpE2Gm9inCdWm85c2pPGcUiaJ
4AiKzcOJJy8GfGDXuO0gOjtoDe3YPRzTcamCrVOiJgEDHjVieGMepovCgxC68ExeKe5aBHGMCRz4
MjYL9m6LJRUXn2Xko68dFX42soW60otVF+XKOQe6EbDEVGwbws+0Mu3XpcbADWGk/5TGjJSkvrBN
ycN4Q3ePph2hNSe7BcP0mCaIvI3M7st7SesxCVlQ8d1QE/SYWpSKNselxuWf6+xzUHrDMl7ctWUz
q0UarLvU7xj4hSbetnMyPcPtDcx4dIHXfAf67W6jRd+I/oxmubbh/EDkBkEamA15qk4evzCjEBQb
ax2CkYUY5872Te1iynfoNDSCnyp8EQR7kpOuLVwuBdYRCYvKNDREiuNu0qK/7maZvSAEMja6arEL
1k0BqyWTpPGcMV0HJvk2li4OEl3C7IcpniGmrY26jSTI/affvJOv9JEckbtt8+MY+EnUDGhiDUoo
9LXT3ej2kYDZUmR5EzRoPLnPhf9usr/9yFSpr4EM0CS1HBkghGuHE4MPTgi2Q13nDTkKU5fVfVWH
XuijkRSbwAybI8tdyo5wbIxsAJMkJRMkDJI59BzxyB2cF0zwYGTODpeE1m1qBlNzUq4zbTYvMKWl
ts0x9N1bNnXe5N6/vGFUYeuEZ9ioHO00HDbXsT6be8+H5XQCkIkxnPB42bm4k9Co9XcM0w2P4QY0
z555DesiQjFiK5FsCOP6g4M0ZAgxNVzjdByy8bPEv1pPoptY+CkRWopFe2cv80HeIH28r8c8AzFg
Li8Eo0giYpAyJfYWAwdGL5pIqOm4I1JSw/qUDKpuKnzaL8GCr/gYw6DwrcxUjuj/GgM4eqO/5GkX
egFmigOxPFCkSC4GC9A25qU5IMeG+i08vEO14sjfZpA16g5SsA8ouEZDhicskAq5dgayaCrjFi9a
KITF8ClvwCeIyozpvmOGtiA/vLDVQg4izAz+1o47YqDw7gQG16hScs1qvkx2CII69A1MVCACDYaX
mqMs7qI+BCRi+qVISKjsxvBxvu7dVGfpsKJnsOcq5mmv9GrNhCE47OnBpKTrBNFQyssEQ+/gwo+n
DmwADcKXRsvrIGPpatBQ6K3isO94YOVVAi8j4OX/mos+CPE6giJ5jobDGM/xnGVdbrCo4qU44gT7
9McngAshFkLw5As62GI1vEMQ/+UIJ3ZHyfoiup4Ikwpn8LzHDgGAsVANTm4Ah5DMc8LpF5VtCJMv
iJqm3+irewKlnnhDT4ajFt4Aj2ytyxJxoeQF2ejLAZUtQE4GBt6g9n4GR+RlaAgsn3DDIMxlRqIj
Q/ojw6YjETPR1NRi1MgQ5B4Sx1SornhC2wiwyLyndBhKJ/IjbO7jcBoCzUgxIQINDbfQj1JLSWQn
qu7GXq5nUsCIG4moHWeiirqEMNimMuzMm/5RTqxroGBvjj5RG9Ng6vbrnfAq9xAs9grF1rZwHTmi
KSnFhuai3iQhAB0F78SnNZDDry6PfA4M+0SpIFxNo7hiC2SwsJypwgyiltRFEu06zQgzJDYwgWnM
cuFmoy4TwlVmhCvIT2xuQDYwohYTb3J47DlyK98kY22gKq3Q0DUsB8DOgiclkAOfQw+fijIEwpju
4mqU58OIKtZMLM/eYjW7TtNwIveiJ3p4wRYmkSK/qFJo0McoxeTkBQ/LQgwI6WqEU5ruzL1W8xAL
8czohf1ADT/AxidkIKaG7PXmghEJkGeChPyUQ6V0Avsi8iPjrd8UbIamBT8Y8+3AQiE2SiMwATjB
LzGO6hedi0Ue50tiIrq4pJk0otbCrxmjjCetInNUxyA0Y0hOc8k68DxjEzbjLDhx5MdcM46443n/
9Kvcci8SMm6N6soS/Yq2MMUuX9B8IGcSJGMYeAZeYsMNSBRSGjTCzpE5GmUiGFMjKYIxF/OFkirT
sPMDZeN/YkRdKGLkbMTDXkg5AuYbhxMxxIALgkqSGCI2iA9TwtI7uoxLhiEnc4ZfNHAvMDE2W0w2
PNPYQnM+CwWHaJLXqA/6ZPATv2fMaqPQFlHPsDKNBOWd8qS/bOFiWnMi/Upp+lHW1GczcYMfDWJI
kqEY9C0NBK1CrbTkps3SCEXU1gJ/jlCodixG764E/6rMQKMgIm5v7qMXpxAy/Ajhmi4f/Y2BZMSB
duI4fDGp3nQScOQMU4e0NM/94OKG2icT4rOx/yQPazSiTAFgo6jll2YorZ7qE/xMN5GHWrpTpHZp
O63D8oICR4pSegIlnhpRElwm74jHzpjLn34zaJZrTjhurU7TRpiJRXssH+HtQYMQw67OYhRFb1yN
VNQlb8qiPudLUWAw2zBRI6YFqIj0gVjoIbJHvurUKJdwVlwjXZglPW10JOtsoDLBwbRTTaQKLwp0
FBdlwMJuRp/EWAXPCQGmLoxOaeT1KhRqEJWnuo7y+ar1slpTivKEZforKnujVdbNTkx2WzkTHf1K
Jm0ESSyzY4/mGXUwKeFLhgjlumpFRiIuknoiI1ylLPjxZpSKZFAmQOpsLIxQLO5DDBdiZHfz+/8G
StgO4ibStvH0ByI6jlWr6/OCTCsNApv8RTlL1GhNJi0mYUCHKAZuoNguDzyWZpioxXLW7kWTDy2X
bgjdjQLpYxfiKR7zxDc+1Wgf1iyX6hwP9WYPpZImo4pU9IXOsNK4Ci1z5jVI1/ti5FeiE6YiKRY1
7loDtB25z+FSEqbEBimFE7lMUGQep5SIdG5PaEqt1ThOBmA1ojJ6h5DehOuAMNZ6hHANxl+ya6vy
7HV/MPaGbAtB7Ub8VtGmySlJt0dwMx7zqtzydBLLMGpXzjOIis5k1ZnsVDb8SEsmA02CQs+kydQ6
1HXl5UwDa8MiEtQmAXHEYjrwcJc81S7TpRj/o2MnYGpquchh5cQzRC3uZCQjXFU635PkLopedoTO
fO4m0aSHhIJ0TA5S6486JuEAsqoeiuRwoQlwPzA0/apoEa0PQTZVa+xmBzVG6UM4erZP8JQ4nsNc
rXd7yPBZRzf8BmNiLkMZbCkuMsEtxKQqSdL7ICdVnWTP/u0IP84isFYu6Xc59xft9rUr+gM6KaT0
zpT+Yi+wlgOE9Ye1EAK4WEgpaSLsuqO4pku8dFIYjc+Mz7M7suoThkR7bcRQuUpZ10le0gpqBuMs
fIwS0/CTs1Lj4GgFA+VlqK4WdvP28q5y66hWg4Jolwc/NA8vTjNknWOAlUo+C+eAoRDf+GYK/1lM
5BiC7i7MCdmCjA0YDbQiLGjEIcGijiqUvtK1NWKFKyx2bDSLhQqxaw0Fde5pdtAkSa63LHvMXh+W
JnR4iKwFGsSge+ELdEuRDE2JLaIjZg/FWizjNI9kXIbNbUH3YgpqJC8G6oQhZvK06nxjOwi5sJTH
IEVSdQYthssCjmJiKNl1APNWnUKPOSa3dV/jZMLAVcJiwzZMAKdveJnULDqMwzaMeePrBZuyR8VE
tpj5hDhkCksP+LACE6QJTFJDIHpnq2APBJUHMTxzLNoFpbFDFRGNEefjNI2kaoAyXXk4C7/2cqTj
zdbsnfK0ZeTihWpRt5iy5oQJbG1uGKXG5f8+pP1qj9bAWIMjtH6TLo46klT0ZpjnpiuhNusukqN6
caS1ZiuAi1P1WFxTR/qi1CT1RpfmWHjd1megl2H4c0jq945xYrg6FE1bxDO3q4x1OQ9lcXfjgzKi
6toGwid/UKmCkzXgsTfgSdz0RNjcDenAo5+W+kcyu4ChJCjZpiNUdNRuaI8wq7YFhilXQw0P7DMW
QgZeRG4y2FkWIkx7tTEQ5YuQZSaYmbWO8GBdGl3t7qCY8OsuyhhTbCGA61ZIKYrrQppc1Feh2kvt
GTbVV/hsxDUmwTNz2nXfGPh6xGnQqijewEGE4TQNI4i8B3J1KoylgxEuoZ5u02Vaxjdy87b/vw34
htr9ktnWfAiqkOS0keog4OXgEteVjfthfzReANlsbyBxMkQhJIG5/YyHkc2Y0WDFrDBaGici+O7U
6CsIFdG2Uqqao7Rr+GN/ESt1YujJziabCGNVotlrEY0ZPxUNOHsLGXoQYRQdMzAZDANk06pKtPg7
KbffvEcNaQ5AhGOedi84XMZPYoahqTidesxk1U4hzccWyyKZdkiq6i6hqMwKM1w1UxOMmHmBIVJ/
ZMpygGihyUc7sRPHWvpVw8AHLsRxdsmhktmVV0wnGOLR6KIiSpjOgnZwPWwo/uLZzgQv7i5MxgRp
H1QIOTtOAETWCTZZPkxo72VVlsFMxukm/6/mkl2TzheXWlsmGFobnviExI/0nKQDGg8tjGhMdXqt
w5vMqDxUqG6i7sZMlUEDbPNHo2IFIjjtVuSyAP2ZHwU90R4NcFpNMVWKkkJwMSRELZuxOQZGpLHd
dg/ddp/kjGVKLVCnMYbkL7DESD6UamO3zLQX5/wz61y9c5FULdQESUYDTexiIMpkS7UxpuF8EafI
v8YtEm8TXMcNemADODfafmuIm7NS2tRTnYRianqndyIeSzNMWhYCXs25xNVxkhOiOqObuTFEQyRO
Uih11HtcDGSggRyOvIO3XSKr5eF5MJcjf/TjIsSdvA3NJ2DtoALQvaSGbfpiYkChnyH03f9S58OZ
yYa58TF2/hc5sfhyQrG0CMwcpDI4STRiTTUREYKpFWvWnPfyCgVpyCIxGuq3btAPZWgUf4odyiG2
pOAlI1dqo4ZDtReBQr1HMFTX6bX0Z/3sesfopZ9yFfGZK2sdyCErIloaU88qslzBulpA6SFvWpK4
IJHrI7ClhRN7uqZ0KL0ohmDPV7QHbC0Wvtga/ntz2fQLH7NNV8+3qShU1HZ8JsA6uYyt441oE3rS
HHp2oXya3fSKQ6fBG90VLad8da0guUhOfTl4el4CGwd0aXchllySmXiY/oSAd7lxWqUAYhIagQTR
SEpzMCHChQcHoknjsGEYHGJwoAkjJqP/mBsZOVIU47CgQIYkJYVEw4jkwIQcJ2ZEo7Hjxow4FIYU
I2NiGI4hY9jMpEmZMmLJlAXVVDTTSIVMF6aUNKbpwUlpxAgcaACA1q1ctwps+DXqwoUhyYp0eJKg
mKJBhykDRZTY0GHDDDJMGzHNU7NiEL55ilekJEm2dvGSVItXJMWHE5MEfDbyw4R5TX5FiFdqSYgE
Jw0dGvdT3ExVCaaJkamvJIEcb3A5WfUgo8qq7YIN7DAmSJAwdzvE7FRlZKuT706yPHCSRoy+X4qh
DJvyWbNloSYUi6aRR5cY0eDg6Bzmb4U7xcSYyfCAyExDkwWV65YYKORNbXMejyZqxOpo/7r6BxBA
Jg7tZR9lDUmXXXGr4SaXfKMNkwmEVumn1mXj3bdZSPphplxBkigmiWGSLBaJLYgJU8tDgBlnl20J
WifcSWIhOJ1lxAmU0kBssfVZWwXGsBJnGpUk2WZnNRKdQ0pJ8oZmkd2GnGQINnUjGgO5QVVamlm2
JYeZ3edhSQ+FdFuYsyGpXGtVZuJTQXF9xp58Q5Fm01MdFrhQQWKFOcl/XYUh2VlTnYQki5Phd5VQ
crFHF1154XYZjZXdJRZxTO1iomK28MIYp5EsGGh+muFG2WZMURgddZNkQgxRmjSYjFxGpYXaZGHK
BlGZQdrEFFqR6gXcoaYupNpIFYqaIP9VVN55K6pkZUgWU6rNOGOVvzp5m16R5XnTS5dNEsMbA4Ek
FyjxveWWWwWNdRuaBX6Ja39+blWTquOqdSomMR4XLXUDMUqXUhea5G6otwIrXUJLOcUYI4x9yAsj
JBbZZX3uFhrqsxUzJAZ7QQk1DChGxSpgQWwGyd+6oMK214oGJ4iQlF7yK6m/wMG4LKS7CsnvbALN
OCxudwWH7FdXCWqvZG0q2aoycTYoMo4sqvxYhgtLMu9WgFqrIF7DQqVgSUDfFnZ9DSFZcIsU9wsl
L4bt8qFhtYTIS2FeIjS2xqaehPOGOK8L2aRoxKlMyA3COe5CPuXKIkNXl/1lSrPhjWf/l/eWzaFU
zOp89d40F0dQxbDhOZCXKxe6M66lSrVnDCS5BVd75n4mc81lgnQtRFlrhcMkWKKUobSXPTXjnQVz
nZdAadeOOZT7ahmJw4TBDWKnxfn8KNJRTrp6zGhZnWxahbcHH5zWAqn9Xe5eh9zXJTXJcaQw9zp8
0idVxj2Y9x89htoKEWggxiUMYTeRioJG4iudiWlxDdGEW4Yims8MRV/7C4ylNtOymMVgdwmxStUs
d5VSce9Q00GSTRamMzQRZy8GRNpADLMY6jWGMItx31OqVBq+peFgDulf6Nx3ocEZRShtgYtohlES
1BCHWwUDE0m0BzSdlYxInMtOu8pi/5r6QFFhybEL1baXxTEoi1sLwxH8mnIcLT3PQ1fLhHpsEydQ
xGpkr1LG1AhVxYNJ4gC7K5mLXiYSKgYtUBeUBNe+qL/O4epo4TvOIuo2Il7UwjCdqoX+PEcmyinP
V6ZSWf/ORsLnOIVVoHGPUBC3MCDBZDbhEU9zeuNKV1Yllq9sZUxg2Zzd1NJKseTlLmupS1i6Mpi5
7OUuh4nLV+KSlrQk5i93OQYYTMJNcWnLZ0iGt4IUyiQJ1GGUwLTBrE2zdCZhm/vAiJfl5c+AOBvk
5VB4rDsNhjGb+lCJDrMYryEIIaq5z5YauURDApKcTEtG7OATO4FZJxMA2Mh3ZsKR83a0Ric4oKhF
b1AeiUJ0o63hgpo+ylGIehSiOcHBFiqak5yAdKUhjWhLWzpSl8rUoxatqE0nctKT1lQnJd1pT28K
1J0e4DaEGwpcTKkMRsoTWGurYELeoILdLeUhm1zY5JrCwsuNK4E/a1+vgjMzEhrEmwR8WWHs//kw
uKnVFjFS50B5ZRb6CY1gTBsfUg6aVIJOAgY44AJOg1pRLqA0DD/VqQwqElPzzESjrmEpYz06UsYq
tiWAdUljNwJZj2xhJoSt6WQ/e1mWsvSmP+2sTWcy2NKWVKek/athXWtTafIzDcNwkGgM2iBinNF+
R0qVZrJ2A8zsUzYXAqAmIfUysIhJWZhDJGXcZbr7uM1hu3AYpxwWwzseCJMYXG7YvImbMbBniLGS
T3zoVLpJHCAG7G2ve1fg3vjGAL7uhYF87ytf+sZXv/jtr3//C+D9vhe//G1vgQOM4AQLeLfn+oxc
ikKM1FhOriJhIUPGoK9y0mgqxjkhog45V/+8sY86I5YOcVSoq18psiSEOQz11IqYw7AVeB7m4VRr
tDd3UgwoD5QVeTXRq9VgojMhyfAZS8akJKdBX1TJcBqQvMOpSPkN/DLZkp98pTH6LpBb+qEfA8WU
3R5EX5lICJ12SE4qh1nJoNoyF6uMJTJeOYt+LLNfCHLGJlkoKBG06zCCcuaNwVWUDxFlAKVMxlDC
dTWGlqvz7PNH+1jYbPqr8QU7fMevKAZTIWox9R4JlkKS5JyoYqRCaDasSccMTqTJRIRAY0fpQOSO
4MNkjfSZyEjLL31aFGvGBF2cyt3Mnb3eta5DTB+ViIVVsoIIqyJU3gSaEGGPeRKx8kScy6n/jrcP
cXKqTEWhdpJNJIZOtHPJMm0NB0eRHxpMdau3GLeBz4So2naONolGX4tKxJ/0kpIeCGSNrEpkscqP
r2T95kwyWpuQGpRgvMdlMSbL3OTsZJAAKeg0NEJhw0K1uLPouOqgWcv4ezhUQK5wtxTlOC9x9QNT
o0BDctuFNbbS5nBc4kzjWmcgDowBjfSbFj3XIIXhxSPdVrd45zOsnTuWXHcraoGus2oGKYZRV5MJ
TIwL1rhmZK5zzTzGBTuBhwavHsXkz6k3T0zBntLAgncfYa2u5KNTGVmbAhrSrGpckqCLXFIl7H/W
jumVE9y9R3inSrMo39ZWXfNsgiSFX1hh/2p1MSPQaosShfGfeJnrwa4lVlPNTmDvcTVS5vS1iITp
XRZq/QFXovrAeHdt29MrVUsXHfmRmDMZ097+ZubwwH/X49yCV1VIaZQhx0kpEBrK4lf/srHdJJ63
n3zeXnbOsKok2fbBnc3nKvlG8k3GMf7Q3Kw3bINcP48BFTFEIDV7UhIDQu+ZU23lqAnsSS44B7GK
/3vGW1axf/0XTz4UPtO2RJt0XO5CLR2kLBRiaNRSOi3jEOp0MStxIx5UYtPGgDbygCPGLEs0gHpR
cSNoGYSzKh8zJ30nF73Gf9EFNgWRODi2H92TGRY0eJBiLeC2MwynQmdBVpA2CRJDPXSDVv8PQ0W9
BUJRdx+MoCeLxhcIcUp0IgmupgwgkXe2pm/ZEz4iZGzRgijfJz8DlGySkjtklyTMNTTqBmmm03ac
IUBhdShhaHz0UTZ9IRCsIkcCcxyakAmA8nIqkn0xGHh3Q2GTByYX5HWnsl1YxV2OuD1hRWEVuHbI
gQnWVSIwlnkOY0mEiGtdgj2zp4P1wxQ85jSpgVL/Iit2Bng4ZnLDJ2hjlHH1UXHZUmypM3J16DmZ
8yyhUnM/NCgp1nlPlD3CBR8R1hsbsSoR8iqpERb/ZIiS6BRTpyurkzdexYOMaEFDJ4ow8naH54Hz
wxCMgCJx026URD1j4nue1Ih3YYtrJHL/TREh7LEqrbJlVsIomvB9Zih5v5hHFTRQqhKNXeZbojhQ
00Em/0g1/4hGUEg/T+YgVuhq+vIc56U2MmIZFLc2VVUchiaDB4lDObdPifOPVWOQBgFyHsYUdLMI
H7IpEfNiEDceDfiNxEh8X1WGxZUdmDB/EJIGp2SPhJMJTohHx9JdoER9VsU4LIQdiddOTJmRUEk0
7rdtT4mIqhMVQHN4G0csHHlzjSSVVQk0F3Qj4qYS4xVhk5BbrkY4tfiCOHN3/cSP5BZynSOOgvd2
qaMc4INzw9eG6LQyHfIhR9dpnyIijqE2IHYrXAhK7hJzitcQxIAJtbUqc+RqhxNsjxM8/3LnW6FH
aXO5dseGjSsjhkGHQLpXdwr0iRrzlwqZPK35NaMBFKvoGQ0iQF3DjlSpYwWJTnqUbR6CexMGg9Io
dSbnPdu0e7cIMYgRN9OldHoURDiHiJNCPCLpficxDLwgH2z5KkMWO0jkeIAEcZM4eKKzmEQyNQzR
jqtxM7D3K5kUe42oRrxiat6DZuj0JRd5blJRJUM0DMvoHvW4h4EJafxIFk1ZoCLWioIIQpwkfssj
jF2VSPHDmZjkVvtmEIzwYpJweZlSXbtAbbpolpLyP42DHFXyVbRVW0qxKkzSKqLxZRdiaHw3W+9k
oyGIffFCbQfBld5IgJRTc2+5o4Pkj//mFCVgoSvTdpA6U6KMiCFQQTiaMGR5eC4jcWIXcmsmV5X9
YmyhkkI0thmK2TzhQ3hemRbtBzy6Zo6M8TaEATGrWZySBo9EmosvAyHn8mftMRRbZTBaaCgfqZ9C
B3z+QnddihuBOnPq6HMyOVxLAaiK9IalGSMbY2EGsSg9gqlIRiqQOSOZuagZ6aQOGIZSIS52tzBc
cx3w4ppDqhkWViLm126GOV0guk64B0/fZxWgyZfUOBABAyFQsyiV6E8TeiBLKp29lnCDdEk0IpN1
OTC4aBPU8XX+WCONx6hotz1TkodTSD6fAT5MwWWDyCH9hBlpU6ZbCq6kQ6Bf+Z6SUZr/k5hxIUEi
LrYp50c3lPio03eoYed20DViMMOTwyAMAgtteUV8qjaaf3mVwNJDBMiU+aOYqKqgaKNDZTlbAvUc
ygEjz6GVCEGxHVKdYjGA/XM8uBKyuEIcWUlXP4iRnrow8qcMpsQeo9l+BDggz7NdibMgXiV+h4dC
qUo1qhZpxLViMLIXQQsR5rpdBPIrGhoxkvQwmyZJTyqyOhcq/hpy7icQTYJDlTESdzoMk/mfpilW
ylmntXd2CVGNw1aGw1qrQ3ORNriQ9oIWDXF3woW3RRqtSBqHcDqIHXM4shIouRYvNyZsXlO0mMNC
sjiNNpYqp5mfSIM9uTOL6uk2ixFJ/5LUbpyiQzehXaoil8IRkmdKuY7jh8TASD06qakHuTSYtgpk
qn4bmObZcO7zQ3YhHGaRt5BqNEI4Ki5ohlWCj2wJc/iWt3eJEBazb6pTSOKXeqDUsCxzH2gicyW2
K3iCSFlluFWEQe2WGNeFCXODKZHAuNm6rN3Ib5OIsKIIEbNxe4aKJiRIsRSrslmZIHair04ppE9R
nCmxSWmDJBLIjiqbTTQKmiF4QsmrP7J3NgaarmxDugRzi3HFbW5VH7PnfYImfYnHJ6TzFauZvxV3
OYGDJAJibjkWOByJEJREItYlY5dgCx58t/+apYKac4zwFywCoSNHV9LKfWlLeHhbiP8TDMHQmUZF
ay+64i/5ejVeJR26x31A1Lq2GiOgm0YNaD/UWpq9xbgoF7v5xo8tZHu+GHfpxrYYFEJ35LOHYsYm
MZgQswjCsBiLwMJUIaakdsB5aZe3qoCFqGraF6GIe3cJJBy28zy7F7fBYqyqumK8yS236CHaOp9p
CDkc6Y2GOxKVihxZFYltq0W1scgdvHjJeZWO/L5cQ6EpCSYcKgyFQY6bYgswPCIxbKi91qk5+rme
PHt4CajBd55mq8WU68iQnEd5LDMVR3tPepKuZxqdx8x8UzBunKjAeMu5UWVvB5zhyrSC844yOhxF
KX7la5PwgiCFsr7cJBnU5W4hAmPPnHIYYpNOXZjECqqbfRqOXnqrZhk4G5Oge5GrsUGVEqex2EG9
x5XJHouvl3OhFyg11hEVK6Q+N7t/IysbVTUtlDi/1uF/wCI52YEwlSKkvzHKnazMbqnFuss+A1Nq
E2e9B7PGz1ye20eVLvusg7s9aAI3ifFuT2sYLYnHYBcdY8NwgYrJMzl0F7rMw+w4u/o4LyM4abS2
2FiQ32cvysyP73IglXy3fAN6TR2LzWOAaZRu+wiP8HqNXBU5+CqmStgv0mZzGWw1cGfM4mgbh+Fi
/53GaUbIoJPRb1MCgwiKQAqRNg+Km3KXiIS0xML6merpXVZr0g76zN6zriHR1dDKLcTIIZzhy8KK
bOwSxKNJgrrpt9OUgViVKm18TtEpw409KkvhwB+0o1bysZ0dalsyy7uwGJkSIvcUCWKTcMqrY35t
nRvjruWpr9ZhwCrC1x5m1bopVyS4FBvcj4lkKZ36mEA7VgEJ2gmr3UyaBhfGkN+6rH6TtFyoEm/n
cFzCsIl70JAnyBWy1pNSuknKOf1EdOHrKTCJeTvXzCKBJSgKyGjG2rrmf8J9nFOXzJv6Py5is8cq
k0gLhJk8OnBViwY40r8hg7NohuoWQKod4aVpQv/u2TVDWp1aba10RYrxOMowo+CsWzlRp28Uox91
4thtHBhOOxhn5Tb1ZBiqsj2TK4RBtD5x2CV7ydy3w8edG8zezWHBF8azxoaVDWz8IqK9CToiPkbH
tp+aLXbKIsZO8tSxV2vgKqbBvDcOvUgimiEWGIZjlBJ3vN3f/cnO/V1f3hhus7mzHCKde5QMO7ve
lTaEiC9J3dThU7XaG7myV7dl6sHkyd+dreIH4dhSnXBF3a5Y2plvJUi/QZRKhZLZHeN+Wdx24TLP
Oty5HKIPfGhfU2rlFsgJTkih02kwWTcisuNWrcIcjjA1W8BLWrnbPVeVUhAstD7YUZzGY5pXStH/
VYvmGH0vV9oh/4cSEVHgAI2VUoc27cvRmiTty853h75Vx5O+2y4qh17I1xk6UZQlsZ7QWy7YwkYW
+tSUoQuN24ZJVaS27XnptRPW14N0mAtjvD0q4no9dQ4cxtXDmokgPovoMK1DJd10hKxhrke4itfm
79KebnmaSszxOZghTH6tVq7A6LTeMHEtgJ0XBBLavfkch2Kd4AeMgwyA6Iyvci3qANnunRfoxiGx
DYEJJgI3RydjRfi/TjXSvJZq8yy0sF54RTuLZKXpwUfwR1OXhogyQMx9FaNI2g3UudPWXN1FfUlt
1gaEpVJVYkeihIecyF3FkW7N4DwcvXW+IxrR/7muM9IDtSMivnFjSVpeXMtq4jM8SNVd71LspJS4
bQa8J2jB0I+yXL/u2Nqi5iTPxDF3kV2fl8P52+XtmhoLt9sWzUmI4X4cXXC/MwqLk1oIRhOG8nts
+p7PGLWACUI/XS7W544uGdukH0qb8wnnmIyU86YCykStM9xT2bfLhvjO6GNOcb/Y2qBuvr6s65rz
elgPLVkNesPmv+NWoBj5GCI87EsW1tAdhFJi09KbFu835NWrhVzP8UbHKYWJVq+6uu9I4+vJ2dDX
Qw4hZqwOEJLSCETTCI1AhAMVJkQzqSGahw8XTiTo0KHChxclTaJoEaJDghUzosHoMaGkkQwrpv8Z
qZGkyIQa05RMOfClSZs2HR6k6dFjT54bg1IkevJmy6FjKqLsKWakQY81Tzb1WfClQkYsUVYFqXRh
w4lIZQq0KEaj160kh05FKIlXJF6MeO2yxcvWLreMdn39mbbvyIFoiV5lW7RhYYRo0IplXLQoVMCS
lEYuW5ZgVoGMXqLljLAzRcGeBZpFk3WSmMxYVadmPXkSZsmiWTZSCPkzZqUc01YUs9rqWJanq0Ku
jJR4Rp2IG4rJ9JBh8MM0VT80mJgrYYWnFwqWiFnn2u8gtUp9aVXScdbObUnaxUsSXLxx2++1ODEr
boQOj/ft+NA16dGu+42wMXyyDzquSPPtOgb/sQsJuqmQE6kqlWzKTKqv2GoMscEE4iso55xzjLfV
RixqKgX9Qiq8q7ADsTgDYxPqrwbrqzAj0kKkUUS/UkRwQNk45A8miuaSK5K63GovEkls+YinDV0U
zzrFmIqwwdAs1GpLK2kSjcfvDPuxRvA8PAmnGRkzMEobMSJrqBfBTKyxNle68skPpyyTRYHGULM8
PSdhSDxGpgQKRSrzJE88iE7qTKzxKBzsuh9pc1S5647zSi+35mLPU1vg42g5kCIik0MNDR10T4Ma
QZXOAX1ScSE9c7rzulXDEgkokKoajChDo6uQRY4krXA3L03cKjtTTSWtwDipFK7FIcPKlCQ0/3+8
Va36Mnpzwj/JIs1XozyqbiCVyrP2KTmTleTdt97KKz68nJyqztKUdcy7VMskTKLY+BoX0LWWw0iw
+wJLqFVS89UMqt5QCvhCGANumGGFBibOLLMmTkOzizBrWL/EoCVJ5GkdQpnfxTY29yqWE8IvDZfa
3JNdh1zjid8FwdwwOAA/HijQiNMw60PpUDp3WxjZNbpON4V+cMKgI2yyXklqifctufZKmlj/psoq
VhCJGptMY6cD7s5yCbb1u1WrxbTZoQ9qt+1E0/pzXb5mJYhmgKHjdVGACUbb7je1k1ZNigYcMTQc
uZp03HIHJlpAn1CDkNe2GbQcQ7Hg/dQ99/+0jne5tin6HNXtdr3SR3DlRrd1fVl30DBcEeRT970D
/zN3tsjN0+8Rf49y95gcw1DmLX3vKm4RkaLywcC7BBdYavNlvjDQJeU5rabcnHYh9kLlpRb24hs9
1c9/BKt6NasuMbGlpSeK4+/oDtIrnD1GNvFxFQ1kA4KK1D7mO80MBDX6eQi/CLgZgljKgGcL4E4g
A5kKNkwSAdTKZySDCQ/mxml6O42KApawxbXqf7qSmnF+5p37rApTTjlNu5ZXFP6lMDhugIyDzhQZ
ETECLu6Bi1uy5h69/CgNLhOWwgbGvOXcLmg8Agv30DMm463wXY3j2+JiFxno3G1oE1EV7pr/JZTO
ZVFC0auPrIBSvIs471KAawwYBYKJ4NTOWkWzXpbyNp3FQS2QVllXIAMYErG8TIkcqs75jsi1+MCl
FvMLUeMo5CcGmbBBgAPfSd5wwg9JK4O6iVr1FMWfoHBvkGkrmEyc17s41mxvgxNUs9hUMDMVZW1b
YuBYXubLPWlulTGB0ssSMqLD3etnCSENZIQ0sictTlv8m5J71HcXXvBiEda0pEK+grt1oXKXf0zN
w9zGoULqUUW/pA5gDkeu27mOVuDZ0JQski5d7o172bqRbtgymYyZhCMDvGfUTNgbINqoSlyipr9i
aZ7G8UZ4bwKolf5lkobmjopYtIwIEdMb/5C0R0m2uMR6RNoewzknS2xkDJG2Ik+xbe5VP0HZQaqy
oi8Bx2eYe1K1/rS0TfIzPNf7GzFlZz0zMkp4wotTGamXmORw1D6R4wnwgrLSWtYIi+2cFut45h0x
2m+fP2tJcpqEJCZl8z0mtcX9DOpHsBlkInLlTWxSglV1/bGJqRErF41ylFDCkXCs++IqoQQ2YU3P
kv7iaBbBVtCs0O6LoyKXS/bD1cLxp1tnkZYlhfnNnDq0r3sC136wWJ0cloSgpmzSJUiHPkdms4hj
upMDm6Yh1gwGMo81CuCK084PFdAoiRORoB4LP0lB6ovK+0s4GeItwbEtnNBlmmNndUPoFaLmexmK
7u0galFJDcwmrzzcuiDmMTVSqkclFOxiK7JNt6CvPdZ8S12QYjz1sgR7wVIqabmksJTyczEl9FOr
DshA2mhGKQXimHAa3OACV2nBsYnwfaxiYQSX5sJWcdWEPSwZDlOYwyP+cIQZduIRP7iGH+5NwhK2
4At/TFWEkV85IVSl7C2kY5yE61ePO6PiKexrhpUZTpFTtYV6BhOsNdGG6BL/H9IhqbVO4qlT9bs9
jE7tv/mportKlLKL3nInYy4cX9xQEzyaULA6vSkpicvK/uaXQ3CSIZqMq+VOsigsSYXddO/MXP+O
FTTHmmrayjUpfW3XqNid35gaTJ13scct22wPI4KhF/coEMxlfJE0ZUir9mkxMNK7oR2ZJUg4vu3T
siOTGLtk6pnerEFQPeZY5aysKTVUUdZ53ZxJGad8UsrHQ9F0PMOWI1m6V2BjARgfTzkSsN5oIKUz
oklJd5c3gjVBioPO97q83FxtML8BHTTcdq1H9fbVaufeLJSIi8h3hqtUVo73rQk9KEzG07c5phK7
+GVlu44Z2a2E5o6Ep+gO/72Nrl62bWTyDVWE54d8dxGGXiJ5PkwgSSpBkixOe8afz6bniojZDVyl
e6z7AvxQVFT5boBHRh3RE1zkXHNTCZ7c1DFltYQKzwLpqRu8JguFkj0QMddpvKU1bzjQdaBipRnx
SWUPniFtkntCdZd31YUXb3S4O0l7lefti5as5cmQMYKRy0a9WZQd7UUYZFAsDi6iUQf0TATtUn7H
3bBCtY54d+KhKm7quFl+31EB/e3/4oalMSqJ/FoCUpx1+TCBOxucZFUTaGNFtvCRLTYjsRdaz+5/
Ow0d2et9kMWQylYJqlug8Dv36uKkcIuu94SG3FLytSiUym29zWP/eJww2/8i1TH0Ih/7xDChhDvZ
YgxjNoZnOdkRmtztI/EU+zm5vYsu7ukUXtgjFwJ5Br9UzZlFmUhmkAyMtdByI4Y0o11SaY5jowEl
xGpI4PSAebf8mr/Qmokj5okZA5oYQgoQ/7iz8zOg7/IT2eglaDo/x3mOLbK+iKE8loM1j0sjj/me
fFO5huAhrxu7l8uXZGKgkvAznIIt9kCfI6IXFtornVksvhAa0NIJweAcZTPAopIQvIo3icA9wpou
cwOfOMK7iRq8aEon+zElJjSJjaKu2QE7fYI5B1QnQJu68YsK5Ug6vuJCJMwt6NGJ+5i3nRGaoWuL
zusUUImvfGqs7DowmzP/QTXTkCbjilyyQF0xNlXhL5JQwmAJQsL5idIbp+PSlyripwtciffpvZ0Q
msMYMMsjjzdsoBahHmNZPkThkpHADpVBQfXqQMXojukiqhfcJSaTBE55C+87qUUQhlHakM5YvkNJ
Kq4al6hzQAI7iNF7OzSqOQrhLPKbwpgiLFcSicuytTn0K2axtR3jtehiRFGUKDqpwMz5swa5oDCD
HnMBCldJsozhMkO7m5fjOISoPDdKF4CTtNiyhSORi7nQqS/Rs9DbO7p5KDIDsV3ZuT3Zt/IqKrMz
vUATE6F4tuILQlTRRrhLFWKxmkWRGJkKi2P0P0QURI+AIdDKQFuJPlxk/zQ0wL5TXDuJSLa5ociy
MorQqIsigjJMaxJ92x7ucqz4+TPE0JmoOEJ9NCipGJJz1EYg6qKSkCfjqZ28+i8HUYuj06t1UybJ
KYhG84t+oq5vG4P+MLxBsj+ANDhs+RODsZKFG8ZnO4k+s6nJI7of0oh6MZJ4GSL2IEjGcUlDmjWd
MUjpW7pAWb5NHIiNwYjKmz7lG8ZHU5m/8yOl4CNMQo3JMAjMkB/8EDz8OJpCYUyFgRYUmjChsUqB
GzX2QiomGwqeQYqacsTCMrkBBBo5y0Bnqca9SrwReRb/WRFtg6CK+pW2UBLty6arkyRHE8k188jG
w7NT+xlsNBZuIRuNcP+ZcJMQi2g41kuj3+yqcvM1BPHIiQor8eivjJSly+pHBhSscDFEj8ioRGyh
QVO3ZyPN6ACrvUyupvEcaKylnrAYi+sauVDH+EioquqpzAoz8UyMf0sab9QciComWZu8VuuivSKv
LES8xcFI66vByQIUkbBPpzq9WnE60kAZWhQnfRsgyLG35iTOk4FI0ywo1yFP28nM3UFQu6KVvJiL
rYkXTGtKm5AgimFQsgGchMQ1dQPFn2izkOMTnwLDgLKlmowmHPkxMmPLOGuqB50xNsNPWZKcN0O7
5iuOwdEuX7TAJIW3otw1wfhRqtGSEw208TuJ39MKkao6uECSk7oyFtH/mbFhJmcMyZZwyCKbtbOr
UTAjp6tyvsyDGaxwM1qKDa2COlh7o7TITinxTcQzDLw5kH+BQw8tlDrNEnPaSP05pb3jkDM0xEF6
MzuyyyUlk+N4zo7QvrtAErXCC72gshKtLN36iMS4Ehm1GDu8whHC0aPzyQUVTg2dzi3FPFRJpg4B
GOEkyFu8qDRiQEgcknz708M5r9lAPZfg0QbaksrTMo+jztVx0LsBnSLzCvGaGwDLifksovrKmu5T
tSbzyl3BRdQ4J0ckwx0ROzMdTXLcsnW5wCMkCBs6R2UZSoF9J7qTPdkTyqmjiE9NvvscU3nsEExa
FRD1UKSCnitiygcl/0vRRIPmmEjtwdejCKlsii1PAZXIiZgOjbGZnNXNsar6EBlP/Dn9JJLVOheL
fBPbiKAGyszc+D/IsMjfMEwKCxj7MwsUGhjBE9oJezAZQw2GmQSlWMx3wR/8mUxglNZa09WD6axl
8SLRK7yAfKZ4+wrBCx7MK0gAIxeAmpmXaixBPbpfg4p3EaJ4ibT2CBWv6ReK+KQwKiPTWLwEnaDv
6EqDqs6wXULmE6pt5TSdytL2yrN7w0lXqpNeOSxRA9v8oSnGUxGeIA6a8EKaS1SbSyjKwT2WatKR
kM5r/baIkKsbzTmgQB2b6BrS2T6s65RIbLlk/SQICi4B/UpDLFWRcf8mxzgqE9013Z3A9sTPxdIq
EppZZpmnep0Q1P2fuHQX5KAOP7wrPj3CkvwPB40rqtqPcR3Alnys5IzDj7BLIV0KI6ELSaMXbbq8
qvAOAI1XPB3TPe0JnaixOuxd+usgehRN8PomyTNFn8pft5UTEuWkwIrQflzPqPwnvarI0+3BoISp
Afus+MkjX/OutYlJKN1WfqQqSXgDglJdkDCiuk1XvNgLbfuckcgEYiAGB/mPJYWjohGWSNVZJ0y/
cWShp3TPCvG27FhYEEvcLOy3pAOMU0xWtN2iMgPcg0PhotPa3mLbcLKczGjgN9wuzCgVIUsjQuGR
HgsP5Bmq6FQgYeTbKHWdL1Utn0+xO59MGWW4Y03YoANiVyqZGf8am1LFOcCRKzKxFm1knV2qQQY1
o3kEoycWNTt9xjThjwcWU0ZUkRxKXiwC1WMJOotqlvINPbHowSkap2iU5B8NnJoELzTQBGLoWAdB
E0BlEpScT20iHb3YRFleiDsmhmFQhv1apu0QrX4Rrnn91wCDmXZqmKKrku/cCgEqkYYzCNldlZzF
VsxCP7A1lMWiqxyRW0fmtqr4vzq8zvxkIPwaOADMEq4wWNPtNyD2034926wkOn00iUy4Y2UIOwBF
TW8p/9kXps/2sMJ8JgZQIAZlsOHKYSfnfVi3tGS/aF4AcQ3au6voW8jm/QjYYQyoezkHBFoZaSHi
/aeXiBj/IcvWSebNnVEwabghBdiRXDsZQ1xTU9AHLjjyS0bWsRyEruF9dqFN+r73HVlOCRVj6jgx
qAdMIIZk6Gkr1qfoMedNI8dDBVx8ldxDVUpGK8uS7Nsc3BN33qQ2vlee1GbZAZKULr8SlsFJNjLX
G6inQWt1CUahNMPzrdhZnMfPDZyCBoWm1oSCaQ58LArZUitPuduSIkrhyedhyOdk0ARlGIbG4q2A
pWZzFkFohR9Ai+kZ8zLCCtnkwx5Vy0ZNzdPVw5BCHv8rs70Iupo9jA7DfhGepxGmxMgEPvLiwQW+
PXGD1wgLhItDlB0UGsIQMaAHUPhlhFYGT1I0aMOaz5vPWsCErjHV3dCEYRAGnyaGT8gEhqDmToQi
sImbWNvIqaboxqErEQqh/WkNULKKkxlO1FIa1HkgtQYx3Phucf1V5HKUECUSoO4Yahpu1gMRsf3d
mBqg6rhhtpBAvRtS5VBSyovemcSuM56KTBiGYYBspn7lceUO9KCv9YiXegmGtlrZjPFlSfhlyE7o
h3wTighOZ3PiGqlAUfZe7wVX9zHlcyxSZkE8NSHjr4vSrKReJHRnKDxkKjRhbwo40osR8ByS8XPN
6MT/0yZfi7IluvzsLbawbkloamXQcNKGW1R9DxeNi8PWFn1NcV7I8KZO7rae1YY652ZRVJrkQWQB
whYSKJBsswQlRE+ru3CrHVkC8nR6kGCRx7uUWICjsyff8/kGXrAc3Dmix7imKUftrn6dQSCXBKbO
8MjuZZVSYHXdGkbIGmGAr1rY0nXJhEzohaVOaL8mBsBuH7SRLJzgUCgK6/EDmyQPZj68xW5l5Iy+
NcM0GKk1w3IVG0ICmT6bEWc7odREL+DwweLbxpMuw7Y+ro15iGb0o+ihDR7mO+UJYEtHA1/GcFBI
aMiGbcExD2tqkk/JGkzAOrxEa9bQBGFI8YT+BJ+G/+WRQ3OHbEsrJGk9jRVHY8skRi4g6qGTm4hk
UeFsPt5dOc9CbItEO0HriTyY8HbL6D3B8m8NLdUaH2GXKHL/Ok3Uk5aRvPALZ+oV/2lZbr/XOCm3
YJJaqLi6XWCLaHWmTuhe5m7VsQxK4XOIvkgnJQxFr9O8ynR6VDlg4vFIBkexGkqnGzyXCjb4+ezg
Iy2H8BH7vZ/McZO7lt7IA55MItDv8l2hM5Gy6OaHuHAMH4Z0HwaEbg4cGhSJuZr1MJ30kY/Q3sqG
wHBhoOGDfuyEPt8gerbdsvQIgZgpH86u0BONQflpAdGf/cYxvnuWgKHKQIsdRohRasbipVO8zke6
A/9aqJWYyfhsRYVGM823c5MMjfKVlCsb1TY+mbjqtpGgJsyXOvIIlm9snz5o254hWTkptYILul3L
iQTBV+YFn4fsX1aGcMY9iI/t0EHWtPCKU6nk533S/CFe0/zfseNC/bwO0e+18dKIMROcmmHNuC6l
3Rp5BtnOjxIkina3K23wRv4QgEAzSUwaSWkEIixYEKFBSQgnoWmoUGLDMZIgQkxDbFivYcOUZVJG
LBmxiQsxmjSIhhEvSbwiSdrFi9cul7ZqPsyJEc3BjcM0JVP2UZPIiA/FQJSIxmJKhWgaRTwIsdHJ
nBRNChSjk6FUq02V7syY8SrZphgdhkXrtazanUr/Ve50Glan2q1fC6I0OEktxbVpFuLdOpcsU7BR
+U6SGzUnYIOMFEJNM5Xs0quPD4dFKnhr34mbHWMFrdKwJI+YehElpkwZ0cVQoULk2lCSpFo2I9ly
yWuRy10mH1O0KIkYpmGqiYE6roznXIxIr24e/FfSGExj/EYs7Bmi9r5jLfJs+HnzdtmHp2Md2zXp
QbZmo5OHy7kq1/D20atny1g8e+ruyfanmGxNATfYgJ+V51xB1011lFt3ibbeQ1jBBp9Ew0wyjDAf
JaPJR8Rkld+CZNVEU0wx7TbTIry0J5dmCKGhDC/GgfJhMqC4gxBw6Z3nXUKUzZXGZf5BWKR7jyEp
/+RTKwnZJCNLLZkkaI8hRRB4A2WUpJZYhlilk0o2CNySmvlnkUVVYilGmZJ4uaOUXzJSUUNVyjni
Qa955eCPdy75Y0IC3eWcoHbtCKh+FSb2ppgBOsSjiP919SKjTvEXHlNoECPMRSKptpoyZN5VKEsv
5TaTS5GYmFtKPaaRyTCugkKSMp+IBNKDA17G3o5EqgWmec2FB1iuCFUoH3uHIZQJQm80xKxczbLl
LG0JJosQJl2ZdK1KiinWnBso+RmWkauOCymrxiI7qUSMJJVTsZsRhC6wOinWGaQ+ZvajdnoCK+9D
lQ4zIyYjsUYSMW5stSdckuBGKqottSRTJArt2P9cJr0IQ4zGrInUobLlNrVknfJdBay6/3XHo6PB
+msyy9RKxxaQdjm01mb1yUfpykGOBvOSWMKlmcvqCXTpVZE1SlF/5/4ssq8Z/cjzqojGSyBDTRuG
dIKamQSRq8OUphpQnWZC4EJkvdRbS4zIZBtNaQhtlISS9DLwrKp9KJSRMHIZF2kKfdfrW1U16JnO
l1UIYX4Mtds4snflpHB54q2amHt+N7bzvwVBd1blA7YFn9l/1vVu32hIvmuLBlXIN82r3/oot6ED
C7K/1OXE9ZweBoxJrWIrM8nQXTW0y0201TITbifaMsm3we51lKvCpLaaJsR8Qkwmw1KMbaWOP1j/
FrGyWS6ZwoLZLlXc5UsEeLCvn/t0dJofGzOE7r3ckN97xtcVVCSvTH+GaspXBPI36MAFS/W6i5oK
+L+T6GcnrwONXyJ0r4K8qiPIwV7HMqG7MTwvQMCB2EtKyDyaKCxlrprRUGS1mrKt62zvyUu3flXB
g/QpNlIziJpcF7751GdxQ7OQ4TrXI+y4BT5jyd+zQqYeRtEMcy67yISCg6/z7Mo+stOL63jFQMu0
aF47QVphRDeblFyJZefr29d4QauRbEx7TBsU53Czi1HZwm01wY0T0YSGryVHKC9UjQchUqjm9HCJ
LqvQolhWGJdVBVEpqRqXiDQ+LjaIO3LKypwG/zUQrwhNK5lsGiPVt5cmGeRSTxoiX57SqFUyaV3j
GyUZVfJAh1AmXHM0I7/SBbr97GlX7HsZLLs3kCKdbmmPuo6ydpgyngjkVcZBjvWCkglEzVInLDlV
TUpEqrflz5GZ0F6nktMp7bUscolyyi3tNCGa3Uc8xfIk6CZyHXRBp5EXpJxEthiY/WkuJez5jo66
xyfzBZBwPrSKAWfZlYeMwWRqIgg84TZQ3SmEgUPEnEqiBk/H9WyTugrRVqCikwbS7jwR2csKJSHI
sYmkmQXVz6kg5jZUoUoStlgpqPgJyI2IJHvJgaHOLMMs/jlHfFQcCFsSZxhF1nOf9JPczMy1nf//
6NKfQPKO+Ia2P3CtCjhGU+kT/4m6vgFQgIYkaCUXWCkqqpWq/0SKQM+KutmZpKdmhYpMDYlGsEiz
VkNZTfkWo0O62AI3D6MJSxL7Np95TTlA+V2HcNk9iayvoTsMWZE2Uywedad/+6wgE79nFR3W8Csz
g9wQqeWvxnAmSCZjJ2f0BaCTSghC2hErWrimOqvWky7l2s/qLKpEYn0tJBtURoe0x1TzhY9SwmBE
MHjBNtqUqDa8MMoW0UAUmBaMbF+Jm+AYxMmqKHQSxXQMgu4VtxpqpnVU20nc4oaoXTEIKfn14nNQ
d8u4aeeDMeTLQpDmNP6OsSC7sm9CqHTY8pj/TS1ObU8aIYLRq4mwKhE040F4G554CeSQpV3dvsTl
pvmgK5LQ/JpxVpM3kHClYk1TMKnUZlPlJWaUUMOIIAlZK1dhAptEM4gTWbVgtyLZiz4ySF+PW7uU
Bgmpv0yMXdg3NwhBM0Dzw6eEMCdXuLovejFL2cxYeRL0XBGgOUurbst8oHbyszyCyeyTJ3IRXrgK
JCIJpBxrqMPnFKREdyzRihjGi52iGCPjVEaNVrNBj+xkWJ7rbXMUisytRNSuRTSlFu1TxiQSLcpT
lGCADlu/G76WduksqjqBuVHiynPEpo3zvdzF3aOorJ9pDu4POXrZv46ru1mCNWO+ttxh1AgUCMFb
aoN55JKb/0LsRDTxjd/MC548H0fZcByYXWNnqCk3sSzAySxb9FqRs2C6fSGmViMoJ6ZLwWZksP6N
iyZNLPG1uyqIM+BUEVjgw4CnXLvFq7Eye9CWOeVzUPTze9uSNISyxbzqUh8YLUvgL/87Px5Srp7P
qazKuFYqcTrhLgZt3ZmcKy6TsB6Mx6lcj4SKT1xUSCjn/fDz0DmURFXyYqDb3gIOrVIKB+LEHw6Y
P6E7o4wL56vN7GZvB91FE2FUwCnynLnMNztY/TXTbybmj9r2nZr0GZwnuehO7fkjetu1W2hi3eya
qptdNiwafkJINolBDJkIiatAdLK8Dg2lKA251484XvCJtv/Im10z0NFrrwTN5tRJAdcp1yhXuxAx
tf4ODsukSs8dhxPoUSHvb+ynZKJp7YK8bpp6fmupgXkEJJLIRKOv9yk60jrQuenmTHaxPONxq0Ba
8RQxJvGGTEjiDWgQg1BchcUWpQ8sv35U/wybzsLK8kEXPmWt51KY76OYtl7kyb7dkkb+oJRBcGMv
KoUjcX7zLb7ZFGN9gEPBiUiKpFpOy4yX7OcqhkZuicn/DYqQwcfmhFQwcRpEpAYoZMIY5J1AhMQL
YVxv1ZRO5ZR29Qbr7UfHaAIm6J3GTMI4bUQvYJWpHUYDtddCjVGncd/nmFQLwp9WFQYPvVJp6R+q
fd/IhBn/As4QyF3fzFjFpxmcZT2Om9gTvxkLVplWUtyT99gJJl3Wp2VFENka1hGR4Q2J/yhhcWFT
V0WEapCEsmTCTsCRMswaKhXEG4xKb+iU8pSQLSgfpZ3H2ZUhUTCX9vCdMBSSrEEhm+FOt/ifYWTW
ZxlR95EVJuHMQQydhqXXrbWSr4UOa+XJbPnbV1VRzCTew7kHVsTPGfVKMXFg5XRZwynUgc2dVjFG
e5GZ4awccgwDIxzfRpTh77RaLdVR8jxMJLDNyeHGAJ0Ux5UhJrDUp6SBUPCC5YTWZe2HE8qGABlY
C7aZcXFHa3Fi5kiOCwrXUxFXN5aPuHTa5gmGuUgHvTic/8/FRQ4pUcnIhnnhi0StmToRGLOlRUGQ
W5KZj9Dtk8TViTdqI0vViEe8gdrFFO0R0qtxDsTckfLExO49YlKMk7KVIQ7kXRggBQm+is01Ihim
TOoNF6jpEp60G5qQpKAA2rutiZn4R5ekiaDEWoOARtVoiRqWZCg1CUE8yZkoyQMhIXtZWJq0h5dM
SRcOIHtdSuXoTohoh4KAobjE0EnZVnGh36RkFSq+JIKE31XOhRh8xKsIj/GN4Ke4lGqM0gIhifHg
1EzwQvKU0Hb9kEIolx7qYaugDlA4H7B8Fm89YpH9z5T11ATZY2tpy9BxxVwcSFxgQjhKxXt0oVRt
lUCEUP8I2ZC38NtYmBbIsAtCXAqwaIunHdFhZZ8VSmIZUYURLRJmZcZbOoRHitTgNeH7JIZBZqQY
WKRWtAqj9RnboYhNYZdONSQ1CoYgIZ9QeEQZvpzjbGTM7Rp05dpUNd0/ElE/HQj+LBwnTma3yQ0L
MocSEVxWOtsfkgubsN3UNaY90ZB8EB0TaSdHqSQBMoaMQZ2U7SVfaEaLyaUmtMWHIN+4RAQGOtah
oUpN1MIlbOWgcIwmjCDvFN8ZNtBZVI2f4J8kZiGQPGju5Y7U8NumpVqCTB3IfGIqVll5olrm1Mzi
FZlZvWBIEc64DF7qTM6cOeXk1RPPgF3RrQ6qwSTnAJv/vNAVXDhaLf5YWJKlI6moQUSMQuqGS9gE
vUQO3gTP3rEGlOJhPE2ORsEP4nGJMX1if5TjPEYVffTLdzLE+9Xj1jHea9qoXHEfYFZlq3FJO0WV
0dSbKzkek+JPo0jZD1lEr6WYkoUZiZlmDXGjy2AKawxDGuTN3mkMrQCaOVKK8aBIL6JKLQRol1lc
QfyocTKgrJTPbzUJ7mEZ0CymvKAnIuWHeU0foGTjgykihv7HsShFuUwa5IheUWloKhZpq2rm5YRH
Oaoiq2bUgCkcXWWmNbonlhWVuR3dSmLpFc6RZugZGu6dx6zcnl2jWiwKbaDICeVUbggdBzqph5xh
p7So/2Fy1JTtR4UthgXZE54aa9IIjafqTyip4pCYYrH2V2GQCfiB3mqiq/tIQoUI7EypISzRa4PN
n2hU5a/5KZoy1DLlxPlRXJXykPdRkOl1j4vGFVudV2a1Z8rVCoKCpSTAVHSBBZkcz4r0nm/KhG8s
IVYcYyA5WvbElBrlqMlSCGzGz5u8VV1pTUTQmSu52sGKBwAdrOXkmHr62vlMzQARGZt4UrnGjxBl
2RBSp85ulqVcnJdhLJjpo8CNTH9UDWWQ6YdCh+gZIMJBB8FgDyEpB4joiUca0MOcCG+UCEzUAte5
RWQ1V4f86AyGX6GkrRpeptV1jXZKZ51ClqM+ZKfBiP9+QBB5hqk4Zi0kzWNdicgcvabSYMbLXNLQ
HRPlLAnhtqLVhRqTbCO/FFyYvmcLNiVp/WRORKRyeCCMfSGEpIgtRNtN6C6qYOL+nB3xKQubRGjE
StWiFGHjPhdlGKBTBislapHo5YXTYq7n+hrGatmGLW4ROdmX7WBuTcvMSJK4pUHz/tLiUq0k4uOI
dkYOsmfFTVJkrUaH+C1IgIpG0saKCKhMmNBCMlGuxM0fZcLGnRWILqLDKt5xCRmIWZmz+oiBZZ1f
WSDD9mgs+ZGdIMmYouZZCRiFrUunstNJAFjFNpCUtGfoBKINEk+LwMhIOmf8JQ0HIqSPgC5gXt/D
6sn/mRrEYDahZP4fpcyuYDUZ645F3NGGWi6kTDhsVpjVXb3m4Q5EH+LsDVOf5JFVeCDwrpEjMB2u
rd4w53ZvbIDpln6pP1LZUqEfvVFRqGKUIk5YXegjEKrxqeLPLWFxh+XgmVWsFZbM2Jbi7VAMy5xx
JnyCyzFiuREujaEKSyjxHkXM3JBZluAFPaWRZ/gfSV1RFYoaiFqmiwBQL5HaiLWarnkxtVhe/Qzi
jabou2rOVrFwma4MNqHjrnKYruKlGmnoe55Upd1L7LLubYUpLJnatkBtk6DOalrnIwXLkwRaCfEG
Y6nIoTHs3OEa1EanK2ptceUcF3XS5WYN+QmJWBjv/8AVJlGuh9DAhuHEknKqsfl8LyqqDtEk3AYH
5nERhr+GmSmmU8/669fuM4g2YSJjllTxMbyNrhWBp08uX6glL5BoWGEl06rShu5uk9u1JaoYbwVK
i/f6qTBz2Fpsph93khU+IpixqbrwMeBs8ee8bkKhsfQi0a2d7o4l4Cf1Gt2lpvW6tNVM8xXBTFKK
SBb9LhHJq1T0Re5pcV45ZmAURAmhyor8nk75BqtgmBn1xYThtGgdV60Cc9AAKz0e0Q3nMjx555dF
lfWGsc4mbmP6oHQ+Z+CEajteBekZBmyFT+me2S5Zzs+d7BTPM/VWSonJ33za9UyxTDfpbpJCqkwU
yf/tXoZzunWeQEojzaolma9HzSqMoNcq9eh2iPT0SYrQCPRXgMeqITQsMQVnhyclVl5EOyOXxO0u
X7GN9mTxVvEWD3WkjYjS+qE3J6HC5psKs+NSQ4cBXiHLoghO2cIlOOTgFC0n5/HXrlfKULbH8pMW
BXCpAa4kc25muy76fuk99/R0QF1Ds1sLh+byKknPck1DdZZTVZA7ZqxhMitVp6OS5Vd0qS91xs1j
p1h8mqgtoc75LSPnHUkX8wU0L6Tb9cZOfY7PibewJvVrCTX+ms/wBp9mK3TtiFh0nSIKih52nDWj
cG1MFx0R8TJ/+vXkGrOlRfbz+kcLyrhcB3JbAaYUsm5sLJmt8goXAPpLvDGjuZ7HWMD/XU04Vm24
xKme99IoVKnCx+3SWltb8njnuASL32g7N59MRrtqbHpEdjUbM+6YrB9e6YfazOSm6SvN8+p8YRAi
i/u6zmqTTgKrS8O18Sz7lauRXyWyHf9o3opWCiOzDSPQ7Vr2hgfPH28H+J8fUCLvahTi+XlVhIWD
IQCfUoG8JzbmW7q1q7DQua2dG5zTN7Bl06Z75HrRXAD6q5VV+TJPh+g45WF2lapRbC3rsWxPEWTY
t4vT3PegcKBYJeco6cpKakssgpCHbsGGyi4zsBzLRzrXmpwtkR5fmWli5Qvqdf6kL7JQ8Wwf5hXj
C2u/T5G659LiLGWfOYTKx7Dgdq+m//VO6OutmAs984cj1taMm9WCODGVE45I+x5j8W+KPIxOoPRy
TrrJtAWZiCbApVQ7QxWLG6FHBxvWXnFcnyd4a1W1g69ZV7biYDJp2vMP9/GkeCoTP7CkA2rCPUmF
UKGI+M3Yvl9XDXaZuZN0CNPN3FKm9Yvuqqx25VRL5G3k3EW3iNJngk7MsyGEw+yAyfZU9vaoYlkp
aZ3+ocmIhMm/QUVE0avgGXNLkmTAMgkSxkkUqqRKosnKL5+cXAfZy0mVoCvVhc6l6HmF3/SGnStn
8Ues1jv86h+PLs7mhUbZxhh/dhb5DntvGnnbsMg5znXgWe5hWpqO2RxjBB7S3W+WOv+skL8F0iGV
G/QMC3bGYHr+Gl6t3g95lvWgIz6ePzbnHnNfij6TAnqqpAGjRJXpUxAOWXw2WoTOVnMz5FhGt5mp
O+636k/E/r7doWFCoe3C6TwhP0vlVLGmLpG7eNN1v/PfjNdZql189ivh8Fj73krZ5b2gIl13x4/W
Rv3656vrWAzTc6KnlJRUVBRKzlC6ce3oubyI+fKqlwGEpDRoJhFEI1ASmkYGGaWRNMagwzEIBxas
iIbRLl6SJGmUxCsSL5AbIyK0mLBgSoMLTzo0OEnMS5kFBTZ8SLGmQ5cwBR7UiUYnSp85e9IMOjFo
UDQybyYtynTn0J8qfzpVShXnxZb/WXHOlMo1qECjXqca5IoUJ1oxOm1GTdkTrNSWQJ8azYr1YtKS
Vmt6hatXZWCCE+miTSMYb1uEUhkmVVxWZVfBLBF+zChyES+NGW2F5Ar0cV2zTgk65qsTE9LQpxkF
Pi0TsNdJSg/vlezTpdvRi2lGtrr7KsajQn0/LR03Kd6ELhfzBl6S7s6qTw373Kpw5e6FzmfbVG3W
LnChYD+/1UpQoBjEsp9vpU1R5uOvpE/bDe5Q88bOG3d97GhrIPLOK4il+JQSLbC1/noKMtgOGu0l
9dCjLyvx0rBJpvYiSinADgVczjm+orttLg7vevC6SYyzisOXTjMJvYkMI07Ahuxb/41BsaASEDuY
8DpOIqL2aigihcbzcCmsLOQuSQnZcmrG3xasTbCmbPvpo8xC2kgzSWrZKBKVCvQNQ7sgwivIqPyK
krjsgpotq7bMIqy8ORHMzkfQHMqTJ9341DM9ONGaiEkCr2yzKRAvdKmRAXc0qkw8hYOtJ4PYc+9D
P80SjyAFz9MUsduwfDFITDEldbE0W7u0x0M7dc25hXa8MEVGtgTJFo/64+VLJJVrULdCrZuvRk2N
K65BHyXc7sI3soNvPeVkKnAhVPeKjshEh5OosTgLis5MhAhbNFDYFPPKsFWrdCq8CyEU91vBDpMw
WjFEjaugQfuSV9i6JGzVUPvAcv/Pp6EyjMw+v/Jq06Joe/SvFv8i2YURkT7aJTYx2YM2QoJVonTE
jiEM7CZKY4sK1WAzHtFRZBENq+UldRKsYBWZOxBUSoU1j2PfoDtVIId6pgvQF1ntc8FL3ZKwvN8m
+XG9USVRL1WTjC6LsookJDTNnDTkKuJdMMnVYop3iQTArp5kbyptQ9z3aHqvZKRT0YLj+UWI4CtQ
tOb2fKnvT7NKjqyhxzrRvakGSvbKo1lOC0ivla3yTJkXM7lwwY3+Fl80kOqUtMgAR5dhlp8jKuWi
FL2zXpWcPEi//j4KySPNgF5a4Ok6fJWxMXn3/WCTwYqUbdXJPfQnlj63sk+RF/L/Djtx635SXIrk
pqpMuZlN1EeEFJy+3HxBBO3dRQ0Wnd/HQ7+etO0IKyjSdp/yHc7g0iIR3OhCRkxBNrftuX9V091t
5seYppAsJGj7Dy8qhraQDOh6M4mgiopHIdKUBFZ8QYvwyhKVoZmGKD5zWersB53QoehxFVrP2yoi
IpsR5zWSgFMFTyWvx6ywa4SjEsCOM5GP4XCC5xvR+6ZVPaVk7X4QNJAKeffClLEnE1KxSX46crGO
8McWOTnXj6blkyBS0GGsYxnd+LawymFlgw5TI+bWGLWnFIpdllJc54pTwSMtx2QjtBqxpCY0rd2I
QpbqycrilRDZMC03nyFhEhnZ/0GK0GY3s8oUHyWoxzRMEC1vkETFGPGfK1JMJA/c2W5up7Y6tdE2
QFFYpkoXFERSJFI3E0qBPierRLGKXFGp1tRSYhO7qIdptZQUtdAjsl6+oS10MxS35AS9k5SkUdi5
D5OeNbNi7lJASiIkIp1ZuGudMklCFNivDGdC8kwvekmJ4NvCSRON6GqToZRErgYivPl46jO75Fae
cti57f0tYH6Biptu8rl1oU5HUJtPwnLHRMLNZWU5Y5zTiofLs8DnQ3+CpTXd5TAXfnGVF5GhMekV
QZcYVFJupB7WIgk03rEyZs9kiVNCYqvYXTEzvNgRUgpyPR6lBJ8Bqg5MSpLGzP9xjCL6vCVNZjI0
gWCCLRs7qLXec0KukPOEOFsd40aJVZhuNUdSssr1TOqkc47lJD58HNGUpLGGOs1eSiHiUt3Ew7RS
5FfgY1QlmXKminWJbB2p2OyAGpwdycSsDcJfgiShyRn5j5IIzWVcimJSoXgQWAIkC1WcSFmU3Ytx
9XPqyQTIpM7l0JfSxF/O1liqLkLpnEcxnW/aGFehvHKR1vpWIyr01SfypT9fqqJI+rMLW+iUVG7F
oCRZFE5hxSZuf+tjOYG6Ov/Rj4+L2R43cyOn2qIyaQjyFCnZs6GQ3lI3dxsWdi2SrVEVbKSss9cZ
9XpWDrYSphHELmkPiSmjsvD/jX4ypcVwFcosFtda5cxtm5TqIaNGRl9+zK6fbOuQNyDrsFfJ7cZ2
IhTkmdYtVgEo4P42WhhhWKmsKi31ivbVmmBqUyo9lU/c8E/JAjNhHMsqE0v2J5UGuCk4IiJWDYIW
SWQmYl0q21+/4rmeNEo0vpPsVlUcJDREMUH8gkxUUfnZvDFyXAlpMIft1hbKvC+uBNWXnRxSUoxe
cjbpTOZUbEuYMYH0IpCd6kGG3E79BZSzksxulbnirDHBEm84wafj8nQnOhL0UkFkykgEe7b9/Gdx
xgPxRoMX0DiBkKXP/OFoMMQxSe1Ee5ZiSWIl20RjvnRGhxZpgIDixvXw9KguhRyZq716WLU6kW6Y
vShgAD2rw2bZkf/7VLD9xkIvZuyyPHK0bn/2WmafECtfGgmXrnjcMAF4c/3tovgshUMLvcTGTwSq
lvE6YTyi0qNhnVC7p/oyZ7fVonoBbZtENF2t/aZAV4mJYi9iJE21mc7w+zKjU0piMd+3csou8m1a
xVwgn+aL/XH/4HHNVkWMuZqJ9Sak+hRpuUQmC7fOsS85/7xyg3kZRhRlqPoYjhhflZuDtpl5sR3G
Wwl3FWYjNRF9yPmWCZv8tHZr5LTzC29JFeuiZuFFrj6ybQV2Jt5pSuXyWMu21K67xQQfpPXaXdU3
38bGEFqb+Ficp9/1CMeFmWVE5AQ8sCuclwFUzWS5qTFr3j06+g2edFV+Ee+yNSa+21MQHxohcFZt
iPgL+GLvebkRhgalhtKkN8PjRi+NLYGU3vafA9/5CieUh6hm58wXOW6GfXFKREoQqRwes9Y3dEkt
jZwsM7vjkSPVLbFFPdtdHjDGA3A9vBtjsrVIQjv+Ue4PlVsM/1EtalZPc7JOmeeujjv1Wy0CjHDn
iPkmI7PDKydK59K3/xiUPviwH+YLxnbu46U0ys/ljmmI4whJXO4p2XbM6s9Vnuur9qf/Cg++JMIN
8OYr9u4sDGaYnAvUlInhFOlDPixmFO/hVKRLKCYYGGERhCEjvAS5uGOHlulYDFBacieV+K8lZM9g
bGwMSGYgVk22cO+ucAyYfGLOZkknTm/h+KmkhCo1qifCeInm3IMC3+JMtMUizEXXAm2NUq906gc4
cGT/SC6mZKNrHG6DMCuksuvBGEPXVs2IxIgmsohXqk7JtuSEBm3PiqP8MAXq/qe8PMas7g8qtAwT
8qec/Ixgfv+iSOyCBsHLfrYwzjxGPOqEvfTqlfpM3OQwgARn7xKQmjrLnNTLq6iEosbw1dAoVtzN
UXgsQEDCir7kMvbDyRDxUGZQUj7nB3EoaKSHn6rwUnqr87RwagDje3JGRyhEtPgCJxhw1IoxnHQH
SIqpjoLP4Y6j2rIOQeTLZmRv+sCNdNhjlwxKPVoCpGpxYUgRCZNrKPSMd1aqQhqxt7LvYtSQdrKE
Pw4OfyJFjHzugxYDR1IJtlZmpPRx1q6q4cIoxKaknNDwvm5RvbDPoaLtDqGiIZgNZFxQQ1BwRs6u
LFhprervoIzuCUvJg0AmDfaLOIDQZOQjIVnjIDhCI/aD0lL/MpU0UOaaDK2kIq5uiK3Oa/1sQz0W
hlUasQJtbwmXCHSeTMGco8pG8gZBDs5cxHLUov5Ard3sjlPCA5zmrbmUq5A8xJoOD5LeohHrg8wC
BKR8qwir7wpPTkWMS3ZqR7g0gnrGAKr+AgYF4wvv8U0QjwXnsHwaCyEm71UEoozyT9FSxM/qUuQI
Ujl8q5UOJ7S4UOiAAybarPz+bpXkKMoY7Tx0UTdq5tzcZw/Fw6+mA+eip4nIiudyLWmMQgygqqJU
AvOWo5M0469mZyO27zw2SjJO78Nc5AL1kU0ckLROkK1isUhQRxlHkxZVKT10pHrO7a0ApVWOsHIw
xCYSZdMS/wk6UsxEIu4tryYleEoosNBxSuw86IsmXBHebsYhS9O1+smaWlD3foRZas4ggNCIPqzq
cMpiaqG4dEpgLA4yupGShk5krOInVWIMPSwm6efiHMd7bGbydqg2oHM5u6ci7+aLdCIW9+k565N/
8E/YfhAlYgLCXs7cGm2yXkL2JIoiwyragHOGZJEulm7ERO1arNJCvOPJZkJDL/CZHGIEL80zPMIW
SK821GkT+a1BJ644CegQK+WteCMfwUpzGnPkLAkmY2whZXFhXkN+YM4mA1NHYXD4irK9bK9cTo6X
ZCQkUUfhGhAnamRI/m4x8Y26Ui484yQqcS5ahEYjgnTqdv8lMzAGf9zGHClkqBLLeY7mTWozh+zs
K1/M1dJF3d5zPoxNSwmyImWD8qjtoIbCRO4r3JAlW6Ywy3AOCW0Gt4hEZSKHKWoyx4Tzf+Qm33qi
z5JO35QtSecJV/rjuEYwlKrrI0nOVdjTcDg03wzIRme1SD3shLaoYO7s07Bj1ayycrRFVR8C7kw0
RFmTSuSGvpRNmb6nETNoKQbR/AoVvziSjjgEy5xs56zEqjTszTjPPxuTO7hHWcnDPDnoJLbEP7hk
DdEmdBzNcXgNSfO0UBVjqPL0M0Lupy4SEFtORbFSINvIgnBQNDCwRu3pLXqji+o1+0KDd+SG8rBU
oRL04k7/ZBjTaJ060V8iSkBINiriUjxkliO8jxcW4Z1MUZ6YT0/brig1MTYiJT6bkgLP0EWFoziA
Z2UedEzrMnBgpKuuFDrqIlUUs1D2jfYKK5dqDTOZhzE8DU3pYsaeafgWLTxAEgXLYuL8LXNoduci
yTEoU9hmZPaiNiiKq+pqSiOSLLeCbUNYjU1gDDID9FEdJWz5ihvN40o57VQJAkNeQ1a68xc5zUTx
piGIycr4JKga0iuIyTniJ3rChc/KRVLCcOwIc0JiZNxykli+th+Xj4wiMShZ7sdGRPAQI370IlPX
TjY6ybi8xDKEITM6QlApdlFCoyvURk+TRCC5NOdophiX/0WCSC/kDLdFROhLaxNrt7RFwS11dex6
BwdacGuhRscKG8nh5KXhONY6gMkpUWVGCC3nms82VTfgeA0D/8L+SKao4KINRYKKgpcr1oKDCAfR
aPcxX9aUNiwY26T2lqNDq1G9qGt/NTN1gOI9jiajkHMnX9c9INLpNlILf3aUpPQBp+T5cpSEkWZ7
hYI8qVL31KT8VE5vvJc2bAKU0AYk+sNXa+EoMdFldm/cGC5+C5TQWqjVAuaEjwfs+NEWEUd/5edJ
4XFsF1VUkA4hHeU3XKJj8g9HJRNSvPLegspWge/EdHSUMBQlkrNK/zHSuozeDoIRguG4JGFLhCtn
eYGLo/+LN77nRkqCPuetosoIKfsiCo9xQnXzRSIjG6tpNWIp5KDPxwYTjVfqWWs0LkyzcLXrILQ1
Oy8rTyYXhfBOtW7VvhpTY3qM/ogYI4lmzJjSrsSJoHQpQsyO/ARNYBhoVyLG4y7mbjjGZsMtHwWT
hiXw00JyXizowwyKiE6ueZ9xY7+JUYVo/HamThDTUulu8ZgYXbPvGKnR/UTMgn2jwR52TKKUrxD0
hT8UQeK1HmG3kR5DMXaFdkJp6kZC+eqvdIwqSk5WivTvgFZxpKBSRMAJIFPlc08NMfHtgbm08XKD
k6uTZQqz4O4qvfwxF00DxrT1NWq1nmz35WIWL3xnXNvb1gLB0EDxdhjZbFBr8JbfVDOOaxGqroF0
9aHm2OY4Jej8rfDgg0DfGIfUjzz6xSk85fz0BEVrYzsaY87CuMIwYiW8ZlqldRXLxLVsEAml7KiI
FGlL15pKB6bkg08uSlDmJNckebrUR2FtcRPxJIhAl8UATudUkAd5FmD3cxcWQatg2nrWhazNSo2x
Y9cCQ3S59XqVi/bKmVg6jzeOhGh0OnFVdxYhw60x2Jrld0wpqBEW8Hwgm0A82z44ZxSNBUmeCEag
7FjXKJkNqEJXx5KyWRPBJWVRObM4Yj9C/wIVqYiPxYxbpMyd1zp7/6URgbs0Bko54hagALSw6iJK
XJmRK2NZu04xnTEXaXRJXAN1KbawSyOMZ3Ghr6K1EjtD0pEkpWau0mAsC0qKr3b5lg5bAkmlHGRe
Y9KlBsQmIkEYIobqTPHAauENxKBdh6dBsIurSfUWe/KUESpkUEdkEdsvBEZW08eJ9lcyE0pwaDCf
tPgcVUkRlQ66AVrrRo0o/rl5jVE96arcJCRcExohfTMCX3lcUw3ssLOp+OUjkuyKSHAN+RNiPYrQ
9rWBtbds/6U8/9hQCsgoqiNHsRAuIsKsIk5yhEN6znA4L4hv9CYxprSFXOQn6U6qYgRph/8HDql8
R0pqvmXqvSe1s1T3doo4z/TQvmdrQC+7TtiToIOCHXv8l4f0LnWxHpmvtLs7pgamYB96cGK68V7I
MuuCuo24jR/yUSxZPju5zxA8uok1qP1RlSuuP5uzQDpN0kfNzZGHaovjC9uYzVmFYWEzr0kQmAtw
gc9jNV5pmLUlSIzMic2VmZ/UPj/UpRenjqQSepXLaZMll2V4lfuxnwSKfds1uD+RyjOtcNkNcaNp
2LVMIZoUeVGpuCNv/vJlDlNOOI1q/mwW/vDYFi6BbNpxJIZ0OETGbdRiwKnbjMNCQ/jiwFt52Elv
vHfiJ/VpFeWOpFZVXSKQwG+CqEoVxdz/JNiipXPSvaPaCUnHtt4AJi/QfFac1aFBlUnRLmJje8Os
9SAPu6m4pKa4JKdCArmXwsTO49iHZvIyr27iJYLQGtF7D1pS+4NXq6WJMU/nHFSKPWReco0aQmbp
Bv6uNHvLMWXn980FZpJIGJ6tU0XCjKBjuD1BsYK31OnJNGKn3iwyQts6wl9zCjnHoF1z/jZf0Bgb
FkoKhkpWbITfrlSTbT5lzkxnu4Ng5cOtk1FB5FKrOYxofgMn6N7tPINXGtif0LPOCqlzgyo4OF6T
7+5/nuKVAm4ZmempfCLibnayZFd4HG3mzTcfTXrZ2k+QXegMWAkliGNIGbDtpBkTLd49/+1MRBQo
snzuaAJ+H3chfI5meQs7Tv+MUs0MMXmn5UVajMa440I+JGJzi1jWlO/ObM7Q8TUOf3zaOzi5CyZF
JU8qxgQiYiOKgmKm/3UNd+XjPn00wtLs8vySAYwqFZKE006j5kjnzcciNRwgJqGRlIagwYIIJaER
OCnhwoEIHx5UKDChRYMQJ6Z5KFDjxIwSOXL8yHChmJIMT2ZMOEllS5RoHjIq6fHiRpgtM5ks2ciN
RZM1B45RGBEjQoESh0acNPShTYNKCYrseBPNU4sIxeiUShUjzqkDeS3ixSsSr1q8JKVNW0tgo4dO
Dz7M5DLm17txoxZE87YiRZEP+3JM6P9VYhqYS63+hakRk1KgVa9CXFi0Kl6/aQhbFknSMObCn6sS
JchwM+KVNRW+5Qo28UuweJ/iXTxyb0upWUOnrkx6MqOfk7zW3YhJjEOCvyV9NSypaXLKGpmL1ps8
7S5Gu6yL5ZWdNszVrncqvtpZ+uiETRF3xrw5MfLaIm0HBhl8M0ExuyXh5+gS/0+PToElGGbxGSRQ
cg4xdlNR6Y0nVXQDilFgZnIJVBdVsDkYnlRx8RXTRGO8sd5UI+J04XwA6obGYzwV5JZVb0U0YGu9
0aSXdxkaJIlaZVnHYyTY2aIhVCDu+JRITYHHmovQXZSjky0VVNdfbwm2G0gFIYggjfL/wQTbYRnS
BGVtD0a2UH4RhYcSkx3xdOZegiF45V0nBrXcix4xxFpDcoG2ImoJmtclZ4HiFdegFWXkxlc33mgT
bCohJKdF2EViC1uYmiXJLvI59JOkpvlHm6NlPkRqqCU5Ohiae35ZoakHMQKrmivVimFJiBaImp5O
AvdmUKW+NsaEUz16GVy6nfoXq0sZV9iMggGnUph5ceVsYmCm9J2dgv41poKKRfUkqzv2qGmP2lkl
EKlkkmefaOgRKdKMuFKL516dytnoR6wxq5G+ByFVH4T8+TWstr6qStWWBtVV14y/XoQrRaLSB9Jq
Jxnr4Eq/eViSTHuJi1JTtokq8UNv/0w6q2qAIjdmv75+VRO9gE7Ga03+NSlroh6h1eOl1tkiCVq5
niawx0Pa1PGxE6ex85keorkhviV6PGh0TKPRsZQlySmoefF5TZWofankcqt8pvEwWLFa1moaM7YH
7l0FNehXxqmJXHPahk1JKXAvS/av2iMGzJmg2pr0n7v6ffZmXDteR5ZZuwit6S4KTuSszHX7eefe
op74FdUoZv0asoqFDW/bhcWFU2S6uQs2Sq8ePVtBzHboMttLTYrjjBQ7zbufMR9KkuhI33ac8Lcm
ba165N0IUceNUO10VRkqyWKd8sV4ttNrRbJp5GTZkl1kzz3anOf2ZqSUZB+n6q97hf/aRS3NKQ4k
Xtr9Sve0mwBcyXc6JLuudI5+E3pOafYWpmuxrzlNWlJq5sVAMbEvc7Br38LYNB8D9k1+2TIMoXwn
nxpJR4Mk2sXQgpYWoakQc5uzCglz95rrua9CFTNg7VayNhM1RHFSoRlK6tI+hJjGYg3xm7xAdag4
PSRSqxJXoMaQEuO9C0cWlMxbkmZFAHXGU80x1Pe4Jb2KABCL7avVbkjoGIWgcH8ZMo8EV5cYRnCH
LWoxi6ZqoSNU2W9iusri/Dw3HOZ0sWgZOuCesAVBxsSuT4gUZKFkgzi2OU9pYPxbYVjnovwc7FAR
vIhS4oe60uCQN1S7EcwWQjIqaU3/kaCKknJapjFTjgeOvFrULUnpphBm8YRqsaMK7yg0PnJHRX7R
4bcOSajz3Gd0ixnRFm33R6SxZksGlNUsacIlN2LQhJ0qHB2J9xFAca5IljEbKsf4qECV6VmlbGak
KMa/EkYSME0zYdt2yU9CNUmEjrubID9ZEQVOBXkCU4kQSTS+s+RxmGURkvrCI6d5qg0mBs0ab/yC
wnzWcmMKEih0qlW3l1xrUk8TDHgOarSD7g4qDelYRsfjH3XODywznYQ20eOl1xDJV13iF6goMpQL
ITQufoNNnmgJyX+lTD4zdOc4Ybkshdmqg9Mb5viy49Du0G19XBvPb9ZVNeqEbD3+/4nWQeapNx82
854OURJ6FvK0TUIPbYmsnbdatc1uLTOfxhvKqYwXH0AiDGvIcgk2V8QVR3mUNuwD4zcBelQA5nB4
13MmVZWy2B/i77HV7EimeGHHPJpvp40DKO+Y6rxLQrBqr+GlgzhbvwP58oZOMeURQxhK11ovf33E
62lgJlzCNs+jr0SbEkHmxQTNiVrPTB00hxrC5LyIo97bbVOla80FEcujBoWfSP6nwZOcpJUJMV8L
KedQ61CoMlC7HRpjgzaLPJY8SEuQRfsXpTWtz5D5G5iDlInXtU6MoMmx24A9k72ROCWqRtnmSXBU
N3v5B6ijUaJUgTXC8JyQwMUzVHZsbWYeZTHOISI0XGgOucnOqUUSZunRi4nJWjAJ8SKVjVpcDck8
Ettogvcd7/Igu5nqRTgrV1FgD2VYvwj9lqBA7Bxzh1WmpT0ucR8NJbc4yuWk0fejGiGQDj2WsW6u
zspdQRq9FIlZNLpLvgxyJf10a5Ds2CLG/9iJKIx58S35PPUjV7lsAYE4RDGZOZHWHUw3ZyvUvl6J
kYaUJJGzhlhqTrcm/wNQg4DMuxlSsFfFFex8x3Uk8ESJuVQ9kn8R2aCfyJW8o7PwmKlpR/Hx4s5B
E8ZYOIXXCJLYyLNS3ZGpdc9jBZjJhDxWmmSZvGZe5ihM9eXVELWR1KinzblitChn9RsIDypazRws
7RDSILX2Ks0aM9ChOWrcSDFRZuwagy4DZeVZHvteqYnoLmJMlkVs9aIFi5pLrlhbSP1y2NcOYHTQ
NhqQTsjafv2prKRcQ4WwiLEVTjigZPpRgxmOus9jMeMebtOhOhB3JetKVCYMmMhKYqWxMv9uu4qL
ExOqqBHL6rFPA8VBlXOpsxF/zI42Fb4WXgJovMDqqs+ml2bT7IRWyla8RBmscLGz4XCM2Soj/E9q
0mrM3LpgZAb58A+rkerVZGbTKPNw8T4S4Au864KuTtuoDGtM3f1eRk4UYldpF+Q7JqW5CeQapw3T
jnyUXFmG1vfObOV6mOj7JOh8bI84duZTr8/kpyKnsb2qL9Dm9LMDdmLRD/K9oLkQWFVc2IncjCXZ
QxM2Ra/Uk6VZII8ndV9NNx6N8366Myl73FelajJ5BRN5VmGMzTIW7mxEf7KKSUyGFf3nS6glEJHQ
ND8kITRISEJu/BP3N9J9D0lfa9LvPvb/Y/J9q5w/dd3vfrXLP/36SwU/5k2/fuz/JwgOy/uvBIB/
8n0KQYAA2H1vISFqc4CyMixikIDetxEd036N0H6MICETqB9S4n4C6H4ds3/4pz9u9H/GEX8DYRzs
N4JuRBQCaCHS93/edx8xQTgRiILht4DoN4PRR4CEQ4KSYj/6MxlBeH3xtxcAiIPQJ4A0qBIKGBMT
d34uWH7R9zTSB0FBCBfgR35V2IH7R34Wx37Pl4BqgWsrdCmXwwsxIAYxcAMywIY3EANbIANh8IY4
sAVryAVvGAM48IY3EAZrmIdseId62IcyEAN6aIc3EIdrGId+iIcxEAaFqIZs6Ic3oIZr/5iGmFiH
jyiHMmCHh+iGXPCIdwiKifiGfiiIeziKjqiJfogDoiiKhAiJN8CHoTiHdXgDriiJrhgGdXiLa+iH
soiHu9iGptiGW8CHxyiHf7iJuIiMe9iGi/iGW9CLcHiJl+iKrhiIMVCIsniMiUiNswiH2HiM2xiI
peiIaXgDeFiK03iJpbiG0OiH0MiNsGiMl6iGsriMb2iJ8HiJ85iHhsiJyCiH2iiJxxiKb9iGrPiJ
o0iOgBgD6CgGdBiHgZiNEGmOdliHhRiQc2iI+FiIFNmJrqiM7UiLpriMjKBHl/Ijl2JMCRkGsiiL
6oiLx3iLlViKYlCIOCAGx8iT+/iIu/+oh63Ii0D5iLg4ikYph9QoiWHwkd84i504izjQkbzojZC4
hk6Jh1pZiUbZk384jdN4lDOplJO4hnUIibxYlrOIh16Zj3OolBTZkRKJiTMZlHuohlM5k1zwjMAo
kAfJlb3Yh+k4lTIgkVwwh3iIlnk5iZMIjVOJiXNZio8pkWHZhn25iDhAjWEgjNOIlhIpmPiYi7mY
ia04k2ooBltpmucImn4oBp85l3j5lq35jemYjgQZloGJh8pImLyIlkjpm5U4h8kIjJWYjUN5k7k4
kTeJlqbohre4lZyYif42OUNTLmlBdHQZlBLpiwaJA6GomYT4lHg4l0RJmY8JmL4ZmDn/yZVuGJZo
SYwfOZsiaZvfaJnwaZSDSInYGJiZKJizWZOjeItKGY3jyYwKiZVtuI7riJdsuYfEGZY+uZvJOIvD
yZ2MWZvU6ItvqZYEeYiE+ZSdmaD7qJcguocNKpTh6Y2xKaLkCImS+JmOWJqt+Im7SIel2Iru2YYi
+pNqaJmf2KESKYkN2pqfOJyDGKKl2IaxeYuw+Ym62ZxKuolgSaIz+aNE2ZRhSZOTuZY3MBaWgi7Z
EQlosSn2KYvmOZOAqaIe2qFpyoZCOqK7WZrpiKOCuaXMyJAmGo5p+ZdDyYwn2ovTeJYaqpQz6p10
qJh8WqYxqaNziI9TOpMliZDrOJYf/5qbXMqY40mHQumkaymXvygDtziUH3qijdqQFJqng0iNj6qb
MyqRAhmjkimUxNiOYSmMq2mLU0qQwkiQXBmTlUmniKmlhHiedBmZPuqqfRiLgciL+IiiIkqa7GmY
k2iTPmqTzjqUcXqPv8iHeNmTZEF0ZYEdM4aGZfmYrpilrKqRgrmuWmmW3viNsgmN3cqe3TiO8Pqq
fZicf9mu7LmVwrihU+qNynioUaqMYtCaxEqU9OqY9Uqnm3qLe9iZKAqdntqNP2maWGmq1gqOTxqW
AHqwhmiTW9mOijmt+AmyMbqHbNiT8BqjxjiLV8mbzOieAkqkeHmRQAmg6UmRCtqeJv/LmFGZiNUK
oXqYhkhapqD6ien5kaKYlwRpjMMIqW4YmkBapUyZjVyZhu+pjpo5lWEQUWLxI/1GFocKmfdKpKa4
lFBbjMH4sJS4oEW5qOv6ofCYr4j4pm44m6PIpe0ItzfJq95JiZLYq4OoiupIl6xKoyX5ohnbsA87
nN/osRE7lcPYl/CqpdNYoMpKuZmYq735iVCJpomIibI4oLgomxepsKuomrrJuFq6iVcZpVeajZ+5
uLYpuNFIkKd5k0bpiE3qtM3KlLM6k/IonOEpidG4nTv7ks4anumIpLBbpqd7iLKIjdtKsncqBtyh
FmFKWqT1QpxajLS5p047u8LJubb/OKOKCbsr24y1mIu+m7OUCKpoG5qDWKA5Kadniq9xOJycuLU0
yZy8irGyWZZV2ZhWC7SxiKL9ObPZmKnYmI/qSonhWb12CIxxG7V0+b9c+q+ym7M/eaVRSry/aIg0
ebp+2YzH2Za76IuJKZBNO7vpuKxWe7u3G7mz2KstPI3E2LOku7Y3i71Maq5GeqZhKYrSWqXeCY+t
moiIaa/YuI9fm3iSADSUg50f6qJ/2LEnDLUx27ljCYxYW5toepgjvI62u4ehWrTIarlyGpNo/Jww
G8UySYl0ipA7mqsdPKKFa7/liZmiaJmamIrmWZpTuohU+byTO8HKaKZRWrOTG6y+/7mOjVyUHwqW
USy5M1yYpOmyQDmUcbil2Qi1OcuXbFuzQnmuuhigFZq2mXiRT1ulySqpRxmbUiu8aQmxhpiW5pmU
wfiUigzCPOmgD3uUB3yabSkMVdxQlbMpdsQLA1uSaOqVkkiW0SjERuqbw4ykYYyVbqiam3qaQvnC
kJic4Qyz9nnCajmkHlq0CpvEnJmZROqgydmgpFiTJdrLecqWbRrLe5mGAyq3EiugWVvAmhupP6nG
kIoDCnmMOBrBTqyvSTq/4VnB8lq285qYcLvD00qb59mdsciZZUui5JiXb9q7h0u5fPyZAeqhRrqL
L9y09Cmzo/nN4myjmRu5RrvSzP94A4yAa8MU1OiS0OmJoaV8jnmar2JZnGsLwofcp6lpuLpM0XaM
yZHqzrfJm8lZxloak2g6s+tMoS+rqxQql+Wqs438tBsKu5Bs0Qtsv7ybxdl4xA89vqkYBlOanA+N
n6Xrs6AawPpauYSKioZcroIImklq16XcwOeJyWZat7w4sC9cl1mKozK8tTttzDBtzI9svIeJmXgd
sUybr2gbsdN7wuIYuhIprg5FxeFjC6HbmVy5pH+ZjuTMqOIIlr9Iu0VrqYvcu3U4uIyYsZQdmDUK
r4B6lOdq2mC5tsf4lwidqQHN2218v8JqsHzL2yfcjkn8iWqIzd9cw+/5tib72LP/Gb8AfJgTaZx/
HZ+B6tAiWaJP6aPoqZwDaq7BaqmuWq+gm9aUbczT+tJ9nZjceZE9GovxzZzt26O2yNY4LIwI2pFJ
vdGke4u1msrp2K3z+7UqlEff6jOLIAwYOqEOTaMUWpvnnJ+BSbKJieHxeqPxOLXenK50apcAnci4
qJV7qtxbPLmajdJBGa17G7AMTd6hSsrkO87KvaFarLCzO77/PJYgSq9yW70ySrtl+abULIpeTd/W
Gp8/vNd/zJ6JuN86eqFdnL5ZrY5626ROKZP2/Nx5K6KDG7SLS9RkuY7MecSynLL6yeX2Otn16os0
6cuyWonTOBYrlHzOzFVl+rhm/8vWM06Ii02VHzrYYazW6ZyVI+25pOmQaZiL7zqKBnvADz3Q5SzG
YX678Ti5JJvOmNy5HwrjDq3d8yqhKjynQOnRpbvWZp6kIYqt6JnOEcyoGCvOCsueBLnij7m+w9yc
lEnerAqpL1ujcSqQTM6NjezjWY3EjXuTBTq0P/nSqY2kZhq1XNCTuE3I+AmOp3m+QEunStod3UEW
MpYdeui7RPvAtemUM8zPqYzQCI23/b63k43JCtynN4uarny4yOqV3DrC+XjTxVq47OmN/xyTW4rd
eWuUmkibukiRNSngsrq8h27eEprcwU6tlyrE7MvPA83EaV7xbwrnxuzLMIysuP/cwwhenmg+oSKN
wMv9iLtbl7weidsKl+zuoLLrinGstymap/A9z2wYxwJru3h5ucrob2aBa7WgQrhGtu6Kzmap4D07
zWRZmOTYrbQ7o95sm58c6bwZjjddzjWp8fDKjIa57+pokAENw2cp8ZrbumlL4sY5iMS77qUam5sq
wsEax3RPh/EpojI5sJEZme0Z+EKbrxk+9rY6pBI7wtuZpYPLlsa+8J4/orXKrT19rLnLrHFr27g6
p0Q59FBOodNL32v7nyFvtw+c5cV86BcvmzUainO5k+781YOrvSt5LsYkCWNB3HLsk5mfwPQZ83gr
wRD/9OmsvkUrteX8iMnoja//vo+m/ZU1SrJzDbEsi660mfhObMkFz+C1vbuIO6Lwj8oqS5r3L6cA
gWPLjRtbcMQIIyOMwINibnC5EUOMxBsLY9xQiLGgwIIRJ4aJgWPjQBkbL2Y0+PDiwC0SXU7EEaZj
SYUUEw6c6NBlR44lHUIEyRGHwoYXQ7I8+BCjTIYhEd5wyNCk0oMgHRrkaBHi0aQTlboMijAkyIQy
M6IUCTEmQqJjEQp8OjHj1qtidkm6W4uXpL3BGPHaxWusQpg8SSbsaLDs4KAdvcqEWPDjDY5KEQc1
SBGnZhwHRW5ZWHVpzc9VnSbU6VDG24tqKZsMavViU4sxNTIky1omzIFSN3oc/7vUJceUFLlklh3z
LFmOMK0SPB1RaeQtJYGOXRvTc+3nIX9zVrpUakmLM6GKtb26ome2HpcqHdia60yQSj92pngRMXK2
R+GLRAwig0oaDTKeEKuopJTUuoxBjY66bDWGDGpJpKqyqw+mlTyjkLJFeBHmL7x44eWvXSIhUSyC
FHzwsoMyqyqj9jB7bbWcRJpvK8tKeoqm82gcCDH/koqMNLMW2kyz83Zs6TDh3qsJvukIosupniIq
L7PMxMisoBhIu+ih0uqjrEsVD4JIhhilq47KitJEUEHyTjqPpIiIY1FBjqr8yiuvyKvpLQqF6pCi
iXpkaku3tBuoT+82gw02Hv8tQkzG/ZpyTzPkeFyzpclME2o2thTLDzGHsDxJJhhXpcwmGVMjLK8Q
A4sksBIB60wxiMSISYyE1nIo2C1OzYmgnBaCiIswgt0IyT2JJQq1svyEqtpdHxIWB4cWWlYgXhUj
qlrluLWvWmYXEmPXl7SzKNiMmPWVXW2huvbcXjvbDSokqzVIjGJ95TVgxWLitldewwB323HjdTZY
hEWSwVdlodLOYYaIhZdR3DYWwyeRfhK3341+WuihggcGt+DdQNMWO2TN1fdbdn86WLuK/IUM5HmD
NRRmkLlQGCF/l2RWonl37RdAHLjwNjashhUPW3MvWoQvSWrBiy9ePsSLkUmwJEljkknQmCQNsMf+
umy0x37jbLXDPptsNDIh22y4xT47brzNFlvur8Mu2224B89bbbAlQZvswte2+2/H3a77cL7deJzw
tRUP3PDEMycb7bAx5/vusD+/PHCzD2fccb8tL71z0AvHZPS8G4+c77VRVzyNTBC3HBO0Z0f898wb
x71yz3k3/XbLQ5ecd73R0Hts2pUvfHbH+XZdbLuD97zv5lknO/bZdxcee9Uz+ZoXvfj/0ssWFEfc
JQ25D5/fbujtdqMRScYAG/r7v2eE2fyGBvltz4CSG6D96Oc/AW6OgJJ4oPwc2L/tDVB6zfvfASso
QblpsIMQPKAF5/fBBj7Qf4kTYQhByIgB9k96cmuh/RJXQAgmjn42lCEaIpjCGpJNDBws4QVpGEQS
ZvB7RhQgEfcnQhzG7XtPJGACSXjDKQ6whUxEYg8dmMMZ9tBs77vLXviyCxHF73uNwOIkxCBESTzP
gWhb4wPfKDf+abCG+7OeC7NYxyduj492JGAA4dhFDn7tj1qUWwD7iEA1oo2PY0Pj5rgINhb+bgwd
lKQF7yhBSS6yi3w8pN28RjY+RhJ6/39MIxMZWT/EpbKJQZykHYFYQ7OFsnlfm9/v0GBK0+XucLZM
AxpTWcddijCOr/wlHrfGi0jY4i4oQhEj3pfDRQJSlBWc49gQWE0qSi92LJSfHjH4yg7GkJtEfOMx
kXg/dSZOmGjEJiunGMRVdlGbIdxi//C4w3m6cI1erOf9/lfEeN4TkReEoTZRidA5Sk6RdisoCdVp
PifGk4hpiOMlxzYGIa6TjfIzZfF2aFA9AjKb8wMMiVBEosAwIhi24EUhI0g/NOozieeEYiMT2M0H
AvNvR/yoPv22yPplsYQ85aIrj2lQD3Zxpml4aA8b4Qao9jOGRnUjTp8q1dVxc4IarP/kVjnqyp3y
cIM2zWn9fghBSirQgBstHv0ON06/tdOCMm0lLtl40nwekC/S5AvXSmSrSKSSl2TdaRy3akEx0HWO
N+VfIGsJwFpCkpVQleBaazlAeOrRsl9VJP9CaUXTRdWPnB2pDi3bTcmtEbOClFtNMYrD0KL2hk1N
qGp1i8NiSk+nmG0eHit4WCGysI4sNGVEe7tLzKbRrvY7bEi1mVrSoSGyvGysPFG4Svt5MKR/DOAa
7apN9mmNViS6WkxPmUxZPtGW7XSoTLcY2/lFNps9bGtaW/vGajLWgJf9nvgye0SgurKHtYNiOLEn
Thmaz4dzfOhy9Ujc7yXOlrklJGP/5UY3Pu4ShIu8Ln3nWF9EtleAdOtr5NJ6PJDO7b9wZR5UGyle
QqKVg36j3HobCNUwLlMSzrxaYBlqwnv6kL1RFTFprdhZxtb4mgVmYxSPGNIQyherR51sCW9azHFG
2KCMrads/bk5BGJZhKkMqDsvS8cJGzGhLbbhaGnpWAL+FLdORmsa8Qvcql6QmGqE8v2+uk0TDzTK
Oh00Pp86P0mgKIwr5Qs0YzrKFLM40ADOsht7KtcXZ9C0nsSioiHJVgVT8aCLNl1/VzlOzc55uaQt
af9qymLiqlOPSqafLK/sajL7UpYPTfF/cUvn7SUvgQFM7dhQq+yAAnK5QyauCMHW/94Hd/WixP7x
j3dhC7yg6EMw3UU/rflhs73By3UrawWHCkvKpnuflcZigUnX3M9yMNpN1OhMAxdqKvM0upQV7q3v
iWR7RtC0I27o9ibq2TqjuqjNu+Qtk9lGamrQhr898JcR3d/WvTKADzUxw6mMXCwD1K19TPLm/gmY
Ni4zpY3mhS3COUgjAlMS6rwqoi1oWQ8Klbd2ZjjKcSpqaR+QmCG3aTFLuPCkPnbFaBb3Ev925pNG
26TSxnSTzVlqAkZ0gmVlKthsDd2tk7qFoJTEG9iZV4c7Nag7rS7Cj2nXesL85XvhdmDw0vAcnjXk
TA0rU3PbackFdctz7DCgM73Quv+6Xdz/M2hkva5KAZ5zq31nOBy/N3P64k5xhq624AeuwfH+z+ZY
tPYTO9vp3spPhI2AM9w/f8368ZXIcCf14ebeypD/19RPlinuFYg1H+8ijIywlRL5jMBzK/veqfd9
PE35aeATmr3PoyAluRzEdrZ6rVs/ZpaXP9NLvtWj/1ysxjGMbjJb+cVhW2u+Txv2Fmc+jsu3W2Mz
rWWH+k+2uUUj/ZOEWlMz+rshOrO9wxq65zu0eUKy/Rs6LYKvvbiLbWuj87oa27M93wMmcCI4bjq7
X9I6VTugk2o6X3OvyRoy+tM4ujKb58IlGaKxeKu8F1Osuqs8XRqbT/szI+qrMnP/IaObNhdMtWLL
pRN0uoIiu5OqLQL7LzG7MRNsq9Bbv3/KP8NjtZOKNJhippi7C5hCkSj6NKXiuMvjIfqKvgRjsA67
uqoCQU7LvKuKwzjTsVUiJaK6KZ0zwFn6HIKrncCLoCFanV2ruFPTJl1Kqj1zwSnsKIQru9RCNtHb
rcsDONxjvMMrusLzG4a6ofvjKZ7LL6iKtC5khK4Rhg8xo88JNDyzMmRqoDiKpLFDsKu7oM0BREKK
smuysAuaO1kipzRrMnQyOJorqrJpNbM5rMnTRO0DNKDjPz9CuREzpR4UPNgzuajrucl7NrLSw1Ry
Py18QTuyrzXbp1yTIgV0Pzob/xGsATcKHMU+i6DuW8TSe7p8Sr22G6AIA8IX+8RitC7f4cYR0sBj
4yCTM62AbKUlmsOGwzh4/KioKzLrM6BIREFsGjsQ0sM1UqTLiqodzKzPwkYb68ca8zCi+0GQNLzn
A66L+6BEAi6b257AmpU2aib14QtbMCfJWjUTiz+zKkMtYjjhW7G1WshEi7diCj2/I6qfg8as20P7
U7bQgsNSSwNMyDcmxDywekGxE6VyKi4TUz9gTEIE9LT66zSdyzOStJ+N3LjowzRD9EZEwr7/okjp
+Ysu3AW9YLm84AVKJKdJgEm2A0V6o8TWq8vLssL4gku4yjnrmrIT6io5tDfTw/8pSZypu+Ihw3sl
GDsnFmLGUBNL6Bm03FGyyXNF3VO2bsyw+4LGs/yhaEuuinLC3Lq+TiOiQ4qibAonSjSzr7kL5Gu5
H1upMPQzBiu7K1w/OnsoASQd5gTB1DShuDMhq8OjxDTCuNmgvqI+gWrE3TpGkWqoP5O6TDzOpWS/
pIrFgdRK6CzDFyqy+Uq4XFPMJyui6TJAn3RD/BNJXbOw57Sgjyuk7ytCsmq5vWA5lkM+EilIbBLC
9JMjQjTPqvxINAgvlCzPkHsuKtq6FKK+CqPQrrSkK6u2EmqhOGK7U1s9tqwieNKu4+QyhxPJxpMp
2apQsgHQ77HCCz3RX0OndOz/oLA6tSdSJ+xqwIiCwDQEx2TSuq/BGgvcNjIiEWbCyUTTvw4ttTrC
ubHsSmpDpqvsPPkZxx/Eq9hTs4SkSv+sTRdKK/0xza7bR+ArT9JU07770HPir1mMw8q0qojspMm8
qSpbyHq8K8/iQ63UpwLEotgsRCQsTy9tueFErxPJuycEzdZUz4DzyW0sQrJsP+Fav9WCKMF0zFAd
qyZKpKeCrUnIMQFavVAUuQeztU7Fxp26JEXFr9/5HCuTzyTKVM1TRWLCoJIzy+e5NkB6JH9UIxmU
QmFsJSj8PTwcz25ETTQTtgLzrATlNuI70BHhTSYSwGqjotn6UnL7MNsjV3Hc/1WwI1A+FCeOtDgf
iicSS8NsJMscQsdyfUQ2JVa0urkVZKKHqqRTU8VELDRLQ4Pu06k0NaDxMtEwhVcqiq6eojrdAqsP
wtWBEsZWtSth+hsrRZw4wgTkAyNJuMtmyrbJokEnXCR5Y9Pm063Vy7DQfDrCM1Tzcy4snMhyqyaK
lDdXrcH4sljetEPVZMgP7c/X6jTRYrCFDLl++5zBI7RHHEj7hNDP+yhgU1ea289o9FYEalVWpS6S
NdD3cabBSqmoM0P4pFUoilE8E1ojm1AUgqQXnAQgXVjFwyDUJEyE+ll89NVrBDjl06IepKh4usj2
UlpmjSeJzD5b6jAQbC49soCvgCtBS12y2wOqnG02RgKxjBM+KqTFgPwpv/wglgOyCuzCH0ssvF3c
eLJSJAKt65RdD+UrWYxPJOw9vSE6uEtENWtDijyqD9IoWJxF/RRcIrI6vuoj/Vud5evJRBtCQI24
V2tIRK1YMaVcuAurnYKj3ju3xA3SIfow3GtJbeK2A/+FKeAEN317oLb5swzdHnNTsC/91BQSqBQN
JMfM1zUjJNciqqRjz1l6y2NlTansvalVPqndtOZC12ekq0X8U5F6Vl/cxifKpLC7IpzlJhN10P6y
VSPNwn7yxPkTwTibzzGC0jBS4TaaodJjQGrVm+47S06VPc4UXe4sRgWytD47ImASobCq1ngF1nmN
NeMV3mclzY46QS5dt7jxMjGoz5Cr1KC7xxlCph9Vu9f929x1vMijYXjT0ggkozFK0FIMo1po4nFr
vIeF4dBlxQh0TbmtuZGk0AbsXllLYvKjXUP7zF7DOBREv+frSBwWolpkX3vkrTpSW0+iO8kTWIHM
Sd//wrB809fWDMxkQy00ctYt45/HyiChnBsTbcV1EjvD4zIKdMcRQUX5DEm6RUwNHbSNNSGArb4J
VVFHdKD/8xyC7FL/1KkMyi7pgd95ctdigqe3M2UpTljt66ONbNX+QbZIgsvsu6a6VCyWhD/fHWT6
ZFyuu7NEmtoY2qJbDuGorTpiHl3oNRsLzLsoXQRhcJ++3NST488N09R4/KRb8l96deCz3LpIPC38
QiW0m19WqyBNu6CllOCkal2eYrtX5MwtpSkJmkwDfOOrZDozPZy2yV0SBTHIlB7lSlJhxLzUctCf
Uzo9zafEs06K2zVGy5ptQ5G805paoMqoIuhWPrL2/1I7ZmM9c51IodTVYrswO0tjh64sBXay/F08
3lvMJKPnWxLaNCjWnr3nnnUrZM1H5EzqVGMiv8JQ+TU54wy7S75Xk3Q4DpLKOaIq7hoz3v0LSBtj
vYtnNb7iv01b0HvXqM7E4IMwzaW2eW1MoK6fP/Lni3W6r5pialtFN3MgAtZiB1Wked4zoVZEyT5s
GXWvna7EIaO9GRrDKKs1jRbg4hwuKtRCTABDs92LWqjAKZ3VJEyyxV4heKSzzhoDxD1DtDyryzRY
kMzZY8y5/lM5oNIv493JdxNe9gMwLzXVGaoiEGUlOROxNTo9msvZ7ozP4XXRv0w/O8qmaz42ZF5j
Lf9Eretmp88y4xJ5qfQKzruY0GitOU0CbESKtqJM2ZRzSY+y7EybaoDiKwcDM9uSqe4aT4ZDtj7a
LKBTq/c8qNKr247eXIgaQx49wD8VTf9bNNkETcdmJdV0zqiu2bTbPqyWt3wSsKFDqQ9hpqwBDG19
V2AEWvoTytI7JPnDosBUIYJtbHwL1rHeSjCtpobyadTx0A/WL4d9o2JFwymkYw2mbah26+Xzs3R6
z1kcVEwKxHNdP03OY2HFow6UINwJXkQM1rNjM3Qq0AQlEcFqpsXqphBXREbt5hILPPT7rXOL7aa8
YybWYCEsIEMuZRxeP7s5rBYFuHwbLZXbwH4URjj/ArDtI3DLA0TLc9rNjieH3Z8tpji51DWmLeL+
y8Z2skGIu135PpwmbXEubKYKXHJJHptMeNdNXfJbKiTg+Zo3SJzYCZy2yXXBxFULHqDdIZ4ShL6H
LrycEtXAQTHzKR3CMZ95013E2ei4MkLKnnVNbD++2uHb2RzKoeC18fXIUd7G8bpZ5/UqXp1I6tPm
8XVADx5foht3d0bnQbFNFE2wufdYrzAMQh9BUxyWS69mgjSY2hl5WRafuReVqZiCiZdtgRd9sZmo
YHh0mZeCQfheEZeHr/iKoZiKp/iZgZle6XiG2Rlz4ZaaSfiIH5qVl3h4QZfdmPiPP/mHpwxfQXlt
/1n5jEcXiY95nlf5nen4m0/59Sh6nLf5kjF5qAiWYBF5eMmYZdn5jnf5oWF5yuiWqo/4o/f4jcd6
ndd4p6d6ewmNnmcWhKf5mrF6fWlt9IrUmF6JauEKtgCJyOCTjziLJXkJnyiVogAZ3kAJL0kL+tAT
LKmMnaCLkQCO8CgL6ygTlZgSrxj85fCP+9gJ2vCRZJEOr6gSnYgUI3kKAdkTx3iUHxmPijgNum+P
+HiM5ZgSHrkPO6mJYmGJVuEQqqCItjCQnZCSPjEJAOEMuocOHLmKwR+U1liR85gM0d+QnXALvDcV
QVF+sXCO+UAO2PD7o3CKiah9ddH8XdETsggPUv+xC6shoxNRKS4Uk4SIC7oHFPFPkPMojZbYF/So
kMZ/EtMgiBjJivwACDExbsQQQ9CgjBg4wsgIM7ChjBtbcAy8weXgwIsXbzSUWFChQxxbCH4UGEYi
RYMxwuAgSHFjQYInRd4IM7HixS0RORJ0OVEix5MxPy5UOJCiS5kRBQrkOVJgy58QnaYEuXPj0hsW
ayrsmRMlzhs4IDpk6hMs0KtBaU79afSGyYhdfzIsGDLkyoxaV3a06LAmRaQjG0YtXNZqz5AjkTbs
OrQoQ68gFY50e/JiyIMUI59cXHHkVrmRY0RcJMzWLkm8UtuStItRal4DKUflCTRmRBkCv+ZtKTb/
xk+YM0euXBhxS0iTRFlSRul840TkDw1uZL71YsfGQbPDTYqVeUjCvYmLGclyYmSoN31rFKv1YnmR
ReUrbkmUbsGnIsHPbplzM1uRASUGZ5sdZ+Bf2l0E3EJrYaSSUN3dZNBPBsp3k1AbxcUVgSj9NJKG
AyH00XVwHXVTiVtZxZKJFg3EUGaLPaWQdoexyEVkW0AlYkxRNYYDRZ4hlKJn6/HFUlWAoRcTF2LE
Votrq/ESCS9RxjTYecYtlGRZLkUmUnRbmbgllv6txFNRFLb0V1MypHlme0E1ZSBKTW0UYlEuBkgT
emJiNtCEYqGIVAx/BojSXx4pJ2FQZ/G5JqAd/5FoVGS6AQVjo5IyhZSKmGZ3mYf+bRkapgLdR1FM
SgGFnqTDubcgmS0lJJhxNR0YQ3HFAbVdl0OSOp5XWkGlJJ12rYjgQyepNRpDP5kYBkLn2foeWCyd
tFVTW+QFo1w0tbSIa4xgAmWVvNRS5bku0RmRQw5pJ8ZOGNLXqJ4YsvsWeKbSqdOzbI3JY1Nsyiio
WIoF9SJhwg71ZaE97Uhfc/t11Ka0U3EBEhdZIUbYXc0tVZx8Yv1JHaMMb4UhSD1FF9FFPnbZkbdn
UvbiQbZBuB+CHzellXgta9tUtohaK1e04hl0l8U8jbagSSYaFKqyOb4F1V/wPdSTcdZemZ5dTv+x
K1dH2D3LUbSkqUh1kg19eRMjUqoWm2tx89IgiAOiGbVMY4FKUF+WLvwxfVMd6V/BCKoqkUnspeRT
yOQhDWOk1XaFKVwfu3ogigJ1NFqDugrYXo4c6YUbqEZVFjOFVHEN7VHF2Zt4TWldexxVmXaJXY7N
WoSUtzNmthtzBtGkUlyBEcdZY0L9FfLFeStP5+c8FfRjiasPRTJGDBEoA3HStwzobxNL9LWyMom9
4OryNTfnmWQVF4YkUL5m7mpt84IarvBeO2F0SMF3b9aY85X6tIt2C+rOvZhzuv60zCaEEsn1eJS3
CU3mN2Lp3ZY+AqMgcUVQw3POwHB3oPrkRUz/BKRJZOI0lfj8xmCLc4tyKIYbW7HoQISR0XwcuKrG
2SdPVCPY2mQ1JocsrDlGUQlkHubC6XGrMoCZFI7Ydbb2hSF6GHJKwRoDM3lxpisfnJGdFFaguYip
aTPCoIhslUaxCaWHi+BFuVQDx0ioho68EBNHBlbCO2nFSHiZD8u0shUAnYiHlCIcfEBFNOLx6mAI
GRhSTBKmJSmtiP7BnPRuRqKaRfBpE5lYsqTntD72sXfUstrJNvMrWUUNQIMByldmpSL1qY9imBRP
1DAJmpHVbC188cuDnCNBQyVKlUCS1yBPRD6OHKplYGnaxaKnHRVJjmQ0ml3prJOTLu1rLFr5/+Aw
adgYCulmJSYJQ5V2YQsq0RE164Tj1eAjO8I1hUQ6KiSiTpXCAeHEdZkhUV281D4JJuiVMRIUeAIz
yA+hhQuGQ9JiHEibmJglZa0iC0H+k6NaHWQp91roE8XEnb4pUijqQSiA2iUQLD3rVkeTYHkwYkrj
vSQpDYNY1n4DNErdkCZkK040jUcV8pzxZZ05mH3a5T+ksIihutnomGBZM341UC9Ga92M+iUdQWmQ
msxS6HbEAhsqRYkRVOKFadrWR5UUJDD8KYleArQt2nELKIvDaLf88jWFxZRgaqLoKAOHlymWbnwJ
zVWbiKO+LO3qSkVZ4VtoeTKuXuhgg4yLu/9AWKuB/cg8k3kTz0YzpBth7VqOHdMry0aTmJiUhn/z
0InserzYIjZXtb3LH03amwR96S4T+d5LjfPK4KgKfeoDqVJ/pjQAavSXm7FKqsQ2PRo+9zBbQec6
W7OLOcIxfsIwW0VNlJE17WSDkNsdT4T3oug2KlCYEU1Q6tISkQSSdKTp3koZt7f3kkq9LaJciKaF
Mup8ZEU7lIi0pBVbyBBss/2Zaq1IFzZEBdJnOl2oYYzILYomqy9hPFJuCMhT3bboWQoJmaU2RLUj
MopJLjEnaUi7z79QcKrTklSsugSS2qzYkyHjFPCQalfnhoqGJGHkalU5EVfy7I2xSQ1Z0br/XVsQ
jCfRBOJzd+ocRg4GRILZXAVXSzKmgMSzTd2sb7i24qRWuFG1TRyK7kOqaS0YYaoSQ1UYUx+a/Kem
LgKMtVhlnSW5TmmRJCPKOjW6PU3lMkfySYjDamRUmqVEYYRVDGV23ee+CS9PY1qn7NOmaVGaRz38
0OJypTrg8CR5/mshXEGjyv8UGiIyy285N9O8Lm3QLpgUw5TupxpbrEY1b3NdnlIEKwHvjlKhvrVO
PSatkx7yKIILXZhWTC0NqrJaROsNicxCzKFgBgeYXeiQnNiRJUFIPAxeLUsSspxknTZgggtajxe2
OFVq8ExGauG7fqnIaaHKpzfdZXfgqrDrNNQqISfV80egU5hUmkeu1PqUlwvITxQGaCm1CUyqhoXq
C4HcaV3RaMjc47vC0JqDjXosuLj/m5r4FXu79lmRccljEXdLVV4NWcw4VQ25WmVm6Nq63XyQiKJA
va9huxE1tRbXGU5XCnnh0/huwfclruDgO8052EbRg8KPfkqhQbVnSyo6pIoYzUUsac9duTI01H6z
bqw9jjkF9SnLOr2U/YM1P2dSKqVF22Af81N6A7nlz0Tyz7AaWLYudN6RCbwrUOPYep+ml4sZBGiW
ZWWDMpahb6b1rG8sV9vUSbZeHn6xMnHsGW/DylmiBCY+RfX1WnSvX25xsWmzDt1YSb1Tvb5zueuR
i+ez5A9xrzZs9E8bK0sR7qQwh+tl2F0giMACvt1EDN3Zx0Gsu0sdBystaljBZnNm/6R1RzIllg7a
eIS+HxmsQgjPDOimmMqIe/Aopfol4oVWYWiLu5XE+LQIaNiLy0DQAL4HoBAOeVTbXzkZL8AGJmRX
asQGQSVEs3Sa4nmLmPzdPXGZt2CKCJ3XqP1VtAjT04CQgyxJZUkUhySFTpzZddGGUiyPvAxX6GUR
12lLHuVJlz1R0UTIf3ySxqlEgH1PF7XfehyG1VjdKYkae0iV8PSP+wgRHzVMVdESuwTJfJTSWSyb
RgHQnxGWVvRWGqFQjaVa5MFVQH0a2BWGv6VdRMjVziTM5+BTRGkHDMoUOknCWcGG3EgCaliZTLQg
aVhfkqwWAmELQfwhD5pajLgVb/8gUa5MXos4FLOhH9C9ClKZR2d5S1akySlFXdMxhuw40ppgkML8
UgLujmcUiJikSqLxV//IGZawHXiwy/fk0zMdWtWkIdHsULjl4F5pnM/oBbtRy4bASl2kDmrNl06g
D2K8EoAgWGfBBVN9Hcm0yv5ZESllBf9IT/8MjbIoVnp4iXhIhFl1V2zA0fxs1x55DabcBIksiD6K
zm1gxOvdUH8AIa74CxHtxWLlY08MBRmxmtjoiUc4xGz9SEDuxUPiSh7xo/pl5EAeiRH9Ul4kBN9g
RFd0Vm6Mocr0RPMxSMOspCjhY1rwzA9GIlWwmmeAGxGxBQA2T2PQWyk9YEZmVEv/2sxsyEXzbORf
TCRJ0FdCAuHFEZHdHaBi4YqyzAbujKRUDuQrOdtx7IRFco8aGeQ8EQf4eGIxxhiulBB6oEskaBda
pVOVoIEYiAFczqVcxiVdosFcSoJd3iUjoMEYzOVf1mUa1KVgioFe4mVf1iUaJOYY6GVgKiZkokEj
EKZeMoJcBuZcWiZdyuVgzmVnwmUa9CVmikEj+CVoGqZcwqVehqZfigFr/qVeHiZkhmZn2qVhSiYa
yOZi3mVqJiZvDqYYNGZkpuZl7qZo5mVw7qZtPmZtKqdpjoEY9OVgsiZkpuZjqiZnaqZraicj1KYk
QKdfSgJ2mqZcWmZd6qYYTEJ5/5KnejJmd/qmaIrnds7mZlJncaLmYOpldS4map4mcgImZDJCY2Im
eAoof5LnXYLnX8LlX2pngjLoYcIGPLZGubBGJExCGmTCJEhCGnDoJEzCG3joJKDBh44ohkqCiZZo
GpCoh0pCi3boiabBhp4ohtbohsqojHIoikpCiKYojU6CG3yoh6bBG5goiZ5okaYojIoois5obi5p
jKIoi+YojuoojJIolmIoieboh3Zoh5IoJsholHrpjaIojJ7pjNIojGKCkaYpjDppjbKoiV5piX4o
iWbCjorplhppmJqoeNIojzapnHoolmaCjGYpGhiqjiJpmZLpjoLokeJoiWapl/9KaYxiAqKOaZse
KafaKYb2qaVWaobeKJuK6o+aaZduqJzKaJAeqaUGKYd26KIyKY1OKahy6Yy26oleoNxMCWoYWy18
aWNWKqJiKV6OqJWK57FyKJaKKrPqKBqs6LPiJbMia7RWa7FaaXoea24upqg+qXgS64h+6Yq6ZrMy
65di67hyaF9uqrNeKbr+6ZZCK6K+q7yua7SCq5fmq5GuaLNe65f2q5Uaa7eOKL8+KZZaaWmiK7Ku
qJH+a8PKa7Ky5riCqxi8QXdC64p26LCKp8cCrLpeK6VOLMmKK8giKrZCq8GqZ8QmrL9Ka7cS6pfW
a6bqa8qKrL0CLF7aqyE+SZT/sEZs1KyJbmubCmylbqqUBmymJusYeKrQCq29Rq2lPq2f0umUJi3S
Sq3WLuymjmhpnmjHfquRLuy7gmsj3CuLNmbXgqy9jikjrC3cou3XZqmVei3HluzVRm3VqqyXOqvL
Mm24lizauivgii3RjuyhriyKpieZZuqwTimWfq3fzungYqnaXuu6iiojBEPb2JGxBRtqiO3fUizb
1ivaWu3EnqvSwi1upqy05mzDRq6xZq7N1uy7Hu7AGinJiqyWtmzLpqvUUu2/HmrZaqzK2uy+RqzD
Juzfuixusq7zpi7rmqy+lq6OHm/mYmvZkmvuIqzgJq/wPmvjLu/xQiv2Rq+o/zYm4oonbCavlWZs
pbqolJxLBhJblLCt+NZt3i5uv45ox/4l5S7v2hJr2Aau1qpu98Jteobs2iar9LauqG7rla5ueEat
s3ZstI4r/Oql7pap6SZu+L6ueDbC0XJrjNbrADNraQYv4SbvBjtswCar6oav8gbud5bsC5fv6+Yw
xNbs9e5rAYMwvm4qBu9u1bawvO6wrxqbi67T/Fwolubw8pKoXLLszuqoYU4ulh4uD1uxkQYxu3qp
FG/wsLYr8oYrBA9sd3or+8Zr1Mqu0SZx9zqr+Nru+farD1Nw5sLvtpam5IIrwG7re2px9l4t2d6w
1HIx/o5od2pw427o43oxFf9nL+w+r/CCseEabbsebgnnL8BKsfSSb/tOqyMnsGS6QR2tBgWelWvY
ggBfKwazbtISag0rbeEycKa6pie37Nyy7roWMBEn65gyrdDiLmuSrYmasdeirIwebvYq7ydL6yHn
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
WVKO6RWY5skeZNEihynGlKmj0wDdAr5KQAAAOw=='''

unLitImage = '''R0lGODlhIwAmAHAAACH5BAEAAPwALAAAAAAjACYAhwAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwAr
ZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCq
mQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMA
zDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA
/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YA
AGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaA
M2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/
Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplV
mZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnV
zJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr
/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zV
AMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8r
M/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+q
Zv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAA
AAj/ANFMEkhw4MCCkzJlSijQIMKCEB0azIQmhsUbNyzGuNHwoUOCIA9OyrjR4oqMN05upIgmZMeP
AzWSFKOxZsoVHVvCFCPyYgwrJDHGEJORZsmWAhtFBGmzps+SUDlGnCSyZdSnGlU61cmV6ySsXIJy
4bKRbMmwGiUSzASV7MwYJ4MOfSp0oVejJVPmlXlxBVS8KzLxbFjW7NyLYVOi3Qj0IsqQJLHeWMyX
ckqMZhuybYsSbuerKA2TZIkmY+KyT/HSJOl2o16OVLH6nAy19mqNYm7HoHrDqNDINXP3lRvZbGyV
wmO0rk37LegYCmvvRRvW71m5Q33v/jo38meUwDU25PYZdqHF1cRnhzcdvjxblNZpW1y8Am1zp1B5
zxe6ly7fsqFptNBnhymX11gAwoWXXAbE1h128mHk12V0vUVVafgtRiFWt91gRWtrSZYabucF59pF
LE1ClFmTOefdXuHF0OCF79mklXfxtTaZWwfp9J+BqGF2GHsyAUDVhQkpZ19U8eU1oWPQIaXiQUKx
iNaCGmk4VkONwGQVfP952B9NUpZ55JfSiTVmDF2ViZRAWcYI4JNevWRnRSWtNtaLZKr1ZlVH8ufU
dx8pZdCUAuV2qGDgmbZRQ0hCtBRICCW00EJn1llQQAA7'''

litImage = '''R0lGODlhIwAmAHAAACH5BAEAAPwALAAAAAAjACYAhwAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwAr
ZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCq
mQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMA
zDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA
/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YA
AGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaA
M2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/
Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplV
mZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnV
zJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr
/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zV
AMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8r
M/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+q
Zv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAA
AAj/ANNIEkhwoEGCacaMSZgGzSSHECc9nIjmoMWGYyQFO7avY8dgmBZetDiwokBJaNKIEeaxpctj
jFKOTFMw48BgLlvC0/cSJc2SQBGmwZnToz54RSUpNJiR4phjHPftRLrvaMedHql2RJNSZhqnUK9a
rUpVq9SWXL8WJBi141GeUuFi1YmWYhpGAl2q44lvnta+WeF6PNbUoZsxV83Ck5dPnz518Obh8yg5
56WGDxtdKtryreO/87JSHfNwIGeje+GZvVr00sM0m88WXR1Yp1bSQ43KJvs55+PdLVEi3tdXNdzf
cWfL7b0vGE2pjAUDlzr3aD6qR+cSxnTaKFJ6VpF3/x9D1DfW80jHvk3eEjbnqTz3etybXV5oqepa
jomdEx699IqRBU8+8gionzC0eUdcgajxxBhnaXB3GlYP1kaWTlYpJNZ7Y7mVIG/GJORhVW5BZl5R
2XnkHBpRHZVfclaVxdpY+Qk2UG7sXSijS2PN5dEYFQ1XVXbSKdiRfKJ1dNkkNMUGmWMvtmQib+dJ
l1FFSrnko3JHXtjRMTQxKZCEdG3IWYf7XCnJmmiQR1d4H+bYiFc/0QQMMFJWhSSMZokhRkN30YTQ
nRiiiWSffw6EF0QO0VTehsbFteefmMn0mk9NluXZWR0G49CaN0YkxkST/DkGmch1eExXD8kUEaNp
lSC0H5kqXtKmJJceFBNEBuGKBl5KKaXQsAtJdGurc04UEAA7'''

buttonUpImage = '''R0lGODlhJwA6AHAAACH5BAEAAPwALAAAAAAnADoAhwAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwAr
ZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCq
mQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMA
zDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA
/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YA
AGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaA
M2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/
Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplV
mZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnV
zJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr
/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zV
AMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8r
M/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+q
Zv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAA
AAj/AGPcEEhwoMEYB8JEOqMOnkN4kSLdkBGjoEWDN7hk3KiRokJ7D+Hdg9fwoT1gYmLICLOyZZiL
F9eFjGcPDBhFNkeShHeS5UWKHDPGQKAOZDx4NwEoXboU58iiwCimxLHlhtWCCRuuq8m0q1cw9o4a
C7PiYMWUGsOEhQfMq1uvDY8OZHnjpUEB9hq2fct3KRiH9l763Mii4b2+iJfCuKduHQKBVxEYc6go
sWWwbFdWrAsv3l7LiWXCM4gjhkx7oFODVEcxRhiHYFKDfg1xYLCislXDC4YQZOzcl3kKiNQZBnDL
KhxGxH3c8shFwdg2v3zUYZjpiSGFrIy9b5iS8X53/3+r/aH48V7NqDu67jP6rn/hYeL53u1ITNHh
qajPFIbDXWN0ZgZ/fjmURhrroUYgACAFkwYawlBGoCLxqOPgJDk0pGB9IB0zhiSSpDGfZ/UBQxIm
aEyShiRjrAcPd93BYM866qQxCRopojGDifYYMB5I6+AgRoo3ioEDI3nZAyNwkMwIj5Fi3CgJGmKE
IeSMJx1nTElohCHGDSmmYaUYZIrRUFHnIQaWTOtASSYOU5aJwxliyHBMZzyBYdxbMGD2kJBfVjkk
mTfICWVJndlTkyJm4ASSUfC0KSQOVJY5aJVdCgpldS6GhCdJRuLgpaCi+vAmGoBSWuibMqCxyyUO
6f8UESMyCDnqpGFU6uWuVI5q5K5GcpGDUrW+aamQmZI5prGiEioGnYCOqlQMZeYqaqZCngGooD74
SqmmzwKKxrRfonosuHPaSmYPzkIZralikEuotbcGaimqYYyxKpmZalvmuACI0e2lUHbZ65BgGoqv
m2XWxS+pY+a6LK5kSnKtoAmPya6bq25rbMRUIpvJvtEKbCmdaOwbhqkra9rltmFMMsmbXkKrbJVC
7muyryQ3POSDb9SbaaHmWjpxsiljumoYK0oyCSPNuln0mNoe7GXOhhYcItDKRi2ol0kTWjSd6wqa
qY1ohOg00QhDCW/XZfprb6VCuqH2jSuKue3GVz9wPGaqXfOq4pQ3Fk5loaNa2auo3/KKaaphEo5G
IzkWaejV8Patrro3YLJi5HmrLaLYfvtsKNliZPLhGDcy8rnhIeJY6Q1RZ27wrz/nWHmOK45RucyV
Xm4u41RmkqLosRuuvOw3ZjJkrjdTuTveyKcYEAA7'''

downButtonImage = '''R0lGODlhFwAQAHAAACH5BAEAAPwALAAAAAAXABAAhwAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwAr
ZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCq
mQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMA
zDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA
/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YA
AGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaA
M2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/
Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplV
mZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnV
zJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr
/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zV
AMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8r
M/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+q
Zv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAA
AAiYANFMEkhwoMGCCA8OzDSJocOGEB9mQkNRIICLGDNqxCjmYKYVG0NeFEPRo8iNYhiW7NjwJMeJ
aEhOciPmBkmXNmtO2ilw0o0YMcSIBPqzY8mVRDfGuHFjBUGBRgcWjZERKFCECX0uvXFxa4yeCQtq
5fLzBhenA7EqFPhzaQwDaycZDSvX6sFGT8GmPSjma1ywUPcSjPo0bUAAOw=='''

upButtonImage = '''R0lGODlhFwARAHAAACH5BAEAAPwALAAAAAAXABEAhwAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwAr
ZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCq
mQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMA
zDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA
/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YA
AGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaA
M2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/
Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplV
mZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnV
zJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr
/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zV
AMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8r
M/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+q
Zv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAA
AAiVANFMEkhwoMGCCA8qTMhwIBqCEA+iAZAJYcGFEgForLjwIZpGBEEO1EjSoBiTGAWSXJmpo8OD
K2O2jGgxps1MJz8exGmzJ8eHIsX0HFrx4SQ3QocOXZip5Y0YYmLciDr1RsuZkwYGjSG169OnXLN+
NEqwK5enZ2Oc/ZqSa9e3YN8unCqmrt27eD2iETPWIVm9EPmKCQgAOw=='''

eni = PhotoImage(data=enigmaImage)
but = PhotoImage(data=buttonUpImage)
un_lit = PhotoImage(data=unLitImage)
pres = PhotoImage(data=buttonDownImage)
lit = PhotoImage(data=litImage)
up = PhotoImage(data=upButtonImage)
down = PhotoImage(data=downButtonImage)

window.create_image(0, 0, image=eni, anchor = NW)

alph = ('Q','W','E','R','T','Z','U','I','O','A','S','D','F','G','H','J','K','P','Y','X','C','V','B','N','M','L') 
low_alph = ('q','w','e','r','t','z','u','i','o','a','s','d','f','g','h','j','k','p','y','x','c','v','b','n','m','l')
conv = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

class Light ():
    def __init__(self, position_x, position_y, relation):
        self.x = position_x
        self.y = position_y
        self.relation = relation
        window.create_image(self.x, self.y, image=un_lit, anchor=NW)
        window.create_text(self.x + 12, self.y + 12, anchor=NW, text = alph[self.relation], fill="white")
        window.addtag_enclosed(low_alph[self.relation], self.x, self.y, self.x + 35, self.y + 37)
    def lighted(self): 
        window.delete(low_alph[self.relation])
        window.create_image(self.x, self.y, image=lit, anchor=NW)
        window.create_text(self.x + 12, self.y + 12, anchor=NW, text = alph[self.relation], fill="black") 
        window.addtag_enclosed(low_alph[self.relation], self.x, self.y, self.x + 35, self.y + 37)
        window.after (900, self.light_off)
    def light_off(self):
        window.delete(low_alph[self.relation])
        window.create_image(self.x, self.y, image=un_lit, anchor=NW)
        window.create_text(self.x + 12, self.y + 12, anchor=NW, text = alph[self.relation], fill="white")
        window.addtag_enclosed(low_alph[self.relation], self.x, self.y, self.x + 35, self.y + 37)

rotor_position = ('one','two','three')
rotor_relation = ('Victor', 'Tango', 'Papa')
rotor_constant = ('Zebra', 'Delta', 'taco')
ring_I = ('R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q')
ring_II = ('F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E')
ring_III = ('W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V')

class Viewer():
    def __init__(self, position_x, position_y, ring, location):
        self.value = 0
        self.location = location
        self.x = position_x
        self.y = position_y
        self.ring = ring
        window.create_text(self.x, self.y, anchor=NW, text= self.ring[self.value], fill="black")
        window.addtag_enclosed(rotor_position[self.location], self.x, self.y, self.x + 20, self.y + 20)
        window.create_image(self.x - 8, self.y - 33, image = up, anchor=NW)
        window.addtag_enclosed(rotor_relation[self.location], self.x - 9, self.y - 34, self.x + 30, self.y)
        window.tag_bind(rotor_relation[self.location], "<Button-1>", self.change_position_up)
        window.create_image(self.x - 8, self.y + 33, image = down, anchor=NW)
        window.addtag_enclosed(rotor_constant[self.location], self.x - 9, self.y + 32, self.x + 19, self.y + 50)
        window.tag_bind(rotor_constant[self.location], "<Button-1>", self.change_position_down)
    def move(self):
        window.delete(rotor_position[self.location])
        self.value += 1
        if self.value > 25:
            self.value -= 26
        window.create_text(self.x, self.y, anchor=NW, text = self.ring[self.value], fill="black")
        window.addtag_enclosed(rotor_position[self.location], self.x, self.y, self.x + 20, self.y + 20)        
    def change_position_up (self, event):
        self.value += 1
        if self.value > 25:
            self.value -= 26
        window.delete(rotor_position[self.location])
        window.create_text(self.x, self.y, anchor=NW, text= self.ring[self.value], fill="black")
        window.addtag_enclosed(rotor_position[self.location], self.x, self.y, self.x + 20, self.y + 20)
    def change_position_down (self, event):
        self.value -= 1
        if self.value < 0:
            self.value += 26
        window.delete(rotor_position[self.location])
        window.create_text(self.x, self.y, anchor=NW, text= self.ring[self.value], fill="black")
        window.addtag_enclosed(rotor_position[self.location], self.x, self.y, self.x + 20, self.y + 20)
    def update_viewer(self):
        self.value = 0
        window.delete(rotor_position[self.location])
        window.create_text(self.x, self.y, anchor=NW, text= self.ring[self.value], fill="black")
        window.addtag_enclosed(rotor_position[self.location], self.x, self.y, self.x + 20, self.y + 20)
    def place(self):
        value = self.ring[self.value]
        return value
    def number(self):
        value = self.value
        return value
    def change_rotor(self, new_ring):
        self.ring = new_ring   
        self.update_viewer()
        
rotor_window_one = Viewer(116,93,ring_I,0)
rotor_window_two = Viewer(169,93,ring_II,1)
rotor_window_three = Viewer(222,93,ring_III,2)

class E_Button():
    def __init__(self, position_x, position_y, relation):
        self.x = position_x
        self.y = position_y
        self.relation = relation
        window.create_image(self.x, self.y, image=but, anchor=NW)
        window.create_text(self.x + 14, self.y + 12, anchor=NW, text = alph[self.relation], fill="white")        
        window.addtag_enclosed(alph[self.relation], self.x-1, self.y-1, self.x + 40, self.y + 59)
    def pressed(self):
        window.delete(alph[self.relation])
        window.create_image(self.x, self.y, image=pres, anchor=NW)
        window.create_text(self.x + 14, self.y + 31, anchor= NW, text = alph[self.relation], fill="white")      
        window.addtag_enclosed(alph[self.relation], self.x-1, self.y-1, self.x + 40, self.y + 59)
    def remake(self):    
        window.delete(alph[self.relation])
        window.create_image(self.x, self.y, image=but, anchor=NW)
        window.create_text(self.x + 14, self.y + 12, anchor=NW, text = alph[self.relation], fill="white")
        window.addtag_enclosed(alph[self.relation], self.x-1, self.y-1, self.x + 40, self.y + 59)    
    def movement_one(self,event):
        self.pressed()
        window.after(250, self.remake)

       ##move window counters up 
        if rotor_window_three.number() == 25 or rotor_window_two.number() == 25:
            if rotor_window_two.number() == 25:
                rotor_window_one.move()
            rotor_window_two.move()
        rotor_window_three.move()
        
        letter = self.relation
       
        mechanism(letter, conv.index(rotor_window_one.place()), conv.index(rotor_window_two.place()), conv.index(rotor_window_three.place()),1)                         

##Keyboard layout and bind
##These were written individually because I had no idea how to name each individually and bind the "instance.movement_one method inside the E_Button class
##I think I can go back later and put this in a loop inside the E_Button class        
Q = E_Button(33,370,0)
window.tag_bind('Q', "<Button-1>", Q.movement_one)
W = E_Button(78,370,1)
window.tag_bind('W', "<Button-1>", W.movement_one)
E = E_Button(123,370,2)
window.tag_bind('E', "<Button-1>", E.movement_one)
R = E_Button(168,370,3)
window.tag_bind('R', "<Button-1>", R.movement_one)
T = E_Button(213,370,4)
window.tag_bind('T', "<Button-1>", T.movement_one)
Z = E_Button(258,370,5)
window.tag_bind('Z', "<Button-1>", Z.movement_one)
U = E_Button(303,370,6)
window.tag_bind('U', "<Button-1>", U.movement_one)
I = E_Button(348,370,7)
window.tag_bind('I', "<Button-1>", I.movement_one)
O = E_Button(393,370,8)
window.tag_bind('O', "<Button-1>", O.movement_one)
A = E_Button(49,428,9)
window.tag_bind('A', "<Button-1>", A.movement_one)
S = E_Button(94,428,10)
window.tag_bind('S', "<Button-1>", S.movement_one)
D = E_Button(139,428,11)
window.tag_bind('D', "<Button-1>", D.movement_one)
F = E_Button(184,428,12)
window.tag_bind('F', "<Button-1>", F.movement_one)
G = E_Button(229,428,13)
window.tag_bind('G', "<Button-1>", G.movement_one)
H = E_Button(274,428,14)
window.tag_bind('H', "<Button-1>", H.movement_one)
J = E_Button(319,428,15)
window.tag_bind('J', "<Button-1>", J.movement_one)
K = E_Button(364,428,16)
window.tag_bind('K', "<Button-1>", K.movement_one)
P = E_Button(21,486,17)
window.tag_bind('P', "<Button-1>", P.movement_one)
Y = E_Button(66,486,18)
window.tag_bind('Y', "<Button-1>", Y.movement_one)
X = E_Button(111,486,19)
window.tag_bind('X', "<Button-1>", X.movement_one)
C = E_Button(156,486,20)
window.tag_bind('C', "<Button-1>", C.movement_one)
V = E_Button(201,486,21)
window.tag_bind('V', "<Button-1>", V.movement_one)
B = E_Button(246,486,22)
window.tag_bind('B', "<Button-1>", B.movement_one)
N = E_Button(291,486,23)
window.tag_bind('N', "<Button-1>", N.movement_one)
M = E_Button(336,486,24)
window.tag_bind('M', "<Button-1>", M.movement_one)
L = E_Button(381,486,25)
window.tag_bind('L', "<Button-1>", L.movement_one)

##Lights
q = Light(33,178,0)
w = Light(78,178,1)
e = Light(123,178,2)
r = Light(168,178,3)
t = Light(213,178,4)
z = Light(258,178,5)
u = Light(303,178,6)
i = Light(348,178,7)
o = Light(393,178,8)
a = Light(49,236,9)
s = Light(94,236,10)
d = Light(139,236,11)
f = Light(184,236,12)
g = Light(229,236,13)
h = Light(274,236,14)
j = Light(319,236,15)
k = Light(364,236,16)
p = Light(21,288,17)
y = Light(66,288,18)
x = Light(111,288,19)
c = Light(156,288,20)
v = Light(201,288,21)
b = Light(246,288,22)
n = Light(291,288,23)
m = Light(336,288,24)
l = Light(381,288,25)

##Settings for the option window
##This allows the user to change rotor postions 
class Rotor_setting():
    def __init__ (self):       
        rotor_win = Toplevel()
        rotor_win.title("Rotors")
        rotor_win.resizable(FALSE, FALSE)
        rotor_info_one = Label(rotor_win, text="Left", width = 6)
        rotor_info_one.grid(row=0, column = 1)
        rotor_info_two = Label(rotor_win, text = "Center", width = 6)
        rotor_info_two.grid(row=0, column=2)
        rotor_info_three = Label (rotor_win, text = "Right", width = 6)
        rotor_info_three.grid(row=0, column=3)
        one_stop = Spinbox(rotor_win, values = ('I', 'II', 'III'),wrap=TRUE, width=5)
        one_stop.grid(row=1, column=1)
        two_stop = Spinbox(rotor_win, values = ('II', 'III', 'I'), wrap=TRUE, width=5)
        two_stop.grid(row=1, column=2)
        three_stop = Spinbox(rotor_win, values = ('III', 'II', 'I'), wrap=TRUE, width=5)
        three_stop.grid(row=1,column=3)        
        rotor_set = Button(rotor_win, text = "Set Rotors", command = lambda: self.change_setting(one_stop.get(), two_stop.get(),three_stop.get()), width = 10)
        rotor_set.grid(row=2, column=2)       
    def change_setting(self, once, twice, thrice):
        global spin3
        global spin2
        global spin1
        global rev_spin1
        global rev_spin2
        global rev_spin3
        
        if once == twice or twice == thrice or once == thrice:
            error_win = Toplevel()
            error_win.title("Error")
            error_name = Message(error_win, text = "Must not use the same rotor twice!").pack()
        else:
            ##Looks confusing, but this is where the rotors get moved around
            if once ==  'I':
                rotor_window_one.change_rotor(ring_I)
                spin1 = ref_spin1[:]
                rev_spin1 = ref_rev_spin1[:]
            elif once == 'II':
                rotor_window_one.change_rotor(ring_II)
                spin1 = ref_spin2[:]
                rev_spin1 = ref_rev_spin2[:]
            elif once == 'III':
                rotor_window_one.change_rotor(ring_III)
                spin1 = ref_spin3[:]
                rev_spin1 = ref_rev_spin3[:]
            if twice == 'I':
                rotor_window_two.change_rotor(ring_I)
                spin2 = ref_spin1[:]
                rev_spin2 = ref_rev_spin1[:]
            elif twice == 'II':
                rotor_window_two.change_rotor(ring_II)
                spin2 = ref_spin2[:]
                rev_spin2 = ref_rev_spin2[:]
            elif twice == 'III':
                rotor_window_two.change_rotor(ring_III)
                spin2 = ref_spin3[:]
                rev_spin2 = ref_rev_spin3[:]
            if thrice == 'I':
                rotor_window_three.change_rotor(ring_I)
                spin3 = ref_spin1[:]
                rev_spin3 = ref_rev_spin1[:]
            elif thrice == 'II':
                rotor_window_three.change_rotor(ring_II)
                spin3 = ref_spin2[:]
                rev_spin3 = ref_rev_spin2[:]
            elif thrice == 'III':
                rotor_window_three.change_rotor(ring_III)
                spin3 = ref_spin3[:]
                rev_spin3 = ref_rev_spin3[:]
            
                    
##This provides automated encoding and decoding of Enigma messages       
class En_decoder():
    def __init__(self):
        global en_code
        global de_code
        new_window = Toplevel()
        new_window.title("Encoder/Decoder")
        new_window.resizable(FALSE, FALSE)
        rotor_info_one = Label(new_window, text="Set your Rotor order and Rotor position before encoding or decoding", width = 60)
        rotor_info_one.grid(row=0, column=0, columnspan=15)
        scroll_1 = Scrollbar(new_window)
        scroll_1.grid(row=1, column=1, sticky=('n,s')) 
        en_code = Text(new_window, width = 30, yscrollcommand = scroll_1.set)
        en_code.grid(row=1, column=0)
        scroll_1.config(command= en_code.yview)
        scroll_2 = Scrollbar(new_window)
        scroll_2.grid(row=1, column=3, sticky=('n,s'))
        de_code = Text(new_window, width = 30, yscrollcommand = scroll_2.set)
        de_code.grid(row=1, column=2)
        scroll_2.config(command= de_code.yview)
        en_code_button = Button(new_window, width= 10, text = "Encode", command = lambda: self.code_getter(en_code.get(1.0, END),1))
        en_code_button.grid(row=2, column=0)
        de_code_button = Button(new_window, width = 10, text = "Decode", command = lambda: self.code_getter(de_code.get(1.0, END),2))
        de_code_button.grid(row=2, column=2)
    def code_getter(self,code,location):
        zig = []
        zag = []
        zig [:] = code[0:]
        x = 0
        for y in zig:
            if zig [x] in alph:
                 if rotor_window_three.number() == 25 or rotor_window_two.number() == 25:
                     if rotor_window_two.number() == 25:
                         rotor_window_one.move()
                     rotor_window_two.move()
                 rotor_window_three.move()
                 key = alph.index(zig[x])
                 key = mechanism(key, conv.index(rotor_window_one.place()), conv.index(rotor_window_two.place()), conv.index(rotor_window_three.place()),2)                  
                 zag.append(key[:])
            elif zig [x] in low_alph:
                 key = zig[x]
                 key = key.upper()                
                 if rotor_window_three.number() == 25 or rotor_window_two.number() == 25:
                     if rotor_window_two.number() == 25:
                         rotor_window_one.move()
                     rotor_window_two.move()
                 rotor_window_three.move()
                 key = alph.index(key)
                 key = mechanism(key, conv.index(rotor_window_one.place()), conv.index(rotor_window_two.place()), conv.index(rotor_window_three.place()),2)                 
                 zag.append(key[:])
            else:
                zag.append(zig[x])
            x += 1   
        code = "".join(zag)
        if location == 1:
            de_code.insert(INSERT,code)
        elif location == 2:
            en_code.insert(INSERT,code)
       
##Help window, provides information about enigma and available options
class Helper ():
    def __init__(self):
        wiendow = Toplevel()
        wiendow.title("About")
        wiendow.resizable(FALSE, FALSE)
        scroll = Scrollbar(wiendow)
        scroll.pack(side=RIGHT, fill=BOTH)
        information = Text(wiendow, width = 45, yscrollcommand=scroll.set)
        information.pack()
        scroll.configure(command=information.yview)
        info = """Dedicated to:
       Alan Mathison Turing,
    23 June 1912 - 7 July 1954,
who's work decyphering Naval Enigma,
    during World War Two, and 
 contributions to computer science 
have helped shape the modern world.

Using Enigma:
     Enigma messages were commonly encoded
     with the first three letters of the 
     message representing the the rotor 
     setting.
     The next six letters of the message 
     would be an encryption of the actual 
     rotor setting that would be used in 
     the message (typed twice), starting 
     at the setting given in the first three
     letters.
     Once this had been accomplished, the
     machine would be set to the rotor 
     setting that had been encrypted and the 
     rest of the message would be encrypted 
     with normal spacing and punctuation.

Rotor setting: 
     The rotor setting is located on the
     machine above the lights in the viewing
     windows and can be changed by using the
     up and down arrows.

Rotor position:
     Rotor position changes allow for a much
     larger number of possible letter 
     combinations, with just three rotors 
     there are only about 17,000 possible 
     combinations by changing rotor position 
     there are around 105,000.  
     To change the rotor position, use the 
     "Rotor Position" option and select a 
     new order for the
     three available rotors.

Encoder/Decoder:
     This can also be found in the options
     menu.
     This is meant to provide the user with
     a bit more convenience by allowing words
     to be typed in directly and encoded or 
     decoded automatically.
     Make sure to set your machine to the 
     desired Rotor setting and Rotor position
     before encrypting or decrypting.
            
Acknowledgements:
     This program was designed, written, and
     compiled in Python by James Woods on
     30 July 2011.  Thanks goes out to all
     the people who have contribute to the
     great Python resources on the web
     especially python.org, tkdocs.com,
     pythonware.com,effbot.org, and 
     infohost.nmt.edu.
     Other resources that were important to
     this project were:
     mckoss.com/Crypto/Enigma.htm (for 
     examples of the actual rotor wirings),
    startpad.googlecode.com/hg/labs/js/enigma
     /enigma-sim.html
    (for a working enigma emulator to compare
     results with),and the book that inspired
     this project"Alan Turing the Enigma"
     written by Andrew Hodges, published 
     by Simon and Shuster, Inc. New York, 
     copyright 1983.

     Source code is available upon request by
     contacting James Woods at
     woodsjt2003@yahoo.com.     """
        
        
        information.insert(INSERT, info)
        information.config(state = DISABLED)
        
            
##calls the rotor position window by creating an instance of the Rotor_setting class        
def rotor_settings():
    setting_window = Rotor_setting()

##calls the help window by creating an instance of the Helper class
def help_window():
    info_window = Helper()

##calls the Encoder/Decoder window by creating an instance of the En_decoder class
def deco_en():
    en_decoder = En_decoder()
    
menu = Menu(master)
options = Menu(menu, tearoff=0)
options.add_command(label="Rotor order", command = rotor_settings)
options.add_command(label="Encoder/\n" "Decoder", command = deco_en)
menu.add_cascade(label="Options", menu = options)
menu.add_command(label="About", command = help_window)

master.config(menu=menu)
master.resizable(FALSE,FALSE)
            
window.pack(expand=YES, fill=BOTH)

mainloop()

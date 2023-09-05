import os
import time

a = """
fv
fy
gk
gu
hu
hw
ih
ij
ik
il
iy
iz
jc
jw
jx
jz
kd
ke
kj
kz
lh
lj
lq
lt
ly
lz
nh
nj
nk
nw
ny
oj
oq
qf
qh
qj
ql
qo
qx
qy
"""
for i in a.split():
    print(f"--------------begin {i}--------------")
    os.system(f"pub.bat {i}")
    print(f"---------------end {i}---------------")
    time.sleep(60)

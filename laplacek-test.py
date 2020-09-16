from laplacek import *

#MD Test 1
AREF=dict(
    A_0 = 1.0667111388123607,
    A_1 = 0.14209682808589968,
    A_2 = -0.5683873123435988,
    A_3 = -0.1654062581863318,
    A_4 = 1.1367746246871977,
    A_5 = 0.5981000731281605,
    A_6 = -2.2112433918103886,
    A_7 = 0.36295417297095134,
    A_8 = 0.3308125163726638,
    A_9 = -0.6616250327453276,
    A_10 = 0.3308125163726638
)

#MD test 1
alfa=0.480597
A0=Dop([1],0,1/2,alfa)/2-AREF["A_0"]
print(f"A_0 = {A0}")
A1=1/8*Dop([0,2*alfa,alfa**2],0,1/2,alfa)-AREF["A_1"]
print(f"A_1 = {A1}")
A2=-alfa/2*Dop([1],1,3/2,alfa)-AREF["A_2"]
print(f"A_2 = {A2}")
A3=1/4*Dop([2,-2*alfa,-alfa**2],1,1/2,alfa)-AREF["A_3"]
print(f"A_3 = {A3}")
A4=alfa*Dop([1],1,3/2,alfa)-AREF["A_4"]
print(f"A_4 = {A4}")
A5=1/8*Dop([21,10*alfa,alfa**2],3,1/2,alfa)-AREF["A_5"]
print(f"A_5 = {A5}")
A6=1/4*Dop([-20,-10*alfa,-alfa**2],2,1/2,alfa)-AREF["A_6"]
print(f"A_6 = {A6}")
A7=1/8*Dop([17,10*alfa,alfa**2],1,1/2,alfa)-27*alfa/8-AREF["A_7"]
print(f"A_7 = {A7}")
A8=alfa/2*Dop([1],2,3/2,alfa)-AREF["A_8"]
print(f"A_8 = {A8}")
A9=-alfa*Dop([1],2,3/2,alfa)-AREF["A_9"]
print(f"A_9 = {A9}")
A10=alfa/2*Dop([1],2,3/2,alfa)-AREF["A_10"]
print(f"A_10 = {A10}")

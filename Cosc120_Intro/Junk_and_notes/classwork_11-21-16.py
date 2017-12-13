import Listops as lops, numpy, time
N = int(raw_input('How many elements in list and array?'))

t_o = time.time()
L1 = []
L2 = []
for i in range(N):
    L1.append(i)
    L2.append(i)
Lsum = lops.Lsum(lops.Lpow(L1,2),lops.Lpow(L2,3))
print Lsum
t_1 = time.time()
T_list = t_1 - t_o
print T_list

t_o = time.time()
N1 = numpy.zeros(N)
N2 = numpy.zeros(N)
for i in range(N):
    N1[i] = i
    N2[i] = i
# for i in range(N):
#     N1[i] = i**2
#     N2[i] = i**3
Nsum = lops.Lsum(lops.Lpow(N1,2),lops.Lpow(N2,3))
print Nsum
 #print N1 + N2
t_1 = time.time()
T_array = t_1 - t_o
print T_array

print type(N2)
# time operator

#### EEEEEEHhhhhhhhh i guess numpy arrays are faster

######################################################################################################################
#imgr = img
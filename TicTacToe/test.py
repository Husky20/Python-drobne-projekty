import EasyThread
# region EasyThread
def potenga(args):
    a = args[0]
    n = args[1]
    ret = a
    for i in range(n):
        ret *= a
    return ret
print(potenga((2, 8)))

tasks =[]
for it in range(20):
    tasks.append((it, 3))

print(EasyThread.EasyThread(tasks, potenga))

#endregion
import tracemalloc
class Point_slot:
    __slot__=["x","y"]
    def __init__(self,x,y):
        self.x=x
        self.y=y
tracemalloc.start()
for i in range (1000000):
    points_with_slot=[Point_slot(i,i)]
current,peak=tracemalloc.get_traced_memory()
tracemalloc.stop()
print(peak/(2**20))

class Point_without_slot:
    def __init__(self,x,y):
        self.x=x
        self.y=y
tracemalloc.start()
for i in range(1000000):
    points_without_slot=[Point_without_slot(i,i)]
current,peak=tracemalloc.get_traced_memory()
tracemalloc.stop()
print(peak/2**20)
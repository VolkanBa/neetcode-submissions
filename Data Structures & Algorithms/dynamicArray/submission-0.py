class DynamicArray:
    
    #Capacity muss >0 sein. Capacity ist die größe des Arrays
    def __init__(self, capacity: int):
        if capacity > 0:
            self.arr = []
            self.capacity = capacity
        else:
            print ("capacity is smaller than 0")
    #Holt das Element an Stelle i (keine prüfung ob i existiert)
    def get(self, i: int) -> int:
        return self.arr[i]
    #setzt Element an Stelle i auf Wert n
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
    #Packt n an das Ende vom Array, wenn Array voll, zuerst resize ausführen 
    def pushback(self, n: int) -> None:
        if len(self.arr) >= self.capacity:
            self.resize()
        self.arr.append(n)
    #gibt den letzten Wert des Arrays wieder und löscht diesen Wert
    def popback(self) -> int:
        return self.arr.pop()
    #Verdoppelt die größe des Arrays
    def resize(self) -> None:
        self.capacity *=2
    #Gibt Anzahl der Elemente im Array wieder
    def getSize(self) -> int:
        return len(self.arr)
    #gibt anzahl des Arrays wieder
    def getCapacity(self) -> int:
        return self.capacity
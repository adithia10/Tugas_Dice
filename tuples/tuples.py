class hari:
    def __init__(self):
        self.__hari=['senin','selasa','rabu']
    def printh1(self):
        return(self.__hari)
    def carihari(self,angka):
        return(self.__hari[angka-1])
    def gantih(self,index,harinya):
        self.__hari[1]=harinya
    def tipe(self):
        return(type(self.__hari))

harihari=hari()
print(harihari.carihari(2))
print(harihari.tipe())
print(harihari.printh1())
harihari.gantih(1,'jumat')
print(harihari.printh1())

bulan=('januari',)
print(type(bulan))
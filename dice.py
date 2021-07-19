import random

randomlist = []
mengulang = True


while mengulang:
    print("Rolling dice. . . . ")
    number=random.randint(1,6)
    randomlist.append(number)
        
    def getStatistik(arrays):
        arr1, arr2, arr3, arr4, arr5, arr6 = [], [], [], [], [], []
        for x in arrays:
            if x == 1:
                arr1.append(x)
            if x == 2:
                arr2.append(x)
            if x == 3:
                arr3.append(x)
            if x == 4:
                arr4.append(x)
            if x == 5:
                arr5.append(x)
            if x == 6:
                arr6.append(x)
        print('Angka "1" ada ' + str(len(arr1)) + '\nAngka "2" ada ' + str(len(arr2)) + '\nAngka "3" ada ' + str(len(arr3)) + '\nAngka "4" ada ' + str(len(arr4)) + '\nAngka "5" ada ' + str(len(arr5)) + '\nAngka "6" ada ' + str(len(arr6)))
    print(f"Your Number:{number}")
    inputUser = input('Apakah mau mengacak lagi? [y/n] : ')
    mengulang = ('y' or 'Y') in inputUser
    if inputUser == 'n' or inputUser == 'N':
        print('##########################')
        print('Dengan Total Lemparan : ' + str(len(randomlist)))
        print(randomlist)
        getStatistik(randomlist)
        break
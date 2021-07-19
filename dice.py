import random

listresult = []
mengulang = True


while mengulang:
    print("Rolling dice. . . . ")
    dice=random.randint(1,6)
    listresult.append(dice)
        
    def Statistik(arrays):
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
        print('Angka "1" muncul sebanyak ' + str(len(arr1)) + ' kali' + '\nAngka "2" muncul sebanyak ' + str(len(arr2)) + ' kali' + '\nAngka "3" muncul sebanyak ' + str(len(arr3)) + ' kali' + '\nAngka "4" muncul sebanyak ' + str(len(arr4)) + ' kali' + '\nAngka "5" muncul sebanyak ' + str(len(arr5)) + ' kali' + '\nAngka "6" muncul sebanyak ' + str(len(arr6)) + ' kali')

    print(f"Your dice:{dice}")
    inputUser = input('Apakah mau mengacak lagi? [y/n] : ')
    mengulang = ('y' or 'Y') in inputUser
    if inputUser == 'n' or inputUser == 'N':
        print('##########################')
        print('Dengan Total Lemparan : ' + str(len(listresult)))
        print(listresult)
        Statistik(listresult)
        break

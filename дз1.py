import time


class Contact:                                         # создали класс 'Contact'
    def __init__(self, name, phone, email):
        self.name, self.phone, self.email = name, phone, email


class Contacts:
    def __init__(self):
        self.baza = [[], [], [], [], [], []]            # айди + имя + фамилия + отчество + номер тел + эл почта

    def __add__(self, contact):                          # вносим данные в матрицу
        self.baza[0].append(len(self.baza[0])+1)
        fio = contact.name.split(' ')
        while len(fio) != 3:
            fio.append(None)
        self.baza[1].append(fio[0])
        self.baza[2].append(fio[1])
        self.baza[3].append(fio[2])
        if contact.phone != '':
            self.baza[4].append(contact.phone)
        else:
            self.baza[4].append(None)
        if contact.email != '':
            self.baza[5].append(contact.email)
        else:
            self.baza[5].append(None)

    def givecon(self, id):                             # ф-ция для выдачи данных контакта
        ans = "ID - " + str(self.baza[0][id]) + "\n"
        if self.baza[1][id] != None:
            ans += "ФИО: " + self.baza[1][id]
        if self.baza[2][id] != None:
            ans += " " + self.baza[2][id]
        if self.baza[3][id] != None:
            ans += " " + self.baza[3][id]
        if self.baza[4][id] != None:
            ans += "\n" + "Номер телефона: " + self.baza[4][id]
        else:
            ans += "\n" + "Номер телефона: " + "None"
        if self.baza[5][id] != None:
            ans += "\n" + "Почта: " + self.baza[5][id] + "\n"
        else:
            ans += "\n" + "Почта: " + "None" + "\n"
        return ans

    def FindPhone(self, phone):                            # поиск по телефону
            if self.baza[4].__contains__(phone):
                id = self.baza[4].index(phone)
                print(self.givecon(id))
            else:
                print("Ничего не нашлось...")


    def FindMail(self, mail):                              # поиск по почте
        if self.baza[5].__contains__(mail):
            id = self.baza[5].index(mail)
            print(self.givecon(id))
        else:
            print("Ничего не нашлось...")

    def Find(self, fio):                                   # поиск по фио
        ido = []
        if fio[0] != None:
            for i in range(len(self.baza[1])):
                if fio[0] == self.baza[1][i]:
                    ido.append(self.baza[0][i] - 1)
        if fio[1] != None:
            if fio[0] != None:
                for id in ido:
                    if fio[1] != self.baza[2][id]:
                        ido.remove(id)
            else:
                for i in range(len(self.baza[2])):
                    if fio[1] == self.baza[2][i]:
                        ido.append(self.baza[0][i] - 1)

        if fio[2] != None:
            if fio[0] != None or fio[1] != None:
                for id in ido:
                    if fio[2] != self.baza[2][id]:
                        ido.remove(id)
            else:
                for i in range(len(self.baza[3])):
                    if fio[2] == self.baza[3][i]:
                        ido.append(self.baza[0][i] - 1)

        if len(ido) == 0:
            print("Ничего не нашлось...")
        else:
            for id in ido:
                print(self.givecon(id))


    def FindWithNoPhone_Mail(self, n):                   # поиск по параметрам: 1 no phone, 2 no mail, 3 both
        if n == 1:
            for i in range(len(self.baza[4])):
                if self.baza[4][i] == None:
                    print(self.givecon(i))
            return
        if n == 2:
            for i in range(len(self.baza[5])):
                if self.baza[5][i] == None:
                    print(self.givecon(i))
            return
        if n == 3:
            for i in range(len(self.baza[4])):
                if self.baza[4][i] == None and self.baza[5][i] == None:
                    print(self.givecon(i))
            return

    def printVse(self):                               # выводим все данные
        for i in range(len(self.baza[0])):
            print(self.givecon(i))

def giveComms():                                      # команды
    print("в вашем распоряжении: ")
    print("|1 - вывод всех контактов|", "|2 - найти по телефону|", "|3 - найти по почте|", "|4 - найти по ФИО|",
          "|5 - найти по отсутствию номера/почты|", "|6 - завершить программу|")


print("пожалуйста, введите имя файла: ")
ImyaFile = input()
file = open(ImyaFile, encoding='utf-8')
base = Contacts()
for stroka in file:
    wasd = stroka.split(",")
    contact = Contact(wasd[0], wasd[1].replace(" ", ""), wasd[2].replace(" ", "").replace("\n", ""))
    base.__add__(contact)
print("база контактов создана ^-^")
giveComms()
zxc = int(input())
while zxc!="heheeebooooooyyyyyy&^*^":
    if zxc==1:
        base.printVse()
    elif zxc==2:
        print("Введите телефон:")
        phone = input()
        base.FindPhone(phone)
    elif zxc == 3:
        print("Введите почту:")
        mail = input()
        base.FindMail(mail)
    elif zxc == 4:
        fio = []
        print("Введите фамилию, либо оставьте пустую строку:")
        f = input()
        if f=='':
            fio.append(None)
        else:
            fio.append(f)
        print("Введите имя, либо оставьте пустую строку:")
        i = input()
        if i == '':
            fio.append(None)
        else:
            fio.append(i)
        print("Введите отчество, либо оставьте пустую строку:")
        o = input()
        if o == '':
            fio.append(None)
        else:
            fio.append(o)
        base.Find(fio)
    elif zxc == 5:
        print("Введите по чему хотите искать: ", "1 - без номера", "2 - без почты", "3 - без обоих", sep="\n")
        num = int(input())
        base.FindWithNoPhone_Mail(num)
    elif zxc == 6:
        print('Вы уверены? (да/нет):')
        check = str(input())
        if check == 'да':
            for k in range(1,4):
                print('завершение программы через:', k)
                time.sleep(1)
            print()
            print("программа приостановлена ;(")
            break
        else:
            print('ура! продолжаем;)')
    print()
    giveComms()
    zxc = int(input())

'''
не придумал, как сделать пункт: 'Реализована возможность редактирования любого контакта' :(
'''
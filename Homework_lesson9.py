def menu():
    print("Нажмите 1, что бы вывести телефонный справочник")
    print("нажмите 2, что бы ввести данные в справлчник")
    print("нажмите 3, что бы найти данные по характеристике")
    print("Нажмите 4, что бы перенести строку справочника в другой файл")
    print("Нажмите 5, что бы заменить данные в справочнике")
    print("нажмите 0, что бы выйти из программы")
    return input()

def find_str():
    str_ = dict()
    count = 1
    data = open('file.txt','r')
    for line in data:
        str_[count] = line.split()
        count += 1
    data.close()
    return str_

def read_inf(is_copy = False):
    data = open('file.txt','r')
    count = 1
    for line in data:
        if is_copy:
            print(f"{count} {line}")
            count += 1
        else: print(line)
    data.close()

def write_inf():
    print("Введите фамилию, имя, отчество и номер телефона через пробел без разделительных знаков")
    data = open('file.txt','a')
    data.write(f"{input()}\n")
    data.close()

def find(word):
    to_find = False
    data = open('file.txt','r')
    for line in data:
        line_ = line.split()
        for i in range(len(line_)):
            if word == line_[i]:
                print(line)
                to_find = True
    data.close()
    
    if not to_find:
        print("По введённый данным ничего не удалось найти")

def copy():
    str_ = find_str()
    
    print("Нужно ли вам показать сам список? Если да, то нажмите 1, иначе enter ")
    
    if input() == "1":
        read_inf(True)
        
    print("")
    print("Какую строку нужно перенести в новый файл? ")
    
    data_2 = open("new_file.txt","a")
    data_2.write(f"{" ".join(str_[int(input())])}\n")
    data_2.close
        
def rename():
    str_ = find_str()
    print("Нужно ли вам показать сам список? Если да, то нажмите 1, иначе enter ")
    
    if input() == "1":
        read_inf(True)
        
    print("В какой строке вы бы хотели изменить данные? ")
    num = int(input())
    print("Какие данные вы хотели бы изменить: фамилию, имя, отчество или номер телефона?")
    match input():
        case "фамилию":
            num_word = 0
        case "имя":
            num_word = 1
        case "отчество":
            num_word = 2
        case "номер телефона":
            num_word = 3  
    
    str_[num][num_word] = input("Введите новое значение: ")
    
    data = open("file.txt","w")
    for i in range(1,len(str_) + 1):
        data.write(f"{" ".join(str_[i])}\n")
    
def main():
    while True:
        match menu():
            case "1":
                print("")
                read_inf()
                print("")
            case "2":
                print("")
                write_inf()
                print("")
            case "3":
                print("")
                print("Введите слово для поиска: ")
                print("")
                find(input())
                print("")
            case "4":
                print("")
                copy()
                print("")
            case "5":
                print("")
                rename()
                print("")
            case "0":
                break

if __name__ == "__main__":
    main()
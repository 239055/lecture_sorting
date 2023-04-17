import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, 'r') as f:
        prochaz = csv.DictReader(f)
        data = {}
        for radek in prochaz:
            for hlavicka, hodnota in radek.items():
                if hlavicka not in data:
                    data[hlavicka] = [int(hodnota)]
                else:
                    data[hlavicka].append(int(hodnota))
        return data


def selection_sort(seznam_cisel, direction="vzestupne"):
    """

    :param seznam_cisel:
    :return:
    """
    n = len(seznam_cisel)


    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if seznam_cisel[j] < seznam_cisel[min_idx]:
                min_idx = j
        seznam_cisel[i], seznam_cisel[min_idx] = seznam_cisel[min_idx], seznam_cisel[i]

    if direction == "vzestupne":
        return seznam_cisel

    elif direction == "sestupne":
        sestupny = []
        pocet_apl = 0

        idx = -1
        for x in range(n):
            sestupny.append(seznam_cisel[idx])
            idx -= 1

        return sestupny

    else:
        return "Error"


def bubble_sort(seznam):
    """

    :param seznam:
    :return:
    """
    delka = len(seznam)

    for x in range(delka):
        for y in range(0, delka-x-1):
            if seznam[y] > seznam[y+1]:
                seznam[y], seznam[y+1] = seznam[y+1], seznam[y]
    return seznam


def insertion_sort(seznam):
    """

    :param seznam:
    :return:
    """
    delka = len(seznam)
    for k in range(1, delka):
        klic_pozice = seznam[k]
        z = k - 1
        while z >= 0 and seznam[z] > klic_pozice:
            seznam[z+1] = seznam[z]
            z -= 1
        seznam[z+1] = klic_pozice
    return seznam



def main():
    # data = read_data('numbers.csv')
    # print(data["series_3"])
    seznam = [1058, 998, 1235, 1147, 3365, 7741, 1011, 6555, 666, 6666, 7777]
    serazeni_vz = selection_sort(seznam)
    serazeni_ses = selection_sort(seznam, "sestupne")
    # print(serazeni_vz)
    # print(serazeni_ses)
    buble = bubble_sort(seznam)
    print(buble)
    insert = insertion_sort(seznam)
    print(insert)

if __name__ == '__main__':
    main()


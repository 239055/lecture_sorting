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


def selection_sort(seznam_cisel):
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
    return seznam_cisel


def main():
    data = read_data('numbers.csv')
    print(data["series_3"])
    seznam = [1058, 998, 1235, 1147, 3365, 7741, 1011, 6555, 666, 6666, 7777]
    serazeni = selection_sort(seznam)
    print(serazeni)

if __name__ == '__main__':
    main()


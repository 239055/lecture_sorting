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


def main():
    data = read_data('numbers.csv')
    print(data["series_3"])


if __name__ == '__main__':
    main()


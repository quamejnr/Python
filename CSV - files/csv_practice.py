import csv

with open('names.csv', 'r') as csv_file:
    # csv.DictReader outputs the file in dictionary mode which helps in using the keys to output values
    csv_dict_reader = csv.DictReader(csv_file)

    # csv.reader just outputs the file in the same format as it is
    csv_reader = csv.reader(csv_file)


    with open('new_file.csv', 'w') as new_file:
        # when using csv.DictReader, fieldnames are to be provided before writing them off
        fieldnames = ['first_name', 'last_name', 'email']

        # csv.DictWriter is used when writing in Dictionary mode with fieldnames passed as argument
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        # The writeheader() method allows csv.DictWriter to write the heading of the csv file or it will be omitted
        csv_writer.writeheader()

        for line in csv_dict_reader:
            csv_writer.writerow(line)




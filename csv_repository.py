import csv

class CSVRepository:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def get_sales_data(self):
        sales_data = []
        with open(self.file_name, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                sales_data.append(row)
        return sales_data

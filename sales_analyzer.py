from collections import defaultdict
from datetime import datetime

class SalesAnalyzer:
    def __init__(self, sales_data):
        self.sales_data = sales_data

    def analyze_monthly_sales(self):
        monthly_sales = defaultdict(lambda: defaultdict(float))
        for sale in self.sales_data:
            branch = sale['branch_id']
            date = sale['date'][:7]  # Extract year and month
            amount = float(sale['total_amount'])
            monthly_sales[branch][date] += amount
        return monthly_sales

    def analyze_price_per_product(self):
        product_price_analysis = defaultdict(float)
        for sale in self.sales_data:
            product = sale['product_name']
            amount = float(sale['total_amount'])
            quantity = int(sale['quantity'])
            product_price_analysis[product] += amount / quantity  # Average price per product
        return product_price_analysis

    def analyze_weekly_sales(self):
        weekly_sales = defaultdict(lambda: defaultdict(float))
        for sale in self.sales_data:
            branch = sale['branch_id']
            week = self.get_week_from_date(sale['date'])
            amount = float(sale['total_amount'])
            weekly_sales[branch][week] += amount
        return weekly_sales

    def analyze_product_preference(self):
        product_preference = defaultdict(int)
        for sale in self.sales_data:
            product = sale['product_name']
            quantity = int(sale['quantity'])
            product_preference[product] += quantity
        return product_preference

    def get_week_from_date(self, date_str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%Y-W%U')  # Format year and week number

    def analyze_total_sales_distribution(self):
        total_sales = 0
        branch_sales = defaultdict(float)
        for sale in self.sales_data:
            branch = sale['branch_id']
            amount = float(sale['total_amount'])
            branch_sales[branch] += amount
            total_sales += amount
        return total_sales, branch_sales

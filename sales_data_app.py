import sys

class SalesDataApp:
    def __init__(self, sales_analyzer):
        self.sales_analyzer = sales_analyzer

    def display_main_menu(self):
        print("\nWelcome to Sampath Food City Sales Data Analysis System")
        print("Please choose an option:")
        print("1. Monthly Sales Analysis")
        print("2. Price Analysis of Each Product")
        print("3. Weekly Sales Analysis")
        print("4. Product Preference Analysis")
        print("5. Total Sales Distribution Analysis")
        print("0. Exit")

    def run(self):
        while True:
            self.display_main_menu()
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.show_monthly_sales()
            elif choice == "2":
                self.show_price_per_product()
            elif choice == "3":
                self.show_weekly_sales()
            elif choice == "4":
                self.show_product_preference()
            elif choice == "5":
                self.show_total_sales_distribution()
            elif choice == "0":
                print("Exiting... Goodbye!")
                sys.exit()
            else:
                print("Invalid choice, please try again.")

    def show_monthly_sales(self):
        monthly_sales = self.sales_analyzer.analyze_monthly_sales()
        print("\nMonthly Sales Analysis:")
        for branch, sales in monthly_sales.items():
            print(f"Branch {branch}:")
            for month, amount in sales.items():
                print(f"  {month}: Rs. {amount:.2f}")

    def show_price_per_product(self):
        price_analysis = self.sales_analyzer.analyze_price_per_product()
        print("\nPrice Analysis of Each Product:")
        for product, price in price_analysis.items():
            print(f"{product}: Rs. {price:.2f}")

    def show_weekly_sales(self):
        weekly_sales = self.sales_analyzer.analyze_weekly_sales()
        print("\nWeekly Sales Analysis:")
        for branch, sales in weekly_sales.items():
            print(f"Branch {branch}:")
            for week, amount in sales.items():
                print(f"  {week}: Rs. {amount:.2f}")

    def show_product_preference(self):
        product_preference = self.sales_analyzer.analyze_product_preference()
        print("\nProduct Preference Analysis:")
        for product, count in product_preference.items():
            print(f"{product}: {count} units sold")

    def show_total_sales_distribution(self):
        total_sales, branch_sales = self.sales_analyzer.analyze_total_sales_distribution()
        print("\nTotal Sales Distribution Analysis:")
        print(f"Total Sales: Rs. {total_sales:.2f}")
        for branch, amount in branch_sales.items():
            print(f"Branch {branch}: Rs. {amount:.2f}")

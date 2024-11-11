from csv_repository import CSVRepository
from sales_analyzer import SalesAnalyzer
from sales_data_app import SalesDataApp

if __name__ == "__main__":
    csv_file = "sales_data.csv"
    
    repository = CSVRepository(csv_file)
    sales_data = repository.get_sales_data()
    
    sales_analyzer = SalesAnalyzer(sales_data)
    
    # Start the application
    app = SalesDataApp(sales_analyzer)
    app.run()

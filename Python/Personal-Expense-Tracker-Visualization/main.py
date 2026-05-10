from src.data_generator import generate_expense_data
from src.database import create_database
from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.analysis import run_analysis
from src.visualization import create_visualizations
from src.report_generator import generate_report

generate_expense_data()
create_database()

df = load_data()
df = clean_data(df)

run_analysis(df)
create_visualizations(df)
generate_report(df)

print("Project Executed Successfully")
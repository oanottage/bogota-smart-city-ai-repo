import pandas as pd
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from pathlib import Path 
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()  # Loads from .env by default

## Define base path (adjust if notebook is in different location)
BASE_PATH = os.getenv('BASE_PATH')

# Verify base path exists
if not BASE_PATH or not os.path.exists(BASE_PATH):
    raise ValueError(f"Invalid BASE_PATH: {BASE_PATH}. Check your .env file and directory structure")


### Data Dictionary Generation Functions
def create_data_dictionary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a data dictionary from a DataFrame.

    Adds:
      - distinct_count
      - python_type
      - min
      - max
    without removing existing fields:
      - column_name
      - sample_value
      - non_null_count
      - percent_populated
    """
    data_dict = {
        'column_name': [],
        'sample_value': [],
        'non_null_count': [],
        'percent_populated': [],
        'distinct_count': [],
        'python_type': [],
        'min': [],
        'max': []
    }

    total_rows = len(df)

    for col in df.columns:
        col_series = df[col]
        non_null_series = col_series.dropna()

        # Sample value from first non-null entry
        sample_val = non_null_series.iloc[0] if len(non_null_series) > 0 else None

        # Count/percentage of non-null
        non_null_count = col_series.count()
        percent_populated = round((non_null_count / total_rows) * 100, 2)

        # Distinct count
        distinct_count = col_series.nunique(dropna=True)

        # Python type
        python_type = str(col_series.dtype)

        # Min/Max (only if numeric)
        col_min = None
        col_max = None
        if pd.api.types.is_numeric_dtype(col_series):
            col_min = col_series.min()
            col_max = col_series.max()

        data_dict['column_name'].append(col)
        data_dict['sample_value'].append(sample_val)
        data_dict['non_null_count'].append(non_null_count)
        data_dict['percent_populated'].append(percent_populated)
        data_dict['distinct_count'].append(distinct_count)
        data_dict['python_type'].append(python_type)
        data_dict['min'].append(col_min)
        data_dict['max'].append(col_max)

    data_dict_df = pd.DataFrame(data_dict)
    return data_dict_df


### Report Generation Functions
def generate_pdf_report(data_dict_df: pd.DataFrame, data_name: str, output_folder: str = os.path.join(BASE_PATH,'reports/EDA_Reports')):
    """
    Generate a PDF report from the data dictionary DataFrame.
    
    Parameters
    ----------
    data_dict_df : pd.DataFrame
        DataFrame containing the data dictionary info.
    data_name : str
        Name of the dataset (used in the PDF title).
    output_folder : str
        Folder path where the PDF will be saved.
    
    Returns
    -------
    None
        Creates a PDF file named f"{data_name}_data_dictionary.pdf" in the specified output folder.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    pdf_filename = os.path.join(output_folder, f"{data_name}_data_dictionary.pdf")
    
    #save the dictionary to an excel file
    data_dict_df.to_excel(os.path.join(output_folder, f"{data_name}_data_dictionary.xlsx"), index=False)

    #create an empty .md file for the data glossary
    with open(os.path.join(output_folder, f"{data_name}_data_glossary.md"), 'w') as f:
        f.write(f"# {data_name} – Data Glossary")

    # Create a PDF document
    doc = SimpleDocTemplate(pdf_filename, pagesize=LETTER)

    # A style sheet for paragraphs
    styles = getSampleStyleSheet()
    style_normal = styles["Normal"]
    style_title = styles["Title"]

    # Title paragraph
    title_paragraph = Paragraph(f"{data_name} – Data Dictionary", style=style_title)

    # Convert data_dict_df into a list of lists for the Table
    # Table header: keep your original 4 columns and add new ones
    table_data = [
        [
            "Column Name", 
            "Sample Value", 
            "Non-null Count", 
            "Percent Populated",
            "Distinct Count",
            "Python Type",
            "Min",
            "Max"
        ]
    ]

    # Table rows
    for _, row in data_dict_df.iterrows():
        table_data.append([
            str(row["column_name"]),
            str(row["sample_value"]),
            str(row["non_null_count"]),
            f"{row['percent_populated']}%",
            str(row["distinct_count"]),
            str(row["python_type"]),
            str(row["min"]),
            str(row["max"])
        ])

    # Create the table
    table = Table(table_data, repeatRows=1)

    # Style the table
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 6),
    ])
    table.setStyle(table_style)

    # Build the PDF elements
    elements = [title_paragraph, Spacer(1, 12), table]

    # Generate the PDF
    doc.build(elements)

    print(f"PDF report generated: {pdf_filename}")


### Main Function
def generate_all_data_dictionaries(
    bronze_folder: str = os.path.join(BASE_PATH,'data/1_Bronze'), 
    report_folder: str = os.path.join(BASE_PATH,'reports/EDA_Reports'),
    file_extension: str = '.parquet'
):
    """
    Reads all files with the specified extension in the `bronze_folder`,
    generates a data dictionary for each, and saves a PDF in the `report_folder`.
    
    Parameters
    ----------
    bronze_folder : str, optional
        Path to the folder containing the input files (default is 'data/1_Bronze').
    report_folder : str, optional
        Path to the folder where PDF reports will be saved (default is 'docs/EDA_Reports').
    file_extension : str, optional
        File extension to search for (default is '.csv').
    
    Returns
    -------
    None
        Generates one PDF report per file in the specified folder.
    """
    # Convert to a Path object for easier manipulation
    bronze_path = Path(bronze_folder)
    if not bronze_path.exists():
        print(f"Folder '{bronze_folder}' does not exist.")
        return
    
    # Gather all files that match the extension
    files = list(bronze_path.glob(f"*{file_extension}"))
    if not files:
        print(f"No files with extension '{file_extension}' found in {bronze_folder}.")
        return
    
    print(f"Found {len(files)} file(s) in '{bronze_folder}' with extension '{file_extension}':")
    
    for file_path in files:
        print(f"Processing file: {file_path.name}")
        data_name = file_path.stem  # file name without extension
        
        # 1. Read the file into a DataFrame
        df = pd.read_parquet(file_path)
        
        # 2. Create the data dictionary
        data_dict_df = create_data_dictionary(df)
        
        # 3. Generate the PDF report
        generate_pdf_report(data_dict_df, data_name=data_name, output_folder=report_folder)

    print("All data dictionary PDFs have been generated.")


if __name__ == '__main__':
    generate_all_data_dictionaries()

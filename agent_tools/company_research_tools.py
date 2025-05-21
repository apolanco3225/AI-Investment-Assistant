# import necessary libraries
import yfinance as yf
from tavily import TavilyClient

# set credentials for sec api
from edgar import Company, set_identity 
set_identity("vito.corleone@gmail.com") 


from langsmith import traceable



#########################
# Company Research Tools #
#########################
    

@traceable(run_type="tool")
def search_financial_news(company_name: str, num_results: int = 3) -> str:
    """
    Search for the latest financial news 
    about a company.
    """
    client = TavilyClient()
    search_query = f"latest financial news {company_name} stock market"
    
    results = client.search(
        query=search_query,
        search_depth="advanced",
        include_domains=["finance.yahoo.com", "reuters.com", "bloomberg.com"],
        max_results=num_results
    )
    
    return "\n".join([f"- {result['title']}: {result['content'][:200]}..." 
                     for result in results['results']])


@traceable(run_type="tool")
def get_basic_info(ticker):
    """
    Get basic information about a stock using yfinance.
    Args:
        ticker (str): The stock ticker symbol.
    Returns:
        dict: A dictionary containing basic information about the stock.
    """
    stock = yf.Ticker(ticker)
    basic_keys = [
        'longName',
        'symbol',
        'companyOfficers',
        'market',
        'address1', 
        'city', 
        'state', 
        'zip', 
        'country', 
        'phone', 
        'website', 
        'industry', 
        'sector', 
        'longBusinessSummary', 
        'fullTimeEmployees'
    ]
    basic_info = {
        basic_key:stock.info[basic_key] for basic_key in basic_keys
    }

    basic_info['companyOfficers'] = basic_info['companyOfficers'][0]
    return basic_info 

@traceable(run_type="tool")
def get_balance_sheet(ticker):
    """
    Get the balance sheet of a stock using yfinance.
    Args:
        ticker (str): The stock ticker symbol.
    Returns:
        DataFrame: A DataFrame containing the balance sheet of the stock.
    """
    stock = yf.Ticker(ticker)
    date = stock.balance_sheet.columns[0]
    balance_sheet = stock.balance_sheet.iloc[:, 0]
    return date, balance_sheet

@traceable(run_type="tool")
def get_quarterly_report(ticker):
    """
    Get the quarterly report of a stock using the EDGAR database.
    Args:
        ticker (str): The stock ticker symbol.
    Returns:
        str: The quarterly report of the stock.
    """
    company = Company(ticker)
    last_filing = company.get_filings(form="10-Q").latest().obj()
    doc_items = last_filing.items
    quarterly_report_list = [last_filing[item] for item in doc_items]
    quarterly_report_string = " \n ".join(quarterly_report_list)
    return quarterly_report_string 
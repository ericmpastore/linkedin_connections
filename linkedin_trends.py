import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def render_plot(csv_file='Connections.csv'):
    """
    Docstring for render_plot

    Render plot reads data from csv file, parses, and shows plot
    
    :param csv_file: Parameter identifies file to read source data
    """
    
    connections_count = pd.read_csv(csv_file,encoding='cp1252')

    connections_count['Connected On'] = pd.to_datetime(connections_count['Connected On'])
    cutoff_date = datetime.now() - timedelta(days=365)
    connections_count = connections_count[connections_count['Connected On'] >= cutoff_date]

    connections_count['connection_count']=1

    final_frame = connections_count.groupby(pd.Grouper(key='Connected On', freq='MS'))['connection_count'].sum()

    final_frame.plot(kind='line')
    plt.xlabel('Month')
    plt.ylabel('Connection Count')
    plt.title('LinkedIn Connections per Month (Last 365 Days)')
    plt.show()

    

def main():
    render_plot()

if __name__ == "__main__":
    main()
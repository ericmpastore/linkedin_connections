import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def render_plot(csv_file='Connections.csv'):
    """
    Docstring for render_plot

    EPastore 01/23/26, Render plot reads data from csv file, parses, and shows plot

    EPastore 01/24/26, Removed axis labels, labeled data points, added comments
    
    :param csv_file: Parameter identifies file to read source data
    """
    # read csv parameter into dataframe, encoded as Windows 1252 due to error reading original csv, EPastore 01/24/26
    connections_count = pd.read_csv(csv_file,encoding='cp1252')

    # convert Connected On field to datetime, filter to last year, EPastore 01/24/26
    connections_count['Connected On'] = pd.to_datetime(connections_count['Connected On'],format='%d-%b-%y')
    cutoff_date = datetime.now() - timedelta(days=365)
    connections_count = connections_count[connections_count['Connected On'] >= cutoff_date]

    # create connection_count field to get sum of connections per date, EPastore 01/24/26
    connections_count['connection_count']=1

    # group sum by Connected On date, EPastore 01/24/26
    final_frame = connections_count.groupby(pd.Grouper(key='Connected On', freq='MS'))['connection_count'].sum()

    # plot line chart, EPastore 01/24/26
    final_frame.plot(kind='line', color='gray', linewidth=2,marker='o')
    for x, y in final_frame.items():
        plt.annotate(str(int(y)), xy=(x, y), xytext=(0, 5), 
                 textcoords='offset points', ha='center', fontsize=9)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.tick_params(left=False,bottom=False)
    plt.xlabel(None)
    plt.ylabel(None)
    plt.title('2025 LinkedIn Connections Per Month')
    plt.show()

def main():
    render_plot()

if __name__ == "__main__":
    main()
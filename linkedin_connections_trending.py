import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def plot_connections_over_time(csv_file='Connections.csv', days=365):
    """
    Plot the running total of unique last names over time.

    Parameters:
    -----------
    csv_file : str
        Path to the LinkedIn Connections CSV file
    days : int
        Number of days to display (default: 365)

    Returns:
    --------
    None (displays a plot)
    """
    # Read the CSV file
    df = pd.read_csv(csv_file, encoding='cp1252')

    # Convert 'Connected On' to datetime
    df['Connected On'] = pd.to_datetime(df['Connected On'], format='%d-%b-%y')

    # Sort by date
    df = df.sort_values('Connected On')

    # Filter for last N days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    df_filtered = df[df['Connected On'] >= start_date]

    # Create a date range for the last N days
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')

    # Get unique last names before the period started
    df_before = df[df['Connected On'] < start_date]
    unique_lastnames_before = set(df_before['Last Name'].dropna())

    # Calculate running total of unique last names by day
    running_totals = []
    unique_lastnames_so_far = unique_lastnames_before.copy()

    for date in date_range:
        # Get all connections on this date
        day_connections = df_filtered[df_filtered['Connected On'] == date]
        # Add new last names from this day
        new_lastnames = list(day_connections['Last Name'].dropna())
        unique_lastnames_so_far.update(new_lastnames)
        running_totals.append(len(unique_lastnames_so_far))

    # Create the plot
    fig, ax = plt.subplots(figsize=(14, 7))

    # Plot running total of unique last names
    ax.plot(date_range, running_totals,
            linewidth=2, color='#0077B5', label='Unique Last Names')

    # Formatting
    ax.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax.set_ylabel('Count of Unique Last Names', fontsize=12, fontweight='bold')
    ax.set_title(f'Running Total of Unique Last Names - Last {days} Days', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(loc='upper left', fontsize=10)

    # Format x-axis to show dates nicely
    fig.autofmt_xdate()

    # Add statistics text box
    # total_unique_lastnames = running_totals[-1]
    # initial_unique_lastnames = len(unique_lastnames_before)
    # new_unique_lastnames = total_unique_lastnames - initial_unique_lastnames
    # stats_text = f'Total Unique Last Names: {total_unique_lastnames}\nNew in last {days} days: {new_unique_lastnames}\nStarting count: {initial_unique_lastnames}'
    # ax.text(0.02, 0.98, stats_text, transform=ax.transAxes,
    #         fontsize=10, verticalalignment='top',
    #         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()
    return fig, ax

def main():
    plot_connections_over_time(csv_file='Connections.csv', days=365)
    plt.show()

if __name__ == "__main__":
    # Plot connections over the last 365 days
    
    main()
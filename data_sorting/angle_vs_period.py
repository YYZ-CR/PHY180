import pandas as pd
import numpy as np

def process_pendulum_data(file_path, output_path_max_min):
    # Load the data from the file
    df = pd.read_csv(file_path, delimiter='\t')

    # Extract angles and times
    angles = np.radians(df['θ (degrees)'])
    times = df['t (seconds)']

    # Identify local maxima
    local_maxima_indices = (np.diff(np.sign(np.diff(angles))) < 0).nonzero()[0] + 1
    local_maxima_angles = angles.iloc[local_maxima_indices]
    local_maxima_times = times.iloc[local_maxima_indices]

    # Calculate the periods (time between successive local maxima)
    periods_max = np.diff(local_maxima_times)

    # Filter periods that are between 1 and 2 seconds
    valid_indices_max = np.where((periods_max >= 1) & (periods_max <= 2))[0]
    valid_maxima = local_maxima_angles.iloc[valid_indices_max]
    valid_periods_max = periods_max[valid_indices_max]

    # Sort the maxima by amplitude (descending) and match the sorted periods
    sorted_indices_max = np.argsort(-valid_maxima)
    sorted_maxima = valid_maxima.iloc[sorted_indices_max]
    sorted_periods_max = valid_periods_max[sorted_indices_max]

    # Identify local minima
    local_minima_indices = (np.diff(np.sign(np.diff(angles))) > 0).nonzero()[0] + 1
    local_minima_angles = angles.iloc[local_minima_indices]
    local_minima_times = times.iloc[local_minima_indices]

    # Calculate the periods (time between successive local minima)
    periods_min = np.diff(local_minima_times)

    # Filter periods that are between 1 and 2 seconds
    valid_indices_min = np.where((periods_min >= 1) & (periods_min <= 2))[0]
    valid_minima = local_minima_angles.iloc[valid_indices_min]
    valid_periods_min = periods_min[valid_indices_min]

    # Sort the minima by amplitude (descending) and match the sorted periods
    sorted_indices_min = np.argsort(-valid_minima)
    sorted_minima = valid_minima.iloc[sorted_indices_min]
    sorted_periods_min = valid_periods_min[sorted_indices_min]

    # Round maxima and minima to 2 decimal places
    sorted_maxima = sorted_maxima.round(2)
    sorted_periods_max = sorted_periods_max.round(3)
    sorted_minima = sorted_minima.round(2)
    sorted_periods_min = sorted_periods_min.round(3)

    # Create dataframes for both maxima and minima
    output_data_max = pd.DataFrame({'Amplitude (radians)': sorted_maxima, 'Period (seconds)': sorted_periods_max, 'Amplitude uncertainty (radians)': 0.02, 'Period uncertainty (seconds)': 0.008})
    output_data_min = pd.DataFrame({'Amplitude (radians)': sorted_minima, 'Period (seconds)': sorted_periods_min, 'Amplitude uncertainty (radians)': 0.02, 'Period uncertainty (seconds)': 0.008})

    # Combine maxima and minima into one dataframe
    combined_output_data = pd.concat([output_data_max, output_data_min])

    # Save the combined output to a txt file
    combined_output_data.to_csv(output_path_max_min, sep='\t', index=False)
    return output_path_max_min

file_path = 'data_sorting/pendulum_data_from_tracker.txt'
output_path_max_min = 'data_sorting/sorted_angle_vs_period.txt'
process_pendulum_data(file_path, output_path_max_min)

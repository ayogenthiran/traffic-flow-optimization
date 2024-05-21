import matplotlib.pyplot as plt
import os

class Visualization:
    def __init__(self, path, dpi):
        self._path = path
        self._dpi = dpi
        os.makedirs(self._path, exist_ok=True)  # Ensure the directory exists

    def save_data_and_plot(self, data, filename, xlabel, ylabel):
        try:
            if not data:
                print(f"No data available to plot for {filename}.")
                return
            
            # Setting the plot size and dpi
            plt.figure(figsize=(20, 10), dpi=self._dpi)
            plt.plot(data, marker='o', linestyle='-')  # You can customize the plot look here
            plt.xlabel(xlabel, fontsize=20)
            plt.ylabel(ylabel, fontsize=20)
            plt.title(f"{filename} Plot", fontsize=24)
            plt.grid(True)

            # Adjust plot limits if necessary
            min_val = min(data)
            max_val = max(data)
            plt.ylim([min_val - 0.05 * abs(min_val), max_val + 0.05 * max_val])

            # Save the plot
            plot_path = os.path.join(self._path, f"{filename}.png")
            plt.savefig(plot_path)
            plt.close()

            # Save data to a text file
            data_path = os.path.join(self._path, f"{filename}_data.txt")
            with open(data_path, 'w') as file:
                for value in data:
                    file.write(f"{value}\n")
            
            print(f"Plot and data saved successfully at {self._path}")

        except Exception as e:
            print(f"Failed to save plot or data for {filename}. Error: {e}")

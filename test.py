from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from math import ceil


if __name__ == "__main__":
    # read info.csv to get the number of the docu which need to be visu
    read_path = Path(r"path")
    for csv_file in list(read_path.glob("*.csv")):

        info_csv = pd.read_csv(csv_file)

        n_observations = len(info_csv["filename"])

        # transform the date to date formate and only have hour and minute
        date_list = pd.to_datetime(info_csv["date"]).dt.strftime("%Y-%m-%d %H:%M")

        # generate the color list and the number of the color is depend on the number of the docu
        color_map = plt.get_cmap("plasma", n_observations)

        color_list = [color_map(i) for i in range(n_observations)]

        # Open zip first to get the number of the subplots
        files = list(read_path.glob("*.zip"))
        if len(files) > 0:
            df = pd.read_csv(files[0])
        else:
            raise Exception("No files found.")

        dimensions = [el for el in df.columns if el != "Time"]  # store all the columns name except the time column
        n_dimensions = len(dimensions)

        # calculate required number of rows / columns for subplots
        n_cols = 3
        n_rows = int(ceil(n_dimensions / n_cols))
        # extra row to display the legend if all cells in the grid will be used for subplots
        if n_rows * n_cols == n_dimensions:
            n_rows += 1

        # create figure object
        fig = plt.figure(figsize=(15, 40))
        # create axes for relevant dimensions / columns
        # relevant columns
        axes_per_dimension = {
            el: (fig.add_subplot(n_rows, n_cols, i + 1), i) for i, el in enumerate(dimensions)
        }  # (fig.add_subplot(2, 2, 1), 0)——it will add the first subplot and the index of the subplot is 0
        # axes_per_dimension is a place for store every subplot
        for i, (file, color, label) in enumerate(zip(files, color_list, date_list)):
            # read file
            df = pd.read_csv(file)

            # transform string-formatted datetime object to datetime object
            t = pd.to_datetime(df["Time"], format="mixed")
            # to relative time
            dt = t - t[0]

            for col in df.columns:
                if col in axes_per_dimension:
                    ax, idx = axes_per_dimension[col]  # ax is the axis(axes) include the title and the xlabel
                    # and ax,idx are strored as a list

                    ax.plot(dt, df[col], label=label, color=color, alpha=0.5)
                    ax.tick_params(axis="x", rotation=45)
                    ax.grid(True)  # to show the gridding
                    ax.set_title(col)

                    if idx % n_rows == 0:
                        # this subplot is in the last row
                        # show axislabel and ticklabel
                        ax.set_xlabel("time t/s")
                    else:
                        ax.set_xticklabels([])

        # add one legend for all plots
        handles, labels = axes_per_dimension[dimensions[0]][0].get_legend_handles_labels()
        fig.legend(handles, labels, loc="lower right")

        plt.tight_layout()
        plt.show()

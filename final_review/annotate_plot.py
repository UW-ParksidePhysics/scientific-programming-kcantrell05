@@ -0,0 +1,41 @@
"""
Annotates a plot using Pyplot's text function.
Parameters:
    annotations (dict): A dictionary where keys represent labels (strings) to be annotated,
        and values are dictionaries with the following key-value pairs:
        - 'string' (str): Text string for the text function.
        - 'position' (ndarray, shape (2)): x and y coordinates for the position of the textbox.
        - 'alignment' (list of str, shape (2)): Horizontal and vertical alignment values for the text function.
        - 'fontsize' (float): Font size value in pixels.
Returns:
    None
"""

__author__ = 'Kelsey'


import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

def annotate_plot(annotations):
    x, y = annotations['position']
    plt.text(x, y, annotations['string'], 
             horizontalalignment=annotations['alignment'][0],
             verticalalignment=annotations['alignment'][1], 
             fontsize=annotations['fontsize'])
    return

if __name__ == "__main__":
    test_annotations = {
        'string': f"Created by Kelsey {datetime.today().isoformat()}",
        'position': np.array([4.75, 9.5]),
        'alignment': ['left', 'bottom'],
        'fontsize': 10
    }

    plt.plot(5, 10)
    annotate_plot(test_annotations)
    plt.show()

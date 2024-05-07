import numpy as np

import matplotlib.pyplot as plt

import matplotlib.animation as animation

import os



# Define the modified parse_animation_code function here

def parse_animation_code(code_filename):

    if not os.path.exists(code_filename):

        raise FileNotFoundError(f"File '{code_filename}' not found.")

    with open(code_filename, 'r') as file:

        code = file.read()

    return code



def format_section_header(header_string):

    return f"<h1>{header_string}</h1>\n"



def write_html_report(report_string, report_filename):

    with open(report_filename, 'w') as file:

        file.write(report_string)

    print(f"Report saved as {report_filename}")



# Function definition

def wave_function(x, t, alpha, f, k, w):

    return np.exp(-(alpha*x - f*t)**2) * np.sin(k*x - w*t)



def create_plots(x_values, t_values, alpha, f, k, w):

    # Create plots for three different time values

    for i, time in enumerate([t_values[0], t_values[len(t_values)//2], t_values[-1]]):

        y_values = wave_function(x_values, time, alpha, f, k, w)

        plt.plot(x_values, y_values, label=f't = {time:.2f}')

        plt.xlabel('x')

        plt.ylabel('f(x, t)')

        plt.title('Wave Function at Different Time Values')

        plt.legend()

        plt.savefig(f'wave_function_plot_{i}.png')  # Save each plot with a unique name

        plt.close()  # Close the current plot to clear the figure



if __name__ == "__main__":

    alpha = 0.5

    f = 3

    k = 3 * np.pi

    w = 3 * np.pi



    x_values = np.linspace(-6, 6, 1001)

    t_values = np.linspace(-1, 1, 61)



    create_plots(x_values, t_values, alpha, f, k, w)



    # Parse animation code from file

    animation_code = parse_animation_code(

        'dictionaries_and_strings/animate_wavepacket.py')



    # Format code snippets

    code_snippets = [f"<pre>{snippet}</pre>\n" for snippet in animation_code.split('\n')]



    # Generate HTML report

    report = ""

    report += format_section_header("Animation Code")

    report += ''.join(code_snippets)



    # Include plot images in the report

    report += format_section_header("Plots")

    for i in range(3):

        report += f"<img src='wave_function_plot_{i}.png' alt='Wave Function Plot {i}'>\n"



    # Include animated GIF in the report

    report += format_section_header("Animated GIF")

    report += "<img src='wave_animation.gif' alt='Wave Animation'>\n"



    # Write HTML report

    write_html_report(report, 'animation_report.html')
import time
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

symbol_count = 1000

x_integer = np.random.randint(0, 4, symbol_count) # generates random integers between 0 and 4 to fill out our symbol values. (generates a random number for each symbol in 'symbol_count')
x_degrees = x_integer*360/4.0 + 45 # four possible angles (degrees), spaced at 45 (45, 135, 225, 315)
x_radians = x_degrees*np.pi/180.0 # sin() and cos() both need radians, this just converts x_degrees to radians for that one use case
x_symbols = np.cos(x_radians) + 1j*np.sin(x_radians)

noise_power = 0.05

timer = 0
while timer < 10:
    noise = (np.random.randn(symbol_count) + 1j*np.random.randn(symbol_count))/np.sqrt(2)
    noisy_symbols = x_symbols + noise * np.sqrt(noise_power)
    plt.plot(np.real(noisy_symbols), np.imag(noisy_symbols), ',b')
    plt.grid(True)
    plt.savefig(f"{timer}.png")
    timer = timer + 1

def create_gif(image_paths, output_path, duration=500, loop=0):
    """
    Creates a GIF from a list of images.

    Args:
        image_paths (list): A list of file paths to the images.
        output_path (str): The path to save the output GIF.
        duration (int, optional): The duration of each frame in milliseconds. Defaults to 500.
        loop (int, optional): Number of times the GIF should loop. 0 means infinite loop. Defaults to 0.
    """
    images = [Image.open(image_path) for image_path in image_paths]
    images[0].save(output_path, save_all=True, append_images=images[1:], duration=duration, loop=loop)

image_paths = ["0.png", "1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png" ]
output_path = "output.gif"
create_gif(image_paths, output_path)
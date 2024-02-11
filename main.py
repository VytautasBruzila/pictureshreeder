import numpy as np
import matplotlib.pyplot as plt

# Load the image using NumPy
image = plt.imread('cat.jpg').copy()  # Make a copy to avoid read-only error

# Define the number of strips and the shredding factor
num_strips = 10
shred_factor = 0.5  # Percentage of image width to be shredded

# Calculate the width of each strip
strip_width = int(image.shape[1] / num_strips)

# Initialize the list to store the results
results = []

# Original image
results.append(image)

# Generate four images with the picture shredding effect
for _ in range(4):
    # Make a copy of the original image
    shredded_image = image.copy()

    # Shred the image into strips
    for i in range(num_strips):
        # Calculate the start and end points of the current strip
        start_col = i * strip_width
        end_col = (i + 1) * strip_width

        # Randomly shuffle the columns within the strip
        np.random.shuffle(shredded_image[:, start_col:end_col].reshape(-1, image.shape[2]))

    # Append the shredded image to the results list
    results.append(shredded_image)

# Display the original and generated images
fig, axes = plt.subplots(1, 5, figsize=(15, 3))
for ax, img in zip(axes, results):
    ax.imshow(img)
    ax.axis('off')

plt.show()

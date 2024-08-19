import cv2
import numpy as np

# Load the input image
img = cv2.imread('im1.jpg', cv2.IMREAD_GRAYSCALE)

# Get the dimensions of the input image
height, width = img.shape[:2]
print(height, width)
# Calculate the number of blocks in each dimension
num_blocks_y = int(np.ceil(height/8))
num_blocks_x = int(np.ceil(width/8))

# Pad the image if necessary to make it divisible by 8
padded_height = num_blocks_y * 8
padded_width = num_blocks_x * 8
padded_img = np.zeros((padded_height, padded_width), dtype=np.uint8)
padded_img[:height, :width] = img

# Divide the padded image into blocks of 8x8
blocks = []
for y in range(num_blocks_y):
    for x in range(num_blocks_x):
        block = padded_img[y*8:(y+1)*8, x*8:(x+1)*8]
        blocks.append(block)

# Apply the DCT to each block
dct_blocks = []
for block in blocks:
    dct_block = cv2.dct(np.float32(block))
    dct_blocks.append(dct_block)

# Define the quantization matrix
quantization_matrix = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                                [12, 12, 14, 19, 26, 58, 60, 55],
                                [14, 13, 16, 24, 40, 57, 69, 56],
                                [14, 17, 22, 29, 51, 87, 80, 62],
                                [18, 22, 37, 56, 68, 109, 103, 77],
                                [24, 35, 55, 64, 81, 104, 113, 92],
                                [49, 64, 78, 87, 103, 121, 120, 101],
                                [72, 92, 95, 98, 112, 100, 103, 99]])

# Quantize the DCT coefficients of each block
quantized_blocks = []
for dct_block in dct_blocks:
    quantized_block = np.round(dct_block / quantization_matrix)
    quantized_blocks.append(quantized_block)

# Save the compressed image as a binary file
with open('compressed_image.bin', 'wb') as f:
    for quantized_block in quantized_blocks:
        np.array(quantized_block, dtype=np.int8).tofile(f)




# Load the compressed image as a binary file
with open('compressed_image.bin', 'rb') as f:
    compressed_data = np.fromfile(f, dtype=np.int8)

# Get the dimensions of the compressed image
num_blocks = len(compressed_data) // 64
compressed_height = num_blocks * 8
compressed_width = 8

# Reconstruct the quantized DCT coefficients of each block
quantized_blocks = []
for i in range(num_blocks):
    quantized_block = np.reshape(compressed_data[i*64:(i+1)*64], (8, 8))
    quantized_blocks.append(quantized_block)

# Define the quantization matrix
quantization_matrix = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                                [12, 12, 14, 19, 26, 58, 60, 55],
                                [14, 13, 16, 24, 40, 57, 69, 56],
                                [14, 17, 22, 29, 51, 87, 80, 62],
                                [18, 22, 37, 56, 68, 109, 103, 77],
                                [24, 35, 55, 64, 81, 104, 113, 92],
                                [49, 64, 78, 87, 103, 121, 120, 101],
                                [72, 92, 95, 98, 112, 100, 103, 99]])

# Reconstruct the DCT coefficients of each block
dct_blocks = []
for quantized_block in quantized_blocks:
    dct_block = quantized_block * quantization_matrix
    dct_blocks.append(dct_block)

# Apply the inverse DCT to each block
blocks = []
for dct_block in dct_blocks:
    block = cv2.idct(np.float32(dct_block))
    blocks.append(block)

# Reconstruct the padded image from the blocks
padded_img = np.zeros((compressed_height, compressed_width), dtype=np.uint8)
for i, block in enumerate(blocks):
    y = i // (compressed_width // 8)
    x = i % (compressed_width // 8)
    padded_img[y*8:(y+1)*8, x*8:(x+1)*8] = block

# Crop the padded image to its original size
img = padded_img[:height, :width]

# Show the reconstructed image
cv2.imshow('Reconstructed Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
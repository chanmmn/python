from PIL import Image
import os

def crop_and_save(input_path, output_path, left, top, right, bottom):
    try:
        # Open the image
        img = Image.open(input_path)

        # Crop the specified area
        cropped_img = img.crop((left, top, right, bottom))

        # Save the cropped image
        cropped_img.save(output_path)

        print(f"Image cropped and saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Specify input and output directory
    input_directory = "input_directory"
    output_directory = "output_directory"

    # Specify input file name and coordinates of the area to be cropped (left, top, right, bottom)
    input_file_name = "input_image.jpg"
    crop_area = (100, 50, 400, 300)

    # Create output file name
    output_file_name = "output_cropped_image.jpg"
    
    # Create full input and output paths
    input_image_path = os.path.join(input_directory, input_file_name)
    output_image_path = os.path.join(output_directory, output_file_name)

    # Call the function to crop and save the image
    crop_and_save(input_image_path, output_image_path, *crop_area)

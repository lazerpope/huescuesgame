from PIL import Image
import os
import shutil

def number_sequence(start=1, step=1):
    """Generator that returns numbers in sequence"""
    current = start
    while True:
        yield current
        current += step

def infinite_alphabet():
    """Generator that infinitely cycles through the alphabet"""
    while True:
        for char_code in range(65, 91):
            yield chr(char_code)

def split_image_to_pieces(image_path, size, xcells, ycells, xoffset=0, yoffset=0, output_folder='out' , x_name_generator = None, y_name_generator= None):
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder)
    
    with Image.open(image_path) as img:
        img_width, img_height = img.size
        total_width = xcells * size + xoffset
        total_height = ycells * size + yoffset
        
        if total_width > img_width or total_height > img_height:
            raise ValueError(f"Image too small. Required: {total_width}x{total_height}, Actual: {img_width}x{img_height}")
        
        if y_name_generator is not None:
            y_sequence = y_name_generator() 
            
        y_shift = 0        
        for y in range(ycells):
            if y_name_generator is not None:
                y_name = next(y_sequence)
            if x_name_generator is not None:
                x_sequence = x_name_generator() 
            
            x_shift = 0
            for x in range(xcells):
                left = xoffset + x * size + x_shift
                upper = yoffset + y * size + y_shift
                right = left + size 
                lower = upper + size
                
                piece = img.crop((left, upper, right, lower))
                
                filename = f"piece_{y if y_name_generator is  None else y_name}{x if x_name_generator is  None else next(x_sequence)}.jpg"
                output_path = os.path.join(output_folder, filename)
                piece.save(output_path, 'JPEG') 
                
                x_shift += 5
            y_shift += 5
                

# Example usage
if __name__ == "__main__":
    # Example parameters
    split_image_to_pieces(
        image_path="huescues.jpg",  # Your input image path
        size=32,                      # Size of each square piece
        xcells=30,                      # Number of pieces horizontally
        ycells=16,                      # Number of pieces vertically
        xoffset=49,                    # X offset from left
        yoffset=186,                    # Y offset from top
        output_folder="out" , # Output folder name
        x_name_generator=number_sequence , # Output folder name
        y_name_generator=infinite_alphabet , # Output folder name
    )
    print(f"Saved: ")
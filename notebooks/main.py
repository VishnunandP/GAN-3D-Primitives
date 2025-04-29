from utils.text_parser import parse_text_spec
from utils.primitive_to_step import generate_step_from_vector

# Prompt the user for input dynamically
user_input = input("Enter a design specification in this format (EG: 'cylinder with diameter 15mm and height 30mm'): ")

# Parse the user's input to get the shape, size, and height
shape, size, height = parse_text_spec(user_input)

# Check if a valid shape and size were found
if shape and size:
    # Generate the 3D model and export it as a .step file
    generate_step_from_vector(shape, size, height)
else:
    print("Invalid. Please recheck the format of your design specification.")

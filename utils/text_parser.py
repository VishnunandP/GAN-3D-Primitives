
import re

def parse_text_spec(text):
    # Identify shape from the text input
    shape = None
    if "cube" in text:
        shape = "cube"
    elif "cylinder" in text:
        shape = "cylinder"
    elif "sphere" in text:
        shape = "sphere"
    elif "cone" in text:
        shape = "cone"

    # Extract dimensions (size and height if applicable)
    dimensions = re.findall(r"(\d+)(mm|cm|m)", text)  # Extract numbers and units
    height = None
    
    if dimensions:
        size = float(dimensions[0][0])  # Shape size (e.g., side length or diameter)
        
        # Check if there's a specific mention of height for cylinders or cones
        if shape in ["cylinder", "cone"]:
            height_match = re.findall(r"height (\d+)(mm|cm|m)", text)  # Extract height
            if height_match:
                height = float(height_match[0][0])  # Height for cylinder or cone
            
        return shape, size, height
    return shape, None, None

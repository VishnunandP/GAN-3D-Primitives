import cadquery as cq

# Function to convert vector (representing a shape) to a .step file
def generate_step_from_vector(vector):
    """
    Generates a .step file from a vector input representing a primitive shape.
    The vector contains dimensions for the shape: [diameter, height] for cylinders,
    [length, width, height] for cuboids, etc.

    Args:
        vector (list or tuple): The dimensions of the shape.
            - For a cylinder: [diameter, height]
            - For a cuboid: [length, width, height]
            - For a sphere: [diameter]
    """
    
    # Determine the type of shape and dimensions
    shape_type = vector[0].lower()

    if shape_type == "cylinder":
        # Assume vector = [diameter, height]
        diameter = vector[1]
        height = vector[2]
        
        # Create the cylinder shape using CadQuery
        result = cq.Workplane("XY").circle(diameter / 2).extrude(height)
    
    elif shape_type == "cuboid":
        # Assume vector = [length, width, height]
        length = vector[1]
        width = vector[2]
        height = vector[3]
        
        # Create the cuboid shape using CadQuery
        result = cq.Workplane("XY").box(length, width, height)
    
    elif shape_type == "sphere":
        # Assume vector = [diameter]
        diameter = vector[1]
        
        # Create the sphere shape using CadQuery
        result = cq.Workplane("XY").sphere(diameter / 2)
    
    else:
        raise ValueError("Shape type not recognized. Available options are 'cylinder', 'cuboid', or 'sphere'.")
    
    # Export to a .step file (this saves it as 'generated_model.step')
    result.exportStep("generated_model.step")
    print("3D model has been saved as 'generated_model.step'.")




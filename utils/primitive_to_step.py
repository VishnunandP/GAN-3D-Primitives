import cadquery as cq

def generate_step_from_vector(shape, size, height=None):
    if shape == "cube" and size is not None:
        # Create a simple cube using CadQuery
        result = cq.Workplane("XY").box(size, size, size)
    
    elif shape == "cylinder" and size is not None and height is not None:
        # Create a cylinder with diameter as size and the specified height
        radius = size / 2  # Convert size to radius
        result = cq.Workplane("XY").cylinder(height, radius)
    
    elif shape == "sphere" and size is not None:
        # Create a sphere (diameter is size, radius is half of size)
        radius = size / 2  # Convert size to radius
        result = cq.Workplane("XY").sphere(radius)
    
    elif shape == "cone" and size is not None and height is not None:
        # Create a cone with diameter as size and the specified height
        radius = size / 2  # Convert size to radius
        result = cq.Workplane("XY").cone(height, radius, radius)
    
    else:
        print("Unsupported shape or invalid size")
        return
    
    # Save the generated shape as a STEP file
    result.exportStep("generated_model.step")
    print(f"STEP file generated: generated_model.step")


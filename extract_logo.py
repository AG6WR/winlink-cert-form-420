#!/usr/bin/env python3
"""Extract images from the CERT Form 420 PDF."""

import fitz  # PyMuPDF
from PIL import Image
import io
import os

def extract_images_from_pdf(pdf_path, output_dir="extracted_images"):
    """Extract all images from the first page of the PDF."""
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    
    print(f"PDF has {len(pdf_document)} page(s)")
    
    # Get the first page (where the logo should be)
    page = pdf_document[0]
    
    # Get all images on the page
    image_list = page.get_images(full=True)
    
    print(f"Found {len(image_list)} image(s) on page 1")
    
    # Extract each image
    for img_index, img in enumerate(image_list):
        xref = img[0]  # XREF number
        
        # Extract the image
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        
        # Get image dimensions
        width = base_image.get("width", 0)
        height = base_image.get("height", 0)
        
        print(f"\nImage {img_index + 1}:")
        print(f"  Format: {image_ext}")
        print(f"  Size: {width}x{height}")
        print(f"  File size: {len(image_bytes)} bytes")
        
        # Save the image
        output_filename = f"{output_dir}/image_{img_index + 1:02d}.{image_ext}"
        
        with open(output_filename, "wb") as img_file:
            img_file.write(image_bytes)
        
        print(f"  Saved as: {output_filename}")
        
        # Also save as PNG if it's not already PNG
        if image_ext != "png":
            png_filename = f"{output_dir}/image_{img_index + 1:02d}.png"
            try:
                img = Image.open(io.BytesIO(image_bytes))
                img.save(png_filename, "PNG")
                print(f"  Also saved as PNG: {png_filename}")
            except Exception as e:
                print(f"  Could not convert to PNG: {e}")
    
    pdf_document.close()
    
    print(f"\n✓ Extraction complete! Check the '{output_dir}' folder.")
    print("\nNote: The logo is likely the smallest image or the one in the upper-left corner.")
    print("Look for images that are logo-sized (typically under 200x200 pixels).")

if __name__ == "__main__":
    pdf_file = "LG CERT Form 420  .pdf"
    
    if os.path.exists(pdf_file):
        extract_images_from_pdf(pdf_file)
    else:
        print(f"Error: PDF file '{pdf_file}' not found!")
        print(f"Current directory: {os.getcwd()}")

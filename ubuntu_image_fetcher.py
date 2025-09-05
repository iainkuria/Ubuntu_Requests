#!/usr/bin/env python3
"""
Ubuntu Image Fetcher
A tool for mindfully collecting images from the web
Created as part of my Python Libraries Assignment - 2025
"""

import requests
import os
import re
import hashlib
from urllib.parse import urlparse, urlunparse
from pathlib import Path

def clean_filename(filename):
    """
    Clean the filename by removing special characters and ensuring it's safe
    """
    # Remove query parameters from filename
    filename = filename.split('?')[0]
    
    # Replace non-alphanumeric characters (except dots) with underscores
    cleaned = re.sub(r'[^a-zA-Z0-9\.]', '_', filename)
    
    # Ensure the filename isn't empty
    if not cleaned or cleaned == '.':
        cleaned = "ubuntu_image"
    
    # Add jpg extension if missing
    if not cleaned.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')):
        cleaned += '.jpg'
        
    return cleaned

def get_filename_from_url(url, response):
    """
    Extract filename from URL or response headers, or generate one
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    
    # Try to get filename from Content-Disposition header
    if 'content-disposition' in response.headers:
        content_disp = response.headers['content-disposition']
        filenames = re.findall('filename=(.+)', content_disp)
        if filenames:
            filename = filenames[0].strip('"')
    
    # Clean the filename
    filename = clean_filename(filename)
    
    return filename

def is_duplicate_image(content, directory):
    """
    Check if an image with the same content already exists to avoid duplicates
    """
    # Create a hash of the image content
    content_hash = hashlib.md5(content).hexdigest()
    
    # Check all files in the directory for matching content
    for existing_file in Path(directory).iterdir():
        if existing_file.is_file():
            try:
                with open(existing_file, 'rb') as f:
                    existing_content = f.read()
                    existing_hash = hashlib.md5(existing_content).hexdigest()
                    
                    if existing_hash == content_hash:
                        return True, existing_file.name
            except (IOError, OSError):
                continue
                
    return False, None

def validate_headers(response):
    """
    Validate HTTP headers before saving content
    """
    # Check content type to ensure it's an image
    content_type = response.headers.get('content-type', '')
    if not content_type.startswith('image/'):
        raise ValueError(f"URL does not point to an image (Content-Type: {content_type})")
    
    # Check content length to avoid extremely large files
    content_length = response.headers.get('content-length')
    if content_length and int(content_length) > 10 * 1024 * 1024:  # 10MB limit
        raise ValueError(f"Image is too large ({int(content_length) / 1024 / 1024:.1f} MB)")
    
    return True

def download_image(url, directory="Fetched_Images"):
    """
    Download an image from a URL and save it to the specified directory
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)
        print(f"✓ Ensuring directory '{directory}' exists")
        
        # Set a user-agent header to identify ourselves
        headers = {
            'User-Agent': 'UbuntuImageFetcher/1.0 (Educational Project)'
        }
        
        # Make the request with timeout
        print(f"🔗 Connecting to {urlparse(url).netloc}...")
        response = requests.get(url, headers=headers, timeout=15, stream=True)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Validate headers before proceeding
        validate_headers(response)
        
        # Read the content
        image_content = response.content
        
        # Check for duplicates
        is_duplicate, existing_name = is_duplicate_image(image_content, directory)
        if is_duplicate:
            print(f"⚠️  Image already exists as '{existing_name}' (duplicate content)")
            return False, existing_name
        
        # Extract filename from URL or generate one
        filename = get_filename_from_url(url, response)
        filepath = os.path.join(directory, filename)
        
        # Ensure filename is unique if file already exists
        counter = 1
        original_filepath = filepath
        while os.path.exists(filepath):
            name, ext = os.path.splitext(original_filepath)
            filepath = f"{name}_{counter}{ext}"
            counter += 1
        
        # Save the image
        with open(filepath, 'wb') as f:
            f.write(image_content)
            
        print(f"✓ Successfully fetched: {os.path.basename(filepath)}")
        print(f"✓ Image saved to {filepath}")
        
        return True, os.path.basename(filepath)
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
        return False, str(e)
    except ValueError as e:
        print(f"✗ Validation error: {e}")
        return False, str(e)
    except Exception as e:
        print(f"✗ An unexpected error occurred: {e}")
        return False, str(e)

def main():
    """
    Main function to run the Ubuntu Image Fetcher
    """
    print("=" * 50)
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web")
    print("In the spirit of Ubuntu: 'I am because we are'")
    print("=" * 50)
    
    # Get URL from user
    url = input("\nPlease enter the image URL (or multiple URLs separated by commas): ").strip()
    
    if not url:
        print("No URL provided. Exiting.")
        return
    
    # Split multiple URLs if provided
    urls = [u.strip() for u in url.split(',') if u.strip()]
    
    successful_downloads = 0
    total_urls = len(urls)
    
    for i, url in enumerate(urls, 1):
        print(f"\n📦 Processing URL {i} of {total_urls}: {url}")
        success, result = download_image(url)
        
        if success:
            successful_downloads += 1
    
    # Print summary
    print("\n" + "=" * 50)
    print("Download Summary:")
    print(f"Attempted: {total_urls}")
    print(f"Successful: {successful_downloads}")
    print(f"Failed: {total_urls - successful_downloads}")
    
    if successful_downloads > 0:
        print("\n🌟 Connection strengthened. Community enriched.")
        print("Thank you for sharing in the spirit of Ubuntu.")
    else:
        print("\n💭 Even in absence, community exists. Please try again with different URLs.")
    
    print("=" * 50)

if __name__ == "__main__":
    main()
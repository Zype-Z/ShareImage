"""
    A Introduction to ShareImage and a working Example
"""
from ShareImage import ShareImage, clean_tags

tags = [
    'Python',
    'Cloudinary'
]

image = ShareImage(
    title="ShareImage - A Python Library to Create Dynamic Share Images powered by Cloudinary",
    cloudName="zype",
    imagePublicId="blog/Post-Image",
    tagline=clean_tags(tags),
    taglineFont="futura"
)

print(image)

"""
    A Introduction to ShareImage and a working Example
"""
from ShareImage import ShareImage, join_tags

tags = [
    'Python',
    'Cloudinary'
]

image = ShareImage(
    title="ShareImage - A Python Library to Create Dynamic Share Images powered by Cloudinary",
    cloudName="zype",
    imagePublicId="blog/Post-Image",
    tagline=join_tags(tags),
    taglineFont="futura"
)

print(image)

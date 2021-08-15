"""
    A Introduction to ShareImage and a working Example
"""
from ShareImage import ShareImage, clean_tags

tags = [
    'React',
    'JSX',
    'Markdown'
]

image = ShareImage(
    title="ShareImage - A Python Library to Create Dynamic Share Images powered by Cloudinary",
    cloudName="zype",
    imagePublicId="CodeWithR/TEMPLATE",
    tagline=clean_tags(tags),
    taglineFont="futura"
)

print(image)
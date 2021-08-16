# ShareImage
A Python Library to Generate Dynamic Share Images. Powered by **Cloudinary**.

## Installation
### Windows
```sh
pip install ShareImage
```
### Linux / macOS
```sh
python3 -m pip install ShareImage
```
## Usage
**ShareImage** Can be easily integrated in any Python Project.  
For example, in **Flask**:
```py
from flask import Flask, render_template
from ShareImage import ShareImage

app = Flask(__name__)

@app.route('/')
def index():
    image = ShareImage(
        title="Home",
        cloudName="CLOUDINARY_CLOUD_NAME",
        imagePublicId="CLOUDINARY_IMAGE_ID"
    )
    return render_template('index.html', image=image)
    
@app.route('/posts/<string:slug>')
def posts(slug):
    image = ShareImage(
        title=bySlug.get(slug)['title'],
        cloudName="CLOUDINARY_CLOUD_NAME",
        imagePublicId="CLOUDINARY_IMAGE_ID"
    )
    return render_template('index.html', image=image)

if __name__=="__main__":
    app.run()
```
Now, you can use the `image` variable in any `img` Tag or `og:image`/`twitter:image`/`image` Meta Tags!  
**Note**: `CLOUDINARY_CLOUD_NAME` and `CLOUDINARY_IMAGE_ID` are respectedly Your Cloudinary Cloud Name and Image Public Id (Including Folder Name) & the `bySlug` is a Special Variable to find specific posts in a Array of Dictionaries by Slug and it can be achieved by the following Code:
```py
def build_dict(seq, key):
    return dict((d[key], dict(d, index=index)) for (index, d) in enumerate(seq))

bySlug = build_dict(ARRAY_OF_POSTS, key="KEY_OF_SLUG")

# Usage: bySlug(SLUG_OF_POST)['KEY_TO_FIND']
```
## Utilites
By default **ShareImage** provides two useful Utility Functions.  
### Clean Text (`clean_text`)
It Cleanes a Text String and makes it URI-Compatible.
**Note**: It uses Double-Escape for most Special Charecters to use it with Cloudinary.
Example:
```py
from ShareImage import clean_text

title = "A Test String"
print(clean_text(title)) # Will return A%2520Test%2520String
```
### Join Tags (`join_tags`)
It Joins a Array of Tags to with `#` to use it as the tagline of ShareImage.  
Example:

```py
from ShareImage import ShareImage, join_tags

tags = [
    'Python',
    'Cloudinary'
]

image = ShareImage(
    cloudName="zype",
    imagePublicId="blog/Post-Image",
    title='A Python Library to Generate Dynamic Share Images',
    tagline=join_tags(tags),
    taglineFont="futura"
)
```

## Parameters
### Required Parameters
Parameter | Type | Description |
:--------: | :------: | :---------: |
`title`    | String     | Title of Text |
`cloudName` | String   | Name of your Cloudinary Cloud |
`imagePublicId` | String | Public Id of Your Image including Folder Name |
### Optional Parameters
Parameter | Type | Default | Description |
:--------: | :-------: | :-----: | :-----: |
`tagline` | String | None |Tagline of Website or Tags of Post |
`titleFont` | String | futura | Font of Title |
`titleExtraConfig` | String | `''` | Extra Title Config |
`taglineExtraConfig` | String | `''` | Extra Config of Tagline |
`cloudinaryUrlBase` | String | https://res.cloudinary.com | URL Base of Cloudinary |
`taglineFont` | String | arial | Font of Tagline |
`imageWidth` | Integer | 1280 | Width of Image |
`imageHeight` | Integer | 669 | Height of Image |
`textAreaWidth` | Integer | 760 | Width of TextArea |
`textLeftOffset` | Integer | 480 | Left Offset of Text |
`titleGravity` | String | `south_west` | Gravity of Title |
`taglineGravity` | String | `north_west` | Gravity of Tagline |
`titleLeftOffset` | Integer | None | Left Offset of Title |
`taglineLeftOffset` | Integer | None | Left Offset of Tagline |
`titleBottomOffset` | Integer | 254 | Bottom Offset of Title |
`taglineTopOffset` | Integer | 445 | Top Offset of Tagline |
`textColor` | String | `000000` | Color of Text |
`titleColor` | String | None | Color of Title (If not provided `textColor` will be used instead |
`taglineColor` | String | None | Color of Tagline (If not provided `textColor` will be used instead |
`titleFontSize` | Integer | 64 | Font Size of Title |
`taglineFontSize` | Integer | 48 | Font Size of Tagline |
**Note**: If you don't provide Tagline, Parameters with `tagline` Prefix will be ignored.  
We may add more Customization to **ShareImage** in the Future.

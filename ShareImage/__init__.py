def join_tags(tags: list) -> str:
    """Generate String Tag with Array of Tags

    Args:
        tags (list): Array of Tags

    Returns:
        str: String of Tags
    """
    tagString = f'#{" #".join(tags)}'
    return tagString

def clean_text(text: str) -> str:
    """Clean Text of a String and make it URI-Compatible

    Args:
        text (str): The Text to String

    Returns:
        str: Cleaned Text
    """
    return text.replace(',', '%252C').replace('?', '%253F').replace('/', '%252F').replace('\\', '%255C').replace('#', '%2523').replace(' ', '%2520')


def ShareImage(
    title: str,
    cloudName: str,
    imagePublicId: str,
    tagline: str = None,
    titleFont: str = "futura",
    titleExtraConfig: str = '',
    taglineExtraConfig: str = '',
    cloudinaryUrlBase: str = "https://res.cloudinary.com",
    taglineFont: str = 'arial',
    imageWidth: int = 1280,
    imageHeight: int = 669,
    textAreaWidth: int = 760,
    textLeftOffset: int = 480,
    titleGravity: str = 'south_west',
    taglineGravity: str = 'north_west',
    titleLeftOffset: int = None,
    taglineLeftOffset: int = None,
    titleBottomOffset: int = 254,
    taglineTopOffset: int = 445,
    textColor: str = '000000',
    titleFontSize: int = 64,
    taglineFontSize: int = 48,
) -> str:
    """Generate Social Images with Cloudinary

    Args:
        title (str): Title to be placed on Image.
        cloudName (str): Cloudinary Cloud Name.
        imagePublicId (str): Public Id of Image (including Folder Name).
        tagline (str, optional): Tagline or Tags to be placed on Image. Defaults to None.
        titleFont (str, optional): Font of Title. Defaults to "futura".
        titleExtraConfig (str, optional): Extra Title Config. Defaults to ''.
        taglineExtraConfig (str, optional): Extra Tagline Config. Defaults to ''.
        cloudinaryUrlBase (str, optional): Url Base of Cloudinary. Defaults to "https://res.cloudinary.com".
        taglineFont (str, optional): Font of Tagline. Defaults to 'arial'.
        imageWidth (int, optional): Width of Image. Defaults to 1280.
        imageHeight (int, optional): Height of Image. Defaults to 669.
        textAreaWidth (int, optional): Width of TextArea. Defaults to 760.
        textLeftOffset (int, optional): Left Offset of Text. Defaults to 480.
        titleGravity (str, optional): Gravity of Title. Defaults to 'south_west'.
        taglineGravity (str, optional): Gravity of Tagline. Defaults to 'north_west'.
        titleLeftOffset (int, optional): Left Offset of Title. Defaults to None.
        taglineLeftOffset (int, optional): Left Offset of Tagline. Defaults to None.
        titleBottomOffset (int, optional): Bottom Offset of Tagline. Defaults to 254.
        taglineTopOffset (int, optional): Top Offset of Tagline. Defaults to 445.
        textColor (str, optional): Color of Text. Defaults to '000000'.
        titleFontSize (int, optional): Font Size of Title. Defaults to 64.
        taglineFontSize (int, optional): Font Size of Tagline. Defaults to 48.

    Returns:
        str: Complete Cloudinary URL
    """

    imageConfig = [
        f'w_{imageWidth}',
        f'h_{imageHeight}',
        'c_fill',
        'q_auto',
        'f_auto'
    ]

    imageConfig = ','.join(imageConfig)

    title = clean_text(title)

    titleConfig = [
        f'w_{textAreaWidth}',
        'c_fit',
        f'co_rgb:{textColor}',
        f'g_{titleGravity}',
        f'x_{titleLeftOffset or textLeftOffset}',
        f'y_{titleBottomOffset}',
        f'l_text:{titleFont}_{titleFontSize}{titleExtraConfig}:{title}',
    ]

    titleConfig = ','.join(titleConfig)

    if tagline is not None:
        tagline = clean_text(tagline)
        taglineConfig = [
            f'w_{textAreaWidth}',
            'c_fit',
            f'co_rgb:{textColor}',
            f'g_{taglineGravity}',
            f'x_{taglineLeftOffset or textLeftOffset}',
            f'y_{taglineTopOffset}',
            f'l_text:{taglineFont}_{taglineFontSize}{taglineExtraConfig}:{clean_text(tagline)}'
        ]

        taglineConfig = ','.join(taglineConfig)
    else:
        taglineConfig = None

    urlParts = []
    if tagline is not None:
        urlParts = [
            cloudinaryUrlBase,
            cloudName,
            'image',
            'upload',
            imageConfig,
            titleConfig,
            taglineConfig,
            imagePublicId,
        ]
    else:
        urlParts = [
            cloudinaryUrlBase,
            cloudName,
            'image',
            'upload',
            imageConfig,
            titleConfig,
            imagePublicId,
        ]

    return '/'.join(urlParts)

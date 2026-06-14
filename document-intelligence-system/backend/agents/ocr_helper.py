# agents/ocr_helper.py

import easyocr

_reader = None

def get_reader():
    global _reader
    if _reader is None:
        _reader = easyocr.Reader(
            ['en'],
            gpu=False
        )
    return _reader

def extract_text_from_image(image_path):

    reader = get_reader()
    result = reader.readtext(
        image_path,
        detail=0
    )

    return "\n".join(result)
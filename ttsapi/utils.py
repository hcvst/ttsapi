
import hashlib

import slugify


def generate_filename(text, extension):
    slug = slugify.slugify(text, max_length=64)
    digest = hashlib.md5(text.encode("utf-8")).hexdigest()
    return f"{slug}-{digest}.{extension}"

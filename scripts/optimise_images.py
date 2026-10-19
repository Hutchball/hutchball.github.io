"""Regenerate responsive WebP assets. Requires Pillow; originals remain unchanged.

Content hashes allow safe long caching on hosts that support custom headers.
Rerunning after changing artwork requires updating HTML to the new filenames.
"""
from pathlib import Path
import hashlib
import io
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

def generate():
    result = {}
    originals = [ROOT / 'assets/cake-logo.png', *sorted(p for p in (ROOT / 'assets').glob('*-icon.*') if p.name != 'apple-touch-icon.png')]
    for source in originals:
        sizes = (48, 96, 144) if source.stem == 'cake-logo' else (160, 280, 420, 640)
        result[source.name] = {}
        with Image.open(source) as original:
            for width in sizes:
                resized = original.convert('RGBA').resize((width, width), Image.Resampling.LANCZOS)
                output = io.BytesIO()
                resized.save(output, format='WEBP', quality=85, method=6)
                data = output.getvalue()
                digest = hashlib.sha256(data).hexdigest()[:10]
                name = f'{source.stem}-{width}.{digest}.webp'
                (ROOT / 'assets' / name).write_bytes(data)
                result[source.name][width] = name
    return result

if __name__ == '__main__':
    generate()

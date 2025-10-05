from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle


#Lisää neliön piirrokseen. Koordinaatit ja pituus numeroina
def drawSquare(PDwg: Drawing, left, top, sideLength, color, strokeColor) -> None:
    left = float(left)
    top = float(top)
    sideLength = float(sideLength)

    square = Rect(
        insert=(left, top),               # (x, y)
        size=(sideLength, sideLength),    # (width, height)
        fill=color,                       # täyttöväri
        stroke=strokeColor                # reunaviivan väri
    )
    PDwg.add(square)

#Lisää ympyrän piirrokseen. 
def drawCircle(PDwg: Drawing, centerX, centerY, radius, color, stroke) -> None:
    centerX = float(centerX)
    centerY = float(centerY)
    radius = float(radius)

    circle = Circle(
        center=(centerX, centerY),   # (x, y)
        r=radius,                    # säde
        fill=color,                  # täyttöväri
        stroke=stroke                # reunaviivan väri
    )
    PDwg.add(circle)

#Tallentaa piirroksen SVG-tiedostoon

from svgwrite import Drawing

def saveSvg(PDwg: Drawing, file: str) -> None:
    PDwg.indent = "  "     # 2 välilyönnin sisennys

    # Tallennus
    PDwg.saveas(file)
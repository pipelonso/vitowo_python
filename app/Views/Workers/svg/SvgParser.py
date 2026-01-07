from typing import List

from PySide6.QtCore import Qt
from svgpathtools import svg2paths
from PySide6.QtGui import QPainterPath, QPainter, QBrush, QPen, QColor

class SvgParser:

    def __init__(self):

        pass

    @staticmethod
    def svg_to_q_painter_paths(svg_file_path: str):
        """
        Returns list of tuples: (QPainterPath, attributes)
        """
        paths, attributes = svg2paths(svg_file_path)
        print(attributes)
        result = []

        for path, attr in zip(paths, attributes):

            attr_style = attr.get("style", None)
            attr_split = str(attr_style).split(";")
            attrs_prop_split: dict = {}

            for att in attr_split:
                prop_name = att.split(":")[0]
                prop_value = att.split(":")[1]
                attrs_prop_split[prop_name] = prop_value

            print(attrs_prop_split)

            qp = QPainterPath()
            first = True

            for seg in path:
                start = seg.start
                end = seg.end

                if first:
                    qp.moveTo(start.real, start.imag)
                    first = False

                if seg.__class__.__name__ == "Line":
                    qp.lineTo(end.real, end.imag)

                elif seg.__class__.__name__ == "CubicBezier":
                    qp.cubicTo(
                        seg.control1.real, seg.control1.imag,
                        seg.control2.real, seg.control2.imag,
                        end.real, end.imag
                    )

                elif seg.__class__.__name__ == "QuadraticBezier":
                    qp.quadTo(
                        seg.control.real, seg.control.imag,
                        end.real, end.imag
                    )

                elif seg.__class__.__name__ == "Arc":
                    for c in seg.as_cubic_curves():
                        qp.cubicTo(
                            c.control1.real, c.control1.imag,
                            c.control2.real, c.control2.imag,
                            c.end.real, c.end.imag
                        )

            qp.closeSubpath()

            result.append((qp, attrs_prop_split))

        return result

    @staticmethod
    def paint_into(painter: QPainter, paths_with_attr):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for path, attr in paths_with_attr:

            # ----------- FILL --------------
            fill = attr.get("fill", None)

            if fill and fill != "none":
                brush = QBrush(QColor(fill))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.BrushStyle.NoBrush)

            # ----------- STROKE --------------
            stroke = attr.get("stroke", None)

            if stroke and stroke != "none":
                pen = QPen(QColor(stroke))

                width = attr.get("stroke-width", "1")
                try:
                    pen.setWidthF(float(width))
                except Exception as e:
                    print('Failed to width' + str(e))
                    pass
            else:
                pen = Qt.PenStyle.NoPen

            painter.setPen(pen)

            # ----------- DRAW --------------
            painter.drawPath(path)


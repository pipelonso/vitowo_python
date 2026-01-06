from typing import List

from svgpathtools import svg2paths
from PySide6.QtGui import QPainterPath, QPainter
from PySide6.QtCore import QPointF

class SvgParser:

    def __init__(self):

        pass

    @staticmethod
    def svg_to_q_painter_paths(svg_file_path: str) -> list[QPainterPath]:
        """
        Converts svg into list of QPainterPath
        """
        paths, attributes = svg2paths(svg_file_path)

        q_painter_paths = []

        for path in paths:
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
                    for curve in seg.as_cubic_curves():
                        qp.cubicTo(
                            curve.control1.real, curve.control1.imag,
                            curve.control2.real, curve.control2.imag,
                            curve.end.real, curve.end.imag
                        )

            qp.closeSubpath()
            q_painter_paths.append(qp)

        return q_painter_paths

    @staticmethod
    def paint_into(painter: QPainter, paths: List[QPainterPath]):
        p = painter
        p.setRenderHint(QPainter.RenderHint.Antialiasing)

        for path in paths:
            p.drawPath(path)

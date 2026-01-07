from PySide6.QtCore import QRectF
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsItem, QWidget, QStyleOptionGraphicsItem
from PySide6.QtGui import QPainter, QBrush, QPen, QColor

class SvgPathItem(QGraphicsItem):
    def __init__(self, paths):
        super().__init__()
        self.paths = paths

    def boundingRect(self):
        rect = QRectF()
        for p in self.paths:
            rect = rect.united(p[0].boundingRect())
        return rect

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem = None, widget: QWidget | None = None):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for path, attr in self.paths:

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
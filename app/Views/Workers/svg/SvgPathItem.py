from PySide6.QtCore import QRectF
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QGraphicsItem, QWidget, QStyleOptionGraphicsItem


class SvgPathItem(QGraphicsItem):
    def __init__(self, paths):
        super().__init__()
        self.paths = paths

    def boundingRect(self):
        rect = QRectF()
        for p in self.paths:
            rect = rect.united(p.boundingRect())
        return rect

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget | None = None):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        for path in self.paths:
            painter.drawPath(path)
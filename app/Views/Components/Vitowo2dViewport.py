from typing import List

from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPainterPath
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QStyleOptionGraphicsItem

from app.Views.Workers.svg.SvgParser import SvgParser
from app.Views.Workers.svg.SvgPathItem import SvgPathItem


class Vitowo2dViewport(QGraphicsView):

    def __init__(self):
        super().__init__()

        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)

        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.scene.setBackgroundBrush(Qt.GlobalColor.white)

        self.svg_parser = SvgParser()
        self.painter = QPainter()
        self.path_items: List[SvgPathItem] = []

    def wheelEvent(self, event):
        """Zoom con la rueda del mouse"""
        zoom_in_factor = 1.25
        zoom_out_factor = 1 / zoom_in_factor

        if event.angleDelta().y() > 0:
            zoom_factor = zoom_in_factor
        else:
            zoom_factor = zoom_out_factor

        self.scale(zoom_factor, zoom_factor)

    def add_path_item(self, paths: List[QPainterPath]):
        svg = SvgPathItem(paths)
        self.scene.addItem(svg)
        style = QStyleOptionGraphicsItem()
        svg.paint(self.painter, style)
        self.path_items.append(svg)
        pass
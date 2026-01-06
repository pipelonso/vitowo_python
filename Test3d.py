from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.Qt3DCore import Qt3DCore
from PySide6.Qt3DExtras import Qt3DExtras
from PySide6.Qt3DRender import Qt3DRender
from PySide6.QtGui import QVector3D
from PySide6.QtWidgets import QWidget
import sys


class Simple3DView(Qt3DExtras.Qt3DWindow):
    def __init__(self):
        super().__init__()

        # Escena raíz
        self.root_entity = Qt3DCore.QEntity()

        # Luz
        light_entity = Qt3DCore.QEntity(self.root_entity)
        light = Qt3DRender.QPointLight(light_entity)
        light.setColor("white")
        light.setIntensity(1)
        light_transform = QVector3D(10, 10, 10)
        light_entity.addComponent(light)

        # Malla (un cubo)
        mesh_entity = Qt3DCore.QEntity(self.root_entity)
        mesh = Qt3DExtras.QCuboidMesh()
        material = Qt3DExtras.QPhongMaterial(mesh_entity)
        material.setDiffuse("royalblue")

        mesh_entity.addComponent(mesh)
        mesh_entity.addComponent(material)

        # Cámara
        self.camera().lens().setPerspectiveProjection(45.0, 16 / 9, 0.1, 1000)
        self.camera().setPosition(QVector3D(0, 0, 10))
        self.camera().setViewCenter(QVector3D(0, 0, 0))

        # Controlador orbital
        cam_controller = Qt3DExtras.QOrbitCameraController(self.root_entity)
        cam_controller.setCamera(self.camera())

        # Asignar la raíz al motor 3D
        self.setRootEntity(self.root_entity)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        label = QLabel("Ejemplo de Qt3D en VBoxLayout")
        layout.addWidget(label)

        # Crear la vista 3D
        view3d = Simple3DView()
        container = QWidget.createWindowContainer(view3d)

        # Ajustar tamaño mínimo
        container.setMinimumSize(400, 300)
        # container.setFocusPolicy(Qt3DExtras.Qt3DWindow.FocusPolicy.TabFocus)

        layout.addWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())

from PySide6.Qt3DExtras import Qt3DExtras
from PySide6.Qt3DCore import Qt3DCore
from PySide6.Qt3DRender import Qt3DRender
from PySide6.QtGui import QVector3D, QColor

class VitowoViewport(Qt3DExtras.Qt3DWindow):
    def __init__(self):
        super().__init__()

        # Fondo
        self.defaultFrameGraph().setClearColor(QColor(30, 30, 30))

        # Entidad raíz
        self.root_entity = Qt3DCore.QEntity()

        # Cámara
        self.camera = self.camera()
        self.camera.lens().setPerspectiveProjection(45.0, 16 / 9, 0.1, 1000.0)
        self.camera.setPosition(QVector3D(0, 0, 10))
        self.camera.setViewCenter(QVector3D(0, 0, 0))

        # Control de cámara
        controller = Qt3DExtras.QOrbitCameraController(self.root_entity)
        controller.setCamera(self.camera)

        # Cubo
        cube_entity = Qt3DCore.QEntity(self.root_entity)
        cube_mesh = Qt3DExtras.QCuboidMesh()
        cube_transform = Qt3DCore.QTransform()
        cube_transform.setScale(1.0)
        cube_transform.setTranslation(QVector3D(0, 0, 0))

        cube_entity.addComponent(cube_mesh)
        cube_entity.addComponent(cube_transform)

        material = Qt3DExtras.QPhongMaterial()
        cube_entity.addComponent(material)

        # Luz direccional
        light_entity = Qt3DCore.QEntity(self.root_entity)
        light = Qt3DRender.QDirectionalLight()
        light.setWorldDirection(QVector3D(-1, -1, -1))
        light_transform = Qt3DCore.QTransform()
        light_transform.setTranslation(QVector3D(5, 5, 5))

        light_entity.addComponent(light)
        light_entity.addComponent(light_transform)

        # Asignar raíz
        self.setRootEntity(self.root_entity)

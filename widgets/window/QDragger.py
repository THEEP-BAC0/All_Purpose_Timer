from PySide6.QtCore import Qt, QPoint

class QDragger:
    def __init__(self, window, titleBar):
        self.init_vars(window, titleBar)

    def init_vars(self, window, titleBar):
        self.window = window
        self.titleBar = titleBar

        self.offset = QPoint()
        self.dragging = False
    
    def start_drag(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            # Store the offset between mouse position and top-left of the window
            self.offset = event.globalPosition().toPoint() - self.window.frameGeometry().topLeft()
            event.accept()

    def drag(self, event):
        if not self.dragging:
            return

        # Get the target position
        new_pos = event.globalPosition().toPoint() - self.offset

        # Get screen geometry where the window currently is
        screen = self.window.screen().availableGeometry()

        # Clamp X
        if new_pos.x() < screen.left():
            new_pos.setX(screen.left())
        elif new_pos.x() + self.window.width > screen.right():
            new_pos.setX(screen.right() - self.window.width)

        # Clamp Y
        if new_pos.y() < screen.top():
            new_pos.setY(screen.top())
        elif new_pos.y() + self.window.height > screen.bottom():
            new_pos.setY(screen.bottom() - self.window.height)

        # Move window
        self.window.move(new_pos)

    def end_drag(self, event):
        self.dragging = False
        event.accept()
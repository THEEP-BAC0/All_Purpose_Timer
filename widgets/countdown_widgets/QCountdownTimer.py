from PySide6.QtCore import QObject, QTimer, QElapsedTimer, QTime, Signal

class QCountdownTimer(QObject):
    time_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self.running = False
        self.elapsed = QElapsedTimer()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_time)

    def toggle(self):
        self.running = not self.running
        if self.running:
            self.elapsed.start()
            self.timer.start()
        else:
            self.timer.stop()

    def update_time(self):
        ms = self.elapsed.elapsed()

        minutes = (ms // 60000)
        seconds = (ms // 1000) % 60
        milliseconds = (ms % 1000) // 10

        self.time_changed.emit(f"{minutes:02d}:{seconds:02d}:{milliseconds:02d}")

    def return_time(self) -> QTime:
        ms = self.elapsed.elapsed()
        return QTime(0, 0).addMSecs(ms)
from PySide6.QtCore import QObject, QTimer, QElapsedTimer, Signal

class QStopwatch(QObject):
    time_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self.running = False
        self.accumulated_ms = 0

        self.elapsed = QElapsedTimer()
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update_time)

    def toggle(self) -> None:
        if not self.running:
            # Start or resume
            self.elapsed.start()
            self.timer.start()
            self.running = True
        else:
            # Pause
            self.accumulated_ms += self.elapsed.elapsed()
            self.timer.stop()
            self.running = False

    def update_time(self) -> None:
        current_ms = self.accumulated_ms

        # Adds current_ms to time passing
        if self.running:
            current_ms += self.elapsed.elapsed()

        # Gets minutes, seconds, and milliseconds
        minutes = current_ms // 60000
        seconds = (current_ms // 1000) % 60
        milliseconds = (current_ms % 1000) // 10

        # Constructs time
        self.time_changed.emit(
            f"{minutes:02d}:{seconds:02d}:{milliseconds:02d}"
        )

    def reset_time(self) -> None:
        self.timer.stop()
        self.elapsed.invalidate()
        self.accumulated_ms = 0
        self.running = False

        self.time_changed.emit("00:00:00")
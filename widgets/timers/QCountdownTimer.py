from PySide6.QtCore import QObject, QTimer, Signal, QTime

class QCountdownTimer(QObject):
    time_changed = Signal(QTime)

    def __init__(self):
        super().__init__()
        self.running: bool = False
        self.time_left: QTime = QTime(0, 0, 0)

        self.timer: QTimer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self._tick)
    
    def toggle(self, time: QTime) -> None:
        self.running = not self.running
        
        if self.running:
            self.time_left = QTime(time.hour(), time.minute(), time.second())
            self.timer.start()
            self.running = True
        else:
            self.timer.stop()
            self.running = False

    def _tick(self) -> None:
        # Convert QTime to total seconds
        total_seconds = (
            self.time_left.hour() * 3600 +
            self.time_left.minute() * 60 +
            self.time_left.second()
        )

        # Stop if already zero
        if total_seconds <= 0:
            self.stop_time()
            return

        # Subtract 1 second
        total_seconds -= 1

        # Convert seconds to QTime
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        self.time_left = QTime(h, m, s)

        # Update UI
        self.time_changed.emit(self.time_left)
    
    def stop_time(self) -> None:
        self.time_left = QTime(0, 0, 0)
        self.time_changed.emit(self.time_left)
        self.timer.stop()
        self.running = False

    def set_time(self, qtime: QTime) -> None:
        self.time_left = QTime(qtime.hour(), qtime.minute(), qtime.second())
        self.time_changed.emit(self.time_left)
import logging
from PyQt6.QtWidgets import QPlainTextEdit
from PyQt6.QtCore import QObject, pyqtSignal
import Tools

# general logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename=Tools.LOGFILE_PATH, encoding='utf-8', level=logging.INFO, filemode='w')

# Logger for GUI
class QPlainTextEditLogHandler(logging.Handler, QObject):
    sigLog = pyqtSignal(str)

    def __init__(self, textWgt: QPlainTextEdit) -> None:
        super().__init__()
        QObject.__init__(self)
        self.plainTextWgt = textWgt
        self.plainTextWgt.setReadOnly(True)
        self.sigLog.connect(self.plainTextWgt.appendPlainText)

    def emit(self, record):
        msg = self.format(record)
        self.sigLog.emit(msg)


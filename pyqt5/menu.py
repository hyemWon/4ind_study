# 메뉴바 생성
# QWidget은 메뉴바를 만들 수 없다. QMainWindow는 MenuBar 생성 가능
# QMainWindow를 만들면 자동으로 QWidget이 안에 포함되어 만들어 진다.

# PYQT5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QPushButton, QDesktopWidget, QMessageBox, QAction
from PyQt5.QtCore import QCoreApplication # 이벤트 처리 (이벤트-시그널 signal, 호출 함수 - 슬롯 slot)


class Exam(QMainWindow):
    def __init__(self):
        super().__init__() # 상위 객체 생성
        self.initUI()

    def initUI(self):
        # 버튼생성
        btn = QPushButton('Button', self)
        btn.resize(btn.sizeHint())  # 글씨를 기준으로 크기 조절
        btn.setToolTip('버튼입니다.<b> 안녕하세요</b>') # 마우스 위치시 설명 보여주기 (태그 사용 가능)
        btn.move(50,50) # 위치 변경

        # 버튼이 클릭되었을때 연결되는 슬롯
        btn.clicked.connect(QCoreApplication.instance().quit) # 프로그램 종료

        # 상태표시줄
        self.statusBar()
        self.statusBar().showMessage("상태표시줄입니다.")

        # 메뉴바
        menu = self.menuBar()
        menu_file = menu.addMenu('File') # 그룹 생성
        menu_adit = menu.addMenu('Edit')
        menu_view = menu.addMenu('View')

        file_exit = QAction()


        # self.setGeometry(500,500,400,500) # 창 시작위치 (x,y), 창 너비 (w,h)
        self.resize(400,500)
        self.center() # 창 중앙 배치 함수
        self.setWindowTitle('PyQt5 Program')
        self.show()

    def closeEvent(self, QCloseEvent): # 오버라이딩. x버튼 눌렀을 때 실행 함수
        ans = QMessageBox.question(self, "종료 확인", "종료 하시겠습니까?",
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No) # 마지막 값은 기본값

        if ans == QMessageBox.Yes: # Yes 클릭시 종료
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()



    def center(self):
        qr = self.frameGeometry() # 창의 위치와 크기 정보 가져오기
        cp = QDesktopWidget().availableGeometry().center() # 사용하는 모니터 화면의 가운데 위치 파악
        qr.moveCenter(cp) # 창의 직사각형 위치를 화면의 중심의 위치로 이동
        self.move(qr.topLeft()) # 현재 창을 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동





app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_()) # app.은 이벤트 처리를 위한 loop



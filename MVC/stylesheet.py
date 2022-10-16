def get_stylesheet():
    return """
        QMainWindow {
            background-color: #212529;
            color: #e9ecef;  
        }
        .warningDialog {
            background-color: #495057;
        }
        .warningDialog QLabel {
            color: #c92a2a;
        }
        .warningMessage {
            border: 1px solid #c92a2a;
            border-radius: 3;
            background: #ffe3e3;
            padding: 6 12;
        }
        .warningList {
            border: 1px solid #c92a2a;
            border-radius: 3;
            background: #ffe3e3;
        }
        .warningBtn {
            color: #fff5f5;
            border: 1px solid #c92a2a;
            border-radius: 3;
            background: #ff6b6b;
            padding: 6 12;
        }
        .warningBtn:hover {
            background: #f03e3e;
            color: #fff5f5;
        }
        
        .warningDialogScrollArea {
            background-color: transparent;
            border: none;
            border-top-left-radius: 5;
            border-bottom-left-radius: 5;
        }
        .warningScrollBar {
            background: #fff5f5;
            width: 12;
            border-top-right-radius: 5;
            border-bottom-right-radius: 5;
        }
        .warningScrollBar::handle:vertical {
            min-height: 20;
            background: #ff8787;
            border: 1.4px solid #c92a2a;
            border-radius: 5;
        }

        .warningScrollBar::handle:vertical:pressed {
            background: #f03e3e;
        }
        .warningScrollBar::add-line {
            height: 0;
        }
        .warningScrollBar::sub-line {
            height: 0;
        }
        
        QLabel {
            color: #e9ecef;
        }
        .section {
            background-color: #495057;
            border: 1px solid #868e96;
            border-radius: 3;
        }
        .toggle-slider {
            color: #e9ecef;
        }
        .toggle-slider::indicator {
            width: 40;
            height: 20;
        }
        .toggle-slider::indicator:checked {
            image: url(resources/svg/toggle--active.svg);
        }
        .toggle-slider::indicator:unchecked {
            image: url(resources/svg/toggle.svg);
        }

        .renameDiv {
            border: 1px solid #343a40;
            border-radius: 3;
        }
        .renameInput {
            color: #495057;
            background-color: #e9ecef;
            border-bottom-left-radius: 3;
            border-top-left-radius: 3;
            padding: 5;
        }
        .renameInput:disabled {
            color: #495057;
            background-color: #e9ecef;
        }
        .renameBtn {
            color: #087f57;
            background-color: #63e6be;
            border-left: 1px solid #868e96;
            border-bottom-right-radius: 3;
            border-top-right-radius: 3;
            padding: 5 12;
        }
        .renameBtn:disabled {
            color: #495057;
            background-color: #dee2e6;
        }
        .renameBtn:hover {
            color: #087f57;
            background-color: #38d9a9;
        }
        
        .selectBtn::indicator {
            border: 1px solid #343a40;
            border-radius: 3;
        }
        .selectBtn::indicator:checked {
            background-color: #63e6be;
        }
        .selectBtn::indicator:unchecked, .selectBtn::indicator:disabled {
            background-color: #dee2e6;
        }
        .selectBtn::indicator:unchecked:hover {
            background-color: #adb5bd;  
        }
        
        .rotateBtn::indicator {
            width: 90;
            height: 36;
        }
        
        #rotate-left::indicator:checked {
            image: url(resources/svg/rotate-left--active.svg);
        }
        #rotate-left::indicator:unchecked, #rotate-left::indicator:disabled {
            image: url(resources/svg/rotate-left.svg);
        }
        #rotate-left::indicator:unchecked:hover {
            image: url(resources/svg/rotate-left--hover.svg);
        }
        
        #rotate-right::indicator:checked {
            image: url(resources/svg/rotate-right--active.svg);
        }
        #rotate-right::indicator:unchecked, #rotate-right::indicator:disabled {
            image: url(resources/svg/rotate-right.svg);
        }
        #rotate-right::indicator:unchecked:hover {
            image: url(resources/svg/rotate-right--hover.svg);
        }
        
        #rotate-180::indicator:checked {
            image: url(resources/svg/rotate-180--active.svg);
        }
        #rotate-180::indicator:unchecked, #rotate-180::indicator:disabled {
            image: url(resources/svg/rotate-180.svg);
        }
        #rotate-180::indicator:unchecked:hover {
            image: url(resources/svg/rotate-180--hover);
        }
        
        .resolutionBtn::indicator {
            width: 90;
            height: 36;
        }
        
        #resolution-720p::indicator:checked {
            image: url(resources/svg/resolution-720p--active.svg);
        }
        #resolution-720p::indicator:unchecked, #resolution-720p::indicator:disabled {
            image: url(resources/svg/resolution-720p.svg);
        }
        #resolution-720p::indicator:unchecked:hover {
            image: url(resources/svg/resolution-720p--hover.svg);
        }
        
        #resolution-1080p::indicator:checked {
            image: url(resources/svg/resolution-1080p--active.svg);
        }
        #resolution-1080p::indicator:unchecked, #resolution-1080p::indicator:disabled {
            image: url(resources/svg/resolution-1080p.svg);
        }
        #resolution-1080p::indicator:unchecked:hover {
            image: url(resources/svg/resolution-1080p--hover.svg);
        }
        
        #resolution-1440p::indicator:checked {
            image: url(resources/svg/resolution-1440p--active.svg);
        }
        #resolution-1440p::indicator:unchecked, #resolution-1440p::indicator:disabled {
            image: url(resources/svg/resolution-1440p.svg);
        }
        #resolution-1440p::indicator:unchecked:hover {
            image: url(resources/svg/resolution-1440p--hover.svg);
        }
        
        #resolution-4k::indicator:checked {
            image: url(resources/svg/resolution-4k--active.svg);
        }
        #resolution-4k::indicator:unchecked, #resolution-4k::indicator:disabled {
            image: url(resources/svg/resolution-4k.svg);
        }
        #resolution-4k::indicator:unchecked:hover {
            image: url(resources/svg/resolution-4k--hover.svg);
        }
        
        .submitBtn {
            color: #087f57;
            background-color: #63e6be;
            border: 1px solid #087f57;
            border-radius: 3;
        }
        .submitBtn:disabled {
            color: #495057;
            background-color: #868e96;
            border: none;
            border-radius: 3;
        }
        .submitBtn:hover {
            color: #087f57;
            background-color: #38d9a9;
        }
        
        #progressDiv {
            border-radius: 3;
        }
        
        #progressBar {
            color: #087f57;
            text-align: center;
            background-color: #dee2e6;
            border-top-left-radius: 3;
            border-bottom-left-radius: 3;   
        }
        #progressBar:chunk {
            background: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0 #63e6be, stop:1 #96f2d7);
            border-right: 1px solid #087f57;
            border-top-left-radius: 3;
            border-bottom-left-radius: 3;
        }
        
        .progressBtn {
            border-top-right-radius: 3;
            border-bottom-right-radius: 3;
        }
        #abortBtn {
            border-left: 1px solid #a61e4d;
            color: #a61e4d;
            background-color: #f783ac;
        }
        #abortBtn:hover {
            border-left: 1px solid #a61e4d;
            color: #a61e4d;
            background-color: #f06595;
        }
        #continueBtn {
            color: #087f5b;
            background-color: #63e6be;
        }
        #continueBtn:hover {
            color: #087f5b;
            background-color: #38d9a9;
        }
        
    """
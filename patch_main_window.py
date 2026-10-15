import sys
with open("pa_agent/gui/main_window.py", "r") as f:
    content = f.read()

conflict = """<<<<<<< HEAD
            "K 线数据来源：MT5（默认，需终端登录）、"
            "TradingView（tvDatafeed）、东方财富(A股)（HTTP 直连）"
=======
            "K 线数据来源：TradingView（tvDatafeed）、MT5（仅 Windows）、"
            "本地仅支持 MT5 与 TradingView"
>>>>>>> pr18"""

resolution = """            "K 线数据来源：MT5（默认，需终端登录）、"
            "TradingView（tvDatafeed）、东方财富(A股)（HTTP 直连）" """

content = content.replace(conflict, resolution)
with open("pa_agent/gui/main_window.py", "w") as f:
    f.write(content)

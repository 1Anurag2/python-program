import pyqrcode as qrcode
# from pyqrcode import QRCode
# s = import qrcode
s = "https://www.youtube.com/watch?v=ZaC6oCIpjR0" 
icon = qrcode.make(s) 
icon = qrcode.create(s)
icon.svg("first_qrcode.png", scale=10)
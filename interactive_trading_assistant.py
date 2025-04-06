import speech_recognition as sr
import pyttsx3
import tkinter as tk
from datetime import datetime
import MetaTrader5 as mt5

class TradingAssistant:
    def __init__(self):
        self.setup_time = "2025-04-04 20:32:36"
        self.trader = "behicof"
        
        # راه‌اندازی موتور تبدیل متن به گفتار
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        
        # راه‌اندازی تشخیص گفتار
        self.recognizer = sr.Recognizer()
        
        # راه‌اندازی رابط گرافیکی
        self.window = tk.Tk()
        self.window.title("دستیار معاملاتی هوشمند")
        self.setup_gui()
        
        # اتصال به متاتریدر
        self.mt5_connected = mt5.initialize()
        
        # وضعیت فعلی معاملات
        self.current_trades = {}
        self.market_status = {}
        
    def setup_gui(self):
        """راه‌اندازی رابط گرافیکی"""
        # نمایش وضعیت بازار
        self.market_frame = tk.LabelFrame(self.window, text="وضعیت بازار")
        self.market_frame.pack(padx=10, pady=5, fill="x")
        
        # نمایش معاملات فعال
        self.trades_frame = tk.LabelFrame(self.window, text="معاملات فعال")
        self.trades_frame.pack(padx=10, pady=5, fill="x")
        
        # دکمه‌های کنترلی
        self.control_frame = tk.Frame(self.window)
        self.control_frame.pack(padx=10, pady=5)
        
        tk.Button(self.control_frame, text="🎤 شروع گفتگو", 
                 command=self.start_listening).pack(side=tk.LEFT, padx=5)
        
        tk.Button(self.control_frame, text="📊 به‌روزرسانی", 
                 command=self.update_status).pack(side=tk.LEFT, padx=5)
    
    def speak(self, text):
        """تبدیل متن به گفتار"""
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """دریافت دستور صوتی"""
        with sr.Microphone() as source:
            print("در حال گوش دادن...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio, language='fa-IR')
                print(f"User: {text}")
                return text
            except:
                self.speak("متوجه نشدم، لطفا دوباره تکرار کنید")
                return None
    
    def process_command(self, command):
        """پردازش دستورات صوتی"""
        if "وضعیت" in command:
            self.report_status()
        elif "معامله جدید" in command:
            self.analyze_and_trade()
        elif "بستن معامله" in command:
            self.close_trades()
        elif "تحلیل بازار" in command:
            self.market_analysis()
    
    def report_status(self):
        """گزارش وضعیت فعلی"""
        if not self.current_trades:
            self.speak("در حال حاضر معامله فعالی وجود ندارد")
            return
            
        for symbol, trade in self.current_trades.items():
            profit = trade['current_profit']
            self.speak(f"معامله {symbol} با سود {profit} دلار فعال است")
    
    def analyze_and_trade(self):
        """تحلیل و اجرای معامله جدید"""
        self.speak("در حال تحلیل بازار...")
        # اینجا منطق تحلیل و معامله قبلی اجرا می‌شود
        
    def market_analysis(self):
        """تحلیل کلی بازار"""
        self.speak("در حال تحلیل روند بازار...")
        # اجرای تحلیل بازار و اعلام نتایج
    
    def update_status(self):
        """به‌روزرسانی وضعیت در رابط گرافیکی"""
        if self.mt5_connected:
            positions = mt5.positions_get()
            for position in positions:
                symbol = position.symbol
                profit = position.profit
                self.current_trades[symbol] = {
                    'current_profit': profit,
                    'open_price': position.price_open,
                    'current_price': position.price_current
                }
    
    def start_listening(self):
        """شروع گوش دادن به دستورات صوتی"""
        self.speak("سلام، چطور می‌تونم کمکتون کنم؟")
        while True:
            command = self.listen()
            if command:
                self.process_command(command)
    
    def run(self):
        """اجرای اصلی برنامه"""
        self.window.mainloop()

# راه‌اندازی دستیار
assistant = TradingAssistant()
print("دستیار معاملاتی آماده است!")
assistant.run()
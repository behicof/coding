import MetaTrader5 as mt5
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from datetime import datetime
import numpy as np
import pandas as pd
import threading
import queue
import warnings
warnings.filterwarnings('ignore')

class AdvancedTradingAssistant:
    def __init__(self):
        self.setup_time = "2025-04-04 20:35:07"
        self.trader = "behicof"
        self.version = "2.0.0"
        
        # راه‌اندازی سیستم‌های پایه
        self.initialize_systems()
        self.setup_gui()
        self.setup_voice()
        
        # مدیریت داده و تحلیل
        self.market_data = {}
        self.analysis_results = {}
        self.trade_signals = queue.Queue()
        
        # تنظیمات پیشرفته
        self.settings = {
            'trading': {
                'auto_mode': True,
                'risk_level': 'DYNAMIC',
                'position_sizing': 'ADAPTIVE',
                'max_positions': 5,
                'trading_pairs': [
                    'BTCUSD', 'ETHUSD', 'SOLUSD', 
                    'AVAXUSD', 'LINKUSD', 'DOTUSD'
                ]
            },
            'analysis': {
                'timeframes': ['5m', '15m', '1h', '4h', '1d'],
                'indicators': {
                    'trend': ['MA', 'EMA', 'SuperTrend'],
                    'momentum': ['RSI', 'MACD', 'Stochastic'],
                    'volatility': ['BB', 'ATR', 'KC'],
                    'volume': ['OBV', 'MFI', 'ADL']
                },
                'ml_models': ['XGBoost', 'LSTM', 'RandomForest']
            },
            'risk': {
                'position_risk': 'VARIABLE',
                'account_risk': 'DYNAMIC',
                'drawdown_protection': True,
                'smart_recovery': True
            }
        }
        
        # شروع سیستم‌های اصلی
        self.start_background_tasks()
    
    def initialize_systems(self):
        """راه‌اندازی سیستم‌های اصلی"""
        # اتصال به متاتریدر
        if not mt5.initialize():
            raise Exception("خطا در اتصال به متاتریدر")
            
        # راه‌اندازی پایگاه داده
        self.db = pd.DataFrame()
        
        # راه‌اندازی موتور تحلیل
        self.analysis_engine = self.setup_analysis_engine()
    
    def setup_voice(self):
        """راه‌اندازی سیستم صوتی پیشرفته"""
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.recognizer = sr.Recognizer()
        
        # تعریف دستورات صوتی پیشرفته
        self.voice_commands = {
            'status': self.report_full_status,
            'analyze': self.deep_market_analysis,
            'trade': self.smart_trade_execution,
            'optimize': self.optimize_portfolio,
            'risk': self.adjust_risk_parameters,
            'close': self.smart_position_closure
        }
    
    def setup_analysis_engine(self):
        """راه‌اندازی موتور تحلیل پیشرفته"""
        return {
            'technical': self.technical_analysis,
            'fundamental': self.fundamental_analysis,
            'sentiment': self.sentiment_analysis,
            'ml': self.ml_prediction
        }
    
    def process_market_data(self):
        """پردازش داده‌های بازار"""
        while True:
            for symbol in self.settings['trading']['trading_pairs']:
                for timeframe in self.settings['analysis']['timeframes']:
                    data = self.fetch_market_data(symbol, timeframe)
                    self.market_data[(symbol, timeframe)] = data
                    
                    # تحلیل خودکار
                    analysis = self.analyze_data(data)
                    self.analysis_results[(symbol, timeframe)] = analysis
                    
                    # بررسی سیگنال‌ها
                    if self.check_signals(analysis):
                        self.trade_signals.put((symbol, analysis))
    
    def smart_trade_execution(self):
        """اجرای هوشمند معاملات"""
        while True:
            if not self.trade_signals.empty():
                symbol, analysis = self.trade_signals.get()
                
                # محاسبه پارامترهای معامله
                entry, sl, tp = self.calculate_trade_parameters(symbol, analysis)
                size = self.calculate_position_size(symbol, entry, sl)
                
                # اجرای معامله
                if self.validate_trade(symbol, entry, sl, tp, size):
                    self.execute_trade(symbol, entry, sl, tp, size)
                    self.speak(f"معامله جدید در {symbol} اجرا شد")
    
    def portfolio_optimization(self):
        """بهینه‌سازی پورتفولیو"""
        positions = mt5.positions_get()
        
        for position in positions:
            # تحلیل عملکرد
            performance = self.analyze_position_performance(position)
            
            # بهینه‌سازی پارامترها
            if performance['needs_adjustment']:
                self.optimize_position(position)
    
    def risk_management(self):
        """مدیریت ریسک پیشرفته"""
        while True:
            account = mt5.account_info()
            
            # بررسی سلامت حساب
            health = self.check_account_health(account)
            
            if health['warning']:
                self.speak(f"هشدار: {health['message']}")
                self.adjust_risk_parameters(health)
    
    def start_background_tasks(self):
        """شروع تسک‌های پس‌زمینه"""
        tasks = [
            self.process_market_data,
            self.smart_trade_execution,
            self.portfolio_optimization,
            self.risk_management
        ]
        
        for task in tasks:
            thread = threading.Thread(target=task, daemon=True)
            thread.start()
    
    def run(self):
        """اجرای اصلی برنامه"""
        self.speak("سیستم معاملاتی هوشمند فعال شد")
        self.window.mainloop()

# راه‌اندازی سیستم
system = AdvancedTradingAssistant()
system.run()
class MetaTraderSetup:
    def __init__(self):
        self.setup_time = "2025-04-04 20:22:43"
        self.trader = "behicof"
        self.platform = "MetaTrader"
        
        # گزینه‌های اتصال به متاتریدر
        self.connection_options = {
            'ea_based': {
                'title': 'اتصال از طریق EA',
                'description': 'استفاده از Expert Advisor برای کنترل معاملات',
                'requirements': [
                    'ایجاد یک EA ساده برای دریافت سیگنال‌ها',
                    'تنظیم پارامترهای ورودی در EA',
                    'فعال‌سازی AutoTrading',
                    'تنظیم مجوزهای لازم'
                ]
            },
            'api_based': {
                'title': 'اتصال از طریق API',
                'description': 'استفاده از MetaTrader WebAPI یا کتابخانه‌های مرتبط',
                'requirements': [
                    'نصب و راه‌اندازی WebAPI',
                    'تنظیم پورت‌های ارتباطی',
                    'مدیریت اتصال و دسترسی‌ها',
                    'پیاده‌سازی توابع معاملاتی'
                ]
            }
        }
        
        # تنظیمات پیشنهادی EA
        self.ea_settings = {
            'trade_settings': {
                'MaxPositions': 3,
                'MaxLotSize': 2.0,
                'UseStopLoss': True,
                'StopLossPoints': 100,
                'UseTakeProfit': True,
                'TakeProfitPoints': 200,
                'UseTrailingStop': True,
                'TrailingPoints': 50
            },
            'risk_settings': {
                'MaxRiskPerTrade': 2,  # درصد
                'MaxDailyLoss': 5,     # درصد
                'MaxSpread': 3,        # پیپ
                'MinVolume': 0.01,     # لات
                'MaxVolume': 2.0       # لات
            }
        }

# ایجاد راهنما
setup = MetaTraderSetup()

print(f"\n🔧 راه‌اندازی {setup.platform} - {setup.setup_time}")
print(f"معامله‌گر: {setup.trader}")

print("\n=== روش‌های اتصال به متاتریدر ===")
for method_id, method in setup.connection_options.items():
    print(f"\n{method['title']}:")
    print(f"توضیحات: {method['description']}")
    print("\nنیازمندی‌ها:")
    for req in method['requirements']:
        print(f"• {req}")

print("\n⚙️ تنظیمات پیشنهادی EA:")
settings = setup.ea_settings

print("\nتنظیمات معاملاتی:")
for key, value in settings['trade_settings'].items():
    print(f"• {key}: {value}")

print("\nتنظیمات ریسک:")
for key, value in settings['risk_settings'].items():
    print(f"• {key}: {value}")

# مراحل راه‌اندازی
setup_steps = [
    "1. نصب متاتریدر و اطمینان از عملکرد صحیح",
    "2. باز کردن حساب دمو یا اتصال حساب واقعی",
    "3. نصب EA مورد نظر در پوشه Experts",
    "4. فعال‌سازی AutoTrading در متاتریدر",
    "5. تنظیم پارامترهای EA",
    "6. تست اولیه با حجم کوچک"
]

print("\n📝 مراحل راه‌اندازی:")
for step in setup_steps:
    print(f"• {step}")

# نکات مهم
important_notes = [
    "اطمینان از فعال بودن AlgoTrading در متاتریدر",
    "بررسی تنظیمات امنیتی و مجوزها",
    "تست کامل در حساب دمو قبل از حساب واقعی",
    "شروع با حجم کم و افزایش تدریجی",
    "بررسی مداوم عملکرد و لاگ‌های سیستم"
]

print("\n⚠️ نکات مهم:")
for note in important_notes:
    print(f"• {note}")
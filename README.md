# آپلودر فایل جنگو

<p align="center">
  <img src="https://raw.githubusercontent.com/django/django/main/django/contrib/admin/static/admin/img/icon-yes.svg" alt="Django File Uploader" width="100" />
</p>

یک سیستم آپلود و مدیریت فایل ساده و کاربردی با استفاده از فریم‌ورک جنگو

## ویژگی‌ها

- **رابط کاربری زیبا** با Tailwind CSS
- **آپلود فایل با کشیدن و رها کردن**
- **نمایش زنده پیشرفت آپلود** با نمایش زمان باقی‌مانده و سرعت آپلود
- **کپی لینک دانلود** با یک کلیک
- **مدیریت آسان فایل‌ها** (مشاهده، دانلود، حذف)
- **پشتیبانی کامل از زبان فارسی** با فونت وزیر
- **طراحی واکنش‌گرا** برای تمام دستگاه‌ها (موبایل، تبلت، دسکتاپ)
- **نمایش نوع فایل** با آیکون‌های مختلف

## نصب و راه‌اندازی

### پیش‌نیازها

- Python 3.8 یا بالاتر
- Pip (مدیریت پکیج‌های پایتون)

### مراحل نصب

1. **کلون کردن مخزن**
   ```
   git clone https://your-repository-url.git
   cd django_uploader
   ```

2. **ساخت محیط مجازی**
   ```
   python -m venv env
   ```

3. **فعال‌سازی محیط مجازی**
   - در ویندوز:
     ```
     env\Scripts\activate
     ```
   - در لینوکس/مک:
     ```
     source env/bin/activate
     ```

4. **نصب وابستگی‌ها**
   ```
   pip install -r requirements.txt
   ```

5. **اجرای مهاجرت‌های دیتابیس**
   ```
   python manage.py migrate
   ```

6. **ایجاد کاربر مدیر (اختیاری)**
   ```
   python manage.py createsuperuser
   ```

7. **اجرای سرور توسعه**
   ```
   python manage.py runserver
   ```

8. **مشاهده برنامه** در مرورگر:
   - آدرس: http://127.0.0.1:8000/

## ساختار پروژه

```
django_uploader/
│
├── core/                   # اپلیکیشن اصلی
│   ├── migrations/         # فایل‌های مهاجرت دیتابیس
│   ├── templates/          # قالب‌های HTML
│   │   └── core/           # قالب‌های مختص اپلیکیشن
│   │       ├── base.html   # قالب پایه
│   │       ├── home.html   # صفحه اصلی
│   │       └── ...         # سایر قالب‌ها
│   ├── admin.py            # تنظیمات پنل مدیریت
│   ├── models.py           # مدل‌های دیتابیس
│   ├── views.py            # ویوها
│   ├── forms.py            # فرم‌ها
│   └── urls.py             # مسیریابی URL
│
├── uploader/               # پروژه اصلی جنگو
│   ├── settings.py         # تنظیمات پروژه
│   ├── urls.py             # مسیریابی URL اصلی
│   └── ...                 # سایر فایل‌های پروژه
│
├── media/                  # فایل‌های آپلود شده (در زمان اجرا ایجاد می‌شود)
├── staticfiles/            # فایل‌های استاتیک جمع‌آوری شده
├── manage.py               # اسکریپت مدیریت جنگو
├── requirements.txt        # وابستگی‌های پروژه
└── README.md               # این فایل
```

## نحوه استفاده

### آپلود فایل
1. روی دکمه "آپلود فایل" کلیک کنید
2. عنوان و توضیحات دلخواه را وارد کنید
3. فایل خود را انتخاب کنید یا آن را به محل مشخص شده بکشید و رها کنید
4. روی دکمه "آپلود" کلیک کنید
5. پیشرفت آپلود را به صورت زنده مشاهده کنید

### مدیریت فایل‌ها
- **مشاهده فایل**: روی آیکون چشم کلیک کنید
- **دانلود فایل**: روی آیکون دانلود کلیک کنید
- **کپی لینک دانلود**: روی آیکون کپی کلیک کنید
- **حذف فایل**: روی آیکون سطل زباله کلیک کنید و تأیید کنید

## تنظیمات پیشرفته

### تغییر مسیر ذخیره فایل‌ها
در فایل `settings.py` می‌توانید مسیر ذخیره فایل‌ها را تغییر دهید:

```python
MEDIA_ROOT = BASE_DIR / 'your_custom_path'
```

### محدودیت حجم فایل
برای تنظیم محدودیت حجم فایل‌های آپلودی، در فایل `settings.py` کد زیر را اضافه کنید:

```python
# حداکثر حجم فایل (به بایت) - مثال: 50 مگابایت
MAX_UPLOAD_SIZE = 50 * 1024 * 1024
```


<p align="center">
  با ❤️ در ایران توسعه یافته است
</p> 

"""Persian fallbacks for the portfolio's existing database content.

Admin-entered Persian text always wins. These mappings keep imported fixtures and
older rows translated even when they were created after the original data migration.
"""

PROJECT_TRANSLATIONS = {
    'Khurmarket': {
        'title_fa': 'خورمارکت',
        'status_fa': 'تست و رفع اشکال',
        'cilend_or_role_fa': 'فریلنسری',
        'description_fa': (
            'خورمارکت یک بازار آنلاین محلی و جامع است که از پایه برای تغییر شیوه خرید و فروش مردم در شهر خور ساخته شده است.\n\n'
            'این پروژه فقط محصولات را آنلاین نمی‌کند؛ بلکه یک اکوسیستم دیجیتال کامل برای تجارت محلی می‌سازد و مردم، کسب‌وکارها و فرصت‌ها را در یک پلتفرم یکپارچه به هم متصل می‌کند.\n\n'
            'معماری و تجربه کاربری خورمارکت با هدف تبدیل یک نیاز واقعی محلی به محصولی مدرن، مقیاس‌پذیر و قابل اتکا طراحی شده است.'
        ),
    },
    'Digital Menu': {
        'title_fa': 'منوی دیجیتال',
        'status_fa': 'نسخه دمو',
        'cilend_or_role_fa': 'فریلنسری',
        'description_fa': (
            'یک منوی دیجیتال مدرن که تجربه سنتی رستوران را به تجربه‌ای سریع، تعاملی و کاملاً دیجیتال تبدیل می‌کند.\n\n'
            'این پروژه بستری اختصاصی در اختیار رستوران‌ها و کافه‌ها قرار می‌دهد تا منوی خود را تمیز و جذاب نمایش دهند و مشتریان نیز بتوانند آیتم‌های موجود را ساده و روان بررسی کنند.\n\n'
            'تمرکز اصلی سیستم بر استفاده واقعی است؛ رابطی مدرن در کنار ساختار مدیریتی قدرتمند که راهکاری کاربردی برای کافه‌ها و رستوران‌های امروزی ایجاد می‌کند.'
        ),
    },
    'Monopoly Wallet': {
        'title_fa': 'کیف پول مونوپولی',
        'status_fa': 'تکمیل‌شده',
        'cilend_or_role_fa': 'فریلنسری',
        'description_fa': (
            'کیف پول مونوپولی یک سیستم ساده کیف پول دیجیتال است که برای جایگزینی پول نقد در بازی مونوپولی طراحی شده است.\n\n'
            'این پروژه ابزاری کاربردی برای بازی واقعی است و به بازیکنان اجازه می‌دهد موجودی خود را مدیریت کنند و مستقیماً با تلفن همراه برای یکدیگر پول انتقال دهند. تمرکز اصلی آن بر سادگی و کارایی است تا تمام ابزارهای ضروری مدیریت امور مالی بازی بدون نیاز به پول فیزیکی فراهم باشد.'
        ),
    },
    'TradeJournal Back-end': {
        'title_fa': 'بک‌اند ترید ژورنال',
        'status_fa': 'در حال توسعه بک‌اند',
        'cilend_or_role_fa': 'توسعه‌دهنده بک‌اند',
        'description_fa': (
            'MDF یک پلتفرم مدیریت و تحلیل معاملات مبتنی بر بک‌اند است که به متاتریدر متصل می‌شود و محیطی متمرکز برای مدیریت و تحلیل فعالیت‌های معاملاتی در اختیار کاربران قرار می‌دهد.\n\n'
            'این پلتفرم داده‌های معاملاتی متاتریدر را پردازش می‌کند و آن‌ها را به اطلاعات ساختاریافته، گزارش‌های دقیق و بینش‌های معنادار عملکردی تبدیل می‌کند. سامانه با معماری مقیاس‌پذیر و یک لایه API اختصاصی ساخته شده و به فرانت‌اند مستقل React سرویس می‌دهد.\n\n'
            'در نقش توسعه‌دهنده بک‌اند، مسئول طراحی و توسعه معماری اصلی بک‌اند، APIها، سیستم احراز هویت، ابزارهای مدیریتی و اتصال‌های موردنیاز پلتفرم بوده‌ام.'
        ),
    },
}

FEATURE_TRANSLATIONS = {
    'Full Marketplace System': 'سیستم کامل بازار آنلاین',
    'User & Seller Accounts': 'حساب‌های کاربری و فروشندگی',
    'Product Search & Filtering': 'جست‌وجو و فیلتر محصولات',
    'Shopping Cart & Order Management': 'سبد خرید و مدیریت سفارش‌ها',
    'Digital Wallet & Transactions': 'کیف پول دیجیتال و تراکنش‌ها',
    'Seller & Inventory Management': 'مدیریت فروشندگان و موجودی',
    'Order Notifications': 'اعلان‌های سفارش',
    'Role-Based Access & Security': 'دسترسی نقش‌محور و امنیت',
    'Advanced Admin Panel': 'پنل مدیریت پیشرفته',
    'Sales & Order Management': 'مدیریت فروش و سفارش‌ها',
    'Digital Menu': 'منوی دیجیتال',
    'QR Code Access': 'دسترسی با کد QR',
    'Category Management': 'مدیریت دسته‌بندی‌ها',
    'Menu Item Management': 'مدیریت آیتم‌های منو',
    'Item Details & Pricing': 'جزئیات و قیمت‌گذاری آیتم‌ها',
    'Image Management': 'مدیریت تصاویر',
    'Restaurant/Café Profiles': 'پروفایل رستوران‌ها و کافه‌ها',
    'Responsive Design': 'طراحی واکنش‌گرا',
    'Admin Dashboard': 'داشبورد مدیریت',
    'Menu Availability Control': 'کنترل موجودی منو',
    'Real-Time Menu Updates': 'به‌روزرسانی لحظه‌ای منو',
    'MetaTrader Integration': 'اتصال به متاتریدر',
    'Trading Account Management': 'مدیریت حساب‌های معاملاتی',
    'AI think': 'تحلیل هوش مصنوعی',
    'Trade & Position Tracking': 'رهگیری معاملات و موقعیت‌ها',
    'Detailed Trading Reports': 'گزارش‌های دقیق معاملاتی',
    'Performance Analytics': 'تحلیل عملکرد',
    'Player Balance Display': 'نمایش موجودی بازیکن',
    'Money Transfers Between Players': 'انتقال پول بین بازیکنان',
    'Admin Panel': 'پنل مدیریت',
    'Player Management': 'مدیریت بازیکنان',
    'Balance Management': 'مدیریت موجودی',
    'Transaction Management': 'مدیریت تراکنش‌ها',
    'Digital Wallet System': 'سیستم کیف پول دیجیتال',
    'Advanced Dashboard': 'داشبورد پیشرفته',
    'Trade Search, Filtering & Sorting': 'جست‌وجو، فیلتر و مرتب‌سازی معاملات',
    'Historical Trading Data': 'داده‌های تاریخی معاملات',
    'Authentication & Authorization': 'احراز هویت و سطح دسترسی',
    'User Management': 'مدیریت کاربران',
    'Payment Management': 'مدیریت پرداخت‌ها',
    'Subscription Plan Management': 'مدیریت پلن‌های اشتراک',
    'AI API Integration': 'اتصال API هوش مصنوعی',
    'System Logs & Monitoring': 'لاگ‌ها و پایش سیستم',
    'React Frontend API Integration': 'اتصال API به فرانت‌اند React',
}

IMAGE_TRANSLATIONS = {
    'Login Page': 'صفحه ورود',
    'Login page': 'صفحه ورود',
    'Wallet User Page': 'صفحه کیف پول کاربر',
    'Admin Wallet Page': 'صفحه مدیریت کیف پول',
}

CATEGORY_TRANSLATIONS = {
    'Web App': 'اپلیکیشن وب',
    'Backend': 'بک‌اند',
    'Full Stack': 'فول‌استک',
    'E-commerce': 'فروشگاه اینترنتی',
    'Fintech': 'فین‌تک',
}

TECH_TRANSLATIONS = {
    'Python': 'پایتون',
    'HTML': 'HTML',
    'JavaScript': 'جاوااسکریپت',
    'Tailwind CSS': 'تیلویند CSS',
    'Django': 'جنگو',
    'SQL': 'SQL',
    'REST API': 'REST API',
    'GitHub': 'گیت‌هاب',
}

COMMON_TEXT_TRANSLATIONS = {
    'test': 'تست',
    'Done': 'تکمیل‌شده',
    'Complete': 'تکمیل‌شده',
    'Finished': 'تکمیل‌شده',
    'In progress': 'در حال توسعه',
    'Demo': 'نسخه دمو',
    'QA and debugging': 'تست و رفع اشکال',
    'Writing Backend': 'در حال توسعه بک‌اند',
    'freelance': 'فریلنسری',
    'Freelance': 'فریلنسری',
    'Backend Developer': 'توسعه‌دهنده بک‌اند',
}


def translated_value(explicit_value, source_value, translations):
    """Prefer curated admin text, then a known fallback, then the source text."""
    return explicit_value or translations.get(source_value, source_value or '')

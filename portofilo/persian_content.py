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
    'Liora Cafe': {
        'title_fa': 'کافه لیورا',
        'status_fa': 'فعال',
        'cilend_or_role_fa': 'توسعه‌دهنده فول‌استک',
        'description_fa': (
            'یک منوی دیجیتال مدرن که تجربه سنتی رستوران را به تجربه‌ای سریع، تعاملی و کاملاً دیجیتال تبدیل می‌کند.\n\n'
            'این پروژه بستری اختصاصی در اختیار رستوران‌ها و کافه‌ها قرار می‌دهد تا منوی خود را تمیز و جذاب نمایش دهند و مشتریان نیز بتوانند آیتم‌های موجود را ساده و روان بررسی کنند.\n\n'
            'تمرکز اصلی سیستم بر استفاده واقعی است؛ رابطی مدرن در کنار ساختار مدیریتی قدرتمند که راهکاری کاربردی برای کافه‌ها و رستوران‌های امروزی ایجاد می‌کند.'
        ),
    },
    'Cafe Gavazn': {
        'title_fa': 'کافه گوزن',
        'status_fa': 'در آستانه شروع',
        'cilend_or_role_fa': 'توسعه‌دهنده فول‌استک',
        'description_fa': 'به‌زودی',
    },
    'Personal AI Assistant': {
        'title_fa': 'دستیار هوش مصنوعی شخصی',
        'status_fa': 'فعال',
        'description_fa': (
            'یک دستیار تلگرامی مبتنی بر هوش مصنوعی که به‌عنوان نماینده حرفه‌ای من فعالیت می‌کند. این دستیار با اتصال به Google Gemini به پرسش‌های بازدیدکنندگان درباره مهارت‌ها، پروژه‌ها و خدمات من پاسخ می‌دهد.\n\n'
            'بات تشخیص می‌دهد کاربر مشتری است یا توسعه‌دهنده و لحن پاسخ را متناسب با او تنظیم می‌کند. اگر کاربر درخواست قیمت، پیشنهاد پروژه یا اطلاعات تماس ارسال کند، بات آن را فوراً به‌عنوان یک سرنخ کاری به من اطلاع می‌دهد. این سیستم همچنین به دکمه خرید پروژه در سایت متصل است و درخواست‌های خرید را مستقیم به تلگرام من می‌فرستد.\n\n'
            'معماری پروژه تمیز و ماژولار است و منطق پاسخ‌گویی را از پایگاه دانش جدا می‌کند. تمام ارتباط‌ها با API تلگرام و Gemini نیز از طریق Cloudflare Workers انجام می‌شوند.'
        ),
    },
    'Barber shop booking': {
        'title_fa': 'سامانه نوبت‌دهی آرایشگاه',
        'status_fa': 'در حال توسعه',
        'cilend_or_role_fa': 'توسعه‌دهنده فول‌استک',
        'description_fa': (
            'یک سامانه کامل و موبایل‌محور برای مدیریت نوبت‌های آرایشگاه که تماس‌ها، پیام‌ها، تداخل زمان‌ها و نوبت‌های فراموش‌شده را به یک جریان ساده و منظم تبدیل می‌کند.\n\n'
            'مشتری بدون ساخت حساب می‌تواند در کمتر از چند ثانیه روز و ساعت آزاد را انتخاب کند، نوبت‌های خود را ببیند و در صورت نیاز آن‌ها را لغو کند. زمان‌های رزروشده به‌صورت لحظه‌ای غیرفعال می‌شوند و یادآوری‌های خودکار احتمال فراموش‌شدن نوبت را کاهش می‌دهند.\n\n'
            'آرایشگر نیز از طریق یک پنل مدیریتی متمرکز، برنامه روزانه و هفتگی را بررسی می‌کند، وضعیت نوبت‌ها را تغییر می‌دهد، تأخیرها را به مشتریان اطلاع می‌دهد و کاربران مسئله‌دار را موقتاً مسدود می‌کند. پاک‌سازی سوابق قدیمی، لغو خودکار نوبت‌های از‌دست‌رفته و اعلان‌های زمان‌بندی‌شده در پس‌زمینه انجام می‌شوند.\n\n'
            'رابط فارسی راست‌به‌چپ، تقویم و اعداد محلی، طراحی واکنش‌گرا و بازخوردهای بصری سریع باعث شده‌اند تجربه استفاده از سیستم روان و قابل پیش‌بینی باشد. این پروژه با Django و Tailwind برای استفاده واقعی در یک آرایشگاه طراحی شده است.'
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
    'Revenue Management': 'مدیریت درآمد',
    '42 automated tests': '۴۲ تست خودکار',
    'AJAX / no refresh': 'AJAX بدون بارگذاری مجدد',
    'Auto calls': 'تماس‌های خودکار',
    'Auto-cancel overdue': 'لغو خودکار نوبت‌های معوق',
    'Auto-cleanup old records': 'پاک‌سازی خودکار سوابق قدیمی',
    'Background scheduler': 'زمان‌بندی پردازش‌های پس‌زمینه',
    'Customer blocking': 'مسدودسازی مشتری',
    'Custom admin panel': 'پنل مدیریت اختصاصی',
    'Custom animations': 'انیمیشن‌های اختصاصی',
    'Date filtering': 'فیلتر بر اساس تاریخ',
    'Delay notifications': 'اعلان تأخیر',
    'Double-booking prevention': 'جلوگیری از رزرو هم‌زمان',
    'Guest checkout': 'رزرو بدون حساب کاربری',
    'Live availability': 'نمایش لحظه‌ای زمان‌های آزاد',
    'Mobile-first design': 'طراحی موبایل‌محور',
    'Notification pluggable': 'سیستم اعلان قابل توسعه',
    'One-tap cancel': 'لغو با یک لمس',
    'One-tap complete': 'تکمیل با یک لمس',
    'Online booking': 'نوبت‌دهی آنلاین',
    'Optimized queries': 'کوئری‌های بهینه',
    'Pagination': 'صفحه‌بندی',
    'Persian RTL UI': 'رابط فارسی راست‌به‌چپ',
    'Race-condition safe': 'ایمن در برابر تداخل هم‌زمان',
    'Self-service cancel': 'لغو نوبت توسط مشتری',
    'Settings-driven config': 'پیکربندی از طریق تنظیمات',
    'Shared base template': 'قالب پایه مشترک',
    'SMS reminders': 'یادآوری پیامکی',
    'Stackable delays': 'ثبت تأخیرهای متوالی',
    'Status filtering': 'فیلتر بر اساس وضعیت',
    'Adaptive Response Tone': 'لحن پاسخ‌گویی تطبیقی',
    'Buy Request Handling': 'مدیریت درخواست خرید',
    'Cloudflare Workers Relay': 'ارتباط از طریق Cloudflare Workers',
    'Conversation Memory': 'حافظه مکالمه',
    'Gemini AI Integration': 'اتصال به هوش مصنوعی Gemini',
    'Lead Detection': 'تشخیص سرنخ کاری',
}

IMAGE_TRANSLATIONS = {
    'Login Page': 'صفحه ورود',
    'Login page': 'صفحه ورود',
    'Wallet User Page': 'صفحه کیف پول کاربر',
    'Admin Wallet Page': 'صفحه مدیریت کیف پول',
    'Account Page without login': 'صفحه حساب بدون ورود',
    'Add work clock': 'افزودن ساعت کاری',
    'Cart': 'سبد خرید',
    'Checkout': 'تسویه‌حساب',
    'Checkout2': 'تسویه‌حساب ۲',
    'Edit Information': 'ویرایش اطلاعات',
    'Login': 'ورود',
    'Management Panel': 'پنل مدیریت',
    'Management Panel - Product': 'مدیریت محصول',
    'Message': 'پیام‌ها',
    'My cards': 'کارت‌های من',
    'My Products': 'محصولات من',
    'Orders': 'سفارش‌ها',
    'Product Details': 'جزئیات محصول',
    'Product Details2': 'جزئیات محصول ۲',
    'Product Details - Report': 'گزارش جزئیات محصول',
    'SignUp': 'ثبت‌نام',
    'Verify phone': 'تأیید شماره تلفن',
    'Admin': 'پنل مدیریت',
    'Admin2': 'پنل مدیریت ۲',
    'Admin Category': 'مدیریت دسته‌بندی‌ها',
    'Admin Menu': 'مدیریت منو',
    'Admin News': 'مدیریت اخبار',
    'Admin Order': 'مدیریت سفارش‌ها',
    'Admin Table': 'مدیریت میزها',
    'Home': 'صفحه اصلی',
    'Menu': 'منو',
    'Admin_list': 'فهرست مدیریت',
    'Blocked-user screen': 'صفحه کاربر مسدودشده',
    'My bookings': 'نوبت‌های من',
    'Take_ticket': 'دریافت نوبت',
    'Notification': 'اعلان',
    'Speak': 'گفت‌وگو',
}

CATEGORY_TRANSLATIONS = {
    'Web App': 'اپلیکیشن وب',
    'Backend': 'بک‌اند',
    'Full Stack': 'فول‌استک',
    'E-commerce': 'فروشگاه اینترنتی',
    'Fintech': 'فین‌تک',
    'Bots': 'بات‌ها',
    'Client Work': 'پروژه مشتری',
    'Contract': 'قراردادی',
    'For Sale': 'آماده فروش',
    'Personal': 'شخصی',
    'REST API': 'رابط برنامه‌نویسی REST',
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
    'DevOps': 'دواپس',
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
    'Full-Stack Developer': 'توسعه‌دهنده فول‌استک',
    'Full Stack Developer': 'توسعه‌دهنده فول‌استک',
    'Live': 'فعال',
    'Coming soon': 'به‌زودی',
    'Coming to start': 'در آستانه شروع',
    'Writing': 'در حال توسعه',
}


def translated_value(explicit_value, source_value, translations):
    """Prefer curated admin text, then a known fallback, then the source text."""
    return explicit_value or translations.get(source_value, source_value or '')

from django.db import migrations, models


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


def populate_persian_content(apps, schema_editor):
    Project = apps.get_model('projects', 'Project')
    ProjectFeature = apps.get_model('projects', 'ProjectFeature')
    ProjectImage = apps.get_model('projects', 'ProjectImage')
    Category = apps.get_model('projects', 'Category')

    for project in Project.objects.all():
        translated = PROJECT_TRANSLATIONS.get(project.title)
        if translated:
            for field, value in translated.items():
                setattr(project, field, value)
            project.save(update_fields=list(translated))

    for feature in ProjectFeature.objects.all():
        translated = FEATURE_TRANSLATIONS.get(feature.feature)
        if translated:
            feature.feature_fa = translated
            feature.save(update_fields=['feature_fa'])

    for image in ProjectImage.objects.exclude(image_name__isnull=True):
        translated = IMAGE_TRANSLATIONS.get(image.image_name)
        if translated:
            image.image_name_fa = translated
            image.save(update_fields=['image_name_fa'])

    for category in Category.objects.all():
        translated = CATEGORY_TRANSLATIONS.get(category.name)
        if translated:
            category.name_fa = translated
            category.save(update_fields=['name_fa'])


class Migration(migrations.Migration):
    dependencies = [
        ('projects', '0008_projectimage_number_sort'),
        ('tech_stack', '0002_techstack_title_fa'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_fa',
            field=models.CharField(blank=True, max_length=100, verbose_name='نام فارسی'),
        ),
        migrations.AddField(
            model_name='project',
            name='title_fa',
            field=models.CharField(blank=True, max_length=100, verbose_name='عنوان فارسی'),
        ),
        migrations.AddField(
            model_name='project',
            name='status_fa',
            field=models.CharField(blank=True, max_length=100, verbose_name='وضعیت فارسی'),
        ),
        migrations.AddField(
            model_name='project',
            name='description_fa',
            field=models.TextField(blank=True, verbose_name='توضیحات فارسی'),
        ),
        migrations.AddField(
            model_name='project',
            name='cilend_or_role_fa',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='نقش یا کارفرما به فارسی'),
        ),
        migrations.AddField(
            model_name='projectfeature',
            name='feature_fa',
            field=models.TextField(blank=True, verbose_name='ویژگی به فارسی'),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='image_name_fa',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='نام فارسی تصویر'),
        ),
        migrations.RunPython(populate_persian_content, migrations.RunPython.noop),
    ]

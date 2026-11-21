(() => {
    const storageKey = 'portfolio-language';
    const persianDigits = '۰۱۲۳۴۵۶۷۸۹';

    function readLanguage() {
        try {
            return sessionStorage.getItem(storageKey) === 'fa' ? 'fa' : 'en';
        } catch (error) {
            return 'en';
        }
    }

    function storeLanguage(language) {
        try {
            sessionStorage.setItem(storageKey, language);
        } catch (error) {
            // The current page can still switch even if storage is blocked.
        }
    }

    function localizeDigits(value, language) {
        if (language !== 'fa') return value;
        return String(value).replace(/\d/g, (digit) => persianDigits[Number(digit)]);
    }

    function translatedValue(element, language) {
        const value = element.getAttribute(`data-${language}`);
        return value === null ? null : localizeDigits(value, language);
    }

    function formatDate(element, language) {
        const rawDate = element.dataset.date;
        if (!rawDate) return;
        const date = new Date(`${rawDate}T00:00:00`);
        if (Number.isNaN(date.getTime())) return;

        const locale = language === 'fa' ? 'fa-IR' : 'en-US';
        element.textContent = new Intl.DateTimeFormat(locale, {
            year: 'numeric',
            month: 'short',
        }).format(date);
    }

    function applyLanguage(language, announce = true) {
        const isPersian = language === 'fa';
        document.documentElement.lang = language;
        document.documentElement.dir = isPersian ? 'rtl' : 'ltr';
        document.documentElement.dataset.language = language;

        document.querySelectorAll('[data-en][data-fa]').forEach((element) => {
            const value = translatedValue(element, language);
            if (value !== null) element.textContent = value;
            element.dir = isPersian ? 'auto' : 'ltr';
        });

        document.querySelectorAll('[data-en-html][data-fa-html]').forEach((element) => {
            const value = element.getAttribute(`data-${language}-html`);
            if (value !== null) element.innerHTML = localizeDigits(value, language);
        });

        document.querySelectorAll('[data-en-text][data-fa-text]').forEach((element) => {
            const value = localizeDigits(element.getAttribute(`data-${language}-text`) || '', language);
            element.dataset.text = value;
            if (element.textContent) element.textContent = value;
        });

        document.querySelectorAll('[data-en-aria][data-fa-aria]').forEach((element) => {
            const value = element.getAttribute(`data-${language}-aria`);
            if (value !== null) element.setAttribute('aria-label', value);
        });

        document.querySelectorAll('[data-en-content][data-fa-content]').forEach((element) => {
            const value = element.getAttribute(`data-${language}-content`);
            if (value !== null) element.setAttribute('content', value);
        });

        document.querySelectorAll('[data-caption-en][data-caption-fa]').forEach((element) => {
            element.dataset.lightboxCaption = localizeDigits(
                element.getAttribute(`data-caption-${language}`) || '',
                language,
            );
        });

        document.querySelectorAll('[data-alt-en][data-alt-fa]').forEach((element) => {
            element.alt = element.getAttribute(`data-alt-${language}`) || '';
        });

        document.querySelectorAll('[data-date]').forEach((element) => formatDate(element, language));

        const page = document.querySelector('[data-page-title-en][data-page-title-fa]');
        if (page) {
            document.title = page.getAttribute(`data-page-title-${language}`) || document.title;
        }

        const toggle = document.getElementById('language-toggle');
        const toggleLabel = document.querySelector('[data-language-toggle-label]');
        if (toggleLabel) {
            toggleLabel.textContent = isPersian ? 'Switch to English' : 'تغییر زبان به فارسی';
        }
        if (toggle) {
            toggle.setAttribute(
                'aria-label',
                isPersian ? 'Switch language to English' : 'تغییر زبان سایت به فارسی',
            );
        }

        if (announce) {
            document.dispatchEvent(new CustomEvent('portfolio:languagechange', {
                detail: { language },
            }));
        }
    }

    document.addEventListener('DOMContentLoaded', () => {
        let currentLanguage = readLanguage();
        applyLanguage(currentLanguage);

        const toggle = document.getElementById('language-toggle');
        if (!toggle) return;

        toggle.addEventListener('click', () => {
            currentLanguage = document.documentElement.dataset.language === 'fa' ? 'en' : 'fa';
            storeLanguage(currentLanguage);
            applyLanguage(currentLanguage);
        });
    });
})();

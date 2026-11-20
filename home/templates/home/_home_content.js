document.documentElement.classList.add('has-home-motion');

document.addEventListener('DOMContentLoaded', () => {
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const revealItems = document.querySelectorAll('.portfolio-v2 .reveal-item');
    const stackPanel = document.querySelector('.portfolio-v2 .stack-panel');

    function renderCurrentYear(language = document.documentElement.dataset.language || 'en') {
        const locale = language === 'fa' ? 'fa-IR' : 'en-US';
        const year = new Intl.NumberFormat(locale, { useGrouping: false }).format(new Date().getFullYear());
        document.querySelectorAll('[data-current-year]').forEach((element) => {
            element.textContent = year;
        });
    }

    renderCurrentYear();
    document.addEventListener('portfolio:languagechange', (event) => {
        renderCurrentYear(event.detail.language);
    });

    if (reduceMotion || !('IntersectionObserver' in window)) {
        revealItems.forEach((element) => element.classList.add('is-visible'));
        if (stackPanel) stackPanel.classList.add('is-visible');
    } else {
        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach((entry) => {
                if (!entry.isIntersecting) return;
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            });
        }, { threshold: 0.14, rootMargin: '0px 0px -6% 0px' });

        revealItems.forEach((element) => revealObserver.observe(element));

        if (stackPanel) {
            const stackObserver = new IntersectionObserver((entries, observer) => {
                if (!entries[0].isIntersecting) return;
                stackPanel.classList.add('is-visible');
                observer.disconnect();
            }, { threshold: 0.25 });
            stackObserver.observe(stackPanel);
        }
    }

    const navLinks = Array.from(document.querySelectorAll('.portfolio-nav__links a[href^="#"]'));
    const sections = navLinks
        .map((link) => document.querySelector(link.getAttribute('href')))
        .filter(Boolean);

    if ('IntersectionObserver' in window && sections.length) {
        const sectionObserver = new IntersectionObserver((entries) => {
            const visibleSection = entries
                .filter((entry) => entry.isIntersecting)
                .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];

            if (!visibleSection) return;
            navLinks.forEach((link) => {
                const isActive = link.getAttribute('href') === `#${visibleSection.target.id}`;
                link.classList.toggle('is-active', isActive);
                if (isActive) link.setAttribute('aria-current', 'location');
                else link.removeAttribute('aria-current');
            });
        }, { rootMargin: '-25% 0px -60% 0px', threshold: [0, 0.2, 0.5] });

        sections.forEach((section) => sectionObserver.observe(section));
    }
});

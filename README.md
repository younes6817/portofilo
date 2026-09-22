# portofilo
introducing myself

## Front-end assets

Tailwind is **compiled ahead of time** into `static/css/tailwind.css` — the templates no
longer load the ~400 KB Play-CDN runtime compiler (that was blocking the first paint and
re-compiling every utility on the visitor's phone).

```bash
npm install          # once
npm run build:css    # rebuild static/css/tailwind.css after changing templates/classes
npm run watch:css    # same, but rebuilds on every change while developing
```

The build input is `assets/css/tailwind.input.css` (kept outside `static/`, so the source
file never ends up in `collectstatic` output). `tailwind.config.js` scans all templates.
Because the admin stores free-form colour values for the tech-stack bars
(`bg-[{{ tech_stack.color }}]`), that one bar also gets an inline
`style="background-color: …"`, so new colours in the admin work **without** a rebuild.

After a rebuild, refresh what the web server serves:

```bash
python manage.py collectstatic --noinput
```

### Running locally

`DEBUG` is read from `.env` and defaults to `False`. Put `DEBUG=True` in `.env`
(git-ignored, **local only**) before `python manage.py runserver`: without it Django serves
neither `/static/` nor `/media/`, so every stylesheet, script and image a template points at
404s and the page looks unstyled with a missing photo. `runserver --insecure` is the
no-config alternative, but it only covers `/static/`, not `/media/`.

### Deploying

The precompiled CSS and the hero WebP variants are static files, so they have to reach the
server as well:

```bash
git pull
python manage.py collectstatic --noinput
```

If `static/css/tailwind.css` or `static/img/younes-*.webp` are missing there, the page
still renders correctly: `templates/base.html` falls back to the old runtime compiler when
the precompiled stylesheet fails to load, and the hero `<img>` falls back to the original
PNG when no WebP variant can be loaded. Both fallbacks are inert on a healthy deploy.

Hero photo variants (WebP for phones) can be regenerated from `media/younes.png` with:

```bash
python scripts/make_hero_variants.py
```

`static/js/tailwind.js` is the old runtime compiler. It is kept only as a rollback path —
if you restore the `<script>` tag in `templates/base.html`, everything works exactly as
before and the precompiled CSS can be ignored.

# Site illustrations

New visual assets for the course site (October 2026). These files are assets only; no page references them yet. All imagery is abstract or conceptual: no text inside images, no logos, no Yale marks, no people.

## Inventory

| File | Size (px) | Bytes | What it is | How it was made |
|---|---|---|---|---|
| `icons/module-0N-*.svg` (6) | 24×24 | 0.4 KB each | Line icon per module | Hand-written SVG, 1.75 stroke, round caps, `#002856` |
| `icons/module-0N-*@48px.png`, `@80px.png` | 48, 80 | 1–2.5 KB | Transparent PNG exports (2× for 24 px and 40 px display) | Rendered from the SVGs with headless Chrome |
| `home-header-vector-light.svg` / `.webp` / `.png` | 2400×800 | 14 KB SVG, 22 KB WebP | Option (a), light: faint ledger rules, two time series, sparse network on the right; left 40% fades to plain `#F5F7FA` for text | Programmatic SVG (Python, fixed seed 816) |
| `home-header-vector-navy.svg` / `.webp` / `.png` | 2400×800 | 14 KB SVG, 19 KB WebP | Option (a), navy `#002856` ground with the same motif in white at low opacity, for white hero text | Same script |
| `home-header-ai.webp` / `.jpg` | 2400×800 | 159 KB / 238 KB | Option (b): ledger paper with a navy time series and network that gets denser toward the right; left half blank | AI, gpt-image-2 |
| `banners/module-01-foundations.webp` / `.jpg` | 1600×896 | 212 / 256 KB | Library ladder against shelves, reading desk | AI, gpt-image-2 |
| `banners/module-02-empirical-loop.webp` / `.jpg` | 1600×896 | 112 / 181 KB | Four chart sheets (scatter + fit, bars, time series, coefficient plot) in a loop | AI, gpt-image-2 |
| `banners/module-03-edgar-text.webp` / `.jpg` | 1600×896 | 125 / 193 KB | Stacked filings dissolving into a data grid | AI, gpt-image-2 |
| `banners/module-04-wrds-mcp.webp` / `.jpg` | 1600×896 | 163 / 236 KB | Compact archive stacks, with fine threads running to one reading table | AI, gpt-image-2 |
| `banners/module-05-writing-verify.webp` / `.jpg` | 1600×896 | 187 / 236 KB | Manuscript with checked lines, loupe, fountain pen, locked padlock | AI, gpt-image-2 |
| `banners/module-06-seminar.webp` / `.jpg` | 1600×896 | 142 / 201 KB | Seminar table from above: eight chairs, papers, cups, no people | AI, gpt-image-2 |

Use the WebP files; the JPEGs are fallbacks. The banners are 1600×896 (the model's native 16:9 size). Display them with `object-fit: cover` at any 16:9 or wider crop. In every banner the left third is empty pale ground, so a wide crop such as 1600×500 (centre-right) still works.

## AI generation

- Tool: ElevenLabs Creative (flow "Claude Code for Accounting Research - site illustrations"), model **gpt-image-2**, quality medium. Banners were generated at a custom size of 1600×896 and the header at 2400×800.
- Candidates: 2 per banner and 3 for the header, so 15 images in all. Rejected candidates are kept in the scratch folder, not in the repo.
- Cost: 15 generations, about **$0.66** in total (12 × $0.047 + 3 × $0.033).
- Checks: each pick was inspected at full resolution for pseudo-text, warped objects and logos. Two small notes: the open book in the Module 4 banner has illegible scribble lines that suggest text, and the book spines carry tiny gold rules. Neither reads as letters.
- License and attribution: these are AI-generated with gpt-image-2 through ElevenLabs. Under the ElevenLabs and OpenAI terms, the output belongs to the account holder, and no third-party attribution is required. Suggested credit line for the About page: "Illustrations generated with AI (gpt-image-2) and art-directed by the course; icons and vector header drawn for this site."

### Shared style block (appended to every banner prompt)

```
Style: fine editorial print, gouache and risograph texture with subtle paper grain, flat matte color, delicate ink linework, soft diffuse daylight from the left, generous negative space, calm and restrained composition, left third mostly empty pale background.
Palette strictly limited: deep navy #002856, slate blue-gray, warm stone and parchment neutrals, off-white. No other hues.
Constraints: absolutely no text, letters, numbers, words, labels, logos, emblems, crests, seals or signage anywhere. No people, no faces, no hands, no robots, no glowing effects, no neon, no gradients-as-sci-fi glow, no computer screens, no futuristic imagery.
```

Every banner prompt starts with: "Use: a quiet landscape banner illustration for an academic course web page, in the manner of university press book cover art or a scholarly journal's issue art." The subject lines are:

- **M1**: a tall wooden library ladder leaning against plain, mostly empty bookshelves; at its foot a reading desk with a closed laptop, blank notebooks and an unlit desk lamp; unmarked navy and stone spines.
- **M2**: seen from above, loose sheets arranged in a circular loop, each with a simple navy chart (scatter with fitted line, bar chart, time series, coefficient plot with whiskers); a thin curved line links them; a pencil nearby; no axis labels or numbers.
- **M3**: a stack of bound reports and filing pages whose top pages lift and dissolve into a fine orderly grid of small squares, like documents turning into a spreadsheet; pages show only faint rules.
- **M4**: an archive of tall compact shelving stacks receding to the right, with plain boxes and unmarked ledgers; fine navy threads run from the stacks to one small reading table.
- **M5**: a manuscript page with abstract rules and small navy tick marks in the margin, a brass loupe, a fountain pen and a small locked brass padlock (muted antique brass allowed).
- **M6**: a long oval seminar table from directly above, with eight empty chairs, loose pages, open notebooks, pencils and coffee cups; the table sits toward the right.
- **Header (AI)**: a very wide abstract on pale off-white paper: faint horizontal ledger rules and thin column rules, a single delicate navy time-series line, and a sparse dot-and-hairline network that grows denser toward the right; the left half nearly empty; no text or digits.

## Recommended placement

| Asset | Page / spot | Alt text |
|---|---|---|
| `home-header-vector-light.svg` (default) | `index.qmd` hero background, with navy title text on the left. The motif sits in the right 60%. | "" (decorative; use `alt=""` or CSS `background-image`) |
| `home-header-vector-navy.svg` | Alternative hero if the restyle uses a navy band with white text | "" (decorative) |
| `home-header-ai.webp` | Alternative hero with a warmer, paper-like feel. Text goes over the left half. Pair it with navy text, not white. | "" (decorative) or "Ledger paper with a faint time series and network motif" |
| `icons/module-01-foundations.svg` | Module 1 card on the home page and `modules/index.qmd`, at 28–40 px beside the card title | "" (decorative next to the visible title) |
| `icons/module-02-empirical-loop.svg` | Module 2 card | "" |
| `icons/module-03-edgar-text.svg` | Module 3 card | "" |
| `icons/module-04-wrds-mcp.svg` | Module 4 card | "" |
| `icons/module-05-writing-verify.svg` | Module 5 card | "" |
| `icons/module-06-seminar.svg` | Module 6 card | "" |
| `banners/module-01-foundations.webp` | Top of `modules/01-foundations.qmd`, full content width, cropped to about 16:5 | "Illustration: a library ladder leaning against bookshelves beside a reading desk" |
| `banners/module-02-empirical-loop.webp` | Top of `modules/02-empirical-loop.qmd` | "Illustration: four sheets with a scatter plot, bar chart, time series and coefficient plot arranged in a loop" |
| `banners/module-03-edgar-text.webp` | Top of `modules/03-edgar-text.qmd` | "Illustration: a stack of paper filings whose pages dissolve into a data grid" |
| `banners/module-04-wrds-mcp.webp` | Top of `modules/04-wrds-mcp-scale.qmd` | "Illustration: archive shelving stacks connected by fine threads to a single reading table" |
| `banners/module-05-writing-verify.webp` | Top of `modules/05-writing-verify.qmd` | "Illustration: a manuscript with checked lines, a magnifying loupe, a fountain pen and a padlock" |
| `banners/module-06-seminar.webp` | Top of `modules/06-ai-knowledge-market.qmd` | "Illustration: an empty seminar table seen from above, set with papers and coffee cups" |

Notes for the page designer:

- Keep banners subordinate to the page. A height of about 220–300 px with `object-fit: cover; object-position: 70% 50%` keeps the subject in view and leaves the empty left side under any overlay.
- The icon SVGs have a hard-coded `stroke="#002856"`. For a dark theme, inline the SVG and set `stroke="currentColor"`.
- The icons are self-contained. Their `aria-label` attributes name the module. Use `alt=""` when the module title is already visible beside the icon.
- The vector headers are built by `make_header.py` in this folder (seed 816): `python3 make_header.py <outdir>`. Edit its colors to retint them.

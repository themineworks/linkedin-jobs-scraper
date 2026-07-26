# LinkedIn Jobs Scraper: Posting Monitor, No Cookies

Python client for **[LinkedIn Jobs Scraper: Posting Monitor, No Cookies](https://apify.com/themineworks/linkedin-jobs-scraper)** — scrape LinkedIn job postings — no cookies, no login.

> ⚡ No login, no cookies, no ban risk · runs in the cloud on [Apify](https://apify.com/themineworks/linkedin-jobs-scraper)
>
> 💸 From **$3.0 per 1,000 results** (volume discounts on paid Apify plans). You are only charged for delivered results — empty searches and failed pages are never billed.

## Quick start

```bash
pip install apify-client
python3 linkedin_jobs_scraper.py --token YOUR_APIFY_TOKEN --keywords "software engineer"
```

Get a free API token: [console.apify.com/sign-up](https://console.apify.com/sign-up) — then find it under **Settings → API & Integrations**.

## Options

| Flag | Type | Description |
|---|---|---|
| `--token` | string | Apify API token (or `APIFY_TOKEN` env var) |
| `--out` | string | Output basename — writes `results.json` + `results.csv` |
| `--keywords` | string | Job title, skill, or keyword to search for |
| `--location` | string | City, country, or 'Remote' |
| `--max-results` | integer | Maximum number of job listings to return |
| `--include-description` | boolean | Also fetch each job's description, seniority level and employment type (one extra request  |

Flags map 1:1 to the actor's input schema — full reference and a live output sample on the [Store listing](https://apify.com/themineworks/linkedin-jobs-scraper).

## Output

One row per result, saved as both JSON and CSV with every field the actor returns. Preview the exact fields on the [listing's output tab](https://apify.com/themineworks/linkedin-jobs-scraper).

## Why this actor

- **HTTP-native** — fast, stable, no headless-browser overhead
- **No account risk** — never asks for your login or cookies
- **Fair billing** — pay per delivered result only

MIT © [The Mine Works](https://apify.com/themineworks) — part of a 69-scraper suite trusted by 450+ developers.

# LinkedIn Jobs Scraper: No Login, Pay Per Job

Scrape LinkedIn job listings by keyword and location without login: job title, company, location, posting date, job type, seniority level, applicant count, and description snippet. Paginate across hundreds of results per search.

**Run it on Apify:** [apify.com/themineworks/linkedin-jobs-scraper](https://apify.com/themineworks/linkedin-jobs-scraper)
**Docs, FAQ and pricing:** [themineworks.com/actors/linkedin-jobs-scraper](https://themineworks.com/actors/linkedin-jobs-scraper/)

**Price:** From $1.50 per 1,000 jobs on Apify's higher plans. Failed and empty results are never charged.

## What it returns

* Job title, company, and location per listing
* Seniority level, job type, and applicant count
* Search by keyword and location
* Pagination across hundreds of results
* No login or cookies required

## Quick start

You need a free [Apify account](https://console.apify.com/sign-up) and its API token (Settings, API & Integrations).

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("themineworks/linkedin-jobs-scraper").call(run_input={
    "keywords": "software engineer",
    "location": "United States"
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### Node.js

```bash
npm install apify-client
```

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: 'YOUR_APIFY_TOKEN' });
const run = await client.actor('themineworks/linkedin-jobs-scraper').call({
    "keywords": "software engineer",
    "location": "United States"
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL

One request that runs the actor and returns the results in the response (for runs under 5 minutes):

```bash
curl -X POST "https://api.apify.com/v2/acts/themineworks~linkedin-jobs-scraper/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"keywords": "software engineer", "location": "United States"}'
```

### Command line

This repo includes ready-made clients that save results to JSON and CSV:

```bash
python3 linkedin_jobs_scraper.py --token YOUR_APIFY_TOKEN --keywords "software engineer" --location "United States"
node linkedin_jobs_scraper.mjs --token YOUR_APIFY_TOKEN --keywords "software engineer" --location "United States"
```

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `keywords` (required) | string |  | Job title, skill, or keyword to search for, for example "software engineer" or "product manager" |
| `location` | string |  | City, country, or 'Remote' to filter job listings by, for example "United States", "London", or "Remote" for… |
| `maxResults` | integer | `25` | Maximum number of job listings to return |
| `includeDescription` | boolean | `true` | Also fetch each job's description, seniority level and employment type (one extra request per job) |

## Output

One row per result, as JSON, CSV, Excel or through the API.

| Field | Type | Description |
|---|---|---|
| `job_id` | string | LinkedIn numeric job ID |
| `job_url` | string | URL to the LinkedIn job posting |
| `title` | string | Job title |
| `company` | string | Company name |
| `company_url` | string | URL to the company's LinkedIn page |
| `location` | string | Job location |
| `posted_at` | string | Posting date or relative time (for example '2 days ago') |
| `job_type` | string | Employment type (Full-time, Part-time, Contract, etc.) |
| `seniority_level` | string | Seniority level (Entry level, Mid-Senior level, etc.) |
| `description` | string | Job description snippet (up to 500 characters) |
| `applicant_count` | string | Number of applicants if shown |
| `scraped_at` | string | ISO timestamp when this record was scraped |

## Use it from an AI agent

The actor works as a tool in Claude, Cursor or any MCP client through Apify's MCP server:

```
https://mcp.apify.com/?tools=themineworks/linkedin-jobs-scraper
```

## FAQ

### How much does the LinkedIn Jobs Scraper cost?

From $1.50 per 1,000 jobs on Apify's higher plans. Failed and empty results are never charged. You can cap what a single run may spend with the maximum cost setting on Apify.

### Can I export the results to CSV or Excel?

Yes. Every run saves to an Apify dataset you can download as JSON, CSV, Excel or XML, or read through the API. The Python and Node clients in this repo also write the results to local files.

### Can I run it on a schedule?

Yes. Save your input as a task on Apify and attach a schedule, or call the API from your own cron job. Scheduled runs are billed the same way as manual ones.

## Related scrapers

* [Foundit Jobs Scraper](https://themineworks.com/actors/foundit-jobs-scraper/): Foundit.in (Monster India): 20 fields, monitor mode
* [Hirist Jobs Scraper](https://themineworks.com/actors/hirist-jobs-scraper/): India IT jobs across 147 locations, 19 fields
* [Naukri Jobs Scraper](https://themineworks.com/actors/naukri-jobs/): India's largest job board structured as clean JSON

Part of [The Mine Works](https://themineworks.com/): 151 pay-per-result scrapers with no login and no browser setup on your side.

## License

MIT © The Mine Works

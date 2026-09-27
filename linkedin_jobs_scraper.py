#!/usr/bin/env python3
"""Job listings by keyword and location without login. Python, Node.js and cURL clients for the LinkedIn Jobs Scraper on Apify, pay per result.

Command-line client for the themineworks/linkedin-jobs-scraper actor on Apify: runs it, waits for it
to finish and saves every result as JSON and CSV. Flags map 1:1 to the actor's input.
Free Apify account and API token: https://console.apify.com/sign-up
Docs and pricing: https://themineworks.com/actors/linkedin-jobs-scraper/
"""
import argparse, csv, json, os, sys
from apify_client import ApifyClient

ACTOR = "themineworks/linkedin-jobs-scraper"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--token", default=os.environ.get("APIFY_TOKEN"), help="Apify API token (or set APIFY_TOKEN)")
    ap.add_argument("--out", default="results", help="Output basename, writes .json and .csv")
    ap.add_argument("--keywords", help="Job title, skill, or keyword to search for, for example 'software engineer' or 'product…")
    ap.add_argument("--location", help="City, country, or 'Remote' to filter job listings by, for example 'United States'…")
    ap.add_argument("--max-results", type=int, help="Maximum number of job listings to return")
    ap.add_argument("--include-description", action=argparse.BooleanOptionalAction, help="Also fetch each job's description, seniority level and employment type (one extra request…")
    a = ap.parse_args()
    if not a.token:
        sys.exit("Provide --token or set APIFY_TOKEN. Free token: https://console.apify.com/sign-up")

    run_input = {}
    if a.keywords is not None: run_input["keywords"] = a.keywords
    if a.location is not None: run_input["location"] = a.location
    if a.max_results is not None: run_input["maxResults"] = a.max_results
    if a.include_description is not None: run_input["includeDescription"] = a.include_description

    client = ApifyClient(a.token)
    print(f"Running {ACTOR} ...")
    run = client.actor(ACTOR).call(run_input=run_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

    with open(a.out + ".json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    keys = []
    for it in items:
        keys += [k for k in it if k not in keys]
    if items:
        with open(a.out + ".csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
            w.writeheader()
            for it in items:
                w.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v for k, v in it.items()})
    print(f"Done: {len(items)} results saved to {a.out}.json and {a.out}.csv")


if __name__ == "__main__":
    main()

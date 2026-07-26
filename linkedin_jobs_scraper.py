#!/usr/bin/env python3
"""Scrape LinkedIn job postings — no cookies, no login.
CLI for the themineworks/linkedin-jobs-scraper Apify actor: runs it, waits, saves JSON + CSV.
Free Apify account + API token: https://console.apify.com/sign-up
"""
import argparse, csv, json, os, sys
from apify_client import ApifyClient

ACTOR = "themineworks/linkedin-jobs-scraper"

def main():
    ap = argparse.ArgumentParser(description="scrape LinkedIn job postings — no cookies, no login")
    ap.add_argument("--token", default=os.environ.get("APIFY_TOKEN"),
                    help="Apify API token (or set APIFY_TOKEN env var)")
    ap.add_argument("--out", default="results", help="Output basename (.json and .csv)")
    ap.add_argument("--keywords", default="software engineer", help="Job title, skill, or keyword to search for")
    ap.add_argument("--location", help="City, country, or 'Remote'")
    ap.add_argument("--max-results", type=int, default=25, help="Maximum number of job listings to return")
    ap.add_argument("--include-description", action="store_true", help="Also fetch each job's description, seniority level and employment type (one extra request per job)")
    a = ap.parse_args()
    if not a.token:
        sys.exit("Provide --token or set APIFY_TOKEN — free token at https://console.apify.com/sign-up")

    run_input = {}
    if a.keywords is not None: run_input["keywords"] = a.keywords
    if a.location is not None: run_input["location"] = a.location
    if a.max_results is not None: run_input["maxResults"] = a.max_results
    if a.include_description: run_input["includeDescription"] = True

    client = ApifyClient(a.token)
    print(f"Running {ACTOR} ...")
    run = client.actor(ACTOR).call(run_input=run_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

    with open(a.out + ".json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    if items:
        keys = []
        for it in items:
            for k in it:
                if k not in keys: keys.append(k)
        with open(a.out + ".csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
            w.writeheader()
            for it in items:
                w.writerow({k: ("" if v is None else v) for k, v in it.items()})
    print(f"Done: {len(items)} results -> {a.out}.json / {a.out}.csv")

if __name__ == "__main__":
    main()

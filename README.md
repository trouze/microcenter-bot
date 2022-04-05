# Microcenter GPU Price Check Script
This script does only one thing, checks a URL for whether a GPU is in stock at Microcenter.

It is not a CLI, I'm just defining URLs in a python list that I'd like to check inventory for. Nothing more.

It uses Twilio's SMS API, you need an account.

I scheduled as a cronjob on a GCP free tier VM, you could go serverless but I'm lazy.

It writes logs to `out.log` text file. Parses html with bs4. Requests html document via requests.
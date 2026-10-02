# Source Scout (round 3): websites and URLs visited

Agent: Source Scout (round 3). Date: 2026-10-02. All requests used curl through the configured proxy with the User-Agent "AskWhy-Enron research contact via repository owner", one request per URL, with pauses between requests. No search engine was used; URLs were requested directly. No bankrupt.com or tinyurl.com address was requested.
Candidates are NOT part of the library and may not be cited until the owner approves them. Contents are not summarized here.

**Refusals.** dol.gov returned an "Access Denied" page; sec.gov returned "Request Rate Threshold Exceeded" and then "Your Request Originates from an Undeclared Automated Tool". sec.gov's message refers to the User-Agent; changing it (for example, adding a personal email) would be getting around the refusal, so I stopped instead. No refused URL was retried, and no other way around the block was tried. The owner could open these pages in a browser.

| Time (UTC) | URL | HTTP result | What it was / what I found |
|---|---|---|---|
| 2026-10-02T18:11:23Z | https://www.justice.gov/archive/index-enron.html | 200 | DOJ Enron archive index; no target releases listed |
| 2026-10-02T18:11:27Z | https://www.justice.gov/archive/opa/pr/2004/April/ | 200 | DOJ press index; Lea Fastow statement #217 listed |
| 2026-10-02T18:11:33Z | https://www.justice.gov/archive/opa/pr/2004/April/04_crm_217.htm | 200 | DOJ press index; Lea Fastow statement #217 listed |
| 2026-10-02T18:11:37Z | https://www.justice.gov/archive/opa/pr/2004/May/ | 200 | DOJ press index; Lea Fastow sentencing #306 listed |
| 2026-10-02T18:11:45Z | https://www.justice.gov/archive/opa/pr/2004/May/04_crm_306.htm | 200 | DOJ press index; Lea Fastow sentencing #306 listed |
| 2026-10-02T18:11:49Z | https://www.justice.gov/archive/opa/pr/2002/October/ | 200 | DOJ press index; no Andersen-titled release; checked untitled DAG statement #597 |
| 2026-10-02T18:11:58Z | https://www.justice.gov/archive/opa/pr/2002/October/02_dag_597.htm | 200 | DOJ press index; no Andersen-titled release; checked untitled DAG statement #597 |
| 2026-10-02T18:12:06Z | https://www.justice.gov/archive/opa/pr/2006/September/ | 200 | DOJ press index; no Kopper or Koenig release |
| 2026-10-02T18:12:10Z | https://www.justice.gov/archive/opa/pr/2006/October/ | 200 | DOJ press index; no Kopper or Koenig release |
| 2026-10-02T18:12:15Z | https://www.justice.gov/archive/opa/pr/2006/November/ | 200 | DOJ press index; no Kopper or Koenig release |
| 2026-10-02T18:12:29Z | https://www.justice.gov/archive/opa/pr/2008/February/ | 200 | DOJ press index; British bankers sentencing 08-135 listed |
| 2026-10-02T18:12:34Z | https://www.justice.gov/archive/opa/pr/2007/November/ | 200 | DOJ press index; British bankers plea 07-949 listed (not downloaded) |
| 2026-10-02T18:12:40Z | https://www.justice.gov/archive/opa/pr/2008/February/08_crm_135.html | 200 | DOJ press index; British bankers sentencing 08-135 listed |
| 2026-10-02T18:12:45Z | https://www.justice.gov/archive/opa/pr/2003/September/ | 200 | DOJ press index; Merrill release #510 listed |
| 2026-10-02T18:12:49Z | https://www.justice.gov/archive/opa/pr/2003/December/ | 200 | DOJ press index; CIBC release #718 listed |
| 2026-10-02T18:12:59Z | https://www.justice.gov/archive/opa/pr/2003/December/03_crm_718.htm | 200 | DOJ press index; CIBC release #718 listed |
| 2026-10-02T18:13:03Z | https://www.justice.gov/archive/opa/pr/2003/September/03_crm_510.htm | 200 | DOJ press index; Merrill release #510 listed |
| 2026-10-02T18:13:07Z | https://www.ca5.uscourts.gov/opinions/pub/05/05-20319-CR0.wpd.pdf | 200 | Candidate ca5-us-v-brown-2006 |
| 2026-10-02T18:13:11Z | https://www.ca5.uscourts.gov/opinions/pub/05/05-20319-CR1.wpd.pdf | 404 | Not found (no revised opinion at this address) |
| 2026-10-02T18:13:17Z | https://www.dol.gov/newsroom/releases/ebsa/ebsa20040512 | 403 | REFUSED: 'Access Denied' page. Stopped; dol.gov not tried again |
| 2026-10-02T18:13:25Z | https://www.sec.gov/litigation/litreleases/lr18038.htm | 403 | REFUSED: 'Request Rate Threshold Exceeded' page. Stopped this URL |
| 2026-10-02T18:14:31Z | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=dynegy&type=8-K&dateb=20011231&owner=include&count=40 | 403 | REFUSED: 'Your Request Originates from an Undeclared Automated Tool' page. Stopped; sec.gov not tried again |
| 2026-10-02T18:14:47Z | https://www.justice.gov/archive/opa/pr/2006/August/ | 200 | DOJ press index; no Kopper or Koenig release |
| 2026-10-02T18:14:53Z | https://www.justice.gov/archive/opa/pr/2006/December/ | 200 | DOJ press index; no Kopper or Koenig release |
| 2026-10-02T18:14:58Z | https://www.justice.gov/archive/opa/pr/2007/January/ | 200 | DOJ press index; no Kopper or Koenig release |
| 2026-10-02T18:15:03Z | https://www.justice.gov/archive/opa/pr/2007/February/ | 200 | DOJ press index; no Kopper or Koenig release |
| 2026-10-02T18:15:08Z | https://www.justice.gov/archive/opa/pr/2007/March/ | 200 | DOJ press index; no Kopper or Koenig release |

Not attempted because of the refusals above: SEC litigation release on CIBC (target 7); Dynegy 8-K of Nov 28, 2001 (target 10); Enron 8-K of Oct 16, 2001 (substitute); DOL release of Feb 16, 2006 (substitute).
Seven candidates were collected, under the 10-candidate limit.

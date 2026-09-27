# Websites used by the Image Researcher & Diagrammer (first pass, 2026-09-26)

The web was used only to find and download images. No text or facts were taken from any website for the story.

## Sites visited

| Website | What I did there | What I took |
|---|---|---|
| commons.wikimedia.org (search and category API: `w/api.php`) | Searched for Enron, Sarbanes-Oxley, Arthur Andersen, Supreme Court, SEC building, gas pipeline, trading floor, Houston skyline; listed the categories "Enron", "Enron scandal", "Arthur Andersen", "1500 Louisiana Street", "Allen Center" | Candidate file names and their license metadata |
| commons.wikimedia.org (file description pages) | Read the licensing section of each file I used, plus `File:Immeuble_Andersen.jpg` (rejected) | License confirmation (see table below) |
| upload.wikimedia.org | Downloaded standard-size thumbnails (500, 960 or 1280 px wide) and the logo SVG | The 8 image files listed below |
| www.loc.gov (JSON item records, `?fo=json`) | Checked the Library of Congress rights advisory for the two Carol M. Highsmith photos (LCCN 2011632073, 2011632435) | Rights advisory text: "No known restrictions on publication." |

## Refused or failed requests (noted and moved on)

- **Wikimedia API:** repeated `HTTP 429 Too Many Requests` (rate limiting). I slowed down and retried. Some searches (SEC building, Andersen building) returned nothing usable.
- **upload.wikimedia.org:** `HTTP 400` for non-standard thumbnail widths (1600 px), and `HTTP 429` for the full-size originals of three small files. I used standard-size thumbnails instead. Nothing was hot-linked.
- **www.loc.gov/pictures/item/...** (HTML pages): `HTTP 403`. I used the loc.gov JSON record instead.
- **georgewbush-whitehouse.archives.gov** and **webarchive.loc.gov** (the original sources that Commons cites for the White House and Senate photos): not visited. I relied on the Commons file pages, which quote those sources.

## Images taken (license checked on the Commons file page before download)

| File in images/ | Commons file | License as shown on the source page |
|---|---|---|
| enron-complex.jpg | File:Enron_Complex.jpg | CC BY 2.0 (Flickr, "Alex"; license confirmed by Flickr review, Aug 2008) |
| enron-logo-1997.svg | File:Logo_of_Enron_Corporation_(1997).svg | Public domain, PD-textlogo (trademark warning) |
| gas-pipeline-station.jpg | File:Natural_Gas_Pipeline_Station.jpg | CC BY 4.0 (Mbrickn, own work) |
| nyse-trading-floor.jpg | File:Trading_floor_of_the_New_York_Stock_Exchange,_New_York_City_LCCN2011632435.tif | Public domain, PD-Highsmith; loc.gov: no known restrictions |
| senate-hearing-2002-01-24.jpg | File:Senator_Thompson_questions_former_SEC_Chairman_Arthur_Levitt_during_the_Governmental_Affairs_Committee's_opening_hearing_into_the_Enron_bankruptcy.jpg | Public domain, work of the U.S. Congress (Office of Sen. Fred Thompson) |
| enron-downtown-2009.jpg | File:Enron_Downtown_Houston_TX_-_panoramio.jpg | CC BY-SA 3.0 (Chanilim714; Panoramio review, Oct 2016) |
| supreme-court-building.jpg | File:Supreme_Court_Building,_Washington,_D.C_LCCN2011632073.tif | Public domain, PD-Highsmith; loc.gov: no known restrictions |
| sox-signing-oxley.jpg | File:President_George_W._Bush_shakes_hands_with_Congressman_Mike_Oxley.jpg | Public domain, Executive Office of the President (photo by Eric Draper) |

No AP, Getty or Reuters photos were used. None of the files' pages credited a news agency.

## Candidates looked at and rejected

- `File:Immeuble_Andersen.jpg` (CC BY 1.0): the source page does not say which Andersen building it is or where. It does not clearly show an Arthur Andersen office, so I left it out.
- `File:Arthur_Andersen_Witnesses.jpg` and `File:Sub-Committee_on_Energy_and_Commerce_012402.jpg` (public domain, House hearing, Jan. 24, 2002): the people are not named by the source.
- `File:Jeffrey_Skilling_mug_shot.jpg`: not used; not needed for any chapter image.
- `File:Enron_closing_stock,_1997-2002.svg`, `File:EnronStockPriceAugust2000toJanuary2001.svg`, `File:Andersen_revenue.svg`: charts with data that are not from our library, so I did not take them.
- `File:Logo_of_Enron_Corporation_(1986).svg`: CC BY-SA 4.0 redrawing; the public-domain 1997 logo is enough.
- `File:Panorama_of_United_States_Supreme_Court_Building_at_Dusk.jpg`, `File:US_Supreme_Court.JPG` (CC BY-SA 3.0): I preferred the public-domain Library of Congress photo.
- `File:DowntownHouston.jpg` (CC BY-SA 2.0, 2005 skyline): not needed.
- `File:United_States_Capitol_west_front_edit2.jpg` (public domain) and `File:President_George_W._Bush_meets_with_Senator_Paul_Sarbanes_and_Secretary_of_Labor_Elaine_Chao.jpg` (public domain, White House, July 30, 2002): suitable backups for Aftermath, not downloaded.
- SEC headquarters building: no suitable file found in the searches I could run.

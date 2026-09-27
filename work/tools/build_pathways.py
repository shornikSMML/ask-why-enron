#!/usr/bin/env python3
"""Pathways Designer (Phase 2): writes work/drafts/pathways.json.
Bridges add no new facts. Where a bridge states a fact, it carries `cites`
copied from the checked chapter citations (card ids verified OK/FIXED in
work/facts/factcheck-*.md). Anchors not yet on the site are listed in
work/drafts/pathway-anchor-requests.md.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def cite(src, page, loc, card):
    return {"source_id": src, "page": page, "loc": loc, "card": card}

C = {
    "A-007": cite("rpt-jct-vol1", 90, "p. 62, Part Two, II.B.2, footnote 67", "A-007"),
    "C-055": cite("rpt-sga-watchdogs", 36, "p. 32, Part One II (SEC's mark-to-market determination)", "C-055"),
    "A-047": cite("powers-report-sec", None, "p. 13 (also pp. 82-83), Executive Summary - Hedging Transactions; IV.C.1, lines 698-712, 3054-3066", "A-047"),
    "A-040": cite("powers-report-sec", None, "pp. 68-70, III.A Formation and Authorization of LJM Cayman, L.P. and LJM2, lines 2625-2674", "A-040"),
    "A-041": cite("powers-report-sec", None, "pp. 70-73, III.A Formation and Authorization of LJM Cayman, L.P. and LJM2, lines 2694-2775", "A-041"),
    "A-032": cite("powers-report-sec", None, "pp. 43-44, II.A Formation of Chewco, lines 1702-1727", "A-032"),
    "A-083": cite("enron-8k-nov-2001-ex99-1", None, "p. 1, Press release, Nov 8, 2001 (Exhibit 99.1), lines 44-47", "A-083"),
    "B-063": cite("rpt-psi-board", 21, "p. 17, Factual Basis for Findings (High Risk Accounting)", "B-063"),
    "C-011": cite("hrg-hec-andersen-shredding", 36, "p. 32, Testimony of C.E. Andrews, Andersen (oral)", "C-011"),
    "B-059": cite("sec-duncan-complaint", 2, "p. 2, Complaint, para. 5 (Defendant)", "B-059"),
    "G-032": cite("hrg-hfs-enron-investors-pt1", 122, "pp. 113, 115-116, Appendix: 'Remarks of Joseph F. Berardino, Managing Partner - Chief Executive Officer, Andersen' (prepared statement) (PDF pages covered: 119, 121-122)", "G-032"),
    "C-001": cite("hrg-hec-andersen-shredding", 49, "p. 45, Hearing record exhibit (e-mail dated 10/12/2001 from Nancy A. Temple to Michael C. Odom)", "C-001"),
    "B-055": cite("hrg-commerce-skilling-watkins", 16, "p. 12, Statement of Sherron Watkins", "B-055"),
    "C-076": cite("sox-plaw-html", None, "Sec. 302(a)", "C-076"),
    "G-019": cite("andersen-scotus-full-usreports", 2, "p. 544 U.S. at 697, Reporter's line preceding the opinion", "G-019"),
    "A-072": cite("rpt-psi-fishtail", 5, "pp. 1-2, Introduction", "A-072"),
}

def stop(page, anchor, label, bridge, cites=None):
    s = {"page": page, "anchor": anchor, "label": label, "bridge": bridge}
    if cites:
        s["cites"] = [C[c] for c in cites]
    return s

def handout(p, questions):
    return {
        "title": p["title"],
        "subtitle": "%s · about %d minutes" % (p["for_whom"], p["minutes"]),
        "stops": ["%s: %s" % (s["label"], s["bridge"]) for s in p["stops"]],
        "closing_question": p["closing_question"],
        "discussion_questions": questions,
    }

P = []

# 1. A First Reading -------------------------------------------------------
p = {
    "id": "first-reading",
    "title": "A First Reading",
    "for_whom": "Anyone new to the story",
    "minutes": 45,
    "intro": "The shortest route through the whole story, from a pipeline merger to a new federal law. You will read parts of five chapters and meet three people from the Cast of Characters. Use the arrows in the pathway bar, and read each stop at your own pace.",
    "stops": [
        stop("chapters/ch1.html", "growing-fast", "Chapter 1: Growing fast",
             "Start with the numbers Enron reported as it grew. As you read, keep two measures apart: revenue (how much a company sells) and profit (what it keeps)."),
        stop("chapters/ch2.html", "what-mark-to-market-means", "Chapter 2: What mark-to-market accounting means",
             "This is the accounting method at the heart of the story. Work through the made-up example and its diagram, and notice that the cash is the same either way; only the timing of the reported profit changes."),
        stop("chapters/ch3.html", "chapter", "Chapter 3: What a special purpose entity is",
             "Read the opening and the first diagram, then move on. The key question is the 3% test: was an independent owner's own money really at risk?"),
        stop("chapters/ch3.html", "what-it-added-up-to", "Chapter 3: What it added up to",
             "Skip ahead to the chapter's summary. Notice what the investigators said about how clearly Enron's public filings described these deals."),
        stop("cast.html", "andrew-fastow", "Cast: Andrew Fastow",
             "The board approved Fastow, Enron's chief financial officer, as the general partner of the LJM partnerships you just read about. Read his outcome closely: the Cast uses exact legal words such as alleged, pleaded guilty, and sentenced.",
             ["A-040", "A-041"]),
        stop("chapters/ch5.html", "november-8-restatement", "Chapter 5: November 8, the restatement",
             "Here Enron told investors not to rely on four years of its audited financial statements. As you read, connect the corrections to the entities from Chapter 3.",
             ["A-083"]),
        stop("chapters/ch5.html", "november-28-to-december-2", "Chapter 5: November 28 to December 2",
             "Notice how quickly the end came once confidence was gone, and notice where the sources disagree about why the rescue merger failed."),
        stop("cast.html", "kenneth-lay", "Cast: Kenneth Lay",
             "Read Lay's outcome slowly, word by word. What does it mean, in law, that a conviction was vacated?"),
        stop("cast.html", "jeffrey-skilling", "Cast: Jeffrey Skilling",
             "Compare what the jury decided with what the appeals courts did afterwards. Which parts of the outcome does the library leave open?"),
        stop("chapters/ch7.html", "a-new-law", "Chapter 7: A new law",
             "Finish with Congress's response. For each change in the list, try to name the problem from an earlier stop that it was meant to address."),
    ],
    "closing_question": "Enron's numbers were checked by its own managers, its board, its auditor, and outside analysts. Which of those checks do you think failed first, and why?",
}
p["handout"] = handout(p, [
    "Revenue, profit, and market value measure different things. Which one would you trust most to judge a company's health, and why?",
    "The 3% test for special purpose entities was a bright-line rule. What are the advantages and the dangers of accounting rules built on an exact number?",
    "Pick one change in Chapter 7's list of Sarbanes-Oxley reforms. Which earlier stop on this pathway shows the problem it was meant to fix?",
])
P.append(p)

# 2. Mark-to-Market Explained ---------------------------------------------
p = {
    "id": "mark-to-market",
    "title": "Mark-to-Market Explained",
    "for_whom": "Accounting beginners",
    "minutes": 30,
    "intro": "Mark-to-market accounting values a contract or an investment at its current market value, and counts any change in that value as profit or loss right away. This pathway explains the idea in plain language, then follows it through Enron's trading contracts, its investments, and the structures built to protect its gains on paper.",
    "stops": [
        stop("glossary.html", "mark-to-market", "Glossary: mark-to-market accounting",
             "Begin with the short definition. Two related ideas, fair value and unrealized gain, come up at every later stop."),
        stop("glossary.html", "unrealized-gain", "Glossary: unrealized gain",
             "An unrealized gain is a profit on paper: the value has gone up, but nothing has been sold and no cash has arrived. Keep this idea in mind for the rest of the pathway."),
        stop("timeline.html", "tl-1992", "Timeline: mark-to-market accounting for trading",
             "Enron began using the method early. Notice that the sources give two different starting years, 1991 and 1992, and that the site reports both instead of choosing one.",
             ["A-007", "C-055"]),
        stop("chapters/ch2.html", "what-mark-to-market-means", "Chapter 2: What mark-to-market accounting means",
             "Work through the ten-year contract example with the diagram. When a contract has no market price, ask who produces the estimate of what it is worth."),
        stop("chapters/ch2.html", "marking-investments", "Chapter 2: Marking investments to market",
             "Here the same idea is applied to Enron's stakes in other companies. Notice how the stock price of a company Enron had invested in could move Enron's own reported profit."),
        stop("chapters/ch3.html?lens=money", "rhythms", "Chapter 3: Rhythms, a hedge with Enron's own stock (Follow the Money lens)",
             "Mark-to-market now creates a problem: a paper gain that could disappear if the stock fell. Read how Enron tried to protect that gain, and why the board's special committee found that this was not a normal hedge.",
             ["A-047"]),
        stop("chapters/ch3.html", "fig-diagram-raptor", "Chapter 3: The Raptor diagram",
             "The Raptors extended the same approach to many investments. Trace in the diagram where the money to cover a loss would have come from."),
        stop("chapters/ch5.html", "fig-chart-restatement", "Chapter 5: The restatement chart",
             "Profits that rest on estimates and on accounting choices can later be corrected. Compare the reported and restated profit for each year, then read the section to see which corrections the restatement involved."),
        stop("chapters/ch2.html", "ask-why", "Chapter 2: Ask Why",
             "Return to the question at the end of Chapter 2, now that you have seen the method at work."),
    ],
    "closing_question": "Mark-to-market accounting can give investors more up-to-date information, but it depends on estimates. What safeguards would make you trust a company's own estimate of what a long-term contract is worth?",
}
p["handout"] = handout(p, [
    "Using your own example, explain the difference between a realized gain and an unrealized gain.",
    "A hedge protects you only if the other party can pay. Use Rhythms or the Raptors to explain why.",
    "If you were the auditor, what evidence would you ask for before accepting management's estimate of a contract's value?",
])
P.append(p)

# 3. The Special Purpose Entities -----------------------------------------
p = {
    "id": "spes",
    "title": "The Special Purpose Entities",
    "for_whom": "Readers who want the mechanics",
    "minutes": 40,
    "intro": "Special purpose entities were at the center of Enron's accounting. This pathway follows how they worked, from the basic rule to Chewco, the LJM partnerships and the Raptors. It then shows how Enron described these deals in its annual report, and what happened to two of the people who ran them.",
    "stops": [
        stop("chapters/ch3.html", "chapter", "Chapter 3: What an SPE is, and the 3% test",
             "Read the opening and the first diagram carefully. Everything that follows turns on one question: was an independent owner's own money truly at risk?"),
        stop("glossary.html", "three-percent-rule", "Glossary: the 3% rule",
             "A quick look at the rule itself before you see it tested."),
        stop("chapters/ch3.html?lens=money", "chewco", "Chapter 3: Chewco (Follow the Money lens)",
             "With Follow the Money on, track where Chewco's equity came from, and what the board's special committee concluded that meant for the 3% test."),
        stop("chapters/ch3.html", "fig-diagram-chewco-ljm", "Chapter 3: The Chewco and LJM diagram",
             "Use the diagram to see who sat on each side of these deals."),
        stop("chapters/ch3.html?lens=board", "ljm", "Chapter 3: The LJM partnerships (The Board lens)",
             "With The Board on, notice what the board approved and which controls it relied on: two senior officers were to approve every LJM2 deal, and the Audit Committee was to review them each year.",
             ["A-041"]),
        stop("chapters/ch3.html?lens=money", "raptors", "Chapter 3: The Raptors (Follow the Money lens)",
             "Notice where the Raptors' ability to pay came from, and what happened when Enron's stock and the investments they covered fell at the same time."),
        stop("footnote.html", "fn-03", "The Footnote: \"a senior officer of Enron\"",
             "Now read how Enron's annual report described these deals. This annotation looks at how the note referred to the person who ran the partnerships."),
        stop("footnote.html", "fn-06", "The Footnote: \"to hedge certain merchant investments\"",
             "The note calls these deals hedges. Compare its wording with what you read about the Raptors two stops ago."),
        stop("cast.html", "andrew-fastow", "Cast: Andrew Fastow",
             "Read how Fastow's cases ended, and notice where two government announcements give different figures."),
        stop("cast.html", "michael-kopper", "Cast: Michael Kopper",
             "Kopper, who worked for Fastow, took Fastow's place at Chewco. Read what the library shows about his case, and what it does not show.",
             ["A-032"]),
    ],
    "closing_question": "An SPE could stay off Enron's books if an independent owner had at least 3% of its value at risk. Why might a rule based on a single number be easier to get around than a rule based on who really bears the risk?",
}
p["handout"] = handout(p, [
    "Sketch the basic SPE from the first diagram of Chapter 3. Where would you look to check whether the outside 3% was really at risk?",
    "The board approved Fastow's dual role and added controls. Which control would you have strengthened, and how?",
    "Read the footnote's phrase about hedging. What would an ordinary investor have needed to know to see the risk?",
])
P.append(p)

# 4. Andersen's Fall and the Big Five to Big Four -------------------------
p = {
    "id": "andersen",
    "title": "Andersen's Fall and the Big Five to Big Four",
    "for_whom": "Future auditors and accountants",
    "minutes": 40,
    "intro": "This pathway follows Enron's auditor, Arthur Andersen: the audit and its fees, the warning signs, the destruction of documents, the firm's criminal case and what the Supreme Court decided, and how the audit profession changed afterwards.",
    "stops": [
        stop("chapters/ch6.html?lens=auditors", "chapter", "Chapter 6: Why auditors matter (The Auditors lens)",
             "Read the opening and \"Enron's auditor.\" Notice who pays the auditor, and why that makes independence so important."),
        stop("chapters/ch4.html?lens=auditors", "many-push-limits", "Chapter 4: \"Many push limits\" (The Auditors lens)",
             "Here is the Andersen lead partner's own handwritten note about Enron's accounting, as the Senate subcommittee staff reported it. Compare it with what the Audit Committee's chair testified he recalled hearing.",
             ["B-063"]),
        stop("chapters/ch6.html", "the-fees", "Chapter 6: The fees",
             "Notice that the sources give different fee totals, and that Andersen disputed calling some of the work consulting. Why would that label matter?"),
        stop("cast.html", "joseph-berardino", "Cast: Joseph Berardino",
             "Andersen's chief executive. Before reading his entry, look back at \"Errors and what the examiner concluded\" in Chapter 6. Then read what the library records about him, and what it does not show.",
             ["G-032"]),
        stop("chapters/ch6.html", "the-shredding", "Chapter 6: The shredding",
             "The witnesses did not all agree about what happened. As you read, keep track of who said what, and in what setting."),
        stop("cast.html", "david-duncan", "Cast: David Duncan",
             "Andersen's lead partner on Enron. Read his outcome carefully, including what the library does not yet show.",
             ["B-059"]),
        stop("cast.html", "nancy-temple", "Cast: Nancy Temple",
             "The Andersen lawyer whose e-mail about the document policy is quoted in Chapter 6. Notice what the Cast says about charges.",
             ["C-001"]),
        stop("chapters/ch6.html", "conviction-collapse-reversal", "Chapter 6: Conviction, collapse, reversal",
             "The Supreme Court reversed Andersen's conviction in 2005. Read exactly why, and what the reversal did and did not decide. The numbered notes link to the Court's opinion in the source library.",
             ["G-019"]),
        stop("timeline.html?tag=auditors", "", "Timeline: auditor events",
             "The timeline is filtered to auditor events. Scroll through them to see the whole relationship, from the 1985 merger to the 2005 decision."),
        stop("chapters/ch6.html", "big-four", "Chapter 6: The Big Four",
             "Finish with the effect on the profession. Notice what the GAO said it had found, and what it said it had not yet found."),
    ],
    "closing_question": "An auditor is paid by the company it checks. After reading Andersen's story, what arrangements would you want in place so that an auditor can say no to its most important client?",
}
p["handout"] = handout(p, [
    "The Supreme Court reversed Andersen's conviction, but the firm had already collapsed. What is the difference between a legal outcome and a practical one?",
    "Should an audit firm be allowed to sell consulting services to a company it audits? Give one argument for and one against.",
    "With only four large firms left to audit big companies, what could change for companies choosing an auditor, and for auditors deciding whether to keep a client?",
])
P.append(p)

# 5. From Enron to Sarbanes-Oxley and the PCAOB ---------------------------
p = {
    "id": "sox",
    "title": "From Enron to Sarbanes-Oxley and the PCAOB",
    "for_whom": "Business and accounting students",
    "minutes": 35,
    "intro": "This pathway starts with Chapter 7's list of what the Sarbanes-Oxley Act changed. It then goes provision by provision through \"Why This Matters to You,\" linking each rule to the Enron problem it addressed, and ends with what these rules mean for someone starting a career.",
    "stops": [
        stop("chapters/ch7.html", "a-new-law", "Chapter 7: A new law",
             "Read the list of the law's main changes. The next stops take several of them in more detail."),
        stop("timeline.html", "tl-2002-07-30", "Timeline: the law is signed",
             "Place the law in time. Use the year links to look back at how close it came to the events of 2001 and early 2002."),
        stop("why-it-matters.html", "s302", "Why This Matters: CEO and CFO certification",
             "The chief executive and chief financial officer must now personally certify each annual and quarterly report. Think back to the executives in the Cast of Characters as you read.",
             ["C-076"]),
        stop("why-it-matters.html", "s404", "Why This Matters: internal control reporting",
             "Internal controls are a company's own checks on its numbers. Recall the controls the board placed around the LJM2 deals in Chapter 3.",
             ["A-041"]),
        stop("why-it-matters.html", "pcaob", "Why This Matters: the PCAOB",
             "Read what the new oversight board does. Compare it with Chapter 6's account of Andersen."),
        stop("timeline.html", "tl-2003-04-25", "Timeline: the PCAOB is ready",
             "Notice how much time passed between the law's signing and the day the new overseer was ready to operate."),
        stop("why-it-matters.html", "independence", "Why This Matters: auditor independence",
             "Chapter 6 described Andersen's fees for audit work and for other work. Read which services the law now limits, and why."),
        stop("why-it-matters.html", "whistleblowers", "Why This Matters: document destruction and whistleblowers",
             "Two earlier stories meet here: the shredding at Andersen, and the letter Sherron Watkins testified she sent to Lay. Ask how each might have gone differently under the new rules.",
             ["C-011", "B-055"]),
        stop("why-it-matters.html", "today", "Why This Matters: what it means for you",
             "Finish with the part written for you. Notice where the page says the library's documents stop."),
    ],
    "closing_question": "If you could add one more rule based on the Enron story, what would it be, and which stop on this pathway supports your choice?",
}
p["handout"] = handout(p, [
    "Which Sarbanes-Oxley provision do you think would have made the biggest difference at Enron? Support your answer with at least one chapter.",
    "Certification makes the CEO and CFO personally responsible for each report. Can a signature change behavior inside a large company?",
    "Limiting the other services an auditor may sell to its audit client is meant to protect independence. Could it also have costs? For whom?",
])
P.append(p)

# 7. The Banks ------------------------------------------------------------
p = {
    "id": "banks",
    "title": "The Banks",
    "for_whom": "Finance students",
    "minutes": 35,
    "intro": "This pathway looks at the banks and investment banks that did business with Enron. It explains \"prepays,\" deals that looked like trades but worked like loans, then looks at specific transactions, the institutions involved, and how the regulators' cases ended as far as the library shows.",
    "stops": [
        stop("chapters/ch5.html", "tip-of-the-iceberg", "Chapter 5: The tip of the iceberg",
             "The end of Chapter 5 first brings in the banks. Notice the phrase the Senate subcommittee staff used for the prepays.",
             ["A-072"]),
        stop("glossary.html", "prepay", "Glossary: prepay",
             "A short definition before the details."),
        stop("banks.html", "prepays", "The Banks: how a prepay worked",
             "Trace the money around the circle. Ask what made a deal a trade in its paperwork but a loan in its economics."),
        stop("banks.html", "deals", "The Banks: the deals",
             "Read about the specific transactions, and notice which report or complaint describes each one."),
        stop("timeline.html", "tl-1999-12", "Timeline: year-end deals with Merrill Lynch",
             "Notice when in the year these deals took place, and think about why timing can matter for a company's reported results."),
        stop("banks.html", "institutions", "The Banks: institution by institution",
             "Keep the verbs straight: an SEC complaint alleges; a settlement is agreed to, often without admitting or denying the allegations; the bankruptcy examiner concluded what a fact-finder could find."),
        stop("cast.html", "jpmorgan-citigroup", "Cast: JPMorgan Chase and Citigroup",
             "Read how the SEC's cases against the two banks ended, and what \"without admitting or denying\" means."),
        stop("cast.html", "merrill-lynch-executives", "Cast: Merrill Lynch executives",
             "Notice that the Cast marks these executives' outcome as not covered by the library, and that the site says so instead of guessing."),
        stop("timeline.html", "tl-2003-07-28", "Timeline: two banks settle with the SEC",
             "Place the settlements in time. How long after Enron's bankruptcy did they come?"),
        stop("banks.html", "outcomes", "The Banks: how the cases ended",
             "Finish with the outcomes. Note where the library's documents stop, and which questions they leave open."),
    ],
    "closing_question": "When a deal is a loan in substance but a trade on paper, who should be responsible for how it appears in the borrower's financial statements: the borrower, its auditor, or the bank that designed it?",
}
p["handout"] = handout(p, [
    "In your own words, explain how a prepay could work like a loan.",
    "A bank that settles with the SEC without admitting or denying the allegations pays money but makes no admission. What does such a settlement tell the public, and what does it leave unanswered?",
    "Should a bank have a duty to consider how its client will account for a deal the bank designs? Why or why not?",
])
P.append(p)

# 6. Reading the Footnotes (drafted last, from work/facts/footnotes-map.md) --
# Stops on Notes 1, 3, 4, 9, 15 and the Q3 2001 10-Q need NEW sections on
# footnote.html (see anchor requests). Each such stop carries a `fallback`
# stop on an existing page, so the pathway works before those sections exist.
C.update({
    "N-001": cite("enron-10k-2000", None, "Form 10-K 2000, Note 1 Summary of Significant Accounting Policies, lines 4091-4099", "N-001"),
    "N-005": cite("enron-10k-2000", None, "Form 10-K 2000, Note 3 Price Risk Management Activities, Fair Value, lines 4431-4452", "N-005"),
    "N-006": cite("enron-10k-2000", None, "Form 10-K 2000, Note 3, Notional Amounts and Terms, lines 4415-4421", "N-006"),
    "N-011": cite("enron-10k-2000", None, "Form 10-K 2000, Note 4 Merchant Activities, lines 4634-4674", "N-011"),
    "N-014": cite("enron-10k-2000", None, "Form 10-K 2000, Note 9 Unconsolidated Equity Affiliates (tables), lines 5014-5078", "N-014"),
    "A-051": cite("powers-report-sec", None, "p. 97, V. The Raptors (introduction), lines 3592-3612", "A-051"),
    "N-015": cite("enron-10k-2000", None, "Form 10-K 2000, Note 9 Unconsolidated Equity Affiliates, lines 5122-5140", "N-015"),
    "N-019": cite("rpt-sga-watchdogs", 33, "p. 29, SEC's review of Enron's filings", "N-019"),
    "N-024": cite("enron-10k-2000", None, "Form 10-K 2000, Note 15 Commitments, lines 5811-5856", "N-024"),
    "N-026": cite("enron-10q-q3-2001", None, "pp. 22-23, Note 4 Related Party Transactions - Portfolio SPEs, lines 1543-1563", "N-026"),
    "N-029": cite("rpt-psi-board", 52, "p. 48, Finding (4) - Inadequate Public Disclosure", "N-029"),
    "N-032": cite("enron-8k-nov-2001", None, "pp. 1, 4-5, Item 5; 2.A Restatement Number 1, lines 51-72, 263-284", "N-032"),
    "C-054": cite("rpt-sga-watchdogs", 32, "p. 28, Part One II (SEC review of Enron filings)", "C-054"),
})

def fb(page, anchor):
    return {"page": page, "anchor": anchor}

p = {
    "id": "footnotes",
    "title": "Reading the Footnotes",
    "for_whom": "Anyone learning to read an annual report",
    "minutes": 40,
    "intro": "The notes at the back of an annual report explain the numbers in front. The famous Note 16 was only one piece of the story: other notes in Enron's 2000 annual report held other pieces, and later filings and investigations showed what they left out. This pathway reads several notes together, then compares them with what came later.",
    "stops": [
        stop("glossary.html", "notes-to-financial-statements", "Glossary: notes to the financial statements",
             "Start with what notes are for. As you go, ask of each note two questions: what could a careful reader learn here, and what could no reader learn?"),
        dict(stop("footnote.html", "note-1", "Note 1: accounting policies",
             "Note 1 said Enron's statements included \"all subsidiaries controlled by Enron Corp.\" Keep the word \"controlled\" in mind: whether Enron had to consolidate an entity depended on rules about who controlled it and who bore its risk.",
             ["N-001"]), fallback=fb("chapters/ch2.html", "what-mark-to-market-means")),
        dict(stop("footnote.html", "note-3", "Note 3: the trading book",
             "Note 3 reported about $21.5 billion of trading assets at fair value, and cautioned that the face amounts of its contracts did not measure its real exposure to risk. Ask how a reader could tell how much of that value came from Enron's own estimates.",
             ["N-005", "N-006"]), fallback=fb("glossary.html", "price-risk-management")),
        dict(stop("footnote.html", "note-4", "Note 4: merchant investments",
             "Note 4 said these investments were valued using market prices, independent appraisals and cash flow analyses. Compare it with what Chapter 3 says about the Raptors, which were set up to offset losses on the same kind of investment.",
             ["N-011", "A-051"]), fallback=fb("chapters/ch2.html", "marking-investments")),
        dict(stop("footnote.html", "note-9", "Note 9: affiliates kept off the books",
             "Note 9 listed JEDI and Whitewing, each 50% owned and not consolidated. The Senate Governmental Affairs Committee staff later reported that experts pointed to this pattern, just below the level that requires consolidation, as a reason to look closer.",
             ["N-014", "N-019"]), fallback=fb("chapters/ch3.html", "chewco")),
        stop("footnote.html", "fn-p0", "Note 16: related party transactions",
             "Now read the famous note phrase by phrase. Note 9 had already mentioned \"the Related Party\" and pointed ahead to this note; here is what that label covered.",
             ["N-015"]),
        dict(stop("footnote.html", "note-15", "Note 15: commitments and guarantees",
             "Note 15 listed Enron's guarantees and said management did not consider it likely that Enron would have to pay. Ask what a reader would need to know to judge that for themselves.",
             ["N-024"]), fallback=fb("chapters/ch5.html", "rescue-attempt")),
        dict(stop("footnote.html", "q3-10q", "The third-quarter 2001 report",
             "In November 2001, Enron's quarterly report named the Raptors and set out their terms. The Senate subcommittee staff contrasted its nine-page account with the one-page notes of earlier years.",
             ["N-026", "N-029"]), fallback=fb("chapters/ch5.html", "rescue-attempt")),
        stop("chapters/ch5.html", "november-8-restatement", "Chapter 5: November 8, the restatement",
             "Here Enron itself said that three entities should have been consolidated, and that its financial statements for 1997 through 2000 should not be relied upon. Compare that with the wording of Note 1.",
             ["N-032", "A-083"]),
        stop("chapters/ch4.html", "watchdogs-outside", "Chapter 4: The watchdogs outside",
             "Finally, who was supposed to read these notes closely? The Senate staff report said that if the SEC had reviewed Enron's 2000 annual report, items such as Note 16 were likely to have prompted questions.",
             ["C-054"]),
    ],
    "closing_question": "Enron's notes disclosed many facts, yet investigators later found that readers could not see what was going on. Is a disclosure honest if it is accurate but impossible to understand? Who should decide whether a note is clear enough?",
}
p["handout"] = handout(p, [
    "Pick one note from this pathway. List one thing a careful reader could learn from it, and one thing the reader could not learn.",
    "Several notes pointed to each other (Note 9 to Note 16, for example). Does spreading information across notes help or hinder a reader?",
    "Compare the one-page Note 16 with the nine-page account in the November 2001 quarterly report. Why might Enron have written more clearly the second time?",
])
P.insert(5, p)

out = {
    "_note": "Pathways Designer draft. Stop = {page, anchor, label, bridge, cites?}. 'anchor' is an element id on 'page' ('' = top of page). 'page' may carry ?lens= or ?tag=. Bridges add no new facts; any fact carries card cites (checked chapter citations). See work/drafts/pathway-anchor-requests.md for anchors the site must add.",
    "pathways": P,
}
json.dump(out, open(os.path.join(ROOT, "work", "drafts", "pathways.json"), "w"), indent=1, ensure_ascii=False)
print("pathways:", [(x["id"], len(x["stops"])) for x in P])

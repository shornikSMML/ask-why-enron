import json, re, glob, sys
from html.parser import HTMLParser

ROOT = __import__('os').path.abspath(__import__('os').path.join(__import__('os').path.dirname(__file__), '../../..'))
cards = {}
for f in sorted(glob.glob(ROOT + '/work/facts/reader-*.json')):
    for c in json.load(open(f)):
        cards[c['id']] = c

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.paras = []; s.cur = None; s.aside = 0; s.incite = False
    def handle_starttag(s, t, a):
        a = dict(a)
        if t == 'aside': s.aside += 1
        if t == 'p' and s.aside == 0 and a.get('class') != 'dek':
            s.cur = {'lens': a.get('data-lens', ''), 'text': ''}
        if t == 'a' and s.cur is not None and a.get('class') == 'cite':
            s.incite = True
    def handle_endtag(s, t):
        if t == 'aside': s.aside -= 1
        if t == 'p' and s.cur is not None:
            s.paras.append(s.cur); s.cur = None
        if t == 'a': s.incite = False
    def handle_data(s, d):
        if s.cur is not None and not s.incite: s.cur['text'] += d

paras = {}
for n in range(1, 8):
    p = P(); p.feed(open(f'{ROOT}/work/drafts/ch{n}.html').read())
    paras[n] = [' '.join(x['text'].split()) for x in p.paras], [x['lens'].split() for x in p.paras]

def C(cid):
    c = cards[cid]
    assert c['checked'] in ('OK', 'FIXED'), cid
    L = c['locator'] or {}
    page = L.get('pdf_page')
    if isinstance(page, str):
        page = int(page) if page.isdigit() else None
    bits = []
    if L.get('printed_page'): bits.append(str(L['printed_page']))
    if L.get('section'): bits.append(str(L['section']))
    if not L.get('printed_page') and L.get('lines'): bits.append('lines ' + str(L['lines']))
    if c['source_id'] == 'powers-report-sec':
        page = None  # G-1: .txt source; PDF page numbers belong to the separate powers-report copy
    return {'card': cid, 'source_id': c['source_id'], 'page': page, 'loc': ', '.join(bits)}

def cites(*ids): return [C(i) for i in ids]

def note(ch, idx, lens, text, *ids):
    texts, lenses = paras[ch]
    assert lens in lenses[idx - 1], (ch, idx, lens, lenses[idx - 1])
    return {'para_index': idx, 'para_key': f'ch{ch}-p{idx}',
            'para_start': ' '.join(texts[idx - 1].split()[:8]),
            'text': text, 'cites': cites(*ids)}

def B(text, *ids): return {'text': text, 'cites': cites(*ids)}
def S(date, who, what, *ids): return {'date': date, 'who': who, 'what': what, 'cites': cites(*ids)}

L = {}
L['_meta'] = {
  'para_index': 'Counts <p> elements in the chapter fragment work/drafts/chN.html, starting at 1, in document order, skipping <p class="dek"> and any <p> inside <aside class="ask-why">. para_start is the first 8 words of the paragraph text with citation links removed.',
  'cites': 'page is the PDF page (null for .txt/.htm sources); loc is a human-readable locator copied from the fact card.',
  'summary': 'Each summary bullet is {text, cites}. Each knew strip entry is {date, who, what, cites}.',
  'author': 'Lens Writer (Phase 2)'
}

# ---------------- Chapter 1 ----------------
L['ch1'] = {
 'money': {
  'notes': [
   note(1, 13, 'money', "Follow the money: all three Enron 2000 targets were about reported earnings and how fast they grew, year after year. The congressional tax staff described the plan but did not say it caused later accounting choices; Chapter 2 shows why steady reported growth mattered so much to Enron.", 'A-008', 'A-028'),
   note(1, 15, 'money', "Follow the money: reported revenue grew nearly eightfold from 1996 to 2000, and reported assets about fourfold. Chapter 2 compares this with reported net income, which grew far more slowly: from $703 million in 1998 to $979 million in 2000.", 'A-010', 'A-025'),
   note(1, 17, 'money', "Follow the money: market capitalization is set by investors buying and selling shares, not by the company's accountants. The $70 billion figure comes from an Enron press release, as the congressional tax staff noted.", 'A-011'),
  ],
  'summary': [
   B("In 1985 InterNorth paid HNG's shareholders $2.4 billion in cash, creating the company that became Enron.", 'A-002'),
   B("In 1996 Enron publicly set targets for its reported profit: $1 billion of net income by 2000 and double-digit growth every year.", 'A-008'),
   B("Enron's reported revenue rose from $13 billion in 1996 to $101 billion in 2000, and its reported assets from $16.1 billion to $65.5 billion. These are the figures as reported before the 2001 corrections.", 'A-010'),
   B("In early 2001 Enron's shares were worth about $70 billion in total, according to an Enron press release cited by the congressional tax staff.", 'A-011'),
  ],
  'ask_why': "Enron's reported revenue grew almost eightfold in four years. If you were an investor, what would you want to see besides revenue before believing the company was actually earning more money?"
 },
 'auditors': {
  'notes': [
   note(1, 9, 'auditors', "The Auditors: Andersen's relationship with Enron is older than the Enron name; the firm had already audited InterNorth. The bankruptcy examiner describes Andersen's job as giving an opinion on whether Enron's annual financial statements fairly presented its financial position. The relationship lasted until Enron's board voted to end it on January 17, 2002.", 'C-026', 'C-037'),
  ],
  'summary': [
   B("Arthur Andersen had audited InterNorth and became the auditor of the combined company formed in 1985.", 'C-026'),
   B("An auditor's opinion says whether the financial statements fairly present the company's financial position, in all material respects. It is an opinion, not a guarantee.", 'C-026'),
   B("Several people who later held finance jobs at Enron came from Andersen. According to the SEC's complaint, Richard Causey audited Enron for Andersen from 1986 to 1991 before joining Enron; the SEC also describes Ben Glisan as a former Andersen accountant; and Sherron Watkins testified that she spent eight years at Andersen.", 'B-041', 'B-047', 'B-054'),
   B("Andersen remained Enron's auditor until Enron's board voted to terminate it on January 17, 2002.", 'C-037'),
  ],
  'ask_why': "Several of Enron's finance staff had once worked for its auditor. What are the benefits, and what are the risks, when people move from an audit firm to a company that firm audits?"
 },
 'board': {
  'notes': [],
  'summary': [
   B("HNG was the smaller company, but its managers took control: by the end of 1986 most of the combined company's officers and directors came from HNG.", 'A-005'),
   B("Kenneth Lay became chairman of the board and chief executive of the combined company in February 1986, and held both jobs until February 2001.", 'A-005'),
   B("Some directors who oversaw Enron in 2001 had been on its board since the mid-1980s. The Senate subcommittee staff lists Herbert Winokur Jr. and Robert Jaedicke as directors from 1985; the bankruptcy examiner gives some earlier dates because he counts service on the predecessor companies' boards.", 'B-076', 'B-077'),
  ],
  'ask_why': "From 1986 to 2001 Lay was both the chairman of Enron's board and its chief executive. What might a board gain, and what might it lose, when the person it oversees also leads its meetings?"
 },
 'knew': {
  'notes': [],
  'summary': [
   B("What the public was told about Enron's business changed over the decade: its 1989 annual report said \"Enron's business is natural gas, from the reservoir to the burner tip\"; its 2000 annual report described \"a marketing and logistics company.\"", 'A-006', 'A-009'),
   B("In 1996 investors were told of three specific profit targets under the Enron 2000 plan.", 'A-008'),
   B("The revenue and asset figures readers saw in these years were Enron's reported numbers; some were later corrected.", 'A-010'),
   B("The sources differ on when Enron began mark-to-market accounting: Enron told the congressional tax staff 1992, while the Senate Governmental Affairs Committee staff found that a subsidiary used it for its 1991 results.", 'A-007', 'C-055'),
  ],
  'strip': [
   S('1990', 'Readers of Enron\'s 1989 annual report', "Were told \"Enron's business is natural gas, from the reservoir to the burner tip,\" as quoted by the congressional tax staff.", 'A-006'),
   S('1992-01-30', "SEC Office of the Chief Accountant", "Told Enron it would not object to mark-to-market accounting for a subsidiary starting in 1992. Enron replied that it would start from 1991; the Senate staff found the SEC apparently did not respond further.", 'C-055'),
   S('1996', 'Investors', "Were told of the Enron 2000 targets, including $1 billion of net income by 2000.", 'A-008'),
   S('2001', 'Investors and the public', "An Enron press release, cited by the congressional tax staff, put Enron's market capitalization at about $70 billion in early 2001.", 'A-011'),
  ],
  'ask_why': "In ten years Enron's own description of itself changed from a natural gas company to a marketing and logistics company. When a company describes its business that differently, what questions should readers of its annual report start asking?"
 }
}

# ---------------- Chapter 2 ----------------
L['ch2'] = {
 'money': {
  'notes': [
   note(2, 5, 'money', "Follow the money: compare the two growth rates. From 1999 to 2000, reported revenue rose about 150 percent ($40.1 billion to $100.8 billion), while reported net income rose about 10 percent ($893 million to $979 million). Money counted as revenue is not money kept as profit.", 'A-024', 'A-025'),
   note(2, 11, 'money', "Follow the money: the key words are \"unrealized\" and \"newly originated.\" Under this policy, a contract signed during the year could add to revenue before any cash from it arrived, and where market prices had to be estimated, the policy said they reflected management's \"best estimate.\"", 'A-020'),
   note(2, 13, 'money', "Follow the money: because changes in the market value of these stakes went into revenue, a falling share price at a company Enron had invested in could cut Enron's reported earnings that quarter. Chapter 3 shows how Enron tried to offset such losses.", 'A-021', 'A-022'),
   note(2, 15, 'money', "Follow the money: the special committee described a squeeze. Growth needed large investments up front; paying for them with more debt risked Enron's credit rating, and paying with more stock would dilute earnings per share. That squeeze is the background to the off-balance-sheet deals.", 'A-028'),
   note(2, 19, 'money', "Follow the money: the gap is large, $22.1 billion of debt against the $10.2 billion Enron reported for the end of 2000. The examiner summarized this conclusion from an earlier report that is not in this site's library, so the detailed calculation cannot be checked here.", 'A-067'),
  ],
  'summary': [
   B("In 2000 Enron's reported revenue more than doubled, while its reported net income rose by about a tenth.", 'A-024', 'A-025'),
   B("Under mark-to-market accounting, Enron counted unrealized gains on trading contracts and on its merchant investments as revenue, using management's estimates where no market price existed.", 'A-020', 'A-021'),
   B("The special committee found that Enron's growth needed large investments up front, and that keeping an investment-grade credit rating was \"vital\" to its energy trading business.", 'A-028'),
   B("The bankruptcy examiner concluded that six accounting techniques let Enron report $10.2 billion of debt at the end of 2000 rather than $22.1 billion.", 'A-067'),
  ],
  'ask_why': "If a company reports today the profit it expects from a contract over ten years, what happens to its reported profit in the later years? What pressure might that create to keep signing new contracts?"
 },
 'auditors': {
  'notes': [
   note(2, 11, 'auditors', "The Auditors: for contracts without a market price, the fair values came from management's estimates. The auditor had to judge whether the policy and the estimates were reasonable; Andersen's opinion on the 2000 statements said they presented Enron's financial position fairly, in conformity with GAAP.", 'A-020', 'A-027'),
   note(2, 18, 'auditors', "The Auditors: this is Andersen's standard clean, or unqualified, opinion. On November 8, 2001, Enron said that the audit reports for 1997 through 2000 \"should not be relied upon\" (Chapter 5).", 'A-027', 'A-083'),
  ],
  'summary': [
   B("Enron's 2000 Form 10-K described its fair-value policy, including that unrealized gains from newly originated contracts were counted as \"Other Revenues.\"", 'A-020'),
   B("Andersen's audit report, dated February 23, 2001, said Enron's 2000 financial statements \"present fairly, in all material respects\" its financial position.", 'A-027'),
   B("Enron later said that the audit reports for 1997 through 2000 \"should not be relied upon.\"", 'A-083'),
  ],
  'ask_why': "When a contract has no market price, management estimates its value and the auditor reviews the estimate. If you were the auditor, what evidence would you want before agreeing that an estimate of profits many years away is reasonable?"
 },
 'board': {
  'notes': [
   note(2, 17, 'board', "The Board: the committee was told that off-balance-sheet structures were used in many parts of Enron's business, even for its headquarters building. Some of these deals needed board approval: Chapter 3 shows the board's Executive Committee approving a guarantee for Chewco in 1997.", 'A-029', 'A-033'),
  ],
  'summary': [
   B("The special committee found that management preferred off-balance-sheet treatment because it made Enron look better on the ratios used by Wall Street analysts and rating agencies.", 'A-029'),
   B("Keeping its credit rating at investment grade was, in the committee's words, \"vital\" to Enron's energy trading business.", 'A-028'),
   B("Enron's public targets included $1 billion of net income by the year 2000.", 'A-008'),
  ],
  'ask_why': "A board approves strategy but relies on management for the numbers. If a company's growth depends on keeping debt off its balance sheet, what questions should directors ask before approving the deals that do it?"
 },
 'knew': {
  'notes': [
   note(2, 12, 'knew', "Who Knew What, When: the SEC's accounting office said it would not object to mark-to-market accounting for an Enron subsidiary starting in 1992; Enron replied that it would start a year earlier. The Senate staff found that the SEC apparently did not respond further.", 'C-055'),
  ],
  'summary': [
   B("The Senate Governmental Affairs Committee staff found that in January 1992 the SEC's Office of the Chief Accountant said it would not object to mark-to-market accounting for an Enron subsidiary from 1992, and that Enron replied it would start from 1991.", 'C-055'),
   B("The staff wrote: \"Apparently, the SEC did not respond further to this correspondence.\"", 'C-055'),
   B("Enron's annual report told readers that unrealized gains from newly originated contracts were counted as revenue..", 'A-020'),
   B("Enron's description of EnronOnline told readers that customers traded \"with Enron as principal,\" meaning Enron was on one side of every trade.", 'A-018'),
  ],
  'strip': [
   S('1992-01-30', "SEC Office of the Chief Accountant", "Told Enron it would not object to mark-to-market accounting for Enron Gas Services from 1992. Enron replied it would adopt the method from the start of 1991.", 'C-055'),
   S('2001', 'Readers of the 2000 Form 10-K', "Were told that on EnronOnline, launched in late 1999, customers traded \"with Enron as principal.\"", 'A-018'),
   S('2000-12-31', 'Investors', "Enron reported total debt of $10.2 billion. The bankruptcy examiner, in an earlier report summarized in his final one, later concluded that without six accounting techniques the figure would have been $22.1 billion.", 'A-026', 'A-067'),
   S('2001-02-23', 'Readers of the 2000 Form 10-K', "Were told by Andersen's audit report that the 2000 statements \"present fairly, in all material respects\" Enron's financial position.", 'A-027'),
  ],
  'ask_why': "Enron described its mark-to-market policy in its annual report. If a risk is disclosed in the fine print, who is responsible when most readers do not understand it: the company, the auditor, the regulator, or the reader?"
 }
}

# ---------------- Chapter 3 ----------------
L['ch3'] = {
 'money': {
  'notes': [
   note(3, 4, 'money', "Follow the money: Enron put in its own stock, while CalPERS put in cash. When CalPERS left, the new partner, Chewco, had to meet the SPE rules for JEDI to stay off Enron's balance sheet; the special committee found it did not.", 'A-031', 'A-035'),
   note(3, 7, 'money', "Follow the money: of Chewco's $11.5 million of \"equity,\" only about $125,000 came from Kopper. The rest was money from Barclays, and the $6.6 million of cash collateral meant the outside money was not truly at risk.", 'A-034', 'A-035'),
   note(3, 8, 'money', "Follow the money: about $125,000 in, about $10.5 million out, plus about $2 million in fees. The committee was told that Treasurer Jeff McMahon had proposed a $1 million return for the Chewco investors and that Fastow negotiated about $10 million. Fastow said he did not take part; the committee found that contrary to other evidence.", 'A-036', 'A-037'),
   note(3, 12, 'money', "Follow the money: in seven sales near the ends of two 1999 quarters, Enron later bought back five, and LJM made a profit every time; the committee noted plausible, more innocent explanations for some buybacks. Fastow told the board's Finance Committee these deals produced $229 million of \"earnings\" in the second half of 1999; the committee could not confirm that figure.", 'A-044'),
   note(3, 19, 'money', "Follow the money: by the committee's calculation, without the Raptors Enron's pre-tax earnings for July 2000 through September 2001 would have been $429 million instead of $1.506 billion, not counting the $710 million charge to end the Raptors; the committee noted it could not know what Enron would otherwise have done. For LJM2 the money came back fast: about $41 million on each $30 million investment within about six months.", 'A-054', 'A-053'),
   note(3, 21, 'money', "Follow the money: the committee's figures for individuals are minimums: \"at least\" $30 million for Fastow and \"at least\" $10 million for Kopper.", 'A-060'),
  ],
  'summary': [
   B("Chewco: the special committee found that Kopper and another investor turned $125,000 into about $10.5 million, and that Kopper was also paid about $2 million in fees.", 'A-036', 'A-037'),
   B("LJM: the committee found that more than 20 deals increased Enron's reported results \"by more than a billion dollars.\"", 'A-043'),
   B("Raptors: the committee calculated that without them, Enron's pre-tax earnings for five quarters would have been $429 million rather than $1.506 billion, a 72% decline (not counting the $710 million charge to end the Raptors; the committee noted it could not know what Enron would otherwise have done).", 'A-054', 'A-058'),
   B("The committee found that Fastow was enriched by at least $30 million and Kopper by at least $10 million.", 'A-060'),
  ],
  'ask_why': "In several of these deals a small investment by insiders produced a very large return. Where did that money ultimately come from, and who was carrying the risk?"
 },
 'auditors': {
  'notes': [
   note(3, 18, 'auditors', "The Auditors: the committee found Andersen was in a position to understand the Raptors and advised Enron at every step. Enron's records show Andersen billed $5.7 million for advice on the LJM and Chewco deals alone, beyond its regular audit fees.", 'A-052', 'A-061'),
  ],
  'summary': [
   B("Under the rules of the time, an independent owner had to invest at least 3% of an SPE's assets and keep it at risk, or the SPE belonged on the company's books.", 'A-030'),
   B("The committee found that Chewco's cash collateral was \"fatal\" to its compliance with the 3% requirement. In a January 2002 letter to Congress, Andersen's chief executive, Joseph Berardino, wrote that Andersen had not been told in 1997 of an agreement to put $6 million into a reserve account for Barclays' benefit, which left only about half of the required equity at risk. That is Andersen's own account.", 'A-035', 'G-035'),
   B("Andersen's chief executive, Joseph Berardino, said in a written statement to a House hearing in December 2001 that the firm's judgment that the Rhythms entity met the 3 percent test \"was in error.\"", 'G-032'),
   B("The committee found Andersen accountants \"closely involved in structuring the Raptors.\"", 'A-052'),
  ],
  'ask_why': "Andersen was paid to advise Enron on some of these deals and also to audit the results. What problems could arise when the same firm helps design a transaction and then judges whether it was accounted for correctly?"
 },
 'board': {
  'notes': [
   note(3, 5, 'board', "The Board: the swap of Kopper for Fastow mattered for disclosure. Fastow's role would have had to be disclosed in the proxy statement, the document sent to shareholders before their annual meeting; Kopper was not a senior officer, so his role did not require it.", 'A-032'),
   note(3, 6, 'board', "The Board: the Executive Committee approved the guarantee by conference call, based on a description of Chewco as \"an SPE not affiliated with either Enron or CalPERS.\" What the directors approved depended on what they were told.", 'A-033'),
   note(3, 9, 'board', "The Board: the directors did not simply learn of Fastow's role; they voted on it. The Senate subcommittee staff found that Lay approved waiving the code-of-conduct rule for Fastow and asked the board to ratify that decision, though company rules did not explicitly require it. Directors Winokur and Jaedicke later argued that the board had applied the code, not waived it.", 'F-006', 'F-007'),
   note(3, 10, 'board', "The Board: the controls rested on two officers and a yearly Audit Committee review. The special committee also saw no evidence that the board was told that Kopper and Glisan would help manage LJM2.", 'A-041', 'A-042'),
   note(3, 20, 'board', "The Board: twice the Raptors' credit problem was fixed so that Enron avoided a large charge: no reserve at the end of 2000, and only a $36.6 million reserve in March 2001 instead of a charge of more than $500 million. The committee saw no evidence the board was told of the December 2000 fix, and found that the March 2001 restructuring was apparently not disclosed to or authorized by the board.", 'A-056', 'A-057', 'F-023'),
   note(3, 22, 'board', "The Board: this is where the board's safeguards met practice. The committee found that neither Causey nor Buy ignored his responsibilities, but that they did not give the deals \"the degree of review the Board believed was occurring.\"", 'F-011', 'A-062'),
  ],
  'summary': [
   B("The board approved Fastow's role in LJM1 in June 1999 and in LJM2 in October 1999, ratifying a determination that his participation would not adversely affect Enron.", 'A-040', 'A-041', 'F-007'),
   B("The Senate subcommittee staff called it \"an unprecedented arrangement allowing Enron's Chief Financial Officer to establish and operate the LJM private equity funds.\"", 'B-072'),
   B("The special committee found that the officers assigned to review the deals interpreted their roles very narrowly, and that Skilling was almost entirely uninvolved despite what the board had been told.", 'F-011', 'A-062'),
   B("The committee saw no evidence that the board was informed of the Raptors' credit problem in December 2000 or of how it was fixed.", 'A-056'),
  ],
  'ask_why': "The board was told that Skilling had taken on a significant role in reviewing the LJM deals; the special committee found he was almost entirely uninvolved. How can a board check that the controls it approved are actually working?"
 },
 'knew': {
  'notes': [
   note(3, 6, 'knew', "Who Knew What, When: the accounts differ. Lay said he was not informed of Kopper's role in Chewco; Skilling said he approved it and believed he had discussed it with the board; the committee found no written record that the board was told.", 'A-033'),
   note(3, 11, 'knew', "Who Knew What, When: LJM2's outside investors were told in writing that Fastow's position at Enron was an advantage. The committee saw no evidence the board was told that Kopper and Glisan were also named as managers.", 'A-042'),
   note(3, 15, 'knew', "Who Knew What, When: doubts inside Enron were raised early. Kaminski told the committee that he was very uncomfortable with the Rhythms deal in 1999 and brought his concerns to his supervisor, Richard Buy; Buy said he did not recall those discussions. Causey did not recall the later 68% estimate.", 'F-014', 'A-049'),
   note(3, 23, 'knew', "Who Knew What, When: the partnerships were not hidden from the filings; they were mentioned. The committee's point is about understanding: a reader could learn that the deals existed without learning what they did.", 'A-064'),
  ],
  'summary': [
   B("Lay told the special committee he was not informed of Kopper's role in Chewco, and the committee found no written record that the board was told.", 'A-033'),
   B("LJM2's investors were told in writing that Fastow's \"access to Enron's information pertaining to potential investments will contribute to superior returns.\"", 'A-042'),
   B("Kaminski told the committee that his group estimated, in early 2000, a 68% probability that the Rhythms structure would default; Causey told the committee he did not recall that figure.", 'A-049'),
   B("Enron's filings did mention the partnerships, but the committee found the disclosures \"obtuse.\"", 'A-064'),
  ],
  'strip': [
   S('1997-11-05', "Enron board's Executive Committee", "Approved Enron's guarantee of Chewco's loans after Fastow described Chewco as \"an SPE not affiliated with either Enron or CalPERS\"; the special committee found no written record that Kopper's role was disclosed.", 'A-033'),
   S('1999-06-28', 'Enron board', "Was told Fastow would be general partner of LJM1, and ratified a determination that his participation would not adversely affect Enron.", 'A-040', 'F-007'),
   S('1999-06', 'Richard Buy (Chief Risk Officer)', "Kaminski told the special committee he brought his concerns about the Rhythms deal to Buy; Buy said he did not recall those discussions.", 'F-014'),
   S('1999-10', 'LJM2 investors', "Were told in LJM2's offering document that Fastow's access to Enron's information would \"contribute to superior returns.\"", 'A-042'),
   S('2000', "Vince Kaminski (head of research)", "Told the special committee that his group estimated, in early 2000, a 68% probability that the Rhythms structure would default on what it owed Enron; Causey told the committee he did not recall this.", 'A-049'),
   S('2000-10', 'LJM2 investors', "Fastow reported rates of return of 193%, 278%, 2500% and a projected 125% on the four Raptors.", 'A-053'),
   S('2000-12-22', 'Enron board', "The special committee saw no evidence the board was informed of the Raptors' credit problem or of the fix chosen that day.", 'A-056'),
  ],
  'ask_why': "Some people inside Enron raised doubts about the Rhythms deal in 1999 and 2000, but their memories and others' differ. When recollections conflict years later, what kinds of records would help an investigator decide who knew what?"
 }
}

# ---------------- Chapter 4 ----------------
L['ch4'] = {
 'money': {
  'notes': [
   note(4, 11, 'money', "Follow the money: the $700 million Watkins described was owed to Enron by entities whose ability to pay rested mainly on Enron's own stock (Chapter 3). If that stock fell, the money might never come.", 'B-056', 'A-051'),
   note(4, 15, 'money', "Follow the money: ending the Raptors cost Enron a payment of about $35 million to LJM2 and a charge of about $710 million before taxes in the third quarter of 2001 (Chapter 5).", 'A-058'),
  ],
  'summary': [
   B("Watkins testified that by August 2001 the Raptors owed Enron more than $700 million under hedging agreements.", 'B-056'),
   B("The special committee found that in August 2001 Enron and Andersen accountants realized Enron had wrongly counted IOUs for stock issued to the Raptors as increases to equity.", 'A-059'),
   B("According to the Justice Department's announcement, the indictment alleged that in the two months before his September 26, 2001 employee forum, Lay bought $4 million of Enron stock while selling $24 million through nonpublic transactions. These are allegations.", 'B-007'),
   B("Enron ended the Raptors on September 28, 2001, paying LJM2 about $35 million.", 'A-058'),
  ],
  'ask_why': "The Raptors were supposed to protect Enron's earnings, but by 2001 they owed Enron hundreds of millions of dollars they might not be able to pay. At what point does a promise to pay stop being worth counting as an asset?"
 },
 'auditors': {
  'notes': [
   note(4, 2, 'auditors', "The Auditors: \"push limits\" and \"others could have a different view\" describe accounting that Andersen accepted but saw as open to challenge. According to the Senate subcommittee staff, the annotated copy was not given to the Audit Committee during the meeting, but the risk profile was discussed with it.", 'B-063'),
   note(4, 6, 'auditors', "The Auditors: the request to remove Bass came from the client's chief accounting officer, Bass was told. The examiner reported that another Andersen partner, John Stewart, testified at Andersen's 2002 trial that he found Enron's request unprofessional and was upset that the firm had agreed to it.", 'C-034'),
   note(4, 13, 'auditors', "The Auditors: this is the Raptor stock error that became $1 billion of the $1.2 billion cut to equity in October (Chapter 5). The bankruptcy examiner later reported that Andersen accountants acknowledged it as one of three audit errors.", 'A-059', 'C-030'),
  ],
  'summary': [
   B("In February 1999, according to the Senate subcommittee staff, Andersen's lead partner wrote that many of Enron's practices \"push limits.\"", 'B-063'),
   B("On February 5, 2001, senior Andersen partners rated Enron a \"maximum\" risk client and decided to keep it; the Senate Governmental Affairs Committee staff found that the next day's e-mail noted how \"aggressive\" Enron's accounting was.", 'C-033', 'C-056'),
   B("In early 2001, the examiner reported, Carl Bass was told that Causey had asked for his removal from the Enron engagement and that Andersen had agreed.", 'C-034'),
   B("In August 2001, the special committee found, Enron and Andersen accountants realized Enron had made an accounting error in issuing stock to the Raptors.", 'A-059'),
  ],
  'ask_why': "Andersen's own partners described Enron's accounting as high-risk and aggressive, yet in February 2001 the firm issued a clean opinion on Enron's 2000 statements. What options does an auditor have when a client's accounting is allowed by the rules but pushes their limits?"
 },
 'board': {
  'notes': [
   note(4, 2, 'board', "The Board: the Audit Committee is the board's direct line to the outside auditor. Another Andersen partner confirmed, through his lawyer, that Andersen's risk profile was discussed with the committee in February 1999, the Senate subcommittee staff reported.", 'B-063'),
   note(4, 3, 'board', "The Board: Jaedicke's testimony and the subcommittee's conclusion differ in emphasis. He testified the committee knew of \"high-risk and innovative transactions\"; the subcommittee staff found that its investigation \"did not substantiate the claims that the Enron Board members challenged management and asked tough questions.\"", 'B-078', 'B-074'),
  ],
  'summary': [
   B("Andersen's risk profile of Enron's accounting was discussed with the Audit Committee in February 1999, according to the Senate subcommittee staff.", 'B-063'),
   B("Audit Committee chairman Robert Jaedicke testified that the committee \"knew that the company was engaged in high-risk and innovative transactions,\" but that, as far as he recalled, he never heard terms such as \"form over substance\" used.", 'B-078'),
   B("The directors the Senate subcommittee staff interviewed said they saw neither Watkins's letter nor the law firm's report on it until after Enron had begun to collapse.", 'F-002'),
   B("The special committee found that in mid-September 2001 Lay and Enron's chief operating officer, Greg Whalley, directed Causey to end the Raptors.", 'A-058'),
  ],
  'ask_why': "The directors said they did not see Watkins's letter until Enron had begun to collapse. Should a board expect to hear about an employee's warning sent to its chairman? How could it make sure it does?"
 },
 'knew': {
  'notes': [
   note(4, 5, 'knew', "Who Knew What, When: by February 2001, an Andersen partner's e-mail about the client-retention meeting noted how \"aggressive\" Enron's accounting was, the Senate staff found. That was six months before Watkins wrote to Lay.", 'C-056', 'C-033'),
   note(4, 8, 'knew', "Who Knew What, When: this is Skilling's own sworn account of what he believed when he left. The SEC later alleged that he took part in a scheme to defraud from at least 1999; Chapter 7 explains how his criminal case ended.", 'B-023', 'B-019'),
   note(4, 10, 'knew', "Who Knew What, When: Watkins testified that she gave Lay her anonymous letter on August 15, 2001. The letter said, as the Senate subcommittee staff quoted it, that \"Skilling's abrupt departure will raise suspicions of accounting improprieties and valuation issues.\"", 'B-055', 'F-001', 'F-004'),
   note(4, 11, 'knew', "Who Knew What, When: by August 22, Watkins testified, Lay had heard from her in person that the Raptors owed Enron more than $700 million. Lay did not answer questions about this before Congress; declining to testify is a legal right and is not evidence of guilt.", 'B-056', 'B-008'),
   note(4, 14, 'knew', "Who Knew What, When: the SEC alleged these September 26 statements were false and misleading. Lay was later convicted, but his conviction was vacated after his death (Chapter 7).", 'B-004', 'B-011'),
   note(4, 16, 'knew', "Who Knew What, When: the SEC is the public's regulator, but its staff had not reviewed Enron's annual reports after 1997. The Senate staff concluded a review of the 2000 report would likely have prompted questions.", 'C-053', 'C-054'),
  ],
  'summary': [
   B("Andersen's lead partner wrote in February 1999 that many practices \"push limits\"; a partner's February 2001 e-mail called the accounting \"aggressive,\" according to the Senate staff reports.", 'B-063', 'C-056'),
   B("Watkins testified that she sent Lay an anonymous letter on August 15, 2001 and met him on August 22.", 'B-055', 'B-056'),
   B("In August 2001, Enron and Andersen accountants realized the Raptor stock accounting was an error, the special committee found.", 'A-059'),
   B("On September 26, 2001, the SEC alleged, Lay told employees: \"[t]he third quarter is looking great. We will hit our numbers.\"", 'B-004'),
  ],
  'strip': [
   S('1999-02-07', "Enron's Audit Committee", "Andersen's risk profile was discussed with the committee, according to the Senate subcommittee staff; Duncan's handwritten \"push limits\" note was not given to it during the meeting.", 'B-063'),
   S('2001-02-05', 'Senior Andersen partners', "Rated Enron a \"maximum\" risk client and decided to keep it; the next day's e-mail noted how \"aggressive\" its accounting was.", 'C-033', 'C-056'),
   S('2001-08-14', 'Jeffrey Skilling', "Resigned. He later testified: \"When I left Enron on August 14, I did not believe the company was in financial peril.\"", 'B-023'),
   S('2001-08-15', 'Kenneth Lay', "Watkins testified that she gave him her anonymous letter that day. It said: \"I am incredibly nervous that we will implode in a wave of accounting scandals.\"", 'B-055', 'F-004'),
   S('2001-08-22', 'Kenneth Lay', "Watkins testified she told him in person that the Raptors owed Enron more than $700 million.", 'B-056'),
   S('2001-08', 'Enron and Andersen accountants', "Realized Enron had made an accounting error when it issued stock to the Raptors, the special committee found.", 'A-059'),
   S('2001-09-26', 'Enron employees', "The SEC alleged that Lay told them in an online forum that the third quarter was \"looking great.\"", 'B-004'),
  ],
  'ask_why': "Between February and September 2001, warnings reached Andersen's partners, Enron's accountants and, Watkins testified, Enron's chairman, while, the SEC alleged, employees were told the quarter was \"looking great.\" At what point should the public have been told, and whose job was it to tell them?"
 }
}

# ---------------- Chapter 5 ----------------
L['ch5'] = {
 'money': {
  'notes': [
   note(5, 1, 'money', "Follow the money: note the split between \"recurring\" earnings, which Enron led with, and $1.01 billion of \"non-recurring charges.\" In the same release, the examiner reported, Lay said Enron was \"very confident in our strong earnings outlook.\" The quarter's bottom line was a $618 million loss.", 'A-075', 'F-005'),
   note(5, 3, 'money', "Follow the money: this cut was disclosed on a call, not in the written release. About $1 billion of it reversed equity Enron had recorded in exchange for IOUs from the Raptors rather than cash.", 'A-076', 'A-059'),
   note(5, 6, 'money', "Follow the money: in Enron's last weeks, more than $50 million went out to some senior managers as early payouts of deferred pay, the examiner reported. He did not name the individuals in this passage.", 'A-082'),
   note(5, 9, 'money', "Follow the money: across 1997 to 2000, the restatement reduced reported net income by about $613 million in total (our sum of the four figures), and added between $561 million and $711 million of debt in each year.", 'A-085'),
   note(5, 12, 'money', "Follow the money: these were debt triggers: terms that could make debts come due early if Enron's credit rating fell (for some, only if its stock price was also low). One downgrade meant a $690 million note would come due unless Enron posted collateral, and about $3.9 billion more could follow.", 'A-080'),
   note(5, 13, 'money', "Follow the money: this is the chapter's biggest gap: $12.978 billion of debt on the balance sheet, and $38.094 billion in the figure Enron gave its bankers. The examiner noted that he had formed no opinion on whether all of these obligations were properly classified as debt.", 'A-087', 'F-019'),
   note(5, 19, 'money', "Follow the money: the bankruptcy examiner described prepays as loans that Enron reported as trading liabilities rather than debt. The Senate staff also found what it called a \"sham\" sale funded by a $200 million Citigroup loan that inflated Enron's year-end 2000 earnings by $112 million.", 'A-068', 'A-073'),
  ],
  'summary': [
   B("On October 16, 2001, Enron reported $1.01 billion of after-tax non-recurring charges and a third-quarter loss of $618 million.", 'A-075'),
   B("Enron's November 19 quarterly report restated net income lower for each year from 1997 to 2000 and added $561 million to $711 million of debt in each year.", 'A-085'),
   B("That same day Enron told its bankers its debt was $38.094 billion, while its balance sheet showed $12.978 billion.", 'A-087'),
   B("Enron filed for bankruptcy on December 2, 2001, and on February 12, 2002 said it did not expect shareholders to receive anything.", 'A-092', 'A-094'),
  ],
  'ask_why': "On the same day, Enron's balance sheet showed about $13 billion of debt, while its bankers were shown about $38 billion. How can two figures for the same company's debt be so far apart, and which should an investor rely on?"
 },
 'auditors': {
  'notes': [
   note(5, 3, 'auditors', "The Auditors: this $1 billion correction is one of the three errors that, according to the bankruptcy examiner, Andersen accountants later acknowledged: letting Enron record the Raptor notes as assets, which overstated Enron's equity by $1 billion.", 'C-030'),
   note(5, 8, 'auditors', "The Auditors: an audit opinion is only useful if readers can rely on it. Enron's November 19 quarterly report repeated that the 1997-2000 audit reports \"should not be relied upon,\" and said Andersen had been unable to finalize its review of the quarter.", 'A-078'),
  ],
  'summary': [
   B("About $1 billion of the $1.2 billion cut to shareholders' equity corrected the Raptor accounting error, the special committee found.", 'A-059'),
   B("On November 8, 2001, Enron said its financial statements and Andersen's audit reports for 1997 through 2000 \"should not be relied upon.\"", 'A-083'),
   B("Enron's restatement consolidated Chewco, JEDI and an LJM1 entity and recorded prior-year audit adjustments.", 'A-083'),
   B("Enron's November 19 quarterly report said Andersen had been unable to finalize its review of the quarter.", 'A-078'),
  ],
  'ask_why': "Enron told investors not to rely on four years of audit reports. What does it mean for an auditor when a client has to say that, and who should bear the consequences?"
 },
 'board': {
  'notes': [],
  'summary': [
   B("Enron's board formed a special committee in late October 2001, later chaired by William Powers Jr., to investigate the partnerships.", 'A-066'),
   B("The directors the Senate subcommittee staff interviewed said they did not see Watkins's letter or the law firm's report on it until after Enron had begun to collapse.", 'F-002'),
   B("On January 17, 2002, Enron's board voted to terminate Andersen as its auditor.", 'C-037'),
  ],
  'ask_why': "Enron went from its October earnings announcement to bankruptcy in about seven weeks. What should a board do when a crisis unfolds in days rather than over the months between its regular meetings?"
 },
 'knew': {
  'notes': [
   note(5, 5, 'knew', "Who Knew What, When: the SEC's request came on October 17; Enron announced it on October 22, five days later.", 'A-081', 'F-018'),
   note(5, 6, 'knew', "Who Knew What, When: the examiner dates these early payouts from about October 25, after the SEC's request and Fastow's leave had been announced. He does not say what the recipients knew.", 'A-082', 'F-018'),
   note(5, 14, 'knew', "Who Knew What, When: most analysts kept recommending the stock after the bad news. The Senate staff tied this to their firms' investment-banking interests.", 'C-057'),
   note(5, 18, 'knew', "Who Knew What, When: the examiner's \"tip of the iceberg\" is about timing: some information became public only shortly before and after the bankruptcy filing.", 'A-096'),
  ],
  'summary': [
   B("The SEC asked Enron for information on October 17, 2001; Enron announced the request on October 22; the SEC opened a formal investigation on October 31.", 'A-081'),
   B("From about October 25, some senior managers requested and received early payouts of deferred compensation totaling more than $50 million, the examiner reported.", 'A-082'),
   B("The Senate Governmental Affairs Committee staff found that all 15 analysts covering Enron were recommending its stock when the news first came out, and 10 of 15 still were three weeks later.", 'C-057'),
   B("The staff found that the credit rating agencies kept Enron at investment grade until November 28, four days before the bankruptcy filing, and concluded that they did not exercise proper diligence.", 'C-059', 'C-060'),
  ],
  'strip': [
   S('2001-10-16', "Analysts and investors on Enron's conference call", "Were told Enron would reduce shareholders' equity by $1.2 billion, a figure not disclosed in the written earnings release.", 'A-076'),
   S('2001-10-17', 'Enron', "The SEC asked Enron to provide information voluntarily about its related-party deals.", 'A-081'),
   S('2001-10-22', 'The public', "Enron announced the SEC's request for information.", 'F-018'),
   S('2001-10-24', 'The public', "Enron announced that Fastow was on leave and would be replaced as chief financial officer.", 'F-018'),
   S('2001-11-08', 'Investors', "Were told that Enron's financial statements and audit reports for 1997 through 2000 \"should not be relied upon.\"", 'A-083'),
   S('2001-11-19', "Enron's banks", "Were told at a meeting that Enron's debt was $38.094 billion; its balance sheet showed $12.978 billion.", 'A-087'),
   S('2001-11-28', 'Credit rating agencies', "All three cut Enron below investment grade, four days before the bankruptcy filing.", 'C-059'),
  ],
  'ask_why': "Analysts and rating agencies kept favorable views of Enron for weeks after its problems became public. Were they missing information, or not acting on information they had? What would you need to know to tell the difference?"
 }
}

# ---------------- Chapter 6 ----------------
L['ch6'] = {
 'money': {
  'notes': [
   note(6, 4, 'money', "Follow the money: about $50 million a year from a single client. The examiner quotes an internal Andersen e-mail saying Enron had become the firm's largest client \"by a wide margin\" in fiscal 1999.", 'C-022'),
  ],
  'summary': [
   B("The examiner reported that Enron was one of Andersen's most significant clients by fees, and that those fees kept rising.", 'C-022'),
   B("The Senate Governmental Affairs Committee staff found $52 million in 2000 fees: $25 million for audit work and $27 million for consulting. Andersen partner Michael Odom testified that much of the \"consulting\" was work typically done by the auditor.", 'C-019', 'C-020'),
   B("Enron's records show Andersen billed $5.7 million for advice on the LJM and Chewco deals alone.", 'A-061'),
   B("A former SEC commissioner told a House committee that non-audit services made up 73 percent of what audit clients paid their auditors, on average, in 2001.", 'C-025'),
  ],
  'ask_why': "An auditor is paid by the company it audits. If you were designing the system from scratch, who would pay the auditor, and how would that change the auditor's incentives?"
 },
 'auditors': {
  'notes': [
   note(6, 3, 'auditors', "The Auditors: Andersen's own rule rotated lead partners after seven years. The Sarbanes-Oxley Act later made rotation law: an audit firm may not audit a company if its lead or reviewing partner has done so in each of the five previous years.", 'C-036', 'C-075'),
   note(6, 4, 'auditors', "The Auditors: the disagreement is over labels. The Senate staff counted $27 million as consulting; Andersen said much of it was audit-type work. Either way, the examiner found Enron was one of Andersen's \"most significant clients in terms of fees.\"", 'C-019', 'C-020', 'C-022'),
   note(6, 5, 'auditors', "The Auditors: Sarbanes-Oxley later made it unlawful for an audit firm to provide certain non-audit services to a company it audits, and required the audit committee to approve other non-audit services in advance.", 'C-074'),
   note(6, 6, 'auditors', "The Auditors: in his spoken statement to the same December 2001 hearing, Berardino said that on the smaller of the two SPEs behind the restatement, Andersen's team had made \"an error in judgment. An honest error, but an error nonetheless.\" He said important information about the larger one appeared not to have been revealed to Andersen.", 'G-033'),
   note(6, 8, 'auditors', "The Auditors: Duncan wrote in December 2000 that the presentation had to fit \"about a 30 – 45 minute presentation,\" so \"we necessarily have to stay at a certain level.\" The examiner's conclusion is about what a fact-finder could find, not a court finding.", 'C-035', 'F-022', 'C-031'),
   note(6, 9, 'auditors', "The Auditors: telling employees to follow a retention policy is not wrong in itself. The Supreme Court's Syllabus notes that \"under ordinary circumstances, it is not wrongful for a manager to instruct his employees to comply with a valid document retention policy.\" The questions in this case were about intent and timing.", 'C-044'),
   note(6, 12, 'auditors', "The Auditors: two accounts conflict here. Andersen's witness said Duncan acted without consulting others or, so far as Andersen knew, its lawyers; Duncan, as the chairman summarized his interview, said he acted on the lawyer's e-mail. Duncan declined to answer questions at the hearing.", 'C-011', 'C-002', 'C-007'),
   note(6, 15, 'auditors', "The Auditors: the charge was against the firm itself, and it concerned persuading employees to withhold and destroy records, not the quality of the Enron audits.", 'G-015'),
   note(6, 16, 'auditors', "The Auditors: GAO's wording points to the indictment itself, in March 2002, as what led partners, staff and clients to leave, months before the June verdict and years before the 2005 reversal.", 'C-047', 'C-048'),
   note(6, 17, 'auditors', "The Auditors: the reversal came nearly three years after Andersen had stopped practicing before the SEC at the end of August 2002. The Court found the jury instructions flawed; it did not find the firm innocent.", 'G-018', 'C-040'),
   note(6, 18, 'auditors', "The Auditors: the SEC's 2008 actions concerned the audits themselves. The SEC alleged Duncan was reckless in not knowing that his audit reports for 1998-2000 were materially false and misleading; three other partners consented, without admitting or denying, to findings of improper professional conduct.", 'B-060', 'G-029', 'G-030'),
   note(6, 19, 'auditors', "The Auditors: with four firms auditing 99 percent of public companies' annual sales, large companies have few choices. In a GAO follow-up survey, 84 percent of the large public companies GAO surveyed said they wanted more audit firms to choose from.", 'C-046', 'C-052'),
  ],
  'summary': [
   B("Andersen audited Enron from 1985; in February 2001, 113 Andersen professionals worked on the engagement.", 'C-026', 'C-023'),
   B("Andersen earned about $50 million from Enron in 2000; sources give $47.9 million to $54 million depending on the year and categories used.", 'C-019', 'C-021'),
   B("Andersen was indicted on March 7, 2002 and convicted of obstruction on June 15, 2002; the Supreme Court unanimously reversed the conviction on May 31, 2005.", 'C-038', 'G-018', 'G-019'),
   B("GAO reported that the largest audit firms fell from eight to four, partly through the abrupt dissolution of Andersen in 2002.", 'C-045'),
  ],
  'ask_why': "Andersen's conviction was reversed, but the firm was already gone. When a charge alone can destroy an audit firm, what should prosecutors weigh in deciding whether to charge the firm rather than individual people?"
 },
 'board': {
  'notes': [
   note(6, 8, 'board', "The Board: the Audit Committee relies on the auditor to explain unusual accounting. The examiner concluded a fact-finder could find Andersen did not make sure the committee was informed; one director later testified that the directors \"asked probing questions\" (Chapter 7).", 'C-031', 'B-075'),
  ],
  'summary': [
   B("From 1997 to November 2001, Enron's Audit Committee met thirty times, usually with at least three Andersen partners present; meetings generally lasted about an hour.", 'C-035'),
   B("The examiner concluded that a fact-finder could find Andersen failed its duty to make sure the Audit Committee understood how significant unusual transactions were accounted for.", 'C-031'),
   B("At the February 10, 1997 Audit Committee meeting, Andersen reported that its seven-year rotation rule ended its lead partner's role, and David Duncan took over.", 'C-036'),
   B("On January 17, 2002, Enron's board voted to terminate Andersen as its auditor.", 'C-037'),
  ],
  'ask_why': "Enron's Audit Committee usually met with Andersen for about an hour at a time. How much time, and what kind of information, would a committee need to oversee the audit of a company as complex as Enron?"
 },
 'knew': {
  'notes': [
   note(6, 7, 'knew', "Who Knew What, When: the examiner's view is that Andersen did not know everything: Enron officers withheld information in numerous instances, including undisclosed side agreements guaranteeing supposedly at-risk equity. He also concluded that this did not explain the whole of Andersen's role.", 'C-029', 'C-027'),
   note(6, 9, 'knew', "Who Knew What, When: the indictment alleged that by October 16, 2001, Andersen knew significant facts the public did not, including that it had been told of Watkins's concerns and that on about October 9 it had hired an outside law firm in anticipation of litigation. These are allegations; the conviction that followed was later reversed.", 'G-017', 'G-018'),
   note(6, 11, 'knew', "Who Knew What, When: the SEC made its request to Enron on October 17. By the chairman's summary of his interview, Duncan first learned of the SEC's informal inquiry on October 19 or 20. The urgent meeting was October 23.", 'C-012', 'C-005'),
  ],
  'summary': [
   B("The examiner found evidence that Enron officers withheld information from Andersen in numerous instances.", 'C-029'),
   B("The indictment alleged that by October 16, 2001, Andersen was aware of significant facts unknown to the public. These are allegations.", 'G-017'),
   B("Andersen's lawyer e-mailed a partner on October 12 suggesting the engagement team be reminded of the retention policy; the SEC made its request to Enron on October 17; Duncan called an urgent meeting of the Enron team on October 23.", 'C-001', 'C-012', 'C-011'),
   B("The destruction appeared to stop after November 9, the day after Andersen received an SEC subpoena, Andersen said.", 'C-013'),
  ],
  'strip': [
   S('2001-09-28', 'Nancy Temple (Andersen lawyer)', "Testified that she was first asked that day to join a call about an Enron accounting issue.", 'C-018'),
   S('2001-10-09', 'Andersen', "The indictment alleged that on about this date, anticipating litigation, Andersen hired an outside New York law firm. This is an allegation.", 'G-017'),
   S('2001-10-12', 'Andersen partner Michael Odom', "Received Temple's e-mail: \"It might be useful to consider reminding the engagement team of our documentation and retention policy.\"", 'C-001'),
   S('2001-10-17', 'Enron', "The SEC requested information from Enron about its financial accounting and reporting, Andersen said.", 'C-012'),
   S('2001-10-19', 'David Duncan', "Learned of the SEC's informal inquiry on October 19 or 20, according to a House subcommittee chairman's summary of his staff interview.", 'C-005'),
   S('2001-10-23', 'Enron engagement team', "Duncan called an urgent meeting; Andersen's C.E. Andrews testified that Duncan organized an expedited effort to shred or otherwise dispose of Enron documents.", 'C-011'),
   S('2001-11-09', 'Andersen secretaries', "Duncan's assistant e-mailed \"no more shredding,\" the day after Andersen received an SEC subpoena.", 'C-013'),
   S('2002-01-04', 'Justice Department and SEC', "Andersen notified them of the document destruction.", 'C-015'),
  ],
  'ask_why': "Andersen's lawyer suggested on October 12 that the Enron team be reminded of the retention policy, and, by Andersen's account, the shredding stopped shortly after November 9. What would an employee need to know, and when, to tell routine housekeeping from something else?"
 }
}

# ---------------- Chapter 7 ----------------
L['ch7'] = {
 'money': {
  'notes': [
   note(7, 3, 'money', "Follow the money: the sources give different totals because they cover different periods: over $77 million from October 2000 to October 2001 (Senate subcommittee staff); $77.5 million from January to November 2001 (an SEC allegation); and over $94 million from May 1999 to October 2001 (the bankruptcy examiner).", 'B-016', 'B-005', 'B-014'),
   note(7, 6, 'money', "Follow the money: Kopper's $12 million combines $4 million of criminal forfeiture with $8 million paid in the SEC's case. For Fastow, the Justice Department's 2004 announcement gives a forfeiture of more than $29 million and its 2006 announcement more than $20 million; the library does not explain the difference.", 'B-039', 'G-013', 'G-002', 'G-004'),
   note(7, 10, 'money', "Follow the money: these were settlements of civil charges, paid without admitting or denying the SEC's allegations. The Senate subcommittee staff had described the underlying prepays as more than $8 billion of transactions (Chapter 5).", 'B-086', 'A-072'),
   note(7, 11, 'money', "Follow the money: many employees' retirement savings rose and fell with the same company that paid their salaries. The chairman of the plan's administrative committee told the committee that employees could choose among 20 investment options, but could not move the Enron stock match before age 50.", 'C-061', 'C-068'),
  ],
  'summary': [
   B("The Senate subcommittee staff found that the board failed to monitor Lay's company-financed credit line, which he used to obtain over $77 million in one year and repaid with Enron stock.", 'B-016'),
   B("Criminal cases recovered money: Kopper agreed to $12 million covering his plea and the SEC case; and a 2013 agreement says more than $40 million forfeited from Skilling's assets had been available for years for victims.", 'G-013', 'G-028'),
   B("J.P. Morgan Chase agreed to pay $135 million and Citigroup $120 million to settle SEC charges, without admitting or denying the allegations.", 'B-086'),
   B("GAO cited Labor Department figures that 63 percent of Enron's 401(k) assets were in company stock at the end of 2000; a congressman told the committee the plan lost about $1 billion in value.", 'C-062', 'C-065'),
  ],
  'ask_why': "Enron matched employees' retirement savings with Enron stock that they could not move until age 50. What are the risks of holding your savings in the company you work for, and should the law limit it?"
 },
 'auditors': {
  'notes': [],
  'summary': [
   B("The Supreme Court reversed Andersen's conviction in 2005 because the jury had been wrongly instructed.", 'G-018'),
   B("Sarbanes-Oxley created the Public Company Accounting Oversight Board to oversee audits of public companies; at the signing, President Bush said, \"The auditors will be audited.\"", 'C-072', 'C-071'),
   B("The Act banned certain non-audit services for audit clients and required lead and reviewing audit partners to rotate after five years.", 'C-074', 'C-075'),
   B("Section 404 requires a company's auditor to attest to and report on management's assessment of internal control over financial reporting.", 'C-078'),
  ],
  'ask_why': "Sarbanes-Oxley requires that two, and only two, of the PCAOB's five members be or have been certified public accountants. Why might Congress have wanted most of the people overseeing auditors not to be accountants?"
 },
 'board': {
  'notes': [
   note(7, 1, 'board', "The Board: the judgments about the board in the special committee's report came from its two new members, Powers and Troubh, who had not been directors during the events. Winokur, a director since 1985, did not join them.", 'F-015', 'A-063'),
   note(7, 2, 'board', "The Board: the staff reported that all 13 directors it interviewed disagreed with the special committee's conclusion that the board failed in its oversight, and that all five witnesses rejected any share of responsibility.", 'B-074'),
   note(7, 4, 'board', "The Board: the examiner separated two questions. On responding to red flags, he did not find that the outside directors acted in bad faith; on approving the Rhythms and certain Raptor hedges, he concluded a fact-finder could find that certain outside directors breached their duty of good faith. None of the outside directors invoked the Fifth Amendment with him.", 'B-080', 'B-013', 'B-081'),
  ],
  'summary': [
   B("Two of the special committee's three members concluded that \"the Board of Directors failed, in our judgment, in its oversight duties.\"", 'A-063'),
   B("The Senate subcommittee staff found that the board \"failed to safeguard Enron shareholders,\" while the directors who testified rejected any share of responsibility.", 'B-071', 'B-074'),
   B("The bankruptcy examiner concluded that a fact-finder could find certain outside directors breached their duty of good faith in approving the Rhythms and certain Raptor hedges, but that the evidence does not support bad faith in failing to respond to red flags.", 'B-080'),
   B("The library documents show no charges against the outside directors.", 'B-082'),
  ],
  'ask_why': "Three investigations judged Enron's board, and the directors disagreed with them. Winokur called Enron \"a cautionary reminder of the limits of a director's role.\" Where should a part-time director's responsibility end?"
 },
 'knew': {
  'notes': [
   note(7, 12, 'knew', "Who Knew What, When: GAO noted that executives faced no similar limits on company stock they held outside the plan. During the lockdown, employees in the plan could not act on the news.", 'C-063'),
  ],
  'summary': [
   B("Lay was sworn in before a Senate committee in February 2002 and declined to testify, invoking his Fifth Amendment right; he later gave the examiner a one-day interview that was not under oath.", 'B-008', 'B-015'),
   B("Skilling testified that he did not believe Enron was in financial peril when he left. A jury later convicted him on nineteen counts. After the Supreme Court's 2010 ruling limiting one legal theory used against him, the appeals court in 2011 found the error harmless and affirmed his convictions on all counts.", 'B-023', 'B-025', 'B-028', 'G-024'),
   B("The Justice Department announced that Fastow admitted he and other members of Enron's senior management conspired to manipulate Enron's reported financial results.", 'G-003'),
   B("The examiner concluded a fact-finder could find that Lay and Skilling were at least negligent in failing to respond to red flags about the misuse of SPEs.", 'B-012'),
  ],
  'strip': [
   S('2001-10-15', 'Jan Fleetham (Enron employee)', "Told the committee, in her written statement, that on October 15 she received a letter dated October 8 saying she could not access her 401(k) account from October 20 to November 19, 2001. Other accounts of the lockdown's dates differ.", 'C-066', 'C-065'),
   S('2001-11-16', 'Labor Department', "Opened an investigation of Enron's pension plans, over two weeks before the bankruptcy.", 'C-069'),
   S('2002-02-12', 'Kenneth Lay', "Was sworn in before the Senate Commerce Committee and declined to answer questions, invoking his Fifth Amendment right. That is not evidence of guilt.", 'B-008'),
   S('2002-02-26', 'Jeffrey Skilling', "Testified under oath that when he left Enron he did not believe the company was in financial peril.", 'B-023'),
   S('2002-05-07', 'Enron directors', "Audit Committee chairman Jaedicke testified the committee knew of \"high-risk and innovative transactions\"; director John H. Duncan said the Powers Report and press reports indicated that certain managers and the outside auditors knew of the problems and did not tell the board.", 'B-078', 'B-075'),
   S('2003-11-04', 'Kenneth Lay and Jeffrey Skilling', "The bankruptcy examiner concluded a fact-finder could find they were at least negligent in failing to respond to red flags about the misuse of SPEs.", 'B-012'),
   S('2004-01-14', 'Andrew Fastow', "The Justice Department announced he pleaded guilty and admitted that he and other senior managers conspired to manipulate Enron's reported results.", 'G-001', 'G-003'),
  ],
  'ask_why': "Many key people declined to testify, and some who did said they did not recall. If you were writing the history of Enron, how would you decide what someone knew when the people involved will not or cannot say?"
 }
}

# ---------------- checks ----------------
def norm(s):
    return (s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
             .replace("''", '"').replace('—', '-').replace('–', '-').replace('--', '-').lower())

problems = []
CHECKER_VERIFIED = []  # F-022 now carries the Duncan quotation
def check_quotes(text, cs, where):
    src = ' '.join(norm(cards[c['card']]['quote'] + ' ' + cards[c['card']]['claim'] + ' ' + (cards[c['card']]['notes'] or '')) for c in cs)
    for q in re.findall(r'"([^"]+)"', text):
        qq = norm(q).strip(' .,')
        if qq not in src and qq not in CHECKER_VERIFIED:
            problems.append((where, q))

for ch in [k for k in L if k.startswith('ch')]:
    for lens, d in L[ch].items():
        assert 3 <= len(d['summary']) <= 4, (ch, lens)
        for n in d['notes']: check_quotes(n['text'], n['cites'], f'{ch}/{lens}/note{n["para_index"]}')
        for b in d['summary']: check_quotes(b['text'], b['cites'], f'{ch}/{lens}/summary')
        if lens == 'knew':
            assert 3 <= len(d['strip']) <= 8, ch
            d['strip'].sort(key=lambda e: e['date'])
            for s in d['strip']: check_quotes(s['what'], s['cites'], f'{ch}/knew/strip {s["date"]}')
for p in problems: print('QUOTE?', p)

json.dump(L, open(ROOT + '/work/drafts/lenses.json', 'w'), indent=2, ensure_ascii=False)
tot = {}
for ch in [k for k in L if k.startswith('ch')]:
    texts, lenses = paras[ch and int(ch[2:])]
    for lens in ['money', 'auditors', 'board', 'knew']:
        tagged = sum(1 for l in lenses if lens in l)
        print(ch, lens, 'tagged', tagged, 'notes', len(L[ch][lens]['notes']))
        tot.setdefault('t', 0); tot['t'] += tagged; tot.setdefault('n', 0); tot['n'] += len(L[ch][lens]['notes'])
print(tot)

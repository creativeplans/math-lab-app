"""Claim-level source ledger (review item P1).

Every source record in the unit files is one claim. This module adds what is known about checking it, keeping four
ideas apart: verified_on (when someone confirmed this exact claim), effective_from (when the rule took effect),
tax_year (the tax year the claim is about), and hypothetical (the course uses stated example amounts instead).

Honest limits: the authoring environment cannot open government or standards sites (DNS and proxy blocks). The author
could only read web-search results. So nothing is marked "verified" by the author; see the status values below.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'financial_literacy', 'src')
REVIEW_DATE = 'independent review of v1.0.0 (date as in the review file)'
SEARCH_DATE = '2026-10-15'

# All 100 source URLs in v1.0.0. The reviewer fetched each one: 85 returned HTTP 200, 11 returned 404, 4 returned 403.
V100_URLS = set(json.load(open(os.path.join(SRC, 'review', 'source_urls_v1.0.0.json'))))
REVIEW_FAILED = {
    'https://business.nj.gov/': ('403', None),
    'https://consumer.ftc.gov/articles/automatic-renewals-and-subscriptions': ('404', 'https://consumer.ftc.gov/articles/getting-and-out-free-trials-auto-renewals-and-negative-option-subscriptions'),
    'https://consumer.ftc.gov/articles/donating-wisely-avoiding-charity-scams': ('404', 'https://consumer.ftc.gov/features/how-donate-wisely-and-avoid-charity-scams'),
    'https://www.cisa.gov/secure-our-world': ('403', 'https://www.cisa.gov/secure-our-world/use-strong-passwords'),
    'https://www.consumerfinance.gov/about-us/blog/cfpb-warns-consumers-about-deferred-interest-promotions/': ('404', 'https://www.consumerfinance.gov/archive/blog/how-understand-special-promotional-financing-offers-credit-cards/'),
    'https://www.consumerfinance.gov/ask-cfpb/what-is-my-liability-for-unauthorized-credit-card-charges-en-24/': ('404', 'https://www.consumerfinance.gov/ask-cfpb/am-i-responsible-for-unauthorized-charges-if-my-credit-cards-are-lost-or-stolen-en-29/'),
    'https://www.fdic.gov/resources/deposit-insurance': ('403', None),
    'https://www.fdic.gov/resources/deposit-insurance/understanding-deposit-insurance': ('403', 'https://www.fdic.gov/resources/deposit-insurance'),
    'https://www.ftc.gov/legal-library/browse/rules/rule-unfair-or-deceptive-fees': ('404', 'https://www.ftc.gov/news-events/news/press-releases/2025/05/ftc-rule-unfair-or-deceptive-fees-take-effect-may-12-2025'),
    'https://www.investor.gov/introduction-investing/getting-started/working-investment-professional/opening-brokerage-account': ('404', 'https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-43'),
    'https://www.investor.gov/introduction-investing/investing-basics/investment-products/mutual-funds-and-exchange-traded-funds-etfs': ('404', 'https://www.investor.gov/introduction-investing/investing-basics/investment-products/mutual-funds-and-exchange-traded-funds-etfs/mutual-funds'),
    'https://www.investor.gov/introduction-investing/investing-basics/save-and-invest/saving-investing': ('404', 'https://www.investor.gov/introduction-investing/investing-basics/save-and-invest'),
    'https://www.investor.gov/introduction-investing/investing-basics/understanding-fees': ('404', 'https://www.investor.gov/introduction-investing/investing-basics/glossary/mutual-fund-fees-and-expenses'),
    'https://www.irs.gov/filing/check-if-you-need-to-file-a-tax-return': ('404', 'https://www.irs.gov/help/ita/do-i-need-to-file-a-tax-return'),
    'https://www.nj.gov/treasury/taxation/su_over.shtml': ('404', 'https://www.nj.gov/treasury/taxation/businesses/salestax/index.shtml'),
}

# Primary sources the reviewer consulted for a specific topic (review section 5). Status applies to that topic only.
REVIEWER_REFS = {
    'https://www.irs.gov/newsroom/working-families-tax-cuts': 'A1',
    'https://fsapartners.ed.gov/fsa-print/publication/1004279': 'A2',
    'https://www.consumerfinance.gov/rules-policy/regulations/1026/52/': 'A3',
    'https://www.consumerfinance.gov/rules-policy/final-rules/availability-funds-and-collection-checks-regulation-cc-threshold-adjustments/': 'A4',
    'https://www.irs.gov/pub/irs-drop/n-11-17.pdf': 'A5',
    'https://consumer.ftc.gov/articles/buyers-remorse-ftcs-cooling-rule-may-help': 'A6',
    'https://www.consumerfinance.gov/rules-policy/regulations/1006/34/': 'A7',
    'https://www.consumerfinance.gov/rules-policy/regulations/1005/6/': 'A8',
    'https://www.consumerfinance.gov/rules-policy/regulations/1026/13/': 'A9',
    'https://www.consumerfinance.gov/rules-policy/regulations/1026/51/': 'A10',
    'https://www.consumerfinance.gov/ask-cfpb/what-is-a-grace-period-for-a-credit-card-en-47/': 'A11',
    'https://www.dol.gov/agencies/whd/overtime': 'A12',
    'https://www.treasurydirect.gov/savings-bonds/buy-a-bond/': 'A13',
    'https://www.consumerfinance.gov/ask-cfpb/what-is-the-difference-between-a-loan-interest-rate-and-the-apr-en-733/': 'A14',
    'https://www.irs.gov/publications/p590b': 'A15',
    'https://www.irs.gov/publications/p590a': 'A16',
    'https://www.irs.gov/newsroom/what-the-no-tax-on-tips-deduction-means-for-you': 'A18',
    'https://www.irs.gov/businesses/small-businesses-self-employed/am-i-required-to-file-a-form-1099-or-other-information-return': 'A19',
    'https://www.nj.gov/dca/codes/publications/pdf_lti/t_i_r.pdf': 'A22',
    'https://www.ftc.gov/news-events/news/press-releases/2025/05/ftc-rule-unfair-or-deceptive-fees-take-effect-may-12-2025': 'A23',
    'https://www.irs.gov/taxtopics/tc409': 'C26 (Topic 409)',
}

# Claims whose key fact the author found in web-search results on SEARCH_DATE (search snippets of official or
# secondary pages; the page itself could not be opened). Keyed by URL.
SEARCH_CORROBORATED = {
    'https://www.irs.gov/newsroom/working-families-tax-cuts': '2026 nonitemizer deduction $1,000 / $2,000 MFJ; bronze and catastrophic plans HSA-compatible from 2026',
    'https://www.consumerfinance.gov/rules-policy/final-rules/availability-funds-and-collection-checks-regulation-cc-threshold-adjustments/': 'next-day amount $275 from July 1, 2025',
    'https://www.irs.gov/businesses/small-businesses-self-employed/am-i-required-to-file-a-form-1099-or-other-information-return': '1099-NEC threshold $2,000 for payments after 2025',
    'https://fsapartners.ed.gov/fsa-print/publication/1004279': 'no capitalization on entering repayment for Direct Loans since July 1, 2023',
    'https://consumer.ftc.gov/articles/buyers-remorse-ftcs-cooling-rule-may-help': '$25 home / $130 temporary location; 3 business days; Saturday counts',
    'https://consumer.ftc.gov/articles/getting-and-out-free-trials-auto-renewals-and-negative-option-subscriptions': 'page exists (replacement URL found by search)',
    'https://consumer.ftc.gov/features/how-donate-wisely-and-avoid-charity-scams': 'page exists (replacement URL found by search)',
    'https://www.consumerfinance.gov/archive/blog/how-understand-special-promotional-financing-offers-credit-cards/': 'page exists; explains deferred interest back to purchase date',
    'https://www.consumerfinance.gov/ask-cfpb/am-i-responsible-for-unauthorized-charges-if-my-credit-cards-are-lost-or-stolen-en-29/': 'page exists; $50 maximum liability',
    'https://www.investor.gov/introduction-investing/investing-basics/glossary/mutual-fund-fees-and-expenses': 'page exists (replacement URL found by search)',
    'https://www.investor.gov/introduction-investing/investing-basics/investment-products/mutual-funds-and-exchange-traded-funds-etfs/mutual-funds': 'page exists (replacement URL found by search)',
    'https://www.investor.gov/introduction-investing/investing-basics/save-and-invest': 'page exists (replacement URL found by search)',
    'https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-43': 'page exists (replacement URL found by search)',
    'https://www.irs.gov/help/ita/do-i-need-to-file-a-tax-return': 'page exists (replacement URL found by search)',
    'https://www.nj.gov/treasury/taxation/businesses/salestax/index.shtml': 'page exists (replacement URL found by search)',
    'https://www.cisa.gov/secure-our-world/use-strong-passwords': 'page exists (replacement URL found by search)',
}

HYPOTHETICAL_MARKERS = ('hypothetical', 'stated hypothetical')


def status(rec):
    url = rec['url']
    parts = []
    if url in REVIEW_FAILED:
        parts.append('reviewer fetch: HTTP %s (access result, not a content finding)' % REVIEW_FAILED[url][0])
    elif url in V100_URLS:
        parts.append('reviewer fetch: HTTP 200 (link reachable; claim not confirmed by the fetch)')
    else:
        parts.append('new or replaced URL in v1.1; not fetched by the reviewer')
    if url in REVIEWER_REFS:
        parts.append('reviewer consulted this primary source for the specific corrected topic (%s)' % REVIEWER_REFS[url])
    if url in SEARCH_CORROBORATED:
        parts.append('author: search-corroborated on %s: %s' % (SEARCH_DATE, SEARCH_CORROBORATED[url]))
    level = ('reviewer-checked topic' if url in REVIEWER_REFS else
             'search-corroborated' if url in SEARCH_CORROBORATED else 'unverified')
    return level, '; '.join(parts)


def tax_year(rec):
    e = rec.get('effective', '') or ''
    return e if 'ax year' in e else None


def effective_from(rec):
    e = rec.get('effective', '') or ''
    return e if e[:2] == '20' else None


def rows(sets):
    out = []
    for s in sets:
        for rec in s['sources']:
            level, detail = status(rec)
            qids = [q for q in rec.get('qids', []) if q.startswith('S%d-' % s['num'])]
            out.append(dict(
                set='S%d' % s['num'], set_title=s['title'],
                question_ids=qids or None,
                scope='claim used by the listed questions' if qids else 'background for the set',
                organization=rec['org'], claim=rec['claim'], url=rec['url'], section=rec.get('section'),
                jurisdiction=rec.get('jurisdiction', 'US federal'),
                effective_from=effective_from(rec), tax_year=tax_year(rec),
                stated_as_of=rec.get('effective') if not (effective_from(rec) or tax_year(rec)) else None,
                hypothetical=any(m in rec['claim'] for m in HYPOTHETICAL_MARKERS),
                verification_level=level, verification_detail=detail,
                verified_on=None,
                verified_on_note='No claim has an author verified_on date: the author could not open the page. '
                                 'Reviewer-checked topics carry the review date of v1.0.0.' if level != 'reviewer-checked topic'
                                 else REVIEW_DATE))
    return out


def package_fields(rec):
    level, detail = status(rec)
    return dict(verification=level, verification_detail=detail, verified_on=None)


def write(sets, out_dir, md_table):
    R = rows(sets)
    json.dump(dict(description=__doc__.strip(), rows=R,
                   replaced_urls=[dict(old=k, reviewer_fetch=v[0], new=v[1]) for k, v in sorted(REVIEW_FAILED.items())]),
              open(os.path.join(out_dir, 'SOURCE_LEDGER.json'), 'w'), indent=1, ensure_ascii=False)
    levels = {}
    for r in R:
        levels[r['verification_level']] = levels.get(r['verification_level'], 0) + 1
    urls = sorted({r['url'] for r in R})
    L = ['# Financial Literacy — Source Ledger (claim level)', '',
         'One row per claim attached to a set. "question_ids" lists the questions that depend on that exact claim; a '
         'blank means the source is background for the set. Fields kept apart: **effective_from** (when the rule '
         'started), **tax_year**, **stated_as_of** (other dates), **hypothetical** (the course uses stated example '
         'amounts), and **verified_on**.', '',
         '## Honest status', '',
         '- The authoring environment could not open any government or standards website (DNS failure / proxy 403). The '
         'author could only read web-search results. **No claim is marked verified by the author.**',
         '- "reviewer-checked topic": the independent reviewer cited this primary source for the specific corrected topic '
         '(A1-A23). That does not approve every other claim attached to the same page.',
         '- "search-corroborated": the key fact appeared in search results on %s; the page itself was not opened.' % SEARCH_DATE,
         '- "unverified": the link was reachable for the reviewer (HTTP 200) or is new; the claim still needs a check.',
         '- An HTTP 403 is an access limit, not proof the claim is wrong.', '',
         'Counts: %d claim rows, %d distinct URLs. %s.' % (len(R), len(urls), ', '.join('%s: %d' % kv for kv in sorted(levels.items()))), '',
         '## Replaced or blocked links from v1.0.0', '',
         md_table(['v1.0.0 URL', 'Reviewer fetch', 'v1.1 URL'],
                  [[k, v[0], v[1] or 'kept (access limit only)'] for k, v in sorted(REVIEW_FAILED.items())]), '',
         '## Claims', '',
         md_table(['Set', 'Questions', 'Claim', 'Source and section', 'Jurisdiction', 'Effective / tax year', 'Hypothetical', 'Status'],
                  [[r['set'], ', '.join(r['question_ids']) if r['question_ids'] else 'set background', r['claim'],
                    '%s, %s%s' % (r['organization'], r['url'], ' (%s)' % r['section'] if r['section'] else ''),
                    r['jurisdiction'], r['effective_from'] or r['tax_year'] or r['stated_as_of'] or '—',
                    'yes' if r['hypothetical'] else 'no', r['verification_level']] for r in R]), '',
         '## Status detail per URL', '',
         md_table(['URL', 'Detail'], [[u, status(dict(url=u))[1]] for u in urls]), '']
    open(os.path.join(out_dir, 'SOURCE_LEDGER.md'), 'w').write('\n'.join(L))
    return R

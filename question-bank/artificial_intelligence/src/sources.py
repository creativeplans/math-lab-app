"""Source ledger for the Artificial Intelligence collection.

Every time-sensitive, legal, historical or research claim used in the course is listed here with the URL that supports
it, the claim, the date it was checked, the jurisdiction and the review interval. Pages could not be opened directly
from the authoring environment; each claim was checked against web-search results (titles, URLs and quoted text).
Where only secondary sources were returned, or sources disagreed, the entry says so in UNCONFIRMED and the course avoids
the disputed detail. Product names appear only in dated, sourced history; no question attributes a fictional output to
a named product. Review every entry before its review date.
"""
CHECKED = '2026-10-26'
METHOD = 'web search result for the page (quoted text and summary); page not opened directly'

SRC = {
    # ---------------------------------------------------------------- technical and research
    'tokens_openai': dict(
        url='https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them',
        claim='Provider rule of thumb (OpenAI help article): for English text one token is about 4 characters or about '
              'three quarters of a word; exact counts depend on the model and its tokenizer. Token counts are not word '
              'counts.',
        jurisdiction='Provider documentation (example)', review_days=365),
    'tech_rlhf': dict(
        url='https://arxiv.org/abs/2203.02155',
        claim='Ouyang et al. (2022), "Training language models to follow instructions with human feedback": a model is '
              'fine-tuned on human-written demonstrations, a reward model is trained on human rankings of outputs, and '
              'reinforcement learning from human feedback (RLHF) then adjusts the model; the resulting models still '
              'make simple mistakes.',
        jurisdiction='research', review_days=1095),
    'tech_transformer': dict(
        url='https://arxiv.org/abs/1706.03762',
        claim='Vaswani et al. (2017), "Attention Is All You Need", introduced the Transformer, a network built on '
              'attention without recurrence, first posted in June 2017; transformers became the basis of most later '
              'large language models.',
        jurisdiction='research', review_days=1095),
    'tech_osaid': dict(
        url='https://discuss.opensource.org/t/open-weights-or-open-source-ai/601',
        claim='The Open Source Initiative published the Open Source AI Definition 1.0 (October 2024). Downloadable '
              'model weights ("open weights") can still come with license terms that restrict some uses, so open '
              'weights are not automatically open source; the definition itself is disputed by some groups.',
        jurisdiction='Licensing practice (international)', review_days=365),
    'eval_contamination': dict(
        url='https://aclanthology.org/2024.naacl-long.482/',
        claim='Deng et al. (NAACL 2024), "Investigating Data Contamination in Modern Benchmarks for Large Language '
              'Models": test items can leak into training data, which can inflate benchmark scores; simple overlap '
              'checks can miss contaminated examples.',
        jurisdiction='research', review_days=1095),
    'code_slopsquat': dict(
        url='https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen',
        claim='Spracklen et al., "We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code '
              'Generating LLMs" (USENIX Security 2025): code-generating models sometimes recommend software packages '
              'that do not exist, and attackers can register such names. The course uses no rates from the study.',
        jurisdiction='research', review_days=730),
    'sec_owasp': dict(
        url='https://genai.owasp.org/llmrisk/llm01-prompt-injection/',
        claim='OWASP Top 10 for LLM Applications (2025) lists prompt injection first (LLM01). Indirect prompt '
              'injection places instructions in content a system later reads (web pages, emails, documents). '
              'Commonly advised measures include limiting privileges, separating untrusted content and requiring '
              'human approval for high-risk actions; no single measure fully prevents it.',
        corroboration='https://docs.bytehide.com/products/radar/sast/owasp/llm01-2025',
        jurisdiction='Security guidance (international, voluntary)', review_days=365),
    'media_c2pa': dict(
        url='https://arxiv.org/pdf/2602.18681',
        claim='Content provenance (for example C2PA Content Credentials) records signed information about how a file '
              'was made or edited; the record can be stripped by re-uploading or screenshots, a missing record does '
              'not show that content is real or fake, and watermark detection is probabilistic, with false positives '
              'and false negatives.',
        corroboration='https://www.softwareseni.com/how-c2pa-content-credentials-work-and-what-their-limits-are/',
        jurisdiction='Technical standard (international)', review_days=365),
    'fair_gendershades': dict(
        url='https://proceedings.mlr.press/v81/buolamwini18a.html',
        claim='Buolamwini and Gebru (2018), "Gender Shades": three commercial gender-classification systems tested in '
              '2017-2018 had error rates up to 34.7 percent for darker-skinned women versus at most 0.8 percent for '
              'lighter-skinned men. The finding is about those systems at that time.',
        jurisdiction='research', review_days=1095),
    'fair_asr': dict(
        url='https://pmc.ncbi.nlm.nih.gov/articles/PMC7149386',
        claim='Koenecke et al. (PNAS, 2020), "Racial disparities in automated speech recognition": five commercial '
              'speech-recognition systems had an average word error rate of 0.35 for Black speakers versus 0.19 for '
              'white speakers in the studied interviews. The finding is about those systems and speakers.',
        jurisdiction='research', review_days=1095),
    'energy_iea': dict(
        url='https://www.iea.org/reports/energy-and-ai',
        claim='IEA, "Energy and AI" (April 2025): data centres used about 415 TWh of electricity in 2024 (about 1.5 '
              'percent of global use) and are projected to reach around 945 TWh by 2030 in the base case; the IEA '
              'stresses large uncertainty. These are estimates and projections, not a per-question figure.',
        corroboration='https://rcrwireless.com/20250411/rcr-techtrends/ai-electricity-dcs-2030-iea',
        jurisdiction='International (IEA estimate)', review_days=365, effective_year='2025'),

    # ---------------------------------------------------------------- philosophy and history
    'phil_turing': dict(
        url='https://plato.stanford.edu/entries/turing-test/',
        claim='Turing\'s 1950 paper "Computing Machinery and Intelligence" (Mind) proposed replacing "Can machines '
              'think?" with an imitation game in which an interrogator questions a hidden human and a machine; the '
              'test is debated, and the name is sometimes used loosely for any behavioral test.',
        jurisdiction='history and philosophy', review_days=1095),
    'phil_chinese': dict(
        url='https://iep.utm.edu/chinese-room/',
        claim='Searle\'s 1980 Chinese Room argument ("Minds, Brains and Programs"): following rules to manipulate '
              'symbols (syntax) is not by itself understanding (semantics). The systems reply says the whole system, '
              'not the person, might understand; Searle answered by imagining the person memorizing the rules. The '
              'debate continues.',
        jurisdiction='philosophy', review_days=1095),
    'hist_eliza': dict(
        url='https://en.wikipedia.org/wiki/ELIZA_effect',
        claim='Joseph Weizenbaum\'s ELIZA (MIT, 1964-1966) matched keywords and returned scripted replies, yet some '
              'users treated it as understanding them; the tendency is called the ELIZA effect.',
        jurisdiction='history', review_days=1095),
    'hist_dartmouth': dict(
        url='https://ojs.aaai.org/index.php/aimagazine/article/view/1904',
        claim='"A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence" (dated August 31, '
              '1955; McCarthy, Minsky, Rochester, Shannon) proposed a 1956 workshop and is credited with introducing '
              'the term "artificial intelligence".',
        jurisdiction='history', review_days=1095),
    'hist_deepblue_alphago': dict(
        url='https://techcrunch.com/2016/03/09/googles-deepmind-chalks-up-ai-landmark-after-beating-go-world-champion-lee-sedol',
        claim='IBM\'s Deep Blue beat world chess champion Garry Kasparov in a 1997 match, relying mainly on fast search '
              'and hand-crafted evaluation; DeepMind\'s AlphaGo, which used deep neural networks, beat Go champion Lee '
              'Sedol 4-1 in March 2016.',
        corroboration='https://iotworldtoday.com/iiot/25-years-ago-today-how-deep-blue-vs-kasparov-changed-ai-forever',
        jurisdiction='history', review_days=1095),
    'hist_alexnet': dict(
        url='https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks',
        claim='Krizhevsky, Sutskever and Hinton (NeurIPS 2012): a deep convolutional network trained on GPUs won the '
              'ILSVRC-2012 image-recognition competition with a top-5 error of 15.3 percent versus 26.2 percent for '
              'the next entry, a result widely seen as a turning point for deep learning.',
        corroboration='https://cvml.ista.ac.at/courses/DLWT_W17/material/AlexNet.pdf',
        jurisdiction='history', review_days=1095),
    'hist_chatgpt': dict(
        url='https://openai.com/index/chatgpt/',
        claim='OpenAI released ChatGPT as a free research preview on November 30, 2022, which brought chat-style '
              'access to a large language model to a very wide public.',
        corroboration='https://computinghistory.org.uk/det/71180/OpenAI launches ChatGPT',
        jurisdiction='history', review_days=1095),
    'case_mata': dict(
        url='https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc.',
        claim='Mata v. Avianca (S.D.N.Y., June 22, 2023): lawyers who filed a brief citing court decisions that did '
              'not exist, generated with a chatbot and not verified, were sanctioned ($5,000); courts expect lawyers '
              'to verify every authority they cite.',
        corroboration='https://www.americanbar.org/groups/judicial/resources/appellate-issues/2026-fall/limits-appellate-scrutiny-age-ai',
        jurisdiction='US (federal court, New York)', review_days=1095),

    # ---------------------------------------------------------------- careers and work
    'work_bls_ds': dict(
        url='https://www.bls.gov/ooh/math/data-scientists.htm',
        claim='BLS Occupational Outlook Handbook, data scientists: employment is projected to grow 34 percent from 2024 '
              'to 2034, much faster than the 3 percent average for all occupations. A projection, not a guarantee. '
              'The course quotes no pay figures and no credential requirements.',
        jurisdiction='US', review_days=365, effective_year='2024-2034 projection'),
    'work_wef': dict(
        url='https://www.weforum.org/media/future-of-jobs-report-2025-78-million-new-job-opportunities-by-2030-but-urgent-upskilling-needed-to-prepare-workforces/',
        claim='World Economic Forum, Future of Jobs Report 2025 (January 2025): based on a survey of more than 1,000 '
              'employers, it projects 170 million roles created and 92 million displaced worldwide by 2030 (a net '
              '78 million). These are survey-based projections.',
        jurisdiction='International (projection)', review_days=365, effective_year='2025'),

    # ---------------------------------------------------------------- law and policy (US unless marked)
    'law_nist_rmf': dict(
        url='https://www.nist.gov/itl/ai-risk-management-framework',
        claim='The NIST AI Risk Management Framework 1.0 (January 26, 2023) and its Generative AI Profile (NIST AI '
              '600-1, July 26, 2024) are intended for voluntary use: guidance, not a law.',
        jurisdiction='US federal (voluntary guidance)', review_days=365, effective_year='2023'),
    'law_thaler': dict(
        url='https://www.loeb.com/en/insights/publications/2025/03/thaler-v-perlmutter',
        claim='Thaler v. Perlmutter (D.C. Cir., March 18, 2025) held that the US Copyright Act requires human '
              'authorship, upholding the refusal to register an image the applicant said was made entirely by an AI '
              'system; the court did not decide how much human contribution is enough for AI-assisted works. The '
              'Supreme Court declined review on March 2, 2026.',
        corroboration='https://www.iam-media.com/article/human-authorship-remains-cornerstone-requirement-copyright-registration-supreme-court-denies-certiorari-in-thaler-case',
        jurisdiction='US federal', review_days=365, effective_year='2025'),
    'law_usco_part2': dict(
        url='https://ipwatchdog.com/2025/01/29/part-two-copyright-office-ai-report-says-creative-prompting-doesnt-constitute-authorship/',
        claim='US Copyright Office, Copyright and Artificial Intelligence Part 2: Copyrightability (January 29, 2025): '
              'given current generally available technology, prompts alone do not give enough human control to make '
              'the user the author of the output; human-authored expression, and human selection, arrangement or '
              'modification of AI output, can be protected.',
        corroboration='https://datamatters.sidley.com/2025/02/07/u-s-copyright-office-issues-report-on-artificial-intelligence-and-copyrightability/',
        jurisdiction='US federal (agency report)', review_days=365, effective_year='2025'),
    'law_zarya': dict(
        url='https://creativecommons.org/2023/02/27/zarya-of-the-dawn-us-copyright-office-affirms-limits-on-copyright-of-ai-outputs/',
        claim='Zarya of the Dawn (US Copyright Office, February 2023): the comic\'s text and the human selection and '
              'arrangement of its parts were registrable, but the individual AI-generated images were not.',
        jurisdiction='US federal (agency decision)', review_days=1095, effective_year='2023'),
    'law_usco_guidance': dict(
        url='https://skadden.com/insights/publications/2023/03/copyright-office-issues-guidance-on-ai-generated-works',
        claim='US Copyright Office registration guidance (March 16, 2023): applicants must disclose AI-generated '
              'material that is more than minimal and claim only the human-authored parts.',
        jurisdiction='US federal (agency guidance)', review_days=365, effective_year='2023'),
    'law_usco_part3': dict(
        url='https://www.jenner.com/en/news-insights/client-alerts/us-copyright-office-releases-pre-publication-version-of-report-on-copyright-issues-in-generative-ai-training',
        claim='US Copyright Office, Part 3: Generative AI Training (pre-publication version, May 9, 2025): whether '
              'training on copyrighted works is fair use depends on the facts; uses that produce outputs competing '
              'with the originals weigh against fair use. An agency report is not binding law.',
        corroboration='https://datamatters.sidley.com/2025/05/28/generative-ai-meets-copyright-scrutiny-highlights-from-the-copyright-offices-part-iii-report/',
        jurisdiction='US federal (agency report)', review_days=365, effective_year='2025'),
    'law_bartz_kadrey': dict(
        url='https://www.debevoise.com/insights/publications/2025/06/anthropic-and-meta-decisions-on-fair-use',
        claim='In June 2025 two federal district judges in California (Bartz v. Anthropic; Kadrey v. Meta) found that '
              'training on the books at issue was fair use on those records, while treating pirated copies '
              'differently (Bartz) or warning that other evidence could change the result (Kadrey). District-court '
              'rulings are fact-specific and do not settle the question nationwide.',
        corroboration='https://www.manatt.com/insights/newsletters/client-alert/making-sense-of-the-first-two-often-contradictory-sometimes-confounding-gen-ai-fair-use-rulings',
        jurisdiction='US federal (district courts, California)', review_days=365, effective_year='2025'),
    'law_elvis': dict(
        url='https://www.manatt.com/insights/newsletters/client-alert/tennessees-elvis-act-expands-publicity-rights-for',
        claim='Tennessee\'s ELVIS Act (signed March 21, 2024; effective July 1, 2024) added a person\'s voice, '
              'including a simulated voice, to the state\'s right of publicity, with liability for unauthorized '
              'commercial use and for certain tools whose main purpose is imitating a specific person.',
        jurisdiction='US (Tennessee)', review_days=365, effective_year='2024'),
    'law_fcc_voice': dict(
        url='https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/fcc-issues-declaratory-ruling-on-ai-generated-voice-robocalls',
        claim='FCC Declaratory Ruling (February 8, 2024): AI-generated voices in calls count as "artificial" voices '
              'under the Telephone Consumer Protection Act, so such calls need the same prior consent and disclosures '
              'as other prerecorded calls.',
        jurisdiction='US federal', review_days=365, effective_year='2024'),
    'law_takeitdown': dict(
        url='https://search.ftc.gov/news-events/news/press-releases/2026/05/ftc-begins-enforcing-take-it-down-act',
        claim='The federal TAKE IT DOWN Act (2025) addresses nonconsensual intimate images, including AI-generated '
              'ones; from May 19, 2026, covered platforms must provide a removal-request process and act on valid '
              'requests within 48 hours, enforced by the FTC.',
        corroboration='https://wilmerhale.com/en/insights/client-alerts/20260615-the-take-it-down-act-goes-live',
        jurisdiction='US federal', review_days=365, effective_year='2026'),
    'law_coppa': dict(
        url='https://www.federalregister.gov/documents/2025/04/22/2025-05904/childrens-online-privacy-protection-rule',
        claim='The FTC\'s amended Children\'s Online Privacy Protection Rule (COPPA) was published April 22, 2025, took '
              'effect June 23, 2025, with most compliance required by April 22, 2026; COPPA covers personal '
              'information collected online from children under 13.',
        jurisdiction='US federal', review_days=365, effective_year='2025'),
    'law_gdpr22': dict(
        url='https://advisera.com/gdpr/automated-individual-decision-making-including-profiling/',
        claim='EU GDPR Article 22 (international comparison): people have a right not to be subject to a decision based '
              'solely on automated processing that has legal or similarly significant effects, with stated exceptions '
              'and safeguards such as human intervention.',
        jurisdiction='European Union', review_days=730, effective_year='2018'),
    'law_nyc144': dict(
        url='https://www.nyc.gov/assets/dca/downloads/pdf/about/DCWP-AEDT-FAQ.pdf',
        claim='New York City Local Law 144 (enforced from July 5, 2023): employers and employment agencies may use an '
              'automated employment decision tool only after an independent bias audit within the past year, with a '
              'public summary and advance notice to candidates.',
        jurisdiction='US (New York City)', review_days=365, effective_year='2023'),
    'law_illinois': dict(
        url='https://www.isba.org/node/97164',
        claim='Illinois HB 3773 amended the Illinois Human Rights Act, effective January 1, 2026: employers may not use '
              'AI in a way that discriminates against protected classes, may not use ZIP codes as a proxy for '
              'protected classes, and must give notice when AI is used for covered employment decisions.',
        corroboration='https://www.ebglaw.com/workforce-bulletin/illinois-prohibits-discriminatory-artificial-intelligence-in-employment-decisions',
        jurisdiction='US (Illinois)', review_days=365, effective_year='2026'),
    'law_cfpb': dict(
        url='https://consumerfinance.gov/compliance/circulars/circular-2023-03-adverse-action-notification-requirements-and-the-proper-use-of-the-cfpbs-sample-forms-provided-in-regulation-b',
        claim='CFPB Circular 2023-03 (September 2023): a lender that denies credit must give the specific principal '
              'reasons, even when it uses complex algorithms; checking a generic reason on a sample form is not '
              'enough if it does not match the actual reasons. Agency guidance can be withdrawn or revised.',
        jurisdiction='US federal', review_days=365, effective_year='2023'),
    'law_ftc_aicomply': dict(
        url='https://www.mofo.com/pdf/resources/insights/241008-ftc-first-ai-related-enforcement-actions',
        claim='FTC "Operation AI Comply" (September 25, 2024): five actions under existing consumer-protection law, '
              'including a company sold as a "robot lawyer" whose claims were alleged to be untested, a tool alleged to '
              'generate fake reviews, and schemes promising quick earnings from AI-powered online stores.',
        corroboration='https://www.davispolk.com/insights/client-update/ftc-announces-new-enforcement-initiative-targeting-deceptive-ai-practices',
        jurisdiction='US federal', review_days=365, effective_year='2024'),
    'law_ed_ai': dict(
        url='https://www.ed.gov/about/news/press-release/us-department-of-education-issues-guidance-artificial-intelligence-use-schools-proposes-additional-supplemental-priority',
        claim='US Department of Education Dear Colleague Letter (July 22, 2025): federal grant funds may support some '
              'AI uses (for example instructional materials and tutoring) when they meet program requirements, with '
              'attention to privacy, appropriate use and stakeholder involvement; it is guidance about funding, not a '
              'classroom rule. Schools set their own AI policies.',
        jurisdiction='US federal (guidance)', review_days=365, effective_year='2025'),
    'law_euaiact': dict(
        url='https://www.morganlewis.com/pubs/2026/06/eu-approves-delays-and-other-amendments-to-certain-eu-ai-act-obligations-what-businesses-should-know',
        claim='EU AI Act (Regulation (EU) 2024/1689, in force August 1, 2024) uses risk tiers: some practices are '
              'prohibited (from February 2, 2025), high-risk systems face requirements, and some systems face '
              'transparency duties. A 2026 amendment ("digital omnibus", in force July 27, 2026) moved most Annex III '
              'high-risk obligations to December 2, 2027.',
        corroboration='https://www.orrick.com/en/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes',
        jurisdiction='European Union', review_days=180, effective_year='2024; amended 2026'),
    'law_moffatt': dict(
        url='https://manatt.com/insights/newsletters/advertising-law/ai-gone-wild-airline-has-to-honor-a-refund-policy',
        claim='Moffatt v. Air Canada (British Columbia Civil Resolution Tribunal, February 2024): the airline was held '
              'responsible for wrong refund information its website chatbot gave; the tribunal rejected the argument '
              'that the chatbot was responsible for its own statements. A small-claims decision, not binding '
              'precedent.',
        jurisdiction='Canada (British Columbia)', review_days=1095, effective_year='2024'),
    'law_colorado': dict(
        url='https://www.eckertseamans.com/legal-updates/colorado-repeals-and-replaces-its-landmark-ai-statute-what-businesses-need-to-know',
        claim='Colorado\'s 2024 AI Act (SB 24-205) was delayed in 2025 and, on May 14, 2026, repealed and replaced by '
              'SB 26-189, with a narrower law set to take effect January 1, 2027; federal litigation over the earlier '
              'law was also reported. An example of how quickly AI rules change.',
        corroboration='https://www.gtlaw.com/en/insights/2025/9/colorado-delays-comprehensive-ai-law-with-further-changes-anticipated',
        jurisdiction='US (Colorado)', review_days=180, effective_year='2026'),
    'law_eo14365': dict(
        url='https://www.paulhastings.com/insights/client-alerts/president-trump-signs-executive-order-challenging-state-ai-laws',
        claim='Executive Order 14365 (December 11, 2025) directed federal agencies to challenge some state AI laws and '
              'to propose a national framework; an executive order directs federal agencies and does not by itself '
              'repeal state laws.',
        corroboration='https://www.ropesgray.com/en/insights/alerts/2026/03/the-white-house-legislative-recommendations-national-policy-framework-for-artificial-intelligence-an',
        jurisdiction='US federal', review_days=180, effective_year='2025'),
}

UNCONFIRMED = {
    'sec_owasp': 'official OWASP page not returned by search; content confirmed from secondary summaries of LLM01:2025',
    'energy_iea': 'IEA report page not returned by search; figures confirmed from several news summaries of the report',
    'hist_chatgpt': 'OpenAI announcement not returned by search; date confirmed from secondary history sources',
    'hist_alexnet': 'NeurIPS proceedings page not returned by search; figures confirmed from the paper text mirror and '
                    'a course slide deck',
    'hist_eliza': 'secondary source (encyclopedia); Weizenbaum\'s 1966 paper not opened',
    'case_mata': 'secondary source (encyclopedia and news); the court opinion itself not opened',
    'tech_osaid': 'OSI definition page not returned; claim confirmed from OSI forum and commentary',
    'media_c2pa': 'C2PA specification not opened; claims from a research survey and explainer articles',
    'law_thaler': 'court opinion not opened; holding and later denial of review confirmed by law-firm and news sources',
    'law_usco_part2': 'report PDF not opened; core finding quoted by several law-firm summaries',
    'law_usco_part3': 'report PDF not opened; conclusions from law-firm summaries',
    'law_usco_guidance': 'Federal Register text not opened; from law-firm summaries',
    'law_bartz_kadrey': 'opinions not opened; from law-firm summaries',
    'law_elvis': 'statute text not opened; from law-firm summaries',
    'law_fcc_voice': 'FCC order not opened; from law-firm summaries',
    'law_gdpr22': 'EUR-Lex text not opened; article text as reproduced by a GDPR reference site',
    'law_illinois': 'statute text not opened; from bar-association and law-firm summaries',
    'law_ftc_aicomply': 'FTC press release not opened; from law-firm summaries',
    'law_euaiact': 'Official Journal texts not opened; dates from several law-firm summaries of the 2026 amendment',
    'law_moffatt': 'tribunal decision not opened; from law-firm and news summaries',
    'law_colorado': 'Colorado statutes not opened; from law-firm summaries (mid-2026)',
    'law_eo14365': 'Federal Register text not opened; from law-firm summaries',
}


def entry(key):
    e = dict(SRC[key])
    e.setdefault('checked', CHECKED)
    e.setdefault('method', METHOD)
    e['id'] = key
    e['confirmed_by_search'] = key not in UNCONFIRMED
    if key in UNCONFIRMED:
        e['note'] = UNCONFIRMED[key]
    return e

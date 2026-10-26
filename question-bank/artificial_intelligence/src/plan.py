"""Coverage plan for the Artificial Intelligence collection (course "artificial_intelligence", Adults & HS Students,
prefix AI).

One row per focused set, in the order a learner meets them. Set numbers are assigned in this order and never reused.
Row: (outcome code, set title, outcome definition, module id, path references, required outcome codes, sources)
  path references: the paths a SHARED skill serves (the set is written once and listed for each path); [] = all paths
  required: only the prerequisites the set truly needs (suggested reading is listed separately in SUGGESTED)
  sources: keys in sources.SRC; a set with sources is "time_sensitive", otherwise "stable"
The outcome codes are this course's own local outcomes (alignment "local"); they are not official standards.
"""

PATHS = [
    dict(id='everyday', title='Everyday use',
         description='Research, writing, study, planning, files and the practical pitfalls of AI tools.'),
    dict(id='creative', title='Creative work',
         description='Images, design, presentations, audio, music and video, and the rights that come with them.'),
    dict(id='coding', title='Coding & automation',
         description='Reading and checking code, tests, security, agents and automated workflows.'),
    dict(id='work', title='Work & careers',
         description='AI in jobs, AI-related roles, choosing and paying for tools, and measuring results.'),
    dict(id='society', title='Society, law & philosophy',
         description='Fairness, law and policy, responsibility, philosophy of mind, history and future claims.'),
]

MODULES = [
    # id, title, kind, paths, description
    ('basics', 'Foundation 1: What AI is and where it appears', 'foundation', [],
     'Plain-language meaning of AI, learned patterns versus rules, and the common jobs AI does.'),
    ('learning', 'Foundation 2: How a model learns', 'foundation', [],
     'Training versus use, data, testing, overfitting, data quality and fine-tuning.'),
    ('llm', 'Foundation 3: Large language models', 'foundation', [],
     'Tokens, probabilities, context, knowledge limits, memory and why fluent text is not proof.'),
    ('prompting', 'Foundation 4: Asking for what you need', 'foundation', [],
     'Clear tasks, context, formats, examples, stages, clarification, revision and prompt myths.'),
    ('checking', 'Foundation 5: Checking results', 'foundation', [],
     'Hallucinations, citations, numbers, dates, evidence, summaries and when to ask a qualified person.'),
    ('safety', 'Foundation 6: Privacy and security basics', 'foundation', [],
     'Sensitive information, sharing less, permission, secrets, scams and untrusted instructions.'),
    ('deeper', 'Specialty: a closer look inside', 'specialty', [],
     'Optional: kinds of learning, reinforcement learning and the transformer idea.'),
    ('everyday', 'Everyday: getting real tasks done', 'path', ['everyday'],
     'Planning, drafting, summarizing, translating, studying, accessibility and choosing simpler tools.'),
    ('files', 'Everyday: searching and working with documents', 'path', ['everyday', 'coding', 'work'],
     'Search versus generation, source-grounded answers and uploaded files.'),
    ('pitfalls', 'Everyday: practical pitfalls', 'path', ['everyday', 'work'],
     'Context overload, cut-off output, stale links, versions, exports and accounts.'),
    ('images', 'Creative: images, design and presentations', 'path', ['creative'],
     'Describing images, spotting flaws, consistency, diagrams, slides and accessible visuals.'),
    ('media', 'Creative: audio, music, video and synthetic media', 'path', ['creative'],
     'Transcription, subtitles, voice cloning, music, video, deepfakes and provenance.'),
    ('code', 'Coding: code assistance', 'path', ['coding'],
     'Reading tiny programs, checking generated code, tests, errors, reviews, versions and security.'),
    ('agents', 'Coding: agents and automation', 'path', ['coding', 'work'],
     'Tool-using workflows, plans, permissions, human approval, logs and retries.'),
    ('careers', 'Work: jobs and careers', 'path', ['work'],
     'How AI changes tasks, reading forecasts, AI-related roles, learning routes and responsible use at work.'),
    ('costs', 'Work: costs and choosing tools', 'path', ['work', 'everyday', 'coding'],
     'Pricing models, tokens, limits, cloud or local, open weights and licenses, and tool fit.'),
    ('evaluation', 'Work: measuring how well AI works', 'path', ['work', 'coding'],
     'Test sets, false positives and negatives, benchmarks, tradeoffs, fair comparisons and metrics.'),
    ('fairness', 'Society: bias, fairness and access', 'path', ['society'],
     'Data representation, uneven error rates, proxies, fairness goals and accessibility.'),
    ('law', 'Society: law, policy and responsibility', 'path', ['society'],
     'Kinds of rules, copyright, likeness, privacy, discrimination, consumer protection and liability.'),
    ('philosophy', 'Society: philosophy and social questions', 'path', ['society'],
     'Arguments about intelligence, understanding, consciousness, trust, agency and alignment.'),
    ('history', 'Society: history and claims about the future', 'path', ['society'],
     'Selected milestones, narrow versus general abilities, forecasts, evidence and resource use.'),
]

A = []  # all paths
EV, CR, CO, WK, SO = ['everyday'], ['creative'], ['coding'], ['work'], ['society']

ROWS = [
    # ---------------------------------------------------------------- Foundation 1: What AI is
    ('AI.BASICS.01', 'What people mean by "AI"', 'Describe AI in plain language as computer systems that perform tasks '
     'such as recognizing, predicting, recommending or generating, and recognize "AI" as a broad umbrella term',
     'basics', A, [], []),
    ('AI.BASICS.02', 'Written rules versus learned patterns', 'Tell software that follows rules a person wrote from a '
     'system whose behavior comes from patterns learned from examples', 'basics', A, ['AI.BASICS.01'], []),
    ('AI.BASICS.03', 'Machine learning and deep learning', 'Explain machine learning and deep learning as nested ideas, '
     'with deep learning using many-layered neural networks', 'basics', A, ['AI.BASICS.02'], []),
    ('AI.BASICS.04', 'Four everyday AI jobs', 'Classify an AI use as recommending, recognizing, forecasting or '
     'generating', 'basics', A, ['AI.BASICS.01'], []),
    ('AI.BASICS.05', 'Generative versus predictive uses', 'Decide whether a task needs new content generated or a label '
     'or number predicted, and name a typical failure of each', 'basics', A, ['AI.BASICS.04'], []),
    ('AI.BASICS.06', 'The model versus the product', 'Tell an AI model from the app or service built around it, and '
     'avoid assuming that all AI systems or all chatbots behave the same way', 'basics', A, ['AI.BASICS.01'], []),
    ('AI.BASICS.07', 'Comparing AI with people', 'Use human comparisons carefully: say where a comparison helps, where '
     'it misleads, and why abilities can be uneven', 'basics', A, ['AI.BASICS.01'], []),
    # ---------------------------------------------------------------- Foundation 2: How a model learns
    ('AI.LEARN.01', 'Training versus using a model', 'Tell training (learning patterns from data) from inference (using '
     'the finished model on new input)', 'learning', A, ['AI.BASICS.02'], []),
    ('AI.LEARN.02', 'Data, patterns and parameters', 'Describe parameters as the adjustable numbers a model sets during '
     'training, and explain that the model keeps learned patterns, not a copy of every example', 'learning', A,
     ['AI.LEARN.01'], []),
    ('AI.LEARN.03', 'Training, validation and test data', 'Explain why data is split into training, validation and test '
     'sets and why test data must stay unseen during training', 'learning', A, ['AI.LEARN.01'], []),
    ('AI.LEARN.04', 'Overfitting and generalization', 'Recognize overfitting (doing well on familiar examples but poorly '
     'on new ones) and what good generalization looks like', 'learning', A, ['AI.LEARN.03'], []),
    ('AI.LEARN.05', 'Data quality and labels', 'Explain how missing, wrong, outdated or unrepresentative data and labels '
     'affect what a model learns', 'learning', A, ['AI.LEARN.01'], []),
    ('AI.LEARN.08', 'Fine-tuning versus giving information in a request', 'Tell fine-tuning (further training that '
     'changes a model) from supplying information in a request (which does not change the model)', 'learning', A,
     ['AI.LEARN.01'], []),
    # ---------------------------------------------------------------- Foundation 3: Large language models
    ('AI.LLM.01', 'What a large language model is', 'Describe a large language model (LLM) as a model trained on large '
     'amounts of text to predict likely next pieces of text, and say what that does and does not imply',
     'llm', A, ['AI.BASICS.03'], []),
    ('AI.LLM.02', 'Tokens', 'Explain tokens as the pieces of text a language model reads and writes, and why token '
     'counts differ from word counts', 'llm', A, ['AI.LLM.01'], ['tokens_openai']),
    ('AI.LLM.03', 'Probabilities and why answers vary', 'Explain that a language model chooses among likely next '
     'tokens, so the same request can produce different answers', 'llm', A, ['AI.LLM.01'], []),
    ('AI.LLM.04', 'Fluent is not the same as true', 'Explain why smooth, confident language is not evidence that a '
     'statement is correct', 'llm', A, ['AI.LLM.03'], []),
    ('AI.LLM.05', 'Context windows', 'Explain a context window as the limited amount of text a model can consider at once '
     'and predict what happens when a conversation or document exceeds it', 'llm', A, ['AI.LLM.02'], []),
    ('AI.LLM.06', 'What a model learned versus what you supply', 'Tell knowledge learned in training (with a cutoff '
     'date) from information supplied or retrieved during a request', 'llm', A, ['AI.LLM.01'], []),
    ('AI.LLM.07', 'Conversation context versus saved memory', 'Tell the text in the current conversation from product '
     'features that save information between conversations, and check a product\'s own settings',
     'llm', A, ['AI.LLM.05'], []),
    ('AI.LLM.09', 'A product is more than its model', 'Explain that a product adds its own instructions, settings, tools '
     'and limits, so a general description of LLMs cannot predict one product\'s behavior',
     'llm', A, ['AI.BASICS.06', 'AI.LLM.01'], []),
    # ---------------------------------------------------------------- Foundation 4: Asking for what you need
    ('AI.PROMPT.01', 'Task, context, audience and purpose', 'Identify the task, context, audience and purpose a request '
     'needs, and spot which one is missing', 'prompting', A, ['AI.LLM.01'], []),
    ('AI.PROMPT.02', 'Output format and constraints', 'State the output format and constraints (length, tone, things to '
     'avoid) that a result must meet', 'prompting', A, ['AI.PROMPT.01'], []),
    ('AI.PROMPT.03', 'Examples in a request', 'Use a short example to show what is wanted, and notice when an example '
     'pulls the output away from the written instructions', 'prompting', A, ['AI.PROMPT.01'], []),
    ('AI.PROMPT.04', 'Breaking a job into stages', 'Split a large task into stages that can each be checked',
     'prompting', A, ['AI.PROMPT.01'], []),
    ('AI.PROMPT.05', 'Asking for clarification and assumptions', 'Ask the system to state assumptions or ask questions '
     'when the request is missing information', 'prompting', A, ['AI.PROMPT.01'], []),
    ('AI.PROMPT.06', 'Revising against success criteria', 'Write success criteria and use them to revise or compare '
     'drafts', 'prompting', A, ['AI.PROMPT.02'], []),
    ('AI.PROMPT.07', 'Conflicting requirements', 'Notice requirements that cannot all be met and resolve the conflict '
     'before continuing', 'prompting', A, ['AI.PROMPT.02'], []),
    ('AI.PROMPT.08', 'Supplying source material and asking for structure', 'Supply the relevant source material and '
     'request structured output, such as a table, that is easy to check', 'prompting', A, ['AI.PROMPT.02'], []),
    ('AI.PROMPT.09', 'Prompt myths', 'Explain why role-play, magic phrases, or demands for citations or certainty do not '
     'by themselves create expertise or accuracy', 'prompting', A, ['AI.PROMPT.01', 'AI.LLM.04'], []),
    # ---------------------------------------------------------------- Foundation 5: Checking results
    ('AI.CHECK.01', 'Hallucination in plain language', 'Recognize a hallucination (confident output that is false or '
     'unsupported) and why it happens', 'checking', A, ['AI.LLM.04'], []),
    ('AI.CHECK.02', 'Invented and mismatched citations', 'Check whether a cited source exists and whether it actually '
     'supports the claim attached to it', 'checking', A, ['AI.CHECK.01'], ['case_mata']),
    ('AI.CHECK.03', 'Checking numbers', 'Recalculate or estimate numbers in an AI response before relying on them',
     'checking', A, ['AI.CHECK.01'], []),
    ('AI.CHECK.04', 'Outdated information', 'Spot information that may be out of date and check a current, dated source',
     'checking', A, ['AI.LLM.06'], []),
    ('AI.CHECK.05', 'Evidence versus assertion', 'Tell a claim from evidence for it, and prefer a primary source',
     'checking', A, ['AI.CHECK.01'], []),
    ('AI.CHECK.06', 'Independent checks: agreement is not proof', 'Choose an independent check, and explain why asking '
     'again or getting two AI tools to agree is not proof', 'checking', A, ['AI.CHECK.05'], []),
    ('AI.CHECK.07', 'Checking a summary for omissions', 'Compare a summary with its source to find omissions, '
     'distortions and added claims', 'checking', A, ['AI.CHECK.05'], []),
    ('AI.CHECK.08', 'Contradictions and missing information', 'Spot contradictions and identify what information is '
     'missing before a conclusion can be trusted', 'checking', A, ['AI.CHECK.05'], []),
    ('AI.CHECK.09', 'When to involve a qualified person', 'Recognize high-stakes questions (health, law, money, safety) '
     'where a qualified person must review the answer', 'checking', A, ['AI.CHECK.01'], []),
    ('AI.CHECK.10', 'Useful versus correct, and repeatability', 'Judge usefulness and correctness separately, and '
     'explain why results may not repeat exactly', 'checking', A, ['AI.CHECK.06'], []),
    # ---------------------------------------------------------------- Foundation 6: Privacy and security
    ('AI.PRIVACY.01', 'Personal and sensitive information', 'Identify personal and sensitive information in text '
     'before sharing it with an AI tool', 'safety', A, [], []),
    ('AI.PRIVACY.02', 'Share less: minimizing and redacting', 'Remove or replace details a task does not need before '
     'sharing', 'safety', A, ['AI.PRIVACY.01'], []),
    ('AI.PRIVACY.03', 'Permission to share other people\'s information', 'Decide whether you have permission to share '
     'customer, classmate, patient or workplace information with a tool', 'safety', A, ['AI.PRIVACY.01'], []),
    ('AI.PRIVACY.04', 'Provider data practices and settings', 'Find and read what a provider says about storing, '
     'reviewing and training on your data, and remember practices differ', 'safety', A, ['AI.PRIVACY.01'], []),
    ('AI.SECURITY.01', 'Passwords, keys and shared accounts', 'Keep passwords and access keys out of prompts and code, '
     'and avoid sharing accounts', 'safety', A, [], []),
    ('AI.SECURITY.02', 'AI-assisted scams', 'Recognize scams that use AI-written messages or cloned voices and verify '
     'through a trusted channel', 'safety', A, [], ['law_fcc_voice']),
    ('AI.SECURITY.03', 'Prompt injection: untrusted text is not an instruction', 'Explain prompt injection and treat '
     'instructions inside emails, web pages or documents as untrusted data', 'safety', A, ['AI.PROMPT.01'],
     ['sec_owasp']),
    # ---------------------------------------------------------------- Specialty: a closer look inside
    ('AI.LEARN.06', 'Ways of learning: supervised, unsupervised, self-supervised', 'Tell supervised, unsupervised and '
     'self-supervised learning apart by where the learning signal comes from', 'deeper', A, ['AI.LEARN.02'], []),
    ('AI.LEARN.07', 'Reinforcement learning and human feedback', 'Explain reinforcement learning as learning from '
     'rewards, and how human ratings are used to adjust language models', 'deeper', A, ['AI.LEARN.02'],
     ['tech_rlhf']),
    ('AI.LLM.08', 'Transformers and attention, in plain terms', 'Explain at a conceptual level how attention lets a '
     'model weigh other words in the context, without treating it as a human mind', 'deeper', A, ['AI.LLM.02'],
     ['tech_transformer']),
    # ---------------------------------------------------------------- Path: everyday tasks
    ('AI.EVERYDAY.01', 'Brainstorming and planning', 'Use AI to widen options and draft plans, then choose and check '
     'them yourself', 'everyday', EV, ['AI.PROMPT.01'], []),
    ('AI.EVERYDAY.02', 'Drafting and editing without losing your meaning', 'Use AI for drafts and edits while keeping '
     'your meaning, facts and voice', 'everyday', EV + WK, ['AI.PROMPT.02'], []),
    ('AI.EVERYDAY.03', 'Making a summary you can rely on', 'Request a summary grounded in a supplied text and check it '
     'against the source', 'everyday', EV + WK, ['AI.CHECK.07'], []),
    ('AI.EVERYDAY.04', 'Translation', 'Use AI translation for understanding, and know when a human translator or check '
     'is needed', 'everyday', EV, ['AI.CHECK.09'], []),
    ('AI.EVERYDAY.05', 'Study help: tutoring versus copying', 'Use AI in ways that support learning (explanations, '
     'practice, feedback) rather than replacing it', 'everyday', EV, ['AI.PROMPT.01'], []),
    ('AI.EVERYDAY.06', 'Rules about AI use at school and work', 'Find and follow the AI rules of a class, school or '
     'workplace, including disclosure', 'everyday', EV + WK, ['AI.EVERYDAY.05'], []),
    ('AI.EVERYDAY.07', 'Household and travel planning', 'Use AI for household and travel plans while checking prices, '
     'times, rules and safety details', 'everyday', EV, ['AI.CHECK.04'], []),
    ('AI.EVERYDAY.08', 'Accessibility support', 'Use AI features such as reading aloud, simplifying, captioning and '
     'describing images, and check their accuracy', 'everyday', EV + SO, ['AI.PROMPT.01'], []),
    ('AI.EVERYDAY.09', 'When a simpler tool is better', 'Choose a calculator, search engine, spreadsheet or official site '
     'when it fits the task better than a generative AI tool', 'everyday', EV + WK, ['AI.BASICS.05'], []),
    ('AI.EVERYDAY.10', 'Facts versus creative invention', 'Tell requests for facts from requests for invention, and '
     'label invented material', 'everyday', EV + CR, ['AI.CHECK.01'], []),
    # ---------------------------------------------------------------- Path: searching and documents
    ('AI.RETRIEVAL.01', 'Searching, generating and retrieval', 'Tell searching (finding existing sources) from generating '
     'text, and explain retrieval-augmented generation (RAG) simply', 'files', EV + CO + WK, ['AI.LLM.06'], []),
    ('AI.RETRIEVAL.02', 'Answers grounded in sources', 'Check that a source-grounded answer stays within what its sources '
     'say', 'files', EV + CO + WK, ['AI.RETRIEVAL.01', 'AI.CHECK.02'], []),
    ('AI.RETRIEVAL.03', 'Uploaded documents: extracting versus interpreting', 'Tell extracting what a document says from '
     'interpreting what it means, and check each', 'files', EV + WK, ['AI.RETRIEVAL.01'], []),
    ('AI.RETRIEVAL.04', 'Poor-quality and incomplete documents', 'Recognize when a scan, table or partial document may be '
     'read incorrectly or incompletely', 'files', EV + WK, ['AI.RETRIEVAL.03'], []),
    ('AI.RETRIEVAL.05', 'A document in a request does not retrain the model', 'Explain that supplying a document affects '
     'that request\'s context but does not retrain the underlying model', 'files', EV + CO + WK,
     ['AI.RETRIEVAL.01', 'AI.LEARN.08'], []),
    # ---------------------------------------------------------------- Path: practical pitfalls
    ('AI.PITFALL.01', 'Too much context and missing attachments', 'Notice overloaded requests and attachments that did '
     'not arrive or were not read', 'pitfalls', EV + WK, ['AI.LLM.05'], []),
    ('AI.PITFALL.02', 'Cut-off output and formatting errors', 'Spot truncated output and formatting errors before using '
     'a result', 'pitfalls', EV + WK, ['AI.LLM.05'], []),
    ('AI.PITFALL.03', 'Stale facts and broken links', 'Check links and dated facts before sharing them', 'pitfalls',
     EV + WK, ['AI.CHECK.04'], []),
    ('AI.PITFALL.04', 'Keep originals and version your drafts', 'Keep original files and label draft versions so changes '
     'can be compared and undone', 'pitfalls', EV + WK + CR, [], []),
    ('AI.PITFALL.05', 'Moving work between tools and checking exports', 'Check files after exporting or moving them '
     'between tools, including unsupported file types', 'pitfalls', EV + WK + CR, ['AI.PITFALL.04'], []),
    ('AI.PITFALL.06', 'Accounts, limits, support and cancellation', 'Tell a feature of one interface from a model\'s '
     'ability, and handle account limits, support and cancellation', 'pitfalls', EV + WK, ['AI.LLM.09'], []),
    # ---------------------------------------------------------------- Path: images, design, presentations
    ('AI.IMAGE.01', 'Describing an image you want', 'Write an image request that states subject, setting, style and '
     'composition', 'images', CR, ['AI.PROMPT.02'], []),
    ('AI.IMAGE.02', 'Spotting image flaws and garbled text', 'Inspect a generated image for visual errors and unreadable '
     'or misspelled text', 'images', CR, ['AI.IMAGE.01'], []),
    ('AI.IMAGE.03', 'Consistency and editing', 'Keep characters, colors and details consistent across a series, and '
     'request targeted edits', 'images', CR, ['AI.IMAGE.01'], []),
    ('AI.IMAGE.04', 'Diagrams and factual accuracy', 'Check generated diagrams, maps and charts against real data before '
     'using them', 'images', CR + EV, ['AI.IMAGE.02', 'AI.CHECK.05'], []),
    ('AI.IMAGE.05', 'Presentations: structure, visuals and export', 'Plan a clear presentation and tell a text draft from '
     'the separate step of creating and exporting a file', 'images', CR + WK, ['AI.PROMPT.04'], []),
    ('AI.IMAGE.06', 'Accessible visuals', 'Make visuals accessible with alt text, readable contrast and clear labels',
     'images', CR + SO, ['AI.IMAGE.01'], []),
    # ---------------------------------------------------------------- Path: audio, music, video, synthetic media
    ('AI.MEDIA.01', 'Transcription versus speech generation', 'Tell speech-to-text (transcription) from text-to-speech '
     '(generation) and check transcripts for errors and speaker labels', 'media', CR + EV, ['AI.BASICS.05'], []),
    ('AI.MEDIA.02', 'Subtitles and translated audio', 'Check generated subtitles and translated audio for timing, meaning '
     'and names', 'media', CR, ['AI.MEDIA.01'], []),
    ('AI.MEDIA.03', 'Voice cloning and consent', 'Explain voice cloning and why consent and disclosure matter, using '
     'dated legal examples', 'media', CR + SO, ['AI.MEDIA.01'], ['law_elvis', 'law_fcc_voice']),
    ('AI.MEDIA.04', 'Music generation and rights', 'Check the rights and terms that apply before using generated music',
     'media', CR, ['AI.MEDIA.01'], ['law_usco_part2']),
    ('AI.MEDIA.05', 'Generated and edited video', 'Check generated or edited video for consistency over time and '
     'disclose synthetic presenters', 'media', CR, ['AI.IMAGE.03'], []),
    ('AI.MEDIA.06', 'Deepfakes: checking what you see and hear', 'Verify surprising images, audio or video by checking '
     'the source and context, not one visual oddity', 'media', CR + SO + EV, ['AI.CHECK.05'], ['law_takeitdown']),
    ('AI.MEDIA.07', 'Provenance labels and the limits of detection', 'Explain content credentials and watermarks and why '
     'missing labels or detector scores are not proof', 'media', CR + SO, ['AI.MEDIA.06'], ['media_c2pa']),
    # ---------------------------------------------------------------- Path: code assistance
    ('AI.CODE.01', 'Reading a tiny program', 'Read a few lines of Python with defined terms and predict what they do',
     'code', CO, [], []),
    ('AI.CODE.02', 'Why generated code needs checking', 'Explain why code that looks right can still be wrong and how '
     'to check it', 'code', CO, ['AI.CODE.01', 'AI.LLM.04'], []),
    ('AI.CODE.03', 'Requirements and edge cases', 'State requirements clearly, including unusual inputs (edge cases)',
     'code', CO, ['AI.CODE.01'], []),
    ('AI.CODE.04', 'Tests that catch mistakes', 'Choose a test whose expected result would reveal a particular defect',
     'code', CO, ['AI.CODE.03'], []),
    ('AI.CODE.05', 'Reading error messages', 'Use an error message to locate a problem before asking for a fix',
     'code', CO, ['AI.CODE.01'], []),
    ('AI.CODE.06', 'Explaining and reviewing code', 'Use explanations as a starting point and review code line by line '
     'against its requirements', 'code', CO, ['AI.CODE.02'], []),
    ('AI.CODE.07', 'Version control: commits, differences and undoing', 'Explain commits, differences (diffs) and '
     'reverting, and why to commit before accepting generated changes', 'code', CO, ['AI.CODE.01'], []),
    ('AI.CODE.08', 'Dependencies and invented packages', 'Check that a suggested library exists, is the intended one and '
     'is trustworthy before installing it', 'code', CO, ['AI.CODE.02'], ['code_slopsquat']),
    ('AI.CODE.09', 'Secrets and security in code', 'Spot exposed secrets and unsafe handling of input in short code '
     'examples', 'code', CO, ['AI.CODE.02', 'AI.SECURITY.01'], []),
    ('AI.CODE.10', 'Maintaining code you did not write', 'Keep generated code understandable, documented and owned by '
     'someone who can maintain it', 'code', CO + WK, ['AI.CODE.06'], []),
    # ---------------------------------------------------------------- Path: agents and automation
    ('AI.AGENT.01', 'Chatbot, tool-using workflow or agent', 'Tell a chatbot, a fixed tool-using workflow and an agent '
     'that chooses its own steps', 'agents', CO + WK, ['AI.LLM.09'], []),
    ('AI.AGENT.02', 'Goals, tools, plans and stopping', 'Describe an agent\'s goal, tools, plan, feedback and stopping '
     'condition', 'agents', CO + WK, ['AI.AGENT.01'], []),
    ('AI.AGENT.03', 'Scheduled automation versus model decisions', 'Tell fixed scheduled automation from steps where a '
     'model makes choices, and where each is safer', 'agents', CO + WK, ['AI.AGENT.01'], []),
    ('AI.AGENT.04', 'Least access: limiting permissions', 'Give an automated workflow only the access its task needs',
     'agents', CO + WK, ['AI.AGENT.02'], []),
    ('AI.AGENT.05', 'Human approval before consequential actions', 'Require a person to approve messages, payments, '
     'deletions and publication before they happen', 'agents', CO + WK, ['AI.AGENT.02'], []),
    ('AI.AGENT.06', 'Logs, retries and duplicate actions', 'Use logs to check what an automation did and prevent '
     'duplicate actions after retries', 'agents', CO + WK, ['AI.AGENT.05'], []),
    # ---------------------------------------------------------------- Path: jobs and careers
    ('AI.WORK.01', 'Tasks versus whole jobs', 'Analyze how AI may change some tasks in a job without assuming the whole '
     'occupation disappears or stays the same', 'careers', WK, ['AI.BASICS.07'], []),
    ('AI.WORK.02', 'Reading job forecasts', 'Read an employment forecast as a projection with assumptions and '
     'uncertainty', 'careers', WK + SO, ['AI.WORK.01'], ['work_wef', 'work_bls_ds']),
    ('AI.WORK.03', 'Technical AI roles', 'Describe what data scientists, machine learning engineers and AI engineers '
     'typically do, without inventing pay or credential rules', 'careers', WK, ['AI.WORK.01'], ['work_bls_ds']),
    ('AI.WORK.04', 'Roles beyond coding', 'Describe AI-related roles that rely on evaluation, data work, product, design, '
     'governance and subject knowledge', 'careers', WK, ['AI.WORK.01'], []),
    ('AI.WORK.05', 'Learning routes and portfolios', 'Plan a learning route and portfolio evidence that matches a stated '
     'goal, with no guaranteed outcome', 'careers', WK, ['AI.WORK.03'], []),
    ('AI.WORK.06', 'Checking job and course claims', 'Spot exaggerated AI income, job or course promises and check them',
     'careers', WK + EV, ['AI.WORK.05'], ['law_ftc_aicomply']),
    ('AI.WORK.07', 'Responsible AI use at work', 'Follow approved tools, protect confidential information and review AI '
     'output before it reaches others at work', 'careers', WK, ['AI.PRIVACY.03'], []),
    # ---------------------------------------------------------------- Path: costs and choosing tools
    ('AI.COST.01', 'Free, subscription and pay-per-use', 'Compare free plans, subscriptions and metered (pay-per-use) '
     'pricing for a stated pattern of use', 'costs', WK + EV + CO, [], []),
    ('AI.COST.02', 'Tokens and usage pricing', 'Estimate a metered cost from token counts and stated input and output '
     'rates', 'costs', WK + CO, ['AI.LLM.02', 'AI.COST.01'], ['tokens_openai']),
    ('AI.COST.03', 'Usage limits and waiting time', 'Plan around usage limits and response time (latency)', 'costs',
     WK + EV + CO, ['AI.COST.01'], []),
    ('AI.COST.04', 'Cloud versus your own device', 'Compare running a model through a provider with running one on your '
     'own device, including hardware, privacy and upkeep', 'costs', WK + CO, ['AI.COST.01'], []),
    ('AI.COST.05', 'Open weights and licenses', 'Explain that downloadable model weights still come with license terms, '
     'and read those terms for a stated use', 'costs', WK + CO, ['AI.COST.04'], ['tech_osaid']),
    ('AI.COST.06', 'Choosing a tool for a task', 'Choose a tool from stated needs, limits and costs, including switching '
     'costs and avoiding unneeded subscriptions', 'costs', WK + EV + CO, ['AI.COST.01'], []),
    # ---------------------------------------------------------------- Path: measuring how well AI works
    ('AI.EVAL.01', 'A small test set with expected answers', 'Build a small test set of real tasks with expected answers '
     'before trusting a tool', 'evaluation', WK + CO, ['AI.CHECK.10'], []),
    ('AI.EVAL.02', 'False positives and false negatives', 'Read false positives and false negatives from a simple table '
     'and say which matters more in a situation', 'evaluation', WK + CO + SO, ['AI.EVAL.01'], []),
    ('AI.EVAL.03', 'Benchmarks and their limits', 'Explain what a benchmark score shows, why it may not match your task, '
     'and what contamination means', 'evaluation', WK + CO, ['AI.EVAL.01'], ['eval_contamination']),
    ('AI.EVAL.04', 'Accuracy, speed and cost', 'Weigh accuracy against speed and cost for a stated need', 'evaluation',
     WK + CO, ['AI.EVAL.01'], []),
    ('AI.EVAL.05', 'Comparing versions fairly', 'Compare two versions with the same tests and written criteria',
     'evaluation', WK + CO, ['AI.EVAL.01'], []),
    ('AI.EVAL.06', 'Human review and rubrics', 'Use a rubric for human review and look for failures rather than '
     'trusting a demonstration', 'evaluation', WK + CO, ['AI.EVAL.05'], []),
    ('AI.EVAL.07', 'Choosing a measure that fits', 'Choose a measure that matches the goal of a task', 'evaluation',
     WK + CO, ['AI.EVAL.02'], []),
    # ---------------------------------------------------------------- Path: bias, fairness, access
    ('AI.FAIR.01', 'How data can build in bias', 'Explain how unrepresentative or historical data can lead a model to '
     'repeat unfair patterns', 'fairness', SO + WK, ['AI.LEARN.05'], []),
    ('AI.FAIR.02', 'Uneven error rates', 'Compare error rates across groups in a table and describe a measured '
     'disparity accurately', 'fairness', SO + WK, ['AI.FAIR.01'], ['fair_gendershades', 'fair_asr']),
    ('AI.FAIR.03', 'Proxy variables', 'Recognize a proxy (an input that stands in for a protected trait) in a simple '
     'example', 'fairness', SO + WK, ['AI.FAIR.01'], ['law_illinois']),
    ('AI.FAIR.04', 'Different fairness goals', 'Explain that different fairness goals can conflict and that choosing one '
     'is a decision people must make and explain', 'fairness', SO, ['AI.FAIR.02'], []),
    ('AI.FAIR.05', 'One accuracy score can hide problems', 'Explain why an overall accuracy score can hide poor results '
     'for some groups or cases, and plan inclusive testing', 'fairness', SO + WK, ['AI.FAIR.02'], []),
    ('AI.FAIR.06', 'Stereotypes in generated content', 'Spot stereotypes in generated text or images and plan human '
     'review', 'fairness', SO + CR, ['AI.FAIR.01'], []),
    ('AI.FAIR.07', 'Language and disability access', 'Evaluate whether an AI feature works for people with different '
     'languages, accents and disabilities, using measured evidence', 'fairness', SO + EV, ['AI.FAIR.02'],
     ['fair_asr']),
    # ---------------------------------------------------------------- Path: law, policy and responsibility
    ('AI.LAW.01', 'Law, regulation, proposal, ruling, contract or guidance', 'Tell a law, a regulation, a proposed bill, '
     'a court ruling, a contract and voluntary guidance apart', 'law', SO + WK, [], ['law_nist_rmf']),
    ('AI.LAW.02', 'Who owns AI-generated work (United States)', 'Apply the US human-authorship requirement to examples, '
     'separating what is settled from what is open', 'law', SO + CR, ['AI.LAW.01'],
     ['law_thaler', 'law_usco_part2', 'law_zarya', 'law_usco_guidance']),
    ('AI.LAW.03', 'Training data and copyright: still unsettled', 'Describe the open legal questions about training AI '
     'on copyrighted works without presenting them as settled', 'law', SO + CR, ['AI.LAW.02'],
     ['law_usco_part3', 'law_bartz_kadrey']),
    ('AI.LAW.04', 'Provider terms and licenses', 'Read provider terms and licenses for what they allow and require, and '
     'tell a contract from a law', 'law', SO + WK + CR, ['AI.LAW.01'], []),
    ('AI.LAW.05', 'Likeness and voice', 'Explain likeness and voice rights and consent using dated state and federal '
     'examples', 'law', SO + CR, ['AI.LAW.01'], ['law_elvis', 'law_fcc_voice', 'law_takeitdown']),
    ('AI.LAW.06', 'Privacy rules', 'Recognize privacy rules that can apply to data used with AI, with dated US and EU '
     'examples', 'law', SO + WK, ['AI.LAW.01', 'AI.PRIVACY.03'], ['law_coppa', 'law_gdpr22']),
    ('AI.LAW.07', 'Discrimination rules and automated decisions', 'Explain that anti-discrimination and notice rules can '
     'apply when AI helps make hiring or credit decisions', 'law', SO + WK, ['AI.LAW.01', 'AI.FAIR.03'],
     ['law_nyc144', 'law_illinois', 'law_cfpb']),
    ('AI.LAW.08', 'Deceptive AI claims and consumer protection', 'Recognize deceptive claims about AI products and fake '
     'AI-written reviews as consumer-protection issues', 'law', SO + WK, ['AI.LAW.01'], ['law_ftc_aicomply']),
    ('AI.LAW.09', 'School and workplace policies, disclosure and records', 'Follow a written AI policy, disclose AI help '
     'where required and keep records', 'law', SO + WK + EV, ['AI.LAW.01'], ['law_ed_ai']),
    ('AI.LAW.10', 'An international comparison: the EU AI Act', 'Describe the EU AI Act\'s risk-based approach and dated '
     'timeline as an international comparison', 'law', SO + WK, ['AI.LAW.01'], ['law_euaiact']),
    ('AI.LAW.11', 'Responsibility when AI gets it wrong', 'Identify the facts needed before deciding who is responsible '
     'for an AI error', 'law', SO + WK, ['AI.LAW.01'], ['law_moffatt', 'case_mata']),
    ('AI.LAW.12', 'State AI laws and changing federal policy', 'Explain why AI rules differ by state and change over time, '
     'and check the current, dated status of a rule', 'law', SO + WK, ['AI.LAW.01'],
     ['law_colorado', 'law_eo14365']),
    # ---------------------------------------------------------------- Path: philosophy and social questions
    ('AI.PHIL.01', 'Reading an argument about AI', 'Identify the conclusion, premises and assumptions of a short argument '
     'about AI', 'philosophy', SO, [], []),
    ('AI.PHIL.02', 'The Turing test and its limits', 'Explain the imitation game and what passing it would and would not '
     'show', 'philosophy', SO, ['AI.PHIL.01'], ['phil_turing']),
    ('AI.PHIL.03', 'Understanding and the Chinese Room', 'Explain the Chinese Room argument, a main reply, and what remains '
     'disputed', 'philosophy', SO, ['AI.PHIL.01'], ['phil_chinese']),
    ('AI.PHIL.04', 'Claims about AI consciousness', 'Evaluate what kinds of evidence a claim that an AI is conscious would '
     'need, and why fluent self-reports do not settle it', 'philosophy', SO, ['AI.PHIL.03'], []),
    ('AI.PHIL.05', 'Anthropomorphism and trust', 'Recognize anthropomorphism (treating a system as if it had human '
     'traits) and set trust by evidence', 'philosophy', SO + EV, ['AI.PHIL.01'], ['hist_eliza']),
    ('AI.PHIL.06', 'Human agency, dependence and responsibility', 'Explain automation bias and keep human judgment and '
     'responsibility when using AI help', 'philosophy', SO + WK, ['AI.PHIL.01'], []),
    ('AI.PHIL.07', 'Alignment as a concept', 'Explain alignment as getting a system to pursue what people actually '
     'intend, including the gap between a stated goal and the intended goal', 'philosophy', SO + CO, ['AI.PHIL.01'],
     []),
    ('AI.PHIL.08', 'Weighing benefits and harms', 'Compare competing arguments about AI\'s role by their evidence and '
     'values, without treating a disputed view as fact', 'philosophy', SO, ['AI.PHIL.01'], []),
    # ---------------------------------------------------------------- Path: history and future claims
    ('AI.HISTORY.01', 'Early ideas and the name "AI"', 'Place selected early ideas (Turing\'s 1950 paper, the 1955-56 '
     'Dartmouth project) and explain why they matter', 'history', SO, [], ['phil_turing', 'hist_dartmouth']),
    ('AI.HISTORY.02', 'From written rules to learning systems', 'Explain the shift from mainly hand-written rules and '
     'search to learning from data, with dated examples', 'history', SO, ['AI.HISTORY.01', 'AI.BASICS.02'],
     ['hist_deepblue_alphago']),
    ('AI.HISTORY.03', 'The deep learning and transformer era', 'Describe selected milestones (2012 image recognition, '
     'the 2017 transformer, the 2022 chatbot release) and what they changed', 'history', SO,
     ['AI.HISTORY.02'], ['hist_alexnet', 'tech_transformer', 'hist_chatgpt']),
    ('AI.HISTORY.04', 'Narrow skill versus general intelligence claims', 'Tell narrow task performance from claims of '
     'general intelligence', 'history', SO + WK, ['AI.HISTORY.02'], []),
    ('AI.HISTORY.05', 'Forecasts, headlines and evidence', 'Tell recorded events from predictions, and judge the evidence '
     'behind a capability claim or headline', 'history', SO + WK + EV, ['AI.HISTORY.04'], []),
    ('AI.HISTORY.06', 'Energy and resource use', 'Describe energy and resource demands of AI using dated, sourced '
     'estimates and their uncertainty, without one universal per-question number', 'history', SO,
     ['AI.HISTORY.03'], ['energy_iea']),
]

SUGGESTED = {
    # optional reading that helps but is not required (shown as "you may also like")
    'AI.CHECK.02': ['AI.RETRIEVAL.02'], 'AI.SECURITY.03': ['AI.AGENT.04'], 'AI.LEARN.08': ['AI.RETRIEVAL.05'],
    'AI.MEDIA.03': ['AI.LAW.05'], 'AI.EVERYDAY.06': ['AI.LAW.09'],
    'AI.FAIR.03': ['AI.LAW.07'], 'AI.PHIL.02': ['AI.HISTORY.01'], 'AI.EVAL.03': ['AI.HISTORY.05'],
    'AI.LLM.08': ['AI.HISTORY.03'], 'AI.COST.05': ['AI.LAW.04'], 'AI.WORK.07': ['AI.LAW.09'],
}

SET_NUM = {row[0]: i + 1 for i, row in enumerate(ROWS)}
SETS = {i + 1: dict(code=row[0], title=row[1], outcome_title=row[2], module=row[3], paths=row[4],
                    requires=[SET_NUM[c] for c in row[5]], sources=row[6],
                    status='time_sensitive' if row[6] else 'stable')
        for i, row in enumerate(ROWS)}

# sanity: prerequisites point backward, modules and paths exist
_mods = {m[0] for m in MODULES}
_paths = {p['id'] for p in PATHS}
for _n, _s in SETS.items():
    assert _s['module'] in _mods, _s
    assert all(r < _n for r in _s['requires']), ('prerequisite must come earlier', _n, _s['requires'])
    assert all(p in _paths for p in _s['paths'])
assert len(SET_NUM) == len(ROWS), 'duplicate outcome code'
for _k, _v in SUGGESTED.items():
    assert _k in SET_NUM and all(x in SET_NUM for x in _v), _k

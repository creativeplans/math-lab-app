"""Grade 4 configuration: grade number and domain modules in collection order."""
GRADE = 4
VERSION = "2.0.0"
VERSION_DATE = "2026-10-09"
# Deal the correct letter of four-choice questions evenly across A-D.
BALANCE_MC = True
# Every backward branch must use a Grade 3-or-earlier standard (the build stops otherwise).
STRICT_BACKWARD = True
DOMAINS = [
    ('Operations & Algebraic Thinking', 'data_oa'),
    ('Number & Operations in Base Ten', 'data_nbt'),
    ('Number & Operations–Fractions', 'data_nf'),
    ('Number & Operations–Fractions', 'data_nf2'),
    ('Measurement & Data', 'data_md'),
    ('Measurement & Data', 'data_md2'),
    ('Geometry', 'data_g'),
]

"""Grade 5 configuration: grade number and domain modules in collection order."""
GRADE = 5
VERSION = "2.0.0"
VERSION_DATE = "2026-10-04"
# Deal the correct letter of four-choice questions evenly across A-D (Grade 6 keeps its published order).
BALANCE_MC = True
# Every backward branch must use a Grade 4-or-earlier standard (the build stops otherwise).
STRICT_BACKWARD = True
DOMAINS = [
    ('Operations & Algebraic Thinking', 'data_oa'),
    ('Number & Operations in Base Ten', 'data_nbt'),
    ('Number & Operations–Fractions', 'data_nf'),
    ('Number & Operations–Fractions', 'data_nf2'),
    ('Measurement & Data', 'data_md'),
    ('Geometry', 'data_g'),
]

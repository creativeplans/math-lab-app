"""Grade 5 configuration: grade number and domain modules in collection order."""
GRADE = 5
# Deal the correct letter of four-choice questions evenly across A-D (Grade 6 keeps its published order).
BALANCE_MC = True
DOMAINS = [
    ('Operations & Algebraic Thinking', 'data_oa'),
    ('Number & Operations in Base Ten', 'data_nbt'),
    ('Number & Operations–Fractions', 'data_nf'),
    ('Number & Operations–Fractions', 'data_nf2'),
    ('Measurement & Data', 'data_md'),
    ('Geometry', 'data_g'),
]

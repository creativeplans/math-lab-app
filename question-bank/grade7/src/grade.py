"""Grade 7 configuration: grade number and domain modules in collection order.
FORWARD 1 uses Grade 8 standards. FORWARD 2 uses Common Core high-school standards (coded HS...), which this bank
places at Grade 9 as an instructional choice; Common Core itself does not assign high-school standards to a grade."""
GRADE = 7
VERSION = "2.0.0"
VERSION_DATE = "2026-10-11"
# Deal the correct letter of four-choice questions evenly across A-D.
BALANCE_MC = True
# Every backward branch must use a Grade 6-or-earlier standard (the build stops otherwise).
STRICT_BACKWARD = True
DOMAINS = [
    ('Ratios & Proportional Relationships', 'data_rp'),
    ('The Number System', 'data_ns'),
    ('Expressions & Equations', 'data_ee'),
    ('Geometry', 'data_g'),
    ('Statistics & Probability', 'data_sp'),
]

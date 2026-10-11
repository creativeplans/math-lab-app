"""Grade 8 configuration: grade number and domain modules in collection order.
Both forward branches use Common Core high-school standards (coded HS...). Common Core does not assign high-school
standards to a grade; this bank places FORWARD 1 at Grade 9 (a first high-school step, mostly Algebra I and introductory
Geometry) and FORWARD 2 at Grade 10 (a further step in Geometry, Algebra, Functions, or Statistics)."""
GRADE = 8
VERSION = '2.0.0'
VERSION_DATE = "2026-10-11"
# Deal the correct letter of four-choice questions evenly across A-D.
BALANCE_MC = True
# Every backward branch must use a Grade 7-or-earlier standard (the build stops otherwise).
STRICT_BACKWARD = True
DOMAINS = [
    ('The Number System', 'data_ns'),
    ('Expressions & Equations', 'data_ee'),
    ('Functions', 'data_f'),
    ('Geometry', 'data_g'),
    ('Statistics & Probability', 'data_sp'),
]

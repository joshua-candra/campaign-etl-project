DROP TABLE IF EXISTS elections, candidates, finances, scores CASCADE;

CREATE TABLE candidates (
    election TEXT NOT NULL,
    recipient_id TEXT NOT NULL,
    seat TEXT NOT NULL,
    campaign_id BIGINT,
    full_name TEXT,
    first_name TEXT,
    last_name TEXT,
    gender CHAR(1),
    party TEXT,
    state CHAR(2),
    icpsr_id TEXT,
    fec_id TEXT,
    PRIMARY KEY (election, recipient_id, seat)
);

CREATE TABLE elections (
    election TEXT NOT NULL,
    recipient_id TEXT NOT NULL,
    seat TEXT NOT NULL,
    cycle INT,
    fec_year INT,
    distcyc TEXT,
    district TEXT,
    district_pres_vs FLOAT,
    incumbent_status CHAR(1),
    fec_cand_status TEXT,
    general_vote_pct FLOAT,
    general_winner CHAR(1),
    primary_vote_pct FLOAT,
    primary_winner CHAR(1),
    PRIMARY KEY (recipient_id, election, seat),
    FOREIGN KEY (recipient_id, election, seat) REFERENCES candidates(recipient_id, election, seat)
);

CREATE TABLE finances (
    election TEXT NOT NULL,
    recipient_id TEXT NOT NULL,
    seat TEXT NOT NULL,
    total_receipts NUMERIC,
    total_disbursements NUMERIC,
    total_indiv_contribs NUMERIC,
    total_unitemized NUMERIC,
    total_pac_contribs NUMERIC,
    total_party_contribs NUMERIC,
    contribs_from_candidate NUMERIC,
    ind_exp_support NUMERIC,
    ind_exp_oppose NUMERIC,
    num_givers INT,
    num_givers_total INT,
    PRIMARY KEY (recipient_id, election, seat),
    FOREIGN KEY (recipient_id, election, seat) REFERENCES candidates(recipient_id, election, seat)
);

CREATE TABLE scores (
    election TEXT NOT NULL,
    recipient_id TEXT NOT NULL,
    seat TEXT NOT NULL,
    cfscore FLOAT,
    cfscore_dyn FLOAT,
    contributor_cfscore FLOAT,
    dwdime FLOAT,
    dwnom1 FLOAT,
    dwnom2 FLOAT,
    irt_cfscore FLOAT,
    composite_score FLOAT,
    PRIMARY KEY (recipient_id, election, seat),
    FOREIGN KEY (recipient_id, election, seat) REFERENCES candidates(recipient_id, election, seat)
);
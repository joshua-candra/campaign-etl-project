CREATE TABLE candidates (
    candidate_id SERIAL PRIMARY KEY,
    recipient_id TEXT,
    campaign_id BIGINT,
    full_name TEXT,
    first_name TEXT,
    last_name TEXT,
    gender CHAR(1),
    party TEXT,
    state CHAR(2),
    seat TEXT,
    icpsr_id TEXT,
    fec_id TEXT
);

CREATE TABLE elections (
    election_id SERIAL PRIMARY KEY,
    candidate_id INT NOT NULL,
    election TEXT,
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
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id)
);

CREATE TABLE finances (
    finance_id SERIAL PRIMARY KEY,
    candidate_id INT NOT NULL,
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
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id)
);

CREATE TABLE scores (
    score_id SERIAL PRIMARY KEY,
    candidate_id INT NOT NULL,
    cfscore FLOAT,
    cfscore_dyn FLOAT,
    contributor_cfscore FLOAT,
    dwdime FLOAT,
    dwnom1 FLOAT,
    dwnom2 FLOAT,
    irt_cfscore FLOAT,
    composite_score FLOAT,
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id)
);
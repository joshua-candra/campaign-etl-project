import pandas as pd

def transform_data(df_raw):
    df = df_raw.rename(columns={
        # Candidates info
        "bonica.rid": "recipient_id",
        "bonica.cid": "campaign_id",
        "name": "full_name",
        "lname": "last_name",
        "fname": "first_name",
        "cand.gender": "gender",
        "party": "party",
        "state": "state",
        "seat": "seat",
        "recipient.type": "rec_type",
        "ICPSR": "icpsr_id",
        "FEC.ID": "fec_id",

        # Elections info
        "election": "election",
        "cycle": "cycle",
        "fecyear": "fec_year",
        "distcyc": "distcyc",
        "district": "district",
        "district.pres.vs": "district_pres_vs",
        "ico.status": "incumbent_status",
        "fec.cand.status": "fec_cand_status",
        "gen.vote.pct": "general_vote_pct",
        "gwinner": "general_winner",
        "prim.vote.pct": "primary_vote_pct",
        "pwinner": "primary_winner",

        # Finances info
        "total.receipts": "total_receipts",
        "total.disbursements": "total_disbursements",
        "total.indiv.contribs": "total_indiv_contribs",
        "total.unitemized": "total_unitemized",
        "total.pac.contribs": "total_pac_contribs",
        "total.party.contribs": "total_party_contribs",
        "total.contribs.from.candidate": "contribs_from_candidate",
        "ind.exp.support": "ind_exp_support",
        "ind.exp.oppose": "ind_exp_oppose",
        "num.givers": "num_givers",
        "num.givers.total": "num_givers_total",

        # Scores info
        "recipient.cfscore": "cfscore",
        "recipient.cfscore.dyn": "cfscore_dyn",
        "contributor.cfscore": "contributor_cfscore",
        "dwdime": "dwdime",
        "dwnom1": "dwnom1",
        "dwnom2": "dwnom2",
        "irt.cfscore": "irt_cfscore",
        "composite.score": "composite_score"
    })

    # Split into multiple DataFrames
    candidates_df = df[[
        "election", "recipient_id", "seat", "campaign_id", "full_name", "first_name", "last_name",
        "party", "gender", "state", "rec_type", "icpsr_id", "fec_id"
    ]]

    elections_df = df[[
        "election", "recipient_id", "seat", "cycle", "fec_year", "distcyc", "district", "district_pres_vs",
        "incumbent_status", "fec_cand_status", "general_vote_pct", "general_winner", "primary_vote_pct", "primary_winner"
    ]]
    
    finances_df = df[[
        "election", "recipient_id", "seat", "total_receipts", "total_disbursements", "total_indiv_contribs",
        "total_unitemized", "total_pac_contribs", "total_party_contribs", "contribs_from_candidate",
        "ind_exp_support", "ind_exp_oppose", "num_givers", "num_givers_total"
    ]]
    
    scores_df = df[[
        "election", "recipient_id", "seat", "cfscore", "cfscore_dyn", "contributor_cfscore", "dwdime",
        "dwnom1", "dwnom2", "irt_cfscore", "composite_score"
    ]]

    return {
        "candidates": candidates_df,
        "elections": elections_df,
        "finances": finances_df,
        "scores": scores_df
    }

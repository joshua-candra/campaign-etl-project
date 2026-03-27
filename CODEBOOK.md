# Campaign ETL Codebook

### 1. Candidate Identification & Logistics
*These columns identify who the candidate is and which election they are running in.*

election / cycle / fecyear: The year of the election.

bonica.rid / bonica.cid: Unique internal IDs used by the DIME database to track candidates and committees across different years.

name / lname / ffname / fname / mname / title / suffix: Standard name breakdown (Last, First, Middle, etc.).

party: Numeric code for political party (100 is Democrat, 200 is Republican, and 328 is Third Party or Independent).

state / seat / district: Geography of the race; seat usually specifies if it's Federal (Senate/House) or State level.

### 2. Ideology Scores (CFscore)
*These scores measure how liberal or conservative a candidate is based on who gives them money.*

recipient.cfscore: The candidate's primary ideology score. Negative values are Liberal; positive values are Conservative.

contributor.cfscore: The average ideology score of the people who donated to this candidate.

dwnom1 / dwnom2: These are "DW-NOMINATE" scores, which measure ideology based on voting records in Congress rather than donations.

irt.cfscore / composite.score: Alternative statistical methods (Item Response Theory) used to calculate the candidate's ideological position.

### 3. Campaign Finance & Totals
*These columns track the "Money" side of "Money in Politics."*

num.givers / num.givers.total: The count of unique donors.

total.receipts: Total money taken in.

total.disbursements: Total money spent.

total.indiv.contribs: Total money from individual people.

total.unitemized: Small donations (under $200) where the donor's name is not required by the FEC.

total.pac.contribs: Money from Political Action Committees.

ind.exp.support / ind.exp.oppose: "Outside" money spent by groups to help or hurt the candidate respectively (Independent Expenditures).

### 4. Election Results & Status
ico.status: Stands for Incumbent (I), Challenger (C), or Open Seat (O).

prim.vote.pct / gen.vote.pct: The percentage of the vote the candidate received in the Primary and General elections.

pwinner / gwinner: A flag (usually "W") indicating if they won the Primary or General.

district.pres.vs: The "Presidential Vote Share" for that district—essentially, how well the President did in that area, used to measure how "Red" or "Blue" the district is naturally.

### 5. Cross-Reference IDs
*These columns are used to link this dataset to other political databases.*

ICPSR / ICPSR2: IDs used by the Voteview database for Congressional voting records.

FEC.ID / Cand.ID: The official IDs assigned by the Federal Election Commission.

NID: National Identification number.
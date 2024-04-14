USE dota_tournaments;

CREATE TABLE teams (
    team_id INT PRIMARY KEY,
    rating INT,
    wins INT,
    losses INT,
    last_match_time INT,
    name VARCHAR(255),
    tag VARCHAR(255)
);

CREATE TABLE pro_matches (
    match_id BIGINT PRIMARY KEY,
    duration INT,
    start_time INT,
    radiant_team_id INT,
    radiant_name VARCHAR(255),
    dire_team_id INT,
    dire_name VARCHAR(255),
    league_id INT,
    league_name VARCHAR(255),
    series_id INT,
    series_type INT,
    radiant_score INT,
    dire_score INT,
    radiant_win BOOLEAN,
    radiant BOOLEAN,
    FOREIGN KEY (dire_team_id) REFERENCES teams(team_id),
    FOREIGN KEY (radiant_team_id) REFERENCES teams(team_id)
);

CREATE TABLE teams_matches(
    match_id BIGINT,
    team_id INT,
    radiant BOOLEAN,
    radiant_win BOOLEAN,
    radiant_score INT,
    dire_score INT,
    duration INT,
    start_time INT,
    league_id INT,
    league_name VARCHAR(255),
    cluster INT,
    opposing_team_id INT,
    opposing_team_name VARCHAR(255),
    opposing_team_logo VARCHAR(255),
    FOREIGN KEY (opposing_team_id) REFERENCES teams(team_id),
    FOREIGN KEY (match_id) REFERENCES  pro_matches(match_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

CREATE TABLE teams_heroes (
    hero_id INT PRIMARY KEY,
    team_id INT,
    name VARCHAR(255),
    games_played INT,
    wins INT,
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

CREATE TABLE pro_players (
    account_id INT PRIMARY KEY,
    steamid VARCHAR(255),
    avatar VARCHAR(255),
    avatarmedium VARCHAR(255),
    avatarfull VARCHAR(255),
    profileurl VARCHAR(255),
    personaname VARCHAR(255),
    last_login VARCHAR(255),
    full_history_time VARCHAR(255),
    cheese INT,
    fh_unavailable BOOLEAN,
    loccountrycode VARCHAR(255),
    name VARCHAR(255),
    country_code VARCHAR(255),
    fantasy_role INT,
    team_id INT,
    team_name VARCHAR(255),
    team_tag VARCHAR(255),
    is_locked BOOLEAN,
    is_pro BOOLEAN,
    locked_until INT,
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

CREATE TABLE teams_players (
    account_id INT,
    team_id INT,
    name VARCHAR(255),
    games_played INT,
    wins INT,
    is_current_team_member BOOLEAN,
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (account_id) REFERENCES pro_players(account_id)
);

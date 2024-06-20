import requests
from src.database_connect import *


def connect_api(url):
    """
    Connects to API and returns de data from endpoint.

    :param url: (str) url to connect.
    :return: Data from API.

    Exemple: data = connect_api('https://api.opendota.com/api/proPlayers')

    """
    return requests.get(f'{url}').json()


def store_pro_players_data(data, database_client):
    """
    Stores players data in a database.

    :param data: (str) Players data.
    :param database_client: (str) Database client connection
    :return: A message that the data was stored or not.

    Exemple: stored_data = store_pro_players_data(data, database_client)
    """
    try:
        # Preparando o cursor
        cursor = database_client.cursor()

        # Consulta SQL para inserir os dados na tabela pro_players
        insert_query = """
        INSERT INTO pro_players (
            account_id, steamid, avatar, avatarmedium, avatarfull, profileurl, 
            personaname, last_login, full_history_time, cheese, fh_unavailable, 
            loccountrycode, last_match_time, plus, name, country_code, fantasy_role, team_id, team_name, 
            team_tag, is_locked, is_pro, locked_until
        ) VALUES (
            %(account_id)s, %(steamid)s, %(avatar)s, %(avatarmedium)s, %(avatarfull)s, %(profileurl)s, 
            %(personaname)s, %(last_login)s, %(full_history_time)s, %(cheese)s, %(fh_unavailable)s, 
            %(loccountrycode)s, %(last_match_time)s, %(plus)s, %(name)s, %(country_code)s, %(fantasy_role)s, %(team_id)s, %(team_name)s, 
            %(team_tag)s, %(is_locked)s, %(is_pro)s, %(locked_until)s
        )
        """

        # Inserindo os dados
        for player in data:
            cursor.execute(insert_query, player)

        # Commit das alterações
        database_client.commit()

        # Fechando o cursor e a conexão
        cursor.close()
        return f'Successfully stored {len(data)} players in database'

    except Exception as e:
        return f'Failed to store {len(data)} players in database: {e}'


def store_pro_matches_data(data, database_client):
    """
    Stores matches data in a database.

    :param data: (str) Matches data.
    :param database_client: (str) Database client connection
    :return: A message that the data was stored or not.

    Exemple: stored_data = store_pro_matches_data(data, database_client)
    """
    try:
        # Preparando o cursor
        cursor = database_client.cursor()

        # Consulta SQL para inserir os dados na tabela pro_players
        insert_query = """
        INSERT INTO pro_matches (
            match_id, duration, start_time, radiant_team_id, radiant_name, dire_team_id, dire_name, league_id, league_name, series_id, series_type, radiant_score, dire_score, radiant_win, version
        ) VALUES (
            %(match_id)s, %(duration)s, %(start_time)s, %(radiant_team_id)s, %(radiant_name)s, %(dire_team_id)s, 
            %(dire_name)s, %(leagueid)s, %(league_name)s, %(series_id)s, %(series_type)s, 
            %(radiant_score)s, %(dire_score)s, %(radiant_win)s, %(version)s
        )
        """

        # Inserindo os dados
        for matches in data:
            cursor.execute(insert_query, matches)

        # Commit das alterações
        database_client.commit()

        # Fechando o cursor e a conexão
        cursor.close()
        return f'Successfully stored {len(data)} matches in database'

    except Exception as e:
        return f'Failed to store {len(data)} matches in database: {e}'


def store_teams_data(data, database_client):
    """
    Stores teams data in a database.

    :param data: (str) Teams data.
    :param database_client: (str) Database client connection
    :return: A message that the data was stored or not.

    Exemple: stored_data = store_teams_data(data, database_client)
    """
    try:
        # Preparando o cursor
        cursor = database_client.cursor()

        # Consulta SQL para inserir os dados na tabela pro_players
        insert_query = """
        INSERT INTO teams (
            team_id, rating, wins, losses, last_match_time, name, tag
        ) VALUES (
            %(team_id)s, %(rating)s, %(wins)s, %(losses)s, %(last_match_time)s, %(name)s, 
            %(tag)s
        )
        """

        # Inserindo os dados
        for teams in data:
            cursor.execute(insert_query, teams)

        # Commit das alterações
        database_client.commit()

        # Fechando o cursor e a conexão
        cursor.close()
        return f'Successfully stored {len(data)} teams in database'

    except Exception as e:
        return f'Failed to store {len(data)} teams in database: {e}'


def store_teams_heroes_data(data, database_client, team_id):
    """
    Stores teams heroes data in a database.

    :param data: (str) Teams heroes data.
    :param database_client: (str) Database client connection
    :param team_id: (int) ID of the team.
    :return: A message that the data was stored or not.

    Exemple: stored_data = store_teams_heroes_data(data, database_client)
    """
    try:
        # Preparando o cursor
        cursor = database_client.cursor()

        # Consulta SQL para inserir os dados na tabela pro_players
        insert_query = """
        INSERT INTO teams_heroes (
            hero_id, team_id, localized_name, games_played, wins
        ) VALUES (
            %(hero_id)s, %(team_id)s, %(localized_name)s, %(games_played)s, %(wins)s
        )
        """

        # Inserindo os dados
        for teams_heroes in data:
            query_paramms = {
                'hero_id': teams_heroes['hero_id'],
                'team_id': team_id,
                'localized_name': teams_heroes['localized_name'],
                'games_played': teams_heroes['games_played'],
                'wins': teams_heroes['wins']
            }
            cursor.execute(insert_query, query_paramms)

        # Commit das alterações
        database_client.commit()

        # Fechando o cursor e a conexão
        cursor.close()
        return f'Successfully stored {len(data)} teams heroes in database'

    except Exception as e:
        return f'Failed to store {len(data)} teams heroes in database: {e}'


def store_teams_matches_data(data, database_client, team_id):
    """
    Stores teams matches data in a database.

    :param data: (str) Teams matches data.
    :param database_client: (str) Database client connection
    :param team_id: (int) ID of the team.
    :return: A message that the data was stored or not.

    Exemple: stored_data = store_teams_matches_data(data, database_client)
    """
    try:
        # Preparando o cursor
        cursor = database_client.cursor()

        # Consulta SQL para inserir os dados na tabela pro_players
        insert_query = """
        INSERT INTO teams_matches (
            match_id, team_id, radiant, radiant_win, radiant_score, dire_score, duration, start_time, league_id, league_name, cluster, opposing_team_id, opposing_team_name, opposing_team_logo
        ) VALUES (
            %(match_id)s, %(team_id)s, %(radiant)s, %(radiant_win)s, %(radiant_score)s, %(dire_score)s, %(duration)s, %(start_time)s, %(league_id)s, %(league_name)s, %(cluster)s, %(opposing_team_id)s, %(opposing_team_name)s, %(opposing_team_logo)s
        )
        """

        # Inserindo os dados
        for teams_matches in data:
            query_paramms = {
                'match_id': teams_matches['match_id'],
                'team_id': team_id,
                'radiant': teams_matches['radiant'],
                'radiant_win': teams_matches['radiant_win'],
                'radiant_score': teams_matches['radiant_score'],
                'dire_score': teams_matches['dire_score'],
                'duration': teams_matches['duration'],
                'start_time': teams_matches['start_time'],
                'league_id': teams_matches['leagueid'],
                'league_name': teams_matches['league_name'],
                'cluster': teams_matches['cluster'],
                'opposing_team_id': teams_matches['opposing_team_id'],
                'opposing_team_name': teams_matches['opposing_team_name'],
                'opposing_team_logo': teams_matches['opposing_team_logo']
            }
            cursor.execute(insert_query, query_paramms)

        # Commit das alterações
        database_client.commit()

        # Fechando o cursor e a conexão
        cursor.close()
        return f'Successfully stored {len(data)} teams heroes in database'

    except Exception as e:
        return f'Failed to store {len(data)} teams heroes in database: {e}'


def store_teams_players_data(data, database_client, team_id):
    """
    Stores teams players data in a database.

    :param data: (str) Teams players data.
    :param database_client: (str) Database client connection
    :param team_id: (int) ID of the team.
    :return: A message that the data was stored or not.

    Exemple: stored_data = store_teams_players_data(data, database_client)
    """
    try:
        # Preparando o cursor
        cursor = database_client.cursor()

        # Consulta SQL para inserir os dados na tabela pro_players
        insert_query = """
        INSERT INTO teams_players (
            account_id, team_id, name, games_played, wins, is_current_team_member
        ) VALUES (
            %(account_id)s, %(team_id)s, %(name)s, %(games_played)s, %(wins)s, %(is_current_team_member)s
        )
        """

        # Inserindo os dados
        for teams_players in data:
            query_paramms = {
                'account_id': teams_players['account_id'],
                'team_id': team_id,
                'name': teams_players['name'],
                'games_played': teams_players['games_played'],
                'wins': teams_players['wins'],
                'is_current_team_member': teams_players['is_current_team_member']
            }
            cursor.execute(insert_query, query_paramms)

        # Commit das alterações
        database_client.commit()

        # Fechando o cursor e a conexão
        cursor.close()
        return f'Successfully stored {len(data)} teams players in database'

    except Exception as e:
        return f'Failed to store {len(data)} teams players in database: {e}'


def load_data_in_database():
    """
    Loads data in database.
    :return: None
    """
    database_client = connect_to_mysql()

    try:
        # Info of teams
        req_teams = connect_api(f'https://api.opendota.com/api/teams')
        store_teams_data(req_teams, database_client)

        # Info of pro matches
        req_pro_matches = connect_api(f'https://api.opendota.com/api/proMatches')
        store_pro_matches_data(req_pro_matches, database_client)

        # Info of teams matches
        id_of_teams = 36
        req_teams_matches = connect_api(f'https://api.opendota.com/api/teams/{id_of_teams}/matches')
        store_teams_matches_data(req_teams_matches, database_client, id_of_teams)

        # Info of pro players
        req_pro_players = connect_api(f'https://api.opendota.com/api/proPlayers')
        store_pro_players_data(req_pro_players, database_client)

        # Info of teams heroes
        req_teams_heroes = connect_api(f'https://api.opendota.com/api/teams/{id_of_teams}/heroes')
        store_teams_heroes_data(req_teams_heroes, database_client, id_of_teams)

        # Info of team players
        req_team_players = connect_api(f'https://api.opendota.com/api/teams/{id_of_teams}/players')
        store_teams_players_data(req_team_players, database_client, id_of_teams)

        disconnect_to_mysql(database_client)

        return f'All data storaged in the database.'

    except Exception as e:
        return f'Failed to get data from API. Error: {e}'

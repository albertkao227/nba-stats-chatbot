class DataPuller():
    def get_single_game_stats(stat, value, team, year):
        query = f"""
            select 
            player_name, 
            {stat} as target_stat
            from df 
            where {stat} > {value}
            and season = {year}
            and team = '{team}'
            order by {stat} desc
            limit 1
        """
        return query

    def get_agg_stats(stat, value, team, year):
        query = f"""
            select 
            player_name, 
            sum({stat}) as agg_stats, 
            count(game_id) as total_games,
            sum({stat}) / count(game_id) as target_stat
            from df 
            where season = {year}
            and team = '{team}'
            group by player_name
            having agg_stats > {value}
            order by agg_stats desc
            limit 1 
        """
        print(query)
        return query

    def get_multiple_games_stats(num_games, stat, value, team, year):
        query = f"""
            select 
            player_name, 
            count(distinct game_id) as total_games
            from df 
            where {stat} > {value}
            and season = {year}
            and team = '{team}'
            group by player_name
            order by total_games desc
        """
        return query

    def get_consecutive_games_stats(num_games, stat, value, year):
        pass
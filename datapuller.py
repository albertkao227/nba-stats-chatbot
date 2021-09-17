class DataPuller():
    def get_single_game_stats(stat, value, year):
        query = f"""
            select 
            player_name, 
            {stat}
            from df 
            where {stat} > {value}
            and season = {year}
            order by {stat} desc
        """
        return query

    def get_agg_stats(stat, value, year):
        query = f"""
            select 
            player_name, 
            sum({stat}) as agg_stats
            from df 
            where season = {year}
            group by player_name
            having agg_stats > {value}
            order by agg_stats desc 
        """
        return query

    def get_multiple_games_stats(num_games, stat, value, year):
        query = f"""
            select 
            player_name, 
            count(distinct game_id) as total_games
            from df 
            where {stat} > {value}
            and season = {year}
            group by player_name
            order by total_games desc
        """
        return query

    def get_consecutive_games_stats(num_games, stat, value, year):
        pass
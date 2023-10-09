from google.cloud.bigquery import job

from world_cup_stats.load_world_cup_players_stats_bigquery import load_world_cup_players_stats_bigquery, \
    input_players_stats_with_error_domain_file_path


def insert_world_cup_stats(input_player_stats_domain_file: str):
    load_job: job.LoadJob = load_world_cup_players_stats_bigquery(input_player_stats_domain_file)

    load_job.result()


if __name__ == '__main__':
    insert_world_cup_stats(input_players_stats_with_error_domain_file_path)

    print("Data was inserted correctly to BigQuery")

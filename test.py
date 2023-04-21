from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

table_id = "foodpanda-de-test-sharon.test_public_dataset.usa_people"

job_config = bigquery.QueryJobConfig(destination=table_id, write_disposition="WRITE_TRUNCATE")

query = """
    SELECT name, SUM(number) as total_people
    FROM `bigquery-public-data.usa_names.usa_1910_2013`
    WHERE state = 'TX'
    GROUP BY name, state
    ORDER BY total_people DESC
    LIMIT 20
"""
query_job = client.query(query, job_config=job_config)  # Make an API request.
query_job.result()  # Wait for the job to complete.

print("The query data:")
for row in query_job:
    # Row values can be accessed by field name or index.
    print(row)

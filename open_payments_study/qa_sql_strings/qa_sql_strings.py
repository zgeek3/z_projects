

dq_completeness = """
--DQ view - Completeness
CREATE OR REPLACE VIEW qa_1_dq_completeness AS
SELECT 'op' AS TABLE,
       'record_id' AS attribute,
       sum(CASE WHEN "record_id" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "record_id" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'pi_profile_id' AS attribute,
       sum(CASE WHEN "pi_profile_id" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "pi_profile_id" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'pi_npi' AS attribute,
       sum(CASE WHEN "pi_npi" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "pi_npi" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'pi_first_name' AS attribute,
       sum(CASE WHEN "pi_first_name" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "pi_first_name" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'pi_middle_name' AS attribute,
       sum(CASE WHEN "pi_middle_name" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "pi_middle_name" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'pi_last_name' AS attribute,
       sum(CASE WHEN "pi_last_name" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "pi_last_name" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'pi_city' AS attribute,
       sum(CASE WHEN "pi_city" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "pi_city" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'pi_state' AS attribute,
       sum(CASE WHEN "pi_state" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "pi_state" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'pi_zip_code' AS attribute,
       sum(CASE WHEN "pi_zip_code" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "pi_zip_code" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'thl_ccn' AS attribute,
       sum(CASE WHEN "thl_ccn" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "thl_ccn" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'thl_hospital_name' AS attribute,
       sum(CASE WHEN "thl_hospital_name" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "thl_hospital_name" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'thl_city' AS attribute,
       sum(CASE WHEN "thl_city" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "thl_city" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'thl_state' AS attribute,
       sum(CASE WHEN "thl_state" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "thl_state" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'thl_zip_code' AS attribute,
       sum(CASE WHEN "thl_zip_code" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "thl_zip_code" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'am_payment_id' AS attribute,
       sum(CASE WHEN "am_payment_id" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "am_payment_id" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'am_name' AS attribute,
       sum(CASE WHEN "am_name" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "am_name" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'am_state' AS attribute,
       sum(CASE WHEN "am_state" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "am_state" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'am_country' AS attribute,
       sum(CASE WHEN "am_country" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "am_country" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'name_of_study' AS attribute,
       sum(CASE WHEN "name_of_study" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "name_of_study" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'clinicaltrials_gov_identifier' AS attribute,
       sum(CASE WHEN "clinicaltrials_gov_identifier" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "clinicaltrials_gov_identifier" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'drug_or_device_name' AS attribute,
       sum(CASE WHEN "drug_or_device_name" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "drug_or_device_name" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'total_amount_of_payment_usdollars' AS attribute,
       sum(CASE WHEN "total_amount_of_payment_usdollars" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "total_amount_of_payment_usdollars" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'date_of_payment' AS attribute,
       sum(CASE WHEN "date_of_payment" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "date_of_payment" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'year' AS attribute,
       sum(CASE WHEN "year" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "year" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM op
UNION ALL
SELECT 'us_population' AS TABLE,
       'state_abbreviation' AS attribute,
       sum(CASE WHEN "state_abbreviation" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "state_abbreviation" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM us_population
UNION ALL
SELECT 'us_population' AS TABLE,
       'state' AS attribute,
       sum(CASE WHEN "state" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "state" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM us_population
UNION ALL
SELECT 'us_population' AS TABLE,
       'est_population' AS attribute,
       sum(CASE WHEN "est_population" IS NULL THEN 1 ELSE 0 END) AS count_null_records,
       CAST(100 * (count(*) - sum(CASE WHEN "est_population" IS NULL THEN 1 ELSE 0 END))/count(*) AS DECIMAL(5, 2)) AS fill_rate
FROM us_population""" 

dq_uniqueness = """ 
--DQ view - Uniqueness

CREATE OR REPLACE VIEW qa_2_dq_uniqueness AS
SELECT 'op' AS TABLE,
       'record_id' AS unique_contraint,
       count("record_id") AS count_records,
       count(DISTINCT "record_id") AS count_distinct_records,
       count("record_id") - count(DISTINCT "record_id") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'pi_profile_id' AS unique_contraint,
       count("pi_profile_id") AS count_records,
       count(DISTINCT "pi_profile_id") AS count_distinct_records,
       count("pi_profile_id") - count(DISTINCT "pi_profile_id") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'pi_npi' AS unique_contraint,
       count("pi_npi") AS count_records,
       count(DISTINCT "pi_npi") AS count_distinct_records,
       count("pi_npi") - count(DISTINCT "pi_npi") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'pi_first_name' AS unique_contraint,
       count("pi_first_name") AS count_records,
       count(DISTINCT "pi_first_name") AS count_distinct_records,
       count("pi_first_name") - count(DISTINCT "pi_first_name") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'pi_middle_name' AS unique_contraint,
       count("pi_middle_name") AS count_records,
       count(DISTINCT "pi_middle_name") AS count_distinct_records,
       count("pi_middle_name") - count(DISTINCT "pi_middle_name") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'pi_last_name' AS unique_contraint,
       count("pi_last_name") AS count_records,
       count(DISTINCT "pi_last_name") AS count_distinct_records,
       count("pi_last_name") - count(DISTINCT "pi_last_name") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'pi_city' AS unique_contraint,
       count("pi_city") AS count_records,
       count(DISTINCT "pi_city") AS count_distinct_records,
       count("pi_city") - count(DISTINCT "pi_city") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'pi_state' AS unique_contraint,
       count("pi_state") AS count_records,
       count(DISTINCT "pi_state") AS count_distinct_records,
       count("pi_state") - count(DISTINCT "pi_state") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'pi_zip_code' AS unique_contraint,
       count("pi_zip_code") AS count_records,
       count(DISTINCT "pi_zip_code") AS count_distinct_records,
       count("pi_zip_code") - count(DISTINCT "pi_zip_code") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'thl_ccn' AS unique_contraint,
       count("thl_ccn") AS count_records,
       count(DISTINCT "thl_ccn") AS count_distinct_records,
       count("thl_ccn") - count(DISTINCT "thl_ccn") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'thl_hospital_name' AS unique_contraint,
       count("thl_hospital_name") AS count_records,
       count(DISTINCT "thl_hospital_name") AS count_distinct_records,
       count("thl_hospital_name") - count(DISTINCT "thl_hospital_name") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'thl_city' AS unique_contraint,
       count("thl_city") AS count_records,
       count(DISTINCT "thl_city") AS count_distinct_records,
       count("thl_city") - count(DISTINCT "thl_city") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'thl_state' AS unique_contraint,
       count("thl_state") AS count_records,
       count(DISTINCT "thl_state") AS count_distinct_records,
       count("thl_state") - count(DISTINCT "thl_state") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'thl_zip_code' AS unique_contraint,
       count("thl_zip_code") AS count_records,
       count(DISTINCT "thl_zip_code") AS count_distinct_records,
       count("thl_zip_code") - count(DISTINCT "thl_zip_code") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'am_payment_id' AS unique_contraint,
       count("am_payment_id") AS count_records,
       count(DISTINCT "am_payment_id") AS count_distinct_records,
       count("am_payment_id") - count(DISTINCT "am_payment_id") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'am_name' AS unique_contraint,
       count("am_name") AS count_records,
       count(DISTINCT "am_name") AS count_distinct_records,
       count("am_name") - count(DISTINCT "am_name") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'am_state' AS unique_contraint,
       count("am_state") AS count_records,
       count(DISTINCT "am_state") AS count_distinct_records,
       count("am_state") - count(DISTINCT "am_state") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'am_country' AS unique_contraint,
       count("am_country") AS count_records,
       count(DISTINCT "am_country") AS count_distinct_records,
       count("am_country") - count(DISTINCT "am_country") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'name_of_study' AS unique_contraint,
       count("name_of_study") AS count_records,
       count(DISTINCT "name_of_study") AS count_distinct_records,
       count("name_of_study") - count(DISTINCT "name_of_study") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'clinicaltrials_gov_identifier' AS unique_contraint,
       count("clinicaltrials_gov_identifier") AS count_records,
       count(DISTINCT "clinicaltrials_gov_identifier") AS count_distinct_records,
       count("clinicaltrials_gov_identifier") - count(DISTINCT "clinicaltrials_gov_identifier") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'drug_or_device_name' AS unique_contraint,
       count("drug_or_device_name") AS count_records,
       count(DISTINCT "drug_or_device_name") AS count_distinct_records,
       count("drug_or_device_name") - count(DISTINCT "drug_or_device_name") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'total_amount_of_payment_usdollars' AS unique_contraint,
       count("total_amount_of_payment_usdollars") AS count_records,
       count(DISTINCT "total_amount_of_payment_usdollars") AS count_distinct_records,
       count("total_amount_of_payment_usdollars") - count(DISTINCT "total_amount_of_payment_usdollars") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'date_of_payment' AS unique_contraint,
       count("date_of_payment") AS count_records,
       count(DISTINCT "date_of_payment") AS count_distinct_records,
       count("date_of_payment") - count(DISTINCT "date_of_payment") AS count_duplicates
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'year' AS unique_contraint,
       count("year") AS count_records,
       count(DISTINCT "year") AS count_distinct_records,
       count("year") - count(DISTINCT "year") AS count_duplicates
FROM op
UNION ALL
SELECT 'us_population' AS TABLE,
       'state_abbreviation' AS unique_contraint,
       count("state_abbreviation") AS count_records,
       count(DISTINCT "state_abbreviation") AS count_distinct_records,
       count("state_abbreviation") - count(DISTINCT "state_abbreviation") AS count_duplicates
FROM us_population
UNION ALL
SELECT 'us_population' AS TABLE,
       'state' AS unique_contraint,
       count("state") AS count_records,
       count(DISTINCT "state") AS count_distinct_records,
       count("state") - count(DISTINCT "state") AS count_duplicates
FROM us_population
UNION ALL
SELECT 'us_population' AS TABLE,
       'est_population' AS unique_contraint,
       count("est_population") AS count_records,
       count(DISTINCT "est_population") AS count_distinct_records,
       count("est_population") - count(DISTINCT "est_population") AS count_duplicates
FROM us_population"""

dq_validity = """
--DQ view - Validity

CREATE OR REPLACE VIEW qa_3_dq_validity AS
SELECT 'op' AS TABLE,
       'record_id' AS validity_constraint,
       '> 0' AS validity_rule,
       sum(CASE WHEN "record_id" > 0 THEN 1 ELSE 0 END) AS count_valid_records,
       sum(CASE WHEN "record_id" > 0 THEN 0 ELSE 1 END) AS count_invalid_records
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'pi_npi' AS validity_constraint,
       '> 0' AS validity_rule,
       sum(CASE WHEN "pi_npi" > 0 THEN 1 ELSE 0 END) AS count_valid_records,
       sum(CASE WHEN "pi_npi" > 0 THEN 0 ELSE 1 END) AS count_invalid_records
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'am_payment_id' AS validity_constraint,
       '> 0' AS validity_rule,
       sum(CASE WHEN "am_payment_id" > 0 THEN 1 ELSE 0 END) AS count_valid_records,
       sum(CASE WHEN "am_payment_id" > 0 THEN 0 ELSE 1 END) AS count_invalid_records
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'total_amount_of_payment_usdollars' AS validity_constraint,
       '> 0' AS validity_rule,
       sum(CASE WHEN "total_amount_of_payment_usdollars" > 0 THEN 1 ELSE 0 END) AS count_valid_records,
       sum(CASE WHEN "total_amount_of_payment_usdollars" > 0 THEN 0 ELSE 1 END) AS count_invalid_records
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'date_of_payment' AS validity_constraint,
       '> 2010-01-01',
       sum(CASE WHEN "date_of_payment" > to_date('2010-01-01','YYYY-MM-DD') THEN 1 ELSE 0 END),
       sum(CASE WHEN "date_of_payment" > to_date('2010-01-01','YYYY-MM-DD') THEN 0 ELSE 1 END)
FROM op
UNION ALL
SELECT 'op' AS TABLE,
       'year' AS validity_constraint,
       '> 2010' AS validity_rule,
       sum(CASE WHEN "year" > 0 THEN 1 ELSE 0 END) AS count_valid_records,
       sum(CASE WHEN "year" > 0 THEN 0 ELSE 1 END) AS count_invalid_records
FROM op
UNION ALL
SELECT 'us_population' AS TABLE,
       'est_population' AS validity_constraint,
       '> 0' AS validity_rule,
       sum(CASE WHEN "est_population" > 0 THEN 1 ELSE 0 END) AS count_valid_records,
       sum(CASE WHEN "est_population" > 0 THEN 0 ELSE 1 END) AS count_invalid_records
FROM us_population"""

dq_consistency = """
--DQ view - Consistency

CREATE OR REPLACE VIEW qa_4_dq_consistency AS
SELECT DISTINCT "pi_state" AS distinct_values,
                count(*) AS number_records,
                'op' AS TABLE,
                'pi_state' AS COLUMN
FROM op
GROUP BY "pi_state"
UNION ALL
SELECT DISTINCT "thl_state" AS distinct_values,
                count(*) AS number_records,
                'op' AS TABLE,
                'thl_state' AS COLUMN
FROM op
GROUP BY "thl_state"
UNION ALL
SELECT DISTINCT "am_name" AS distinct_values,
                count(*) AS number_records,
                'op' AS TABLE,
                'am_name' AS COLUMN
FROM op
GROUP BY "am_name"
UNION ALL
SELECT DISTINCT "am_state" AS distinct_values,
                count(*) AS number_records,
                'op' AS TABLE,
                'am_state' AS COLUMN
FROM op
GROUP BY "am_state"
UNION ALL
SELECT DISTINCT "am_country" AS distinct_values,
                count(*) AS number_records,
                'op' AS TABLE,
                'am_country' AS COLUMN
FROM op
GROUP BY "am_country"
UNION ALL
SELECT DISTINCT cast("year" AS varchar) AS distinct_values,
                count(*) AS number_records,
                'op' AS TABLE,
                'year' AS COLUMN
FROM op
GROUP BY "year"
"""

profiling_count_records = """
--View - Profiling_count_records

CREATE OR REPLACE VIEW qa_6_data_profiling_count_records AS
SELECT schemaname AS SCHEMA,
       relname AS TABLE,
       n_tup_ins AS COUNT
FROM pg_stat_all_tables
WHERE relname LIKE 'op%'
  OR relname LIKE '%us%'
"""

profiling_information_schema = """
--View - Profiling_information_schema

CREATE OR REPLACE VIEW qa_7_data_profiling_information_schema AS
SELECT *
FROM information_schema.columns
WHERE TABLE_NAME LIKE 'op%'
  OR TABLE_NAME LIKE '%us%'
"""


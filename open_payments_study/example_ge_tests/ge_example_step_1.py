# Import required modules from GX library.
import great_expectations as gx

import pandas as pd
import os
import argparse
import time

data_dir = os.environ['OPENPAYMENTS_DATA_DIR']
print(f"Data directory: {data_dir}")

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID",
              "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO",
              "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI",
              "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "DC"]

step_1_columns = ["Teaching_Hospital_CCN", "Recipient_State", "Recipient_Zip_Code",
                    "CR_Specialty_1", "PI_Profile_ID", "PI_NPI", "PI_First_Name",
                    "PI_Middle_Name", "PI_Last_Name", "PI_City", "PI_State", "PI_Zip_Code",
                    "PI_Primary_Type_1", "PI_Specialty_1", "SAM_Name", "AM_Payment_ID",
                    "AM_Name", "AM_State", "AM_Country", "Related_Product_Indicator",
                    "Covered_or_Noncovered_Indicator_1",
                    "Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_1",
                    "Drug_or_Device_Name", "Associated_Device_or_Medical_Supply_PDI_1",
                    "Total_Amount_of_Payment_USDollars", "Date_of_Payment", "Name_of_Study",
                    "Record_ID", "ClinicalTrials_Gov_Identifier", "Year"]

def step_1_data_checks(year):
    print(f"Year being checked {year}")
    # get directory where data is being kept

    # Create Data Context.
    context = gx.get_context()

    # Import sample data into Pandas DataFrame.
    df = pd.read_csv(f'{data_dir}/step_1_truncated_data/step_1_truncated_op_data_{year}.csv'
    )

    # Connect to data.
    # Create Data Source, Data Asset, Batch Definition, and Batch.
    data_source = context.data_sources.add_pandas("pandas")
    data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

    #
    batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definition")
    batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

    # Create Expectation Suite containing two Expectations.
    suite = context.suites.add(
        gx.core.expectation_suite.ExpectationSuite(name="expectations")
    )

    # check all columns are available
    suite.add_expectation(
        gx.expectations.ExpectTableColumnsToMatchSet(column_set=step_1_columns)

    )

    # Column Teaching_Hospital_CCN:
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeOfType(column="Teaching_Hospital_CCN", type_="float64")

    )
    # Column Recipient_State:
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="Recipient_State")

    )

    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeInSet(column="Recipient_State", value_set=states)

    )

    # Column PI_NPI:
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeOfType(column="PI_NPI", type_="float64")

    )

    # Column PI_State:
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeInSet(column="PI_State", value_set=states)

    )

    # Column AM_Payment_ID:
    suite.add_expectation( # This shouldn't really be float.  Need to go back and fix in data.
        gx.expectations.ExpectColumnValuesToBeOfType(column="AM_Payment_ID", type_="int64")

    )

    # Column AM_State:
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="AM_State")

    )

    suite.add_expectation(  # This fails because there are 2 rows that have UN in the data
        gx.expectations.ExpectColumnValuesToBeInSet(column="AM_State", value_set=states)
    )

    # Column AM_Country:
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="AM_Country")

    )

    # Column Total_Amount_of_Payment_USDollars:
    suite.add_expectation( # This shouldn't really be float.  Need to go back and fix in data.
        gx.expectations.ExpectColumnValuesToBeOfType(column="Total_Amount_of_Payment_USDollars", type_="float64")

    )

    # Column Date_of_Payment:
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToMatchStrftimeFormat(column="Date_of_Payment", strftime_format="%Y-%m-%d")

    )

    # Column Record_ID:
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="Record_ID")

    )

    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeUnique(column="Record_ID")

    )

    # Column: ClinicalTrials_Gov_Identifier:
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToMatchRegex(column="ClinicalTrials_Gov_Identifier", regex="^NCT")

    )
    validation_result = batch.validate(suite)
    return validation_result


def report_results(validation_result, pr=False):

    if pr is True:
        print(validation_result)
        print("")

    print(f'The test result is: {validation_result["success"]}')


    for v in validation_result['results']:
            exp_item = v["expectation_config"]["type"]
            exp_result = v["success"]
            if exp_result == False:

                try:
                    column_tested = v["expectation_config"]["kwargs"]["column"]
                except:
                    column_tested = "N/A"
                print("")
                print(f'Expectation: {exp_item}')
                print(f'Column: {column_tested}')
                print(f'Result: {exp_result}')

                if v["success"] == False:
                    try:
                        print(f'Element count: {v["result"]["element_count"]}')
                        print(f'Unexpected count: {v["result"]["unexpected_count"]}')
                        unexpected_percent = round(v["result"]["unexpected_count"]/v["result"]["element_count"] * 100,2)
                        print(f'Percent unexpected rounded to two decimal places: {unexpected_percent}%')
                        print(f'Partial list: {v["result"]["partial_unexpected_list"][:3]}')

                    except:
                        print("Results were false, look at full results for details.")


if __name__ == "__main__":
    # measuring the time it takes to run the tests
    start_time = time.time()

    # getting command line arguments
    parser = argparse.ArgumentParser(description="Getting command line arguments")
    parser.add_argument("--year", type=int, required=True, help="year of data being checked")
    parser.add_argument("--pr", type=bool, required=False, help="if full json results will be printed")

    args = parser.parse_args()
    year = args.year
    pr = args.pr

    # running test
    step_1_validation_result = step_1_data_checks(year)
    report_results(step_1_validation_result, pr=False)

    print("")
    print("")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")

    if not step_1_validation_result["success"]:
        raise ValueError("Data quality check failed. See Report.")







import openpyxl
from us_state_abbrev import us_state_abbrev
import plotly.graph_objects

def get_data_from_file(file_name):
    file_data = openpyxl.load_workbook(file_name)
    first_sheet = file_data.active
    return first_sheet.rows

def display_data(unemployment_data):
    name_list = []
    unemployment_list = []
    for current_row in unemployment_data:
        name = current_row[0].value
        if name in us_state_abbrev:
            name_abbrev = us_state_abbrev[name]
            name_list.append(name_abbrev)
            unemployment_rate = current_row[1].value
            unemployment_list.append(unemployment_rate)



    our_beautiful_map = plotly.graph_objects.Figure(
        data= plotly.graph_objects.Choropleth(
            locations = name_list,
            z= unemployment_list,
            locationmode= "USA-states",
            colorscale= "Spectral",
            colorbar_title= "Unemployment rate per State"

        )
    )

    our_beautiful_map.update_layout(
        title_text = "Unemployment in the US September 2020",
        geo_scope = "usa"
    )
    our_beautiful_map.show()


def main():
    all_data = get_data_from_file("lanrderr-unemployment.xlsx")
    display_data(all_data)


main()

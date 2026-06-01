def get_coordinate(record: tuple):
    return record[1]


print(get_coordinate(('Scrimshawed Whale Tooth', '2A')))


def convert_coordinate(coordinate: str):
    return tuple(coordinate)


print(convert_coordinate("2A"))


def compare_records(azara_record: tuple, rui_record: tuple):
    return azara_record[1] == "".join(rui_record[1])


print(compare_records(('Model Ship in Large Bottle', '8A'),
      ('Harbor Managers Office', ('8', 'A'), 'purple')))


def create_record(azara_record: tuple, rui_record: tuple):
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"


print(create_record(('Brass Spyglass', '4B'),
      ('Seaside Cottages', ('1', 'C'), 'blue')))


def clean_up(combined_record_group: tuple) -> str:
    report = []
    
    for azara_name, azara_coord, rui_name, rui_coord, rui_color in combined_record_group:
        
        cleaned = (azara_name, rui_name, rui_coord, rui_color)
        report.append(str(cleaned))
        
    
    return "\n".join(report) + "\n"

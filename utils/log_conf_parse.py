import configparser


def get_log_conf(conf_file, section="base_logger"):
    result = {}
    parser = configparser.ConfigParser()
    parser.read(conf_file)
    section_infos = parser[section]
    for item in section_infos.items():
        if not item[1].isdigit():
            result[item[0]] = item[1]
        else:
            result[item[0]] = int(item[1])
    return result
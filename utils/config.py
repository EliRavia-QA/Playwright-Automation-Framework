import configparser
import os


class ConfigReader:
    @staticmethod
    def read_config(section, key):
        current_dir = os.path.dirname(__file__)
        root_dir = os.path.abspath(os.path.join(current_dir, '..'))
        config_path = os.path.join(root_dir, 'config.ini')
        config = configparser.ConfigParser()
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"לא נמצא קובץ config.ini בנתיב: {config_path}")
        config.read(config_path, encoding='utf-8')

        if config.has_section(section) and config.has_option(section, key):
            return config[section][key]
        else:
            raise KeyError(f"הסקשן '{section}' או המפתח '{key}' לא קיימים ב-config.ini")
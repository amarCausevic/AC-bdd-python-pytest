import configparser

class ConfigUtils:
  config = configparser.RawConfigParser()

  @staticmethod
  def get_property(section, option) -> str:
    ConfigUtils.config.read('config_file.properties')
    return ConfigUtils.config.get(section , option)

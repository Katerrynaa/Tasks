import configparser


def read(path):
    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_db(config):
    return config.get(
        "database",
        "DATABASE_URL",
        fallback="mysql://root:rootroot11@localhost:3306/departments",
    )

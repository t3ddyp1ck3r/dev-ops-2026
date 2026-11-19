"""Student scaffold. Implement rules from Lab 2; never print secret values."""
import sys

def validate(values):
    errors = []

    # TODO: APP_PORT must be an integer in 1024..65535.
    if "APP_PORT" not in values:
        errors.append("APP_PORT is missing")
    else:
        try:
            port = int(values["APP_PORT"])
            if not (1024 <= port <= 65535):
                errors.append("APP_PORT is not in the valid range 1024..65535")
        except ValueError:
            errors.append("APP_PORT is not an integer")

    # TODO: DEBUG must be false, DB_HOST and DB_PASSWORD must be nonempty.
    if "DEBUG" not in values:
        errors.append("DEBUG is missing")
    else:
        if values["DEBUG"] != "false":
            errors.append("DEBUG must be false")

    if "DB_HOST" not in values or not values["DB_HOST"]:
        errors.append("DB_HOST is missing or empty")

    if "DB_PASSWORD" not in values or not values["DB_PASSWORD"]:
        errors.append("DB_PASSWORD is missing or empty")

    # Return useful errors naming keys, not secret values.
    return errors

def load(path):
    values = {}
    for line in open(path, encoding="utf8"):
        line = line.strip()
        if line and not line.startswith("#"):
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip()
    return values

if __name__ == "__main__":
    issues = validate(load(sys.argv[1]))
    print("\n".join(issues) if issues else "Configuration accepted")
    sys.exit(bool(issues))
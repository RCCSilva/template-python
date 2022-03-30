import os

from tests.scenarios.load_all_scenarios import load_all_scenarios


def register(app):
    @app.cli.group()
    def localdb():
        """Database mock commands."""
        pass

    @localdb.command()
    def reset():
        if os.system('chmod +x ./scripts/reset_database.sh & ./scripts/reset_database.sh'):
            raise RuntimeError('reset db failed')

    @localdb.command()
    def mock():
        load_all_scenarios()

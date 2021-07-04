from valuta_admin import app
from valuta_admin.data import build_sample_db
import os
import os.path as op

# Build a sample db on the fly, if one does not exist yet.
app_dir = op.join(op.realpath(os.path.dirname(__file__)), 'valuta_admin')
database_path = op.join(app_dir, app.config['DATABASE_FILE'])
if not os.path.exists(database_path):
    build_sample_db()

if __name__ == '__main__':
    # Start app
    app.run(debug=True)

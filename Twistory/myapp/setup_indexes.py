import os.path
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, STORED, ID, TEXT, NUMERIC

# Create Scheme

StateSchema = Schema(name=TEXT, date_founded=TEXT,
                flag=ID(stored=True), population=NUMERIC, size=NUMERIC, video=STORED)

# Make index
if not os.path.exists("index"):
    os.mkdir("index")
ix = create_in("index", StateSchema)

ix = open_dir("index")

writer = ix.writer()
writer.add_document(state=u"Texas", date_founded='01/02/1845')
writer.commit()
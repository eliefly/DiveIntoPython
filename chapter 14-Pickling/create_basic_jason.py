basic_entry = {}
basic_entry['id'] = 256
basic_entry['title'] = 'Dive into history, 2009 edition'
basic_entry['tags'] = ('diveintopython', 'docbook', 'html')
basic_entry['published'] = True
basic_entry['comments_link'] = None
import json
with open('basic.json', mode='w', encoding='utf‐8') as f:
    json.dump(basic_entry, f)
#!/usr/bin/env python
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a set of bibtex of publications and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook ([see more info here](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)). 
# 
# The core python code is also in `pubsFromBibs.py`. 
# Run either from the `markdown_generator` folder after replacing updating the publist dictionary with:
# * bib file names
# * specific venue keys based on your bib file preferences
# * any specific pre-text for specific files
# * Collection Name (future feature)
# 
# TODO: Make this work with other databases of citations, 
# TODO: Merge this with the existing TSV parsing solution


from pybtex.database.input import bibtex
import pybtex.database.input.bibtex 
from time import strptime
import string
import html
import os
import re
import requests
from slugify import slugify
import numpy as np

#todo: incorporate different collection types rather than a catch all publications, requires other changes to template
publist = {
    "talks": {
        "file" : "https://raw.githubusercontent.com/lucasgautheron/CV/main/talks.bib",
        "venuekey": "note",
        "venue-pretext": "",
        "collection" : {"name":"talks",
                        "permalink":"/talks/"},
        "type": "talk"
        
    },
    "publications":{
        "file": "https://raw.githubusercontent.com/lucasgautheron/CV/main/publications.bib",
        "venuekey" : "journal",
        "venue-pretext" : "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"},
        "type": "publication"
    } 
}

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    "\\%": "%",
    }

def html_escape(text):
    """Produce entities within text."""
    #return "".join(html_escape_table.get(c,c) for c in text)
    for pattern in html_escape_table:
        text = text.replace(pattern, html_escape_table[pattern])
    return text

tags_color = {}

hex_codes = [
    "#CD5C5C", "#F08080", "#FA8072", "#E9967A", "#FFA07A", "#DC143C", "#FF0000",
    "#B22222", "#8B0000", "#FFC0CB", "#FFB6C1", "#FF69B4", "#FF1493", "#C71585",
    "#DB7093", "#FFA07A", "#FF7F50", "#FF6347", "#FF4500", "#FF8C00", "#FFA500",
    "#FFD700", "#FFFF00", "#FFFFE0", "#FFFACD", "#FAFAD2", "#FFEFD5", "#FFE4B5",
    "#FFDAB9", "#EEE8AA", "#F0E68C", "#BDB76B", "#E6E6FA", "#D8BFD8", "#DDA0DD",
    "#EE82EE", "#DA70D6", "#FF00FF", "#FF00FF", "#BA55D3", "#9370DB", "#663399",
    "#8A2BE2", "#9400D3", "#9932CC", "#8B008B", "#800080", "#4B0082", "#6A5ACD",
    "#483D8B", "#7B68EE", "#ADFF2F", "#7FFF00", "#7CFC00", "#00FF00", "#32CD32",
    "#98FB98", "#90EE90", "#00FA9A", "#00FF7F", "#3CB371", "#2E8B57", "#228B22",
    "#008000", "#006400", "#9ACD32", "#6B8E23", "#808000", "#556B2F", "#66CDAA",
    "#8FBC8B", "#20B2AA", "#008B8B", "#008080", "#00FFFF", "#00FFFF", "#E0FFFF",
    "#AFEEEE", "#7FFFD4", "#40E0D0", "#48D1CC", "#00CED1", "#5F9EA0", "#4682B4",
    "#B0C4DE", "#B0E0E6", "#ADD8E6", "#87CEEB", "#87CEFA", "#00BFFF", "#1E90FF",
    "#6495ED", "#7B68EE", "#4169E1", "#0000FF", "#0000CD", "#00008B", "#000080",
    "#191970", "#FFF8DC", "#FFEBCD", "#FFE4C4", "#FFDEAD", "#F5DEB3", "#DEB887",
    "#D2B48C", "#BC8F8F", "#F4A460", "#DAA520", "#B8860B", "#CD853F", "#D2691E",
    "#8B4513", "#A0522D", "#A52A2A", "#800000", "#FFFFFF", "#FFFAFA", "#F0FFF0",
    "#F5FFFA", "#F0FFFF", "#F0F8FF", "#F8F8FF", "#F5F5F5", "#FFF5EE", "#F5F5DC",
    "#FDF5E6", "#FFFAF0", "#FFFFF0", "#FAEBD7", "#FAF0E6", "#FFF0F5", "#FFE4E1",
    "#DCDCDC", "#D3D3D3", "#C0C0C0", "#A9A9A9", "#808080", "#696969", "#778899",
    "#708090", "#2F4F4F", "#000000"
]

for pubsource in publist:
    parser = bibtex.Parser()
    bibdata = parser.parse_string(requests.get(publist[pubsource]["file"]).text)

    #loop through the individual references in a given bibtex file
    for bib_id in bibdata.entries:
        print(bib_id)
        #reset default date
        pub_year = "1900"
        pub_month = "01"
        pub_day = "01"
        
        b = bibdata.entries[bib_id].fields
        
        venuekey = "booktitle" if bibdata.entries[bib_id].type == "inproceedings" else publist[pubsource]["venuekey"]
        venuepretext = "In the proceedings of " if bibdata.entries[bib_id].type == "inproceedings" else publist[pubsource]["venue-pretext"]
 
        try:
            pub_year = f'{b["year"]}'

            #todo: this hack for month and day needs some cleanup
            if "month" in b.keys(): 
                if(len(b["month"])<3):
                    pub_month = "0"+b["month"]
                    pub_month = pub_month[-2:]
                elif(b["month"] not in range(12)):
                    tmnth = strptime(b["month"][:3],'%b').tm_mon   
                    pub_month = "{:02d}".format(tmnth) 
                else:
                    pub_month = str(b["month"])
            if "day" in b.keys(): 
                pub_day = str(b["day"])


            pub_date = pub_year+"-"+pub_month+"-"+pub_day
            
            #strip out {} as needed (some bibtex entries that maintain formatting)
            clean_title = b["title"].replace("{", "").replace("}","").replace("\\","").replace(" ","-")    

            url_slug = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_title)
            url_slug = url_slug.replace("--","-")

            md_filename = (str(pub_date) + "-" + url_slug + ".md").replace("--","-")
            html_filename = (str(pub_date) + "-" + url_slug).replace("--","-")

            #Build Citation from text
            citation = ""

            #citation authors - todo - add highlighting for primary author?
            for author in bibdata.entries[bib_id].persons["author"]:
                citation = citation+" "+author.first_names[0]+" "+author.last_names[0]+", "

            #citation title
            citation = citation + "\"" + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + ".\""

            authorlist = []
            for author in bibdata.entries[bib_id].persons["author"]:
                authorname = author.last_names[0]
                if "." in author.first_names[0]:
                    authorname += " " + author.first_names[0]
                else:
                    authorname += " " + author.first_names[0][:1] + "."

                if "Gautheron" in author.last_names[0]:
                    authorname = f"<b>{authorname}</b>"

                authorlist.append(authorname)              

            #add venue logic depending on citation type
            venue = venuepretext+b[venuekey].replace("{", "").replace("}","").replace("\\","")

            citation = citation + " " + html_escape(venue)
            citation = citation + ", " + pub_year + "."

            
            ## YAML variables
            md = "---\ntitle: \""   + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + '"\n'
            
            md += """collection: """ +  publist[pubsource]["collection"]["name"]

            url = False
            if "url" in b.keys():
                if len(str(b["url"])) > 5:
                    md += "\npaperurl: '" + b["url"] + "'"
                    url = True

            if url:
                md += """\nlink: """ + b["url"]
            
            note = False
            # if "note" in b.keys():
            #     if len(str(b["note"])) > 5:
            #         md += "\nexcerpt: '" + html_escape(b["note"]) + "'"
            #         note = True

            #t = publist[pubsource]["type"] if "type" in publist[pubsource] else None
            keywords = bibdata.entries[bib_id].fields["keywords"] if "keywords" in bibdata.entries[bib_id].fields else None
            print(keywords)

            tags = []
            if "tags" in bibdata.entries[bib_id].fields:
                tags = [tag.strip() for tag in bibdata.entries[bib_id].fields["tags"].split(",")]
                print(tags)

            if len(tags):
                md += "\ntags:"
                for tag in tags:
                    tag_id = slugify(tag)
                    md += f"\n    - tag: {tag}"
                    md += f"\n      id: {tag_id}"

                    if tag not in tags_color:
                        tags_color[tag] = np.random.choice(hex_codes)
                        hex_codes.remove(tags_color[tag])

                    md += f"\n      color: '{tags_color[tag]}'"

            if "note" in b and "under review" in  b["note"]:
                t = "under-review"

            if bibdata.entries[bib_id].type == "inproceedings":
                t = "conference proceedings"

            if keywords:
                md += "\ntype: " + keywords

            md += "\ndate: " + str(pub_date) 

            md += "\nvenue: '" + html_escape(venue) + "'"
            md += "\nauthors: " + ", ".join(authorlist)

            if "credit" in bibdata.entries[bib_id].fields:
                credit = bibdata.entries[bib_id].fields["credit"]
                md += "\ncredit: '" + html_escape(credit) + "'"

            if "abstract" in bibdata.entries[bib_id].fields:
                abstract = bibdata.entries[bib_id].fields["abstract"]
                md += "\nabstract: \"" + html_escape(abstract) + "\""

            md += "\ncitation: '" + html_escape(citation) + "'"

            md += "\n---"

            
            ## Markdown description for individual page
            # if note:
            #     md += "\n" + html_escape(b["note"]) + "\n"

            # if url:
            #     md += "\n[Access paper here](" + b["url"] + "){:target=\"_blank\"}\n" 
            # else:
            #     md += "\nUse [Google Scholar](https://scholar.google.com/scholar?q="+html.escape(clean_title.replace("-","+"))+"){:target=\"_blank\"} for full citation"

            md_filename = os.path.basename(md_filename)

            with open("../_publications/" + md_filename, 'w') as f:
                f.write(md)
            print(f'SUCESSFULLY PARSED {bib_id}: \"', b["title"][:60],"..."*(len(b['title'])>60),"\"")
        # field may not exist for a reference
        except KeyError as e:
            print(f'WARNING Missing Expected Field {e} from entry {bib_id}: \"', b["title"][:30],"..."*(len(b['title'])>30),"\"")
            continue

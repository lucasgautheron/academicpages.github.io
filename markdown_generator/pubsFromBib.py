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
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


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

            t = publist[pubsource]["type"] if "type" in publist[pubsource] else None

            if "note" in b and "under review" in  b["note"]:
                t = "under-review"

            if bibdata.entries[bib_id].type == "inproceedings":
                t = "conference proceedings"

            if t:
                md += "\ntype: " + t

            md += "\ndate: " + str(pub_date) 

            md += "\nvenue: '" + html_escape(venue) + "'"
            md += "\nauthors: " + ", ".join(authorlist)

            credit = ""
            if "credit" in bibdata.entries[bib_id].fields:
                credit = bibdata.entries[bib_id].fields["credit"]

            md += "\ncredit: '" + html_escape(credit) + "'"

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

# Post file

The post file is where you store the content of a post. This page describe how to structure these files and make the most out of the them.

## Structure

Each post file start with the frontmatter that contains the meta data associated with the post such as its author, title, publication date and so forth. These meta data are made available in the template used to render the post under the `meta` variable. The frontmatter must be formated in the [YAML format](http://docs.ansible.com/ansible/YAMLSyntax.html). The frontmatter is is isolated by lines that start with three dash:`---`.

The remainder of the file is your content that is expected to be written in the [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

Here is an incomplete but valid example of what the structure of a post look like, a complete example is available below in the example subsection.

 ```md
 ---
title: my title
category: my category
 ---
 ## my content
 This is the text in mark down that will be transformed in *html*
 ```

## Frontmatter

The front matter is used to store the page configuration and meta data. It is written in the YAML format.

The meta data stored in the front matter are made available to template file during the generation process under the meta object. for example the title specified in the 
meta data can be accessed in the template page as follow:

```Python
{% meta.title %}
```

### available fields

| Field               | Type        | Required?    | Description                                   | Example           |
| --------------------|-----------  | ---------  | -----------                                   | ------------------- |
| **title**           | string 		  | Mandatory  | Title of the page                             | Hacking IoT devices |
| **author**          | string 		  | Mandatory  | author of the page                            | Elie, Bursztein |
| **creation_date**   | string 		  | Mandatory  | When was the post created.                    | 2 Jan 2017 17:23|
| **update_date**     | string 		  | Optional   | When was the post was last updated. Used by search engine as hint.                   | 5 Jan 2017 22:23|
| **permanent_url**   | URL 		    | Mandatory  | The url of the page, relative to the hostname | /blog/security/hacking-iot-devices|
| **category**        | string 		  | Mandatory  | Category of the post                          | security | 
| **tags**            | list 		    | Optional   | List of tags associated with the page         | [web, performance] |
| **abstract**        | string 		  | Mandatory  | short description of the page. used in meta and search| this is how to hack iot device|
| **template**        | filename 	  | Mandatory  | which template to use to render the page (without the *.html* extension) | post |
| **lang**      	    | ISO code (default:site lang)	| Optional  | language of the page used for i18n | en |
| **hidden**          | bool         | Optional (default:false)  | Don't list the post in collections or RSS or any other list| true |


## Specifying which template to apply to which post

The template used to render a given post file is specified in the frontmatter under the `template` variable. When specficying the template filename in the frontmatter omit the `.html` at the end. You instruct SiteFab where to fetch the templates from by specifying the following variable in the site configuration:

```yaml
dir:
    templates: "templates/" # where to fetch the templates used to render the various posts
```


### Date fields

When parsing the content, SiteFab attempts to find all the date fields and create for each of them an additional field that contains the data timestamp which make it 
easier to manipulate the date and output it formated in various ways thanks to the template [filter format_date](Fixme). For example SiteFab will recognize the following
field and create an additional meta data field `update_date_ts` which will contains the date as timestamp:

```yaml
update_date: 18 oct 2016 13:29
```

### Custom fields

On top of the specific field, any additional field can be added to the frontmatter and will be accessible by the template as part of the meta object.
For example the easiest way to have a banner image for each post is too add a meta banner:

```
banner: /static/images/iot-device-banner.jpg
```

which then can be used in the template page as follow:

```python
<img src="{% meta.banner %}"/>
```


### Category vs Tags

The reason why Sitefab have both a category and tags for a given is to allows summary pages (e.g the homepage) to display each post only once via the categories.
Categories are also used in the generation of the URL slugs.

### Complete example

Here is an example of a frontmatter. It is the one I used to generate the publication page for one of my paper on my [site](https://www.elie.net/publication/i-am-a-legend-hacking-hearthstone-using-statistical-learning-method)
```YAML
---
template: publication
title: I am a legend hacking Hearthstone using statistical learning methods
banner: https://www.elie.net/image/public/1476002309/i-am-a-legend-hacking-hearthstone-using-statistical-learning-methods.jpg
permanent_url: publication/i-am-a-legend-hacking-hearthstone-using-statistical-learning-method
lang: en

creation_date: 18 oct 2016 13:29

category: video game

tags: 
 - hearthstone
 - offensive technologies
 - machine learning

seo_keywords: 
 - hearthstone
 - hearthstone card game
 - hearthstone bot
 - hearthstone cards 
 - ccg
 - tgc

authors:
  - Elie, Bursztein

conference_name: Computational Intelligence and Games conference
conference_short_name: CIG
conference_location: Santorini, Greece
conference_publisher: IEEE

files:
  paper: https://cdn.elie.net/publications/i-am-a-legend-hacking-hearthstone-using-statistical-learning-methods.pdf

abstract: this paper demonstrate how to apply machine learning to Hearthstone to predict opponent future plays and game outcome.

---
```
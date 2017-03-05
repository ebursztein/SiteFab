from SiteFab.Plugins import SiteRendering
from SiteFab.SiteFab import SiteFab
from SiteFab import files


class Sitemap(SiteRendering):
    def process(self, unused, site, config):
        template_name = config.template
        
        # Loading
        try:
            template = site.jinja2.get_template(template_name)
        except:
            return SiteFab.ERROR, "sitemap", "can't find template:%s" % template_name

        # Rendering
        post_list = []
        for post in site.posts:
            if post.meta.hidden:
                continue
            # add priority and frequency
            post.meta.priority = 0.7
            post.meta.frequency = "monthly"
            if post.meta.microdata_type == "AboutPage":  # about page
                post.meta.priority = 0.8
            if post.meta.microdata_type == "Blog":  # Blog page
                post.meta.priority = 1.0
                post.meta.frequency = "daily"
            if post.meta.microdata_type == "WebSite":  # main page
                post.meta.priority = 1.0
                post.meta.frequency = "daily"
            if post.meta.microdata_type == "CollectionPage":  # publications page
                post.meta.priority = 0.8
                post.meta.frequency = "daily"
            post_list.append(post)

        for collection in site.collections.get_as_list():
            # add priority and frequency
            collection.meta.priority = 0.7
            collection.meta.frequency = "daily"

        try:
            rv = template.render(posts=post_list, collections=site.collections.get_as_list())
        except Exception as e:
            return (SiteFab.ERROR, "sitemap", e)

        # output
        path = site.get_output_dir()
        files.write_file(path, 'sitemap.xml', rv)

        log_info = "template used:%s<br>ouput:%ssitemap.xml" % (template_name, path)
        return SiteFab.OK, "sitemap", log_info
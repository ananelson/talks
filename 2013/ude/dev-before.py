    def apply_and_render_template(self, doc):
        # Figure out which template to use.
        ws_template = doc.setting('ws-template')
        if ws_template and not isinstance(ws_template, bool):
            template_file = ws_template
        else:
            template_file = self.setting('default-template')

        # Look for a file named template_file in nearest parent dir to document.
        template_path = None
        for subpath in reverse_iter_paths(doc.name):
            template_path = os.path.join(subpath, template_file)
            if file_exists(template_path):
                break

        if not template_path:
            raise dexy.exceptions.UserFeedback("no template path for %s" % doc.key)
        else:
            self.log_debug("  using template %s for %s" % (template_path, doc.key))

        # Populate template environment
        env_init_args = {
                'undefined' : jinja2.StrictUndefined
                }

        env = Environment(**env_init_args)


        dirs = [".", os.path.dirname(__file__), os.path.dirname(template_path)]
        env.loader = FileSystemLoader(dirs)

        self.log_debug("  loading template at %s" % template_path)
        template = env.get_template(template_path)

        current_dir = posixpath.dirname(doc.output_data().output_name())
        parent_dir = os.path.split(current_dir)[0]

        env_data = self.run_plugins()

        navigation = {
                }


        def section(section_name=None, url_base="/", link_text = None):
            """
            Returns an HTML link to section without needing to specify which
            document it is in (section name must be globally unique).
            """
            matching_nodes = self.wrapper.lookup_sections.get(section_name)

            if not matching_nodes:
                msg = "Trying to create a link in %s but no section found matching '%s'"
                msgargs = (doc.key, section_name,)
                raise dexy.exceptions.UserFeedback(msg % msgargs)
            elif len(matching_nodes) > 1:
                # TODO make it an option to select a default where there is
                # more than one option
                msg = "Trying to create a link in %s to '%s' but multiple docs match."
                msgargs = (doc.key, section_name,)
                raise dexy.exceptions.UserFeedback(msg % msgargs)

            assert len(matching_nodes) == 1
            data = matching_nodes[0].output_data()
            section = data[section_name]
            anchor = section['id']
            if not link_text:
                link_text = section_name

            return link_for(url_base, data.output_name(), link_text, anchor)

        def link(doc_key, section_name=None, url_base="/", link_text = None, description=False):
            """
            Returns an HTML link to document, optionally with an anchor linking to section.
            """
            matching_nodes = self.wrapper.lookup_nodes.get(doc_key)

            if not matching_nodes:
                msg = "Trying to create a link in %s but no doc found matching '%s'"
                msgargs = (doc.key, doc_key,)
                raise dexy.exceptions.UserFeedback(msg % msgargs)
            elif len(matching_nodes) > 1:
                # TODO make it an option to select a default where there is
                # more than one option
                msg = "Trying to create a link to '%s' but multiple docs match."
                msgargs = (doc_key,)
                raise dexy.exceptions.UserFeedback(msg % msgargs)

            assert len(matching_nodes) == 1
            data = matching_nodes[0].output_data()
            anchor = None

            if section_name:
                if section_name in data.keys():
                    section = data[section_name]
                    anchor = section['id']
                    if not link_text:
                        link_text = section_name
                else:
                    msg = "Did not find section named '%s' in '%s'"
                    msgargs = (section_name, doc_key)
                    raise dexy.exceptions.UserFeedback(msg % msgargs)
            else:
                if not link_text:
                    link_text = data.title()


            link_html = link_for(url_base, data.output_name(), link_text, anchor)

            if description and data.safe_setting('description'):
                return "%s\n<p>%s</p>" % (link_html, data.setting('description'))
            else:
                return link_html

        def link_for(url_base, link, link_text, anchor=None):
            url = urlparse.urljoin(url_base, link)
            if anchor:
                return """<a href="%s#%s">%s</a>""" % (url, anchor, link_text)
            else:
                return """<a href="%s">%s</a>""" % (url, link_text)

        env_data.update({
                'locals' : locals,
                'link' : link,
                'section' : section,
                'navigation' : navigation,
                'nav' : self._navobj.nodes["/%s" % current_dir],
                'root' : self._navobj.nodes["/"],
                'navobj' : self._navobj,
                'page_title' : doc.output_data().title(),
                'parent_dir' : parent_dir,
                'current_dir' : current_dir,
                's' : doc.output_data(),
                'd' : doc.output_data(),
                'source' : doc.output_data().output_name(),
                'template_source' : template_path,
                'wrapper' : self.wrapper,
                'year' : datetime.now().year
                })

        if self.wrapper.globals:
            env_data.update(dict_from_string(self.wrapper.globals))

        if doc.safe_setting('apply-ws-to-content'):
            env_init_args = {
                    'undefined' : jinja2.StrictUndefined
                    }

            if doc.safe_setting('apply-ws-to-content-variable-start-string'):
                env_init_args['variable_start_string'] = doc.setting('apply-ws-to-content-variable-start-string')
            if doc.safe_setting('apply-ws-to-content-variable-end-string'):
                env_init_args['variable_end_string'] = doc.setting('apply-ws-to-content-variable-end-string')
            if doc.safe_setting('apply-ws-to-content-block-start-string'):
                env_init_args['block_start_string'] = doc.setting('apply-ws-to-content-block-start-string')
            if doc.safe_setting('apply-ws-to-content-block-end-string'):
                env_init_args['block_end_string'] = doc.setting('apply-ws-to-content-block-end-string')

            env = Environment(**env_init_args)
            self.log_debug("Applying jinja to doc content %s" % doc.key)
            try:
                content_template = env.from_string(unicode(doc.output_data()))
                content = content_template.render(env_data)
            except Exception:
                self.log_debug("Template:\n%s" % unicode(doc.output_data()))
                self.log_debug("Env args:\n%s" % env_init_args)
                raise

        else:
            content = doc.output_data()
        
        env_data['content'] = content
        fp = os.path.join(self.setting('dir'), doc.output_data().output_name()).replace(".json", ".html")

        parent_dir = os.path.dirname(fp)
        try:
            os.makedirs(os.path.dirname(fp))
        except os.error:
            pass

        self.log_debug("  writing to %s" % (fp))
        template.stream(env_data).dump(fp, encoding="utf-8")


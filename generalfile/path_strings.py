

class _Path_Strings:
    """ String operations for Path. """
    def __str__(self):
        """ :param Path self: """
        return self._str_path

    def __repr__(self):
        """ :param Path self: """
        return self.__str__()

    def __truediv__(self, other):
        """ :param Path self: """
        return self.Path(self._path / str(other))

    def __eq__(self, other):
        """ :param Path self: """
        return str(self) == str(other)

    def __hash__(self):
        """ :param Path self: """
        return hash(str(self))

    def get_replaced_alternative_characters(self):
        """ :param Path self: """
        return {
            self.path_delimiter: "&#47;",
            ":": "&#58",
            ".": "&#46;"
        }

    def get_alternative_path(self):
        """ Get path using alternative delimiter and alternative root for windows.

            :param Path self: """
        path = str(self)
        for char, alternative in self.get_replaced_alternative_characters().items():
            path = path.replace(char, alternative)
        return self.Path(path)

    def get_path_from_alternative(self):
        """ Get path from an alternative representation.

            :param Path self: """
        path = str(self)
        for char, alternative in self.get_replaced_alternative_characters().items():
            path = path.replace(alternative, char)
        return self.Path(path)

    def absolute(self):
        """ Get new Path as absolute.

            :param Path self: """
        if self.is_absolute():
            return self
        else:
            return self.Path(self._path.absolute())

    def relative(self, base=None):
        """ Get new Path as relative.

            :param Path self:
            :param base: Defaults to working dir. """
        if self.is_relative() and base is None:
            return self
        else:
            if base is None:
                base = self.get_working_dir()
            return self.Path() if self == base else self.Path(self._path.relative_to(str(base)))

    def is_absolute(self):
        """ Get whether this Path is absolute.

            :param Path self: """
        return self._path.is_absolute()

    def is_relative(self):
        """ Get whether this Path is relative.

            :param Path self: """
        return not self.is_absolute()

    def startswith(self, path):
        """ Get whether this Path starts with given string.

            :param Path self:
            :param str or Path path:"""
        return str(self).startswith(str(self.Path(path)))

    def endswith(self, path):
        """ Get whether this Path ends with given string.

            :param Path self:
            :param str or Path path:"""
        return str(self).endswith(str(self.Path(path)))

    def remove_start(self, path):
        """ Remove a string from the start of this Path.

            :param Path self:
            :param str or Path path:"""
        str_path = str(path)
        if not self.startswith(str_path):
            return self
        else:
            return self.Path(str(self)[len(str_path):])

    def remove_end(self, path):
        """ Remove a string from the end of this Path.

            :param Path self:
            :param str or Path path:"""
        str_path = str(path)
        if not self.endswith(str_path):
            return self
        else:
            return self.Path(str(self)[:-len(str_path)])

    def same_destination(self, path):
        """ See if two paths point to the same destination.

            :param Path self:
            :param str or Path path:"""
        return self.absolute() == path.absolute()

    def parent(self, index=0):
        """ Get any parent as a new Path.
            Doesn't convert to absolute path even if needed.

            :param Path self:
            :param index: Which parent, 0 is direct parent.
            :raises IndexError: If index doesn't exist.  """
        strParent = str(self._path.parents[index])
        if strParent == ".":
            strParent = ""
        return self.Path(strParent)

    def parts(self):
        """ Get list of parts building this Path as list of strings.

            :param Path self: """
        return str(self).split(self.path_delimiter)

    def name(self):
        """ Get name of Path which is stem + suffix.

            :param Path self: """
        return self._path.name

    def with_name(self, name):
        """ Get a new Path with new name which is stem + suffix.

            :param name: Name.
            :param Path self: """
        return self.Path(self._path.with_name(str(name)))

    def stem(self):
        """ Get stem which is name without last suffix.

            :param Path self: """
        return self._path.stem

    def with_stem(self, stem):
        """ Get a new Path with new stem which is name without last suffix.

            :param stem: Name without suffix.
            :param Path self: """
        return self.Path(self.with_name(f"{stem}{self.suffix()}"))

    def suffix(self):
        """ Get suffix which is name without stem.

            :param Path self: """
        return self._path.suffix

    def with_suffix(self, suffix, index=0):
        """ Get a new Path with new suffix which is name without stem.

            :param suffix: Name without stem.
            :param Path self:
            :param index: """

        # suffixes = self.suffixes()
        # HERE **


        return self.Path(self._path.with_suffix(str(suffix)))

    def suffixes(self):
        """ Get every suffix as a list.

            :param Path self: """
        return self._path.suffixes


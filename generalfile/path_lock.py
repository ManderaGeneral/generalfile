
from generallibrary import Timer, EmptyContext


class _Lock:
    """ A one-time-use lock used by Path.lock.
        Creates a lock for folder or path with these steps:
            Wait until unlocked.
            Create lock.
            Make sure only locked by self.
        A lock is inactive if it can be removed, as there's no Lock holding it's file stream.
        """
    def __init__(self, path, *other_paths):
        self.path = path
        self.all_abs_paths = [path.Path(p).absolute() for p in other_paths + (path, )]
        self.lock_file_stream = None

    def __enter__(self):
        self._attempt_lock_creation()
        self.path.owns_lock = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._close_and_remove_lock()
        self.path.owns_lock = False

    def _get_lock_path(self):
        return self.path.get_lock_dir() / self.path.absolute().get_alternative_path()

    def _attempt_lock_creation(self):
        path_absolute = self.path.absolute()
        timer = Timer()
        while timer.seconds() < self.path.timeout_seconds:
            if self._is_locked():
                try:
                    seconds_since_creation = self._get_lock_path().seconds_since_modified()
                except:
                    pass
                else:
                    if seconds_since_creation > self.path.dead_lock_seconds:
                        self._get_lock_path().delete()
            else:
                if not self._open_and_create_lock():
                    continue

                affecting_locks = list(self._affecting_locks())
                if affecting_locks == [path_absolute]:
                    return
                elif path_absolute in affecting_locks:
                    self._close_and_remove_lock()  # Remove and try again to respect other locks
                else:
                    raise FileNotFoundError(f"Lock '{self.path}' failed to create.")
            # else:
                # print(path_absolute, list(self._affecting_locks()))
        raise TimeoutError(f"Couldn't lock '{self.path}' in time.")

    def _open_and_create_lock(self):
        if self.lock_file_stream is not None:
            raise AttributeError(f"A file stream is already opened for '{self.path}'.")

        try:
            self.lock_file_stream = open(str(self._get_lock_path()), "x")
        except FileExistsError:
            return False

        self.lock_file_stream.write("hello")
        return True

    def _close_and_remove_lock(self):
        if self.lock_file_stream is None:
            raise AttributeError(f"A file stream is not opened for '{self.path}'.")

        self.lock_file_stream.close()
        self._get_lock_path().delete()

    def _affecting_locks(self):
        path_absolute = self.path.absolute()
        for alternative_path in self.path.get_lock_dir().get_paths_in_folder():
            path = alternative_path.remove_start(self.path.get_lock_dir()).get_path_from_alternative()
            if path_absolute.startswith(path) or path.startswith(path_absolute):
                yield path

    def _is_locked(self):
        for _ in self._affecting_locks():
            return True
        return False


class _Path_ContextManager:
    """ Context manager methods for Path. """
    def __init__(self):
        self.owns_lock = False

    @staticmethod
    def _create_context_manager(path, *other_paths):
        """ :param Path path: """
        if path.startswith(path.get_lock_dir()) or path.owns_lock:  # If path is inside lock dir OR path already owns lock
            return EmptyContext()
        else:
            return _Lock(path, *other_paths)

    def lock(self, *other_paths):
        """ Create a lock for this path unless path is inside `lock dir`.
            Optionally supply additional paths to prevent them from interfering as well as creating locks for them too.

            :param generalfile.Path self: """
        other_paths = list(other_paths)
        for path in other_paths:
            paths_list = other_paths.copy()
            paths_list[paths_list.index(path)] = self  # Replace ´path´ with self
            self._create_context_manager(path, *paths_list)

        return self._create_context_manager(self, *other_paths)


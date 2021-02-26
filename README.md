# generalfile
Easily manage files cross platform.

This package and 3 other make up [ManderaGeneral](https://github.com/Mandera).

## Information
| Package                                                      | Ver                                             | Latest Release       | Python                                                                                                                   | Platform        |   Lvl | Todo                                                    | Tests   |
|:-------------------------------------------------------------|:------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------|:----------------|------:|:--------------------------------------------------------|:--------|
| [generalfile](https://github.com/ManderaGeneral/generalfile) | [2.3.14](https://pypi.org/project/generalfile/) | 2021-02-26 15:48 CET | [3.8](https://www.python.org/downloads/release/python-380/), [3.9](https://www.python.org/downloads/release/python-390/) | Windows, Ubuntu |     1 | [7](https://github.com/ManderaGeneral/generalfile#Todo) | 73.1 %  |

## Contents
<pre>
<a href='#generalfile'>generalfile</a>
├─ <a href='#Information'>Information</a>
├─ <a href='#Contents'>Contents</a>
├─ <a href='#Installation'>Installation</a>
├─ <a href='#Attributes'>Attributes</a>
└─ <a href='#Todo'>Todo</a>
</pre>

## Installation
| Command                                | <a href='https://pypi.org/project/generallibrary'>generallibrary</a>   | <a href='https://pypi.org/project/send2trash'>send2trash</a>   | <a href='https://pypi.org/project/appdirs'>appdirs</a>   | <a href='https://pypi.org/project/pandas'>pandas</a>   |
|:---------------------------------------|:-----------------------------------------------------------------------|:---------------------------------------------------------------|:---------------------------------------------------------|:-------------------------------------------------------|
| `pip install generalfile`              | Yes                                                                    | Yes                                                            | Yes                                                      | No                                                     |
| `pip install generalfile[spreadsheet]` | Yes                                                                    | Yes                                                            | Yes                                                      | Yes                                                    |
| `pip install generalfile[full]`        | Yes                                                                    | Yes                                                            | Yes                                                      | Yes                                                    |

## Attributes
<pre>
<a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/__init__.py#L1'>Module: generalfile</a>
├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/errors.py#L4'>Class: CaseSensitivityError</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/errors.py#L5'>Class: InvalidCharacterError</a>
└─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path.py#L17'>Class: Path</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path.py#L17'>Class: Path</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L59'>Method: absolute</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_lock.py#L124'>Method: as_working_dir</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/optional_dependencies/path_cfg.py#L12'>Property: cfg</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L501'>Method: contains</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L158'>Method: copy</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L216'>Method: copy_to_folder</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L325'>Method: create_folder</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L388'>Method: delete</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L415'>Method: delete_folder_content</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L265'>Method: encode</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L102'>Method: endswith</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L244'>Method: exists</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L32'>Method: get_alternative_path</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L343'>Method: get_cache_dir</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L480'>Method: get_differing_files</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L351'>Method: get_lock_dir</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L42'>Method: get_lock_path</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path.py#L43'>Method: get_parent</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L15'>Property: get_part</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L48'>Method: get_path_from_alternative</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L274'>Method: get_paths_in_folder</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L286'>Method: get_paths_recursive</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L22'>Method: get_replaced_alternative_characters</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L359'>Method: get_working_dir</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L82'>Method: is_absolute</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L232'>Method: is_file</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L238'>Method: is_folder</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L457'>Method: is_identical</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L88'>Method: is_relative</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_lock.py#L115'>Method: lock</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L252'>Method: match</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L224'>Method: move</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L157'>Method: name</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L335'>Method: open_folder</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L95'>Method: open_operation</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L150'>Method: parts</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L121'>Method: read</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L70'>Method: relative</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L126'>Method: remove_end</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L110'>Method: remove_start</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L136'>Method: rename</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L142'>Method: same_destination</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L432'>Method: seconds_since_creation</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L440'>Method: seconds_since_modified</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L378'>Method: set_working_dir</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L451'>Method: size</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/optional_dependencies/path_spreadsheet.py#L9'>Property: spreadsheet</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L94'>Method: startswith</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L171'>Method: stem</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L199'>Method: suffix</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L238'>Method: suffixes</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/optional_dependencies/path_text.py#L11'>Property: text</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L406'>Method: trash</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L424'>Method: trash_folder_content</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L185'>Method: true_stem</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path.py#L119'>Method: view</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L163'>Method: with_name</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L177'>Method: with_stem</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L205'>Method: with_suffix</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L244'>Method: with_suffixes</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_strings.py#L191'>Method: with_true_stem</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L264'>Method: without_file</a> <b>(Untested)</b>
   └─ <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L109'>Method: write</a>
</pre>

## Todo
| Module                                                                                                                                                | Message                                                                                                                                                                                      |
|:------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_lock.py#L1'>path_lock.py</a>                                     | <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_lock.py#L12'>Actually lock the additional paths given to Path.lock()</a>                                |
| <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path.py#L1'>path.py</a>                                               | <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path.py#L22'>Add a proper place for all variables, add working_dir, sys.executable and sys.prefix to it.</a> |
| <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path.py#L1'>path.py</a>                                               | <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path.py#L23'>Raise suppressable warning if space in Path.</a>                                                |
| <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path.py#L1'>path.py</a>                                               | <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path.py#L24'>Binary extension.</a>                                                                           |
| <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path.py#L1'>path.py</a>                                               | <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path.py#L25'>Pack and unpack.</a>                                                                            |
| <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L1'>path_operations.py</a>                         | <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/path_operations.py#L390'>Proper decorator to optionally suppress specified errors.</a>                       |
| <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/optional_dependencies/path_spreadsheet.py#L1'>path_spreadsheet.py</a> | <a href='https://github.com/ManderaGeneral/generalfile/blob/7604c57/generalfile/optional_dependencies/path_spreadsheet.py#L113'>Support DataFrame and Series with spreadsheet.append()</a>   |

<sup>
Generated 2021-02-26 15:48 CET for commit <a href='https://github.com/ManderaGeneral/generalfile/commit/7604c57'>7604c57</a>.
</sup>

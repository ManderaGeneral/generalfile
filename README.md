# generalfile
Easily manage files cross platform.

This package and 3 other make up [ManderaGeneral](https://github.com/Mandera).

## Information
| Package                                                      | Ver                                            | Latest Release        | Python                                                                                                                   | Platform        |   Lvl | Todo                                                    | Tests   |
|:-------------------------------------------------------------|:-----------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------|:----------------|------:|:--------------------------------------------------------|:--------|
| [generalfile](https://github.com/ManderaGeneral/generalfile) | [2.5.1](https://pypi.org/project/generalfile/) | 2021-10-28 15:25 CEST | [3.8](https://www.python.org/downloads/release/python-380/), [3.9](https://www.python.org/downloads/release/python-390/) | Windows, Ubuntu |     1 | [3](https://github.com/ManderaGeneral/generalfile#Todo) | 100.0 % |

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
| Command                   | <a href='https://pypi.org/project/generallibrary'>generallibrary</a>   | <a href='https://pypi.org/project/send2trash'>send2trash</a>   | <a href='https://pypi.org/project/appdirs'>appdirs</a>   | <a href='https://pypi.org/project/pandas'>pandas</a>   | <a href='https://pypi.org/project/dill'>dill</a>   |
|:--------------------------|:-----------------------------------------------------------------------|:---------------------------------------------------------------|:---------------------------------------------------------|:-------------------------------------------------------|:---------------------------------------------------|
| `pip install generalfile` | Yes                                                                    | Yes                                                            | Yes                                                      | Yes                                                    | Yes                                                |

## Attributes
<pre>
<a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/__init__.py#L1'>Module: generalfile</a>
├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/errors.py#L6'>Class: CaseSensitivityError</a>
├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/errors.py#L10'>Class: InvalidCharacterError</a>
└─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path.py#L18'>Class: Path</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path.py#L18'>Class: Path</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L32'>Method: absolute</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_lock.py#L124'>Method: as_working_dir</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/optional_dependencies/path_cfg.py#L13'>Property: cfg</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L414'>Method: contains</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L94'>Method: copy</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L155'>Method: copy_to_folder</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L225'>Method: create_folder</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L299'>Method: delete</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L331'>Method: delete_folder_content</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L204'>Method: empty</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L268'>Method: encode</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L94'>Method: endswith</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L196'>Method: exists</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L24'>Method: from_alternative</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L271'>Method: get_cache_dir</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L387'>Method: get_differing_files</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L281'>Method: get_lock_dir</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L290'>Method: get_lock_path</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L243'>Method: get_working_dir</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L59'>Method: is_absolute</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L171'>Method: is_file</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L177'>Method: is_folder</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L369'>Method: is_identical</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L66'>Method: is_relative</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L183'>Method: is_root</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_lock.py#L115'>Method: lock</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L261'>Method: match</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L73'>Method: mirror_path</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L163'>Method: move</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L153'>Method: name</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L235'>Method: open_folder</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L29'>Method: open_operation</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L434'>Method: pack</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L145'>Method: parts</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/optional_dependencies/path_pickle.py#L12'>Property: pickle</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L61'>Method: read</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L42'>Method: relative</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L120'>Method: remove_end</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L103'>Method: remove_start</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L70'>Method: rename</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L136'>Method: same_destination</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path.py#L104'>Method: scrub</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L348'>Method: seconds_since_creation</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L356'>Method: seconds_since_modified</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L262'>Method: set_working_dir</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L363'>Method: size</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/optional_dependencies/path_spreadsheet.py#L13'>Property: spreadsheet</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L85'>Method: startswith</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L169'>Method: stem</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L201'>Method: suffix</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L245'>Method: suffixes</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/optional_dependencies/path_text.py#L12'>Property: text</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L16'>Method: to_alternative</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L320'>Method: trash</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L340'>Method: trash_folder_content</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L185'>Method: true_stem</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L453'>Method: unpack</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L160'>Method: with_name</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L176'>Method: with_stem</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L209'>Method: with_suffix</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L252'>Method: with_suffixes</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_strings.py#L192'>Method: with_true_stem</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L216'>Method: without_file</a>
   └─ <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_operations.py#L49'>Method: write</a>
</pre>

## Todo
| Module                                                                                                                                               | Message                                                                                                                                                                                   |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path.py#L1'>path.py</a>                                               | <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path.py#L23'>Binary extension.</a>                                                                         |
| <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/optional_dependencies/path_spreadsheet.py#L1'>path_spreadsheet.py</a> | <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/optional_dependencies/path_spreadsheet.py#L112'>Support DataFrame and Series with spreadsheet.append()</a> |
| <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_lock.py#L1'>path_lock.py</a>                                     | <a href='https://github.com/ManderaGeneral/generalfile/blob/master/generalfile/path_lock.py#L12'>Lock the optional extra paths.</a>                                                       |

<sup>
Generated 2021-11-02 17:39 CET for commit <a href='https://github.com/ManderaGeneral/generalfile/commit/master'>master</a>.
</sup>

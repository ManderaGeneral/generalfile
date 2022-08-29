# generalpackager
Tools to interface GitHub, PyPI, NPM and local modules / repos. Used for generating files to keep projects dry and synced. Tailored for my general packages.

This package and 3 other make up [ManderaGeneral](https://github.com/ManderaGeneral).

## Information
| Package                                                              | Ver                                              | Latest Release        | Python                                                                                                                   | Platform        |   Lvl | Todo                                                        | Tests   |
|:---------------------------------------------------------------------|:-------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------|:----------------|------:|:------------------------------------------------------------|:--------|
| [generalpackager](https://github.com/ManderaGeneral/generalpackager) | [0.4](https://pypi.org/project/generalpackager/) | 2022-08-24 11:34 CEST | [3.8](https://www.python.org/downloads/release/python-380/), [3.9](https://www.python.org/downloads/release/python-390/) | Windows, Ubuntu |     2 | [8](https://github.com/ManderaGeneral/generalpackager#Todo) | 60.3 %  |

## Contents
<pre>
<a href='#generalpackager'>generalpackager</a>
├─ <a href='#Information'>Information</a>
├─ <a href='#Contents'>Contents</a>
├─ <a href='#Installation'>Installation</a>
├─ <a href='#Attributes'>Attributes</a>
└─ <a href='#Todo'>Todo</a>
</pre>

## Installation
| Command                       | <a href='https://pypi.org/project/generallibrary'>generallibrary</a>   | <a href='https://pypi.org/project/generalfile'>generalfile</a>   | <a href='https://pypi.org/project/pandas'>pandas</a>   | <a href='https://pypi.org/project/gitpython'>gitpython</a>   | <a href='https://pypi.org/project/requests'>requests</a>   | <a href='https://pypi.org/project/pyinstaller'>pyinstaller</a>   |
|:------------------------------|:-----------------------------------------------------------------------|:-----------------------------------------------------------------|:-------------------------------------------------------|:-------------------------------------------------------------|:-----------------------------------------------------------|:-----------------------------------------------------------------|
| `pip install generalpackager` | Yes                                                                    | Yes                                                              | Yes                                                    | Yes                                                          | Yes                                                        | Yes                                                              |

## Attributes
<pre>
<a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/__init__.py#L1'>Module: generalpackager</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/github.py#L13'>Class: GitHub</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/github.py#L29'>Method: download</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/github.py#L25'>Method: exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/github.py#L80'>Method: get_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/github.py#L47'>Method: get_owners_packages</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/github.py#L68'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/github.py#L58'>Method: get_website</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/github.py#L90'>Method: request_kwargs</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/github.py#L86'>Method: set_description</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/github.py#L74'>Method: set_topics</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/github.py#L64'>Method: set_website</a> <b>(Untested)</b>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/github.py#L22'>Property: url</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localmodule.py#L9'>Class: LocalModule</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localmodule.py#L27'>Method: exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localmodule.py#L67'>Method: get_all_local_modules</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localmodule.py#L89'>Method: get_dependants</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localmodule.py#L74'>Method: get_dependencies</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localmodule.py#L21'>Property: module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localmodule.py#L42'>Property: objInfo</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/#L425'>Property: path</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo.py#L14'>Class: LocalRepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_target.py#L6'>Class: Targets</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/metadata.py#L7'>Class: cls_metadata</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo.py#L47'>Method: exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo.py#L126'>Method: format_file</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L61'>Method: get_exeproduct_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L57'>Method: get_exetarget_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L53'>Method: get_generate_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L17'>Method: get_git_exclude_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L65'>Method: get_git_ignore_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L73'>Method: get_index_js_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L45'>Method: get_init_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L29'>Method: get_license_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L25'>Method: get_manifest_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L13'>Method: get_metadata_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L69'>Method: get_npm_ignore_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L9'>Method: get_org_readme_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L81'>Method: get_package_json_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo.py#L72'>Method: get_package_paths_gen</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L49'>Method: get_randomtesting_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L5'>Method: get_readme_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L21'>Method: get_setup_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L77'>Method: get_test_js_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L37'>Method: get_test_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo.py#L58'>Method: get_test_paths</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L41'>Method: get_test_template_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_paths.py#L33'>Method: get_workflow_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo.py#L80'>Method: git_changed_files</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_target.py#L22'>Method: is_django</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_target.py#L26'>Method: is_exe</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_target.py#L18'>Method: is_node</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_target.py#L14'>Method: is_python</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo.py#L35'>Method: metadata_exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo.py#L40'>Property: name</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo.py#L94'>Method: replace_camel_case</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo.py#L123'>Method: replace_docstrings</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo.py#L52'>Method: repo_exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo.py#L29'>Property: target</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_target.py#L52'>Method: targetted</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo.py#L65'>Method: text_in_tests</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/node/localrepo_node.py#L6'>Class: LocalRepo_Node</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/python/localrepo_python.py#L9'>Class: LocalRepo_Python</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/python/localrepo_python.py#L13'>Method: get_venv_path</a> <b>(Untested)</b>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/python/localrepo_python.py#L20'>Method: unittest</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager.py#L18'>Class: Packager</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/github.py#L13'>Class: GitHub</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localmodule.py#L9'>Class: LocalModule</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo.py#L14'>Class: LocalRepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/other/packages.py#L8'>Class: Packages</a> <b>(Untested)</b>
│  │  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/other/packages.py#L28'>Method: all_packages</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/pypi.py#L26'>Class: PyPI</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_target.py#L6'>Class: Targets</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L75'>Property: all_files_by_relative_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_github.py#L20'>Method: commit_and_push</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L153'>Method: compare_local_to_github</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L161'>Method: compare_local_to_pypi</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L103'>Method: create_blank_locally</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L79'>Method: file_by_relative_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L88'>Property: file_secret_readme</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L42'>Property: files</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L132'>Method: filter_relative_filenames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_relations.py#L59'>Method: general_bumped_set</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_relations.py#L65'>Method: general_changed_dict</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L336'>Method: generate_generate</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L228'>Method: generate_git_exclude</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L362'>Method: generate_index_js</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L320'>Method: generate_init</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L234'>Method: generate_license</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L407'>Method: generate_localfiles</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L219'>Method: generate_manifest</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L356'>Method: generate_npm_ignore</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L386'>Method: generate_package_json</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L294'>Method: generate_personal_readme</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L328'>Method: generate_randomtesting</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L264'>Method: generate_readme</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L168'>Method: generate_setup</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L371'>Method: generate_test_js</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L346'>Method: generate_test_template</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L248'>Method: generate_workflow</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_markdown.py#L206'>Method: get_attributes_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_markdown.py#L10'>Method: get_badges_dict</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_metadata.py#L27'>Method: get_classifiers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_relations.py#L26'>Method: get_dependants</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_relations.py#L7'>Method: get_dependencies</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_markdown.py#L87'>Method: get_description_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_workflow.py#L82'>Method: get_env</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_markdown.py#L212'>Method: get_footnote_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_markdown.py#L93'>Method: get_information_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_markdown.py#L122'>Method: get_installation_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_pypi.py#L9'>Method: get_latest_release</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L94'>Method: get_new_packager</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_relations.py#L37'>Method: get_ordered_packagers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_relations.py#L53'>Method: get_owners_package_names</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_workflow.py#L117'>Method: get_sync_job</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_markdown.py#L63'>Method: get_todos</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_markdown.py#L73'>Method: get_todos_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_metadata.py#L16'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_workflow.py#L26'>Method: get_triggers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_workflow.py#L103'>Method: get_unittest_job</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_relations.py#L73'>Method: get_untested_objInfo_dict</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_api.py#L79'>Property: github</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_api.py#L47'>Method: github_available</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_markdown.py#L156'>Method: github_link</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_markdown.py#L165'>Method: github_link_path_line</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_workflow.py#L179'>Method: if_publish_bump</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_workflow.py#L186'>Method: if_publish_publish</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_metadata.py#L33'>Method: is_bumped</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_target.py#L22'>Method: is_django</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_target.py#L26'>Method: is_exe</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/shared.py#L14'>Method: is_general</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_target.py#L18'>Method: is_node</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/localrepo/base/localrepo_target.py#L14'>Method: is_python</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_api.py#L86'>Property: localmodule</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_api.py#L52'>Method: localmodule_available</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_api.py#L71'>Property: localrepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_api.py#L42'>Method: localrepo_available</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/shared.py#L10'>Method: name_is_general</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_api.py#L93'>Property: pypi</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_api.py#L60'>Method: pypi_available</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_files.py#L116'>Method: relative_path_is_aesthetic</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_pypi.py#L23'>Method: reserve_name</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_workflow.py#L133'>Method: run_ordered_methods</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/shared.py#L19'>Property: simple_name</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_workflow.py#L54'>Method: step_install_necessities</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_workflow.py#L69'>Method: step_install_package_git</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_workflow.py#L61'>Method: step_install_package_pip</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_workflow.py#L126'>Method: step_run_packager_method</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_workflow.py#L47'>Method: step_setup_python</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_workflow.py#L41'>Method: step_setup_ssh</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_workflow.py#L93'>Method: steps_setup</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager.py#L43'>Method: summary_packagers</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_github.py#L12'>Method: sync_github_metadata</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_metadata.py#L47'>Property: target</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_workflow.py#L174'>Method: upload_package_summary</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_workflow.py#L153'>Method: workflow_sync</a> <b>(Untested)</b>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/packager_workflow.py#L140'>Method: workflow_unittest</a> <b>(Untested)</b>
└─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/pypi.py#L26'>Class: PyPI</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/pypi.py#L47'>Method: download</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/pypi.py#L37'>Method: exists</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/pypi.py#L70'>Method: get_date</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/pypi.py#L59'>Method: get_owners_packages</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/pypi.py#L41'>Method: get_tarball_url</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/pypi.py#L63'>Method: get_version</a>
   └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/f0340b4/generalpackager/api/pypi.py#L34'>Property: url</a>
</pre>

## Todo
| Module                                                                                                                                                      | Message                                                                                                                                                                                                  |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/other/packages.py#L1'>packages.py</a>                                | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/other/packages.py#L10'>Generate Python file in generalpackager containing general packages.</a>                   |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L1'>pypi.py</a>                                          | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L12'>Move download to it's own package.</a>                                                           |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L1'>pypi.py</a>                                          | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L66'>Find a faster fetch for latest PyPI version and datetime.</a>                                    |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L1'>github.py</a>                                      | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L15'>Get and Set GitHub repo private.</a>                                                           |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/localrepo/base/localrepo.py#L1'>localrepo.py</a>                 | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/localrepo/base/localrepo.py#L19'>Search for imports to list dependencies.</a>                                 |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/localrepo/python/localrepo_python.py#L1'>localrepo_python.py</a> | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/localrepo/python/localrepo_python.py#L45'>Make sure twine is installed when trying to upload to pypi.</a>     |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L1'>packager_markdown.py</a>                    | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L70'>Sort todos by name to decrease automatic commit changes.</a>                            |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L1'>packager_files.py</a>                          | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L43'>Watermark generated files to prevent mistake of thinking you can modify them directly.</a> |

<sup>
Generated 2022-08-24 11:34 CEST for commit <a href='https://github.com/ManderaGeneral/generalpackager/commit/f0340b4'>f0340b4</a>.
</sup>

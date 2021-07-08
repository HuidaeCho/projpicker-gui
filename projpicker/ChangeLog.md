# Change Log

## v0.1.6.post2
Wed Jul 7 18:06:09 2021 -0400

* 6ccc69f  (tag: refs/tags/v0.1.6.post2) Fix test_or.out
* 0973846  0.1.6.post2
* ebe9f5d  Fix #35
* 40c609c  Oops! Revert add widgets order
* 5e50c69  Logical order of widgets (map => list => info)
* fae577b  Resolve conflicts
* bfe4eb4  Merge branch 'main' into desktop_gui_refactor
* dfccdf4  (refs/heads/desktop_gui_refactor) Support for multiple layouts
* 5d0129b  Move confirm_load into sole webview_loaded event handler
* 0a04c52  Javascript error was poping up at startup when there was no title change
* 0b1033a  Use BBox comparison for deduplication
* a983210  Do not append existing BBoxs for OR even before deduplicating
* 2917b1c  Merge branch 'main' of github.com:HuidaeCho/projpicker into main
* 0e1b938  Fix deduplicating code in sort_bbox()
* 7105803  Merge pull request #33 from HuidaeCho/desktop_gui_refactor
* 5c2a360  Refactor logical operation code
* 75999c2  Do not modify input geoms from (parse|query)_mixed_geoms()
* 3a487cd  Refactor desktop GUI
* 8d040bc  Comments
* cf8ddf4  Handle error that occurs when there is no drawn geometry but logical operator is switched
* 64b2e8c  Add logical operator to query, rerun query when new logical operator is chosen
* e63d86f  Bind buttons to get chosen logical operator
* 3981926  Add rb group
* e4e2532  Add logical operator radio buttons. Not bound yet
* cfddc58  Merge pull request #29 from HuidaeCho/folium
* aaad574  Remove unneeded global switches
* c36a68f  Add the default title to map.html
* ff56881  Download external CSSs and JSs just in case (we can even make them available locally)
* c7c333a  Remove unused imports from gui.py
* c42a90d  automatic tabbing
* e7851a4  Add integrity and crossorigin attributes for security
* cfbf88d  Try to remove unnecessary CSSs and JSs
* 14fe4dd  Do we use folium?
* 956bfdc  80cols
* d35744d  Add tabs for aligned text. (#28)
* 0fdfb70  naming
* c16ad00  Refactoring Desktop GUI
* c252c7a  Dont allow drawn features to be clickable
* 589fbda  Map inline with other parts
* f227d1c  Consistent label styles between crs list and info
* 64ac70e  drawCRSBBOX -> drawCRSBBox for consistent naming
* fbd4a95  Update desktop GUI
* 29e4beb  Selection of CRS now draws CRS bbox on map (#25)

## v0.1.6.post1
Fri Jul 2 13:54:23 2021 -0400

* c1aabdc  (tag: refs/tags/v0.1.6.post1) Use self.crs to find selected_crs and expose auth:code to be consistent with the core GUI
* 6811dd3  v0.1.6.post1
* b50809b  tidy_line() should not return anything as documented
* 46da756  Add max argument to avoid broken pipe errors when applying head
* 4ccab08  Use an instance variable instead of a class variable
* d2faf7e  Two blank lines above def
* 12aff8c  Reorder methods; Expose selected CRS to we can reuse the ProjPickerGUI class in another project
* afaffd6  Termux install
* c5937e6  Running on Android

## v0.1.6
Thu Jul 1 20:48:03 2021 -0400

* d2dea0e  (tag: refs/tags/v0.1.6) Core version 0.1.6
* b157191  single only for has_gui
* 20f24a2  Some embedded systems do not provide tkinter
* 3db855d  reversed_coors => latlon_coors to be more specific
* c80cd60  as expected => as documented
* 76e5d6d  chars => characters
* 686b79b  Update README.md
* b2a729a  Update README.md
* 888bdc7  Desktop GUI
* 2d7ec0c  Center CRS Info
* 06d24ff  Remove unused browser_size
* 35d595d  CRS List => Select a CRS
* bc44e74  More refactoring
* 69185fb  Comments
* 5c84e14  Refactor gui.py
* 1e8dacd  verbify method names
* 4ace099  80 columns; no periods in comments (use semi-colons because in many cases for single sentences, we do not use a period)
* cb58392  Merge pull request #19 from HuidaeCho/desktop_gui_python
* 45d09f5  Merge branch 'main' into desktop_gui_python
* eef953d  Remove unneeded line
* d1964c0  Update README
* 13eeaae  functional assignment over if else
* e9f1fc2  geo => geom
* 3eee720  single quotes; CRS's => CRSs
* e770292  openstreat.html => map.html
* 2dedc68  Single blank line within defs
* ae8792d  Url => url
* 744f9dd  Capitalization following PEP8; Two blank lines between defs
* bbfed90  Remove blank lines between HTML tags
* 8868a22  HTML and JavaScript formatting
* 1dad8e0  Shebang, header
* e870bcc  Rename main gui class
* a3ad762  Folium dependencies no longer needed as functionality of Leaflet is expanded through custom JS.
* cb9471a  Commenting
* ead061d  Group event handler functions
* 338de46  Remove json data
* 86a2a53  folium_gui.py -> gui.py
* 7353bbe  It's alive
* 4ac07ec  Remove polyline drawing options
* 4580656  Remove circle and circlemarker drawing options
* 1f003d2  Getting lat lon produces errors for points, circles
* 233b751  Black formatting
* fc4ebca  Hacky method for getting GeoJSON data from drawn shapes in folium
* 6663652  Add JS functions for downloading json, and changing html document title to GeoJSON
* f953854  WIP: GUI layout
* d4820d7  low res countries json
* a3ff911  Test folium GUI layout
* 7310d78  WIP: GUI layout
* d846036  WIP: GUI layout
* d404ac2  comma
* ee3ffcd  Matching => matching
* 25b38c3  Raster => raster
* 4d76e18  ...ing header for consistency
* bb6fdda  Typos
* 8f8ec6a  Update usage examples - #16
* 6625dd9  Add TODOs
* d0e4995  Fix calc_xy_at_lat_noscaling
* fde486f  Simplify __package__ evaluation
* deabc22  Class names; Remove ProjPicker from tool names (already under the ProjPicker toolbox)
* 8cda846  Namedtuple name
* a951f86  text update
* 1193ce5  sqlite => SQLite
* d05718b  Add License
* a05777c  Test update
* 8c81433  Add Sponsor header
* 02012a8  Add works_want.png
* 105a284  Restructure docs
* 2545022  Add a missing hash
* 051a8b6  RTD theme below Press
* 88a7cf5  Does it work?
* 449da85  Go back to the default theme until we figure out the press theme issue
* 73aae73  does it work?
* 350530b  does it work?
* 9346059  does it work?
* 5de9c93  Trying to go back to press
* d22d060  Test external links in the press theme
* 771d575  Remove test section
* ea63a15  test
* 3344e57  Close #7
* 1a7a13f  Change theme to sphinx_rtd_docs theme
* d054862  Test if change to .rst file will trigger changes
* 53a1d48  remove press theme
* a03e122  RTD still using press theme?
* ad53b29  Revert to default theme to test toctree external link
* 80a8175  install from master
* 8c8e05b  Add version tag
* 42e94e7  Try with new relase on fork
* abe3417  Test the removing sphinx-argparse all together
* bc80ed7  Try with .git at end
* c594242  Remove #sphinx-argparse
* 83e3446  Test new sphinx-argparse
* 39df408  GRASS addon is now built
* dc1f9df  GRASS over ArcGIS Pro of course!
* 73e0fb9  external links in the sidebar do not work; sphinx bug?
* b30ea91  ArcGIS Pro Toolbox is good enough now
* f3bc894  Merge branch 'main' of github.com:HuidaeCho/projpicker into main
* b64a35a  message() has only two arguments, omit end=
* 187f2c6  Blank line
* bdc38ab  Remove an unused variable
* 8d273f1  Forgot word
* dee3012  Update readme to reflect documentation
* 8975868  Comment
* 8ad6983  Update install scipt for pyproj
* 9ef2d19  Make bootstrap pytproj a submodule for import
* 3b45579  Add match to toolbox tree, add local path for pyproj
* fdc7995  Minor fixes
* 9366664  Match function
* c84ae0f  two blank lines
* 1e2110e  two blank lines
* 90a8bd0  file mode bits
* 93158ab  Add a limited version of pyproj.Transformer.from_crs for coordinate matching
* 5a0a2e9  Add list of tools to header, close #13
* 11bf748  feature -> raster for variables
* 6c5a7a7  Add reproject raster
* 1295a16  Slight restructure to spatial object error handling
* a9fa124  Add reproject feature class
* 675d3a2  Add guess raster projection

## v0.1.5.post7
Mon Jun 14 17:52:52 2021 -0400

* 31e4d76  (tag: refs/tags/v0.1.5.post7) 0.1.5.post7
* f019e93  Fix hidden buttons (default widget heights can push them outside the window)
* 3440bab  submitted => available
* eab7d6e  Link to g.projpicker
* 0fee4cd  Remove tabs
* 1396f51  Download all images from github; Use figure:: only; Add matching coordinates examples
* ed2c377  Add more info
* 2ba1c3c  Consistent order of query_all*
* fc71e61  leave pyproj 3.1.0 reference only for the packaged projpicker.db
* 2a92ac1  pyproj is not a standard module
* 6734400  comma
* 92ebb99  delete a sentence about match
* f4c37dc  pyproj required for match
* 21daa75  pyproj required for match
* e7d9cef  typo

## v0.1.5.post6
Mon Jun 14 02:23:31 2021 -0400

* 9b3e8ea  (tag: refs/tags/v0.1.5.post6) 0.1.5.post6
* 73e5330  Split stack exception
* 2e93b2d  Document match, match_tol=, match_max=
* 8a14927  Add match operator
* 1408e51  comments
* 75a6b61  Handle a single BBox instance
* ae2e1d4  Introduce g.projpicker

## v0.1.5.post5
Sun Jun 13 15:27:02 2021 -0400

* 1393a01  (tag: refs/tags/v0.1.5.post5) 0.1.5.post5
* e4e84fe  Add support for SRID printing
* e6b7714  If we want to use names, no fixed-width font
* ee1b345  curl name: curl, wget name: Wget

## v0.1.5.post4
Sat Jun 12 15:58:10 2021 -0400

* 0e22ee2  (tag: refs/tags/v0.1.5.post4) 0.1.5.post4
* 3d598e7  Fix an example
* 261db3e  Some CRSs have no bottom, top, left, or right
* 27a5f08  Reorder sections
* a2f30fc  Headers

## v0.1.5.post3
Sat Jun 12 14:08:40 2021 -0400

* f5f696f  (tag: refs/tags/v0.1.5.post3) v0.1.5.post3
* c880af5  Fix selection on filtering
* 5aa165d  Clear selection on filtering because indices change
* 3f5c182  Fix proj_table and unit filters
* e3ed04f  Add single option; Add horizontal scroll bars
* 233628b  Add single option; Add horizontal scroll bars

## v0.1.5.post2
Sat Jun 12 11:19:27 2021 -0400

* 2958709  (tag: refs/tags/v0.1.5.post2) Support no output from projpicker()
* b7b7210  Return queries results from projpicker()
* 7578c89  Case consistency; Out => Output
* 733c377  Lowercase section names in the middle of sentences
* 323307a  restructure query syntax
* d0663d6  Treat ProjPicker as a proper noun without a definite article
* 5116e5d  blank lines
* dcd661d  Minor clean up including typos
* f1f1d8a  ArcGIS toolbox documentation
* 81aad43  OK, let's treat RST files as source code and put one sentence per line for better version control
* ce22b8d  python -> Python
* 8984ff3  Single bullet does not look good to me
* 83f3905  WIP: Toolbox documentation
* 5b25b6b  no bullet
* 32562af  image to figure
* 03f82ae  TODO
* 79ea442  No need to repeat bbox
* fe4387f  Fix query_mixed_geoms usage
* e2c37a6  Revert 45f4835 (check comment)
* 72ee9bb  minor refactoring to check_unit()
* 55abd16  Fix Clarke's unit names; Single-liner for sel_crs; Drop _crs and capitalize CRS_Type
* 3ef6c24  Add unit selector for Guess Projection
* 4f805a4  Add default, docs
* 45f4835  Units for query_mixed_geoms
* f9d68f4  Fix unit check
* f6398fe  Add unit selector to 'Create Feature Class'
* 367fbb3  Use proper ProjPicker when not referring to the files
* 759853f  just coordinate system examples yet
* a11fa58  Reorder sections
* 64ada28  period to colon
* b19faed  Try to sort units by length
* c7a3fa4  SI units first
* 1ab429d  Sort units
* 2535db5  Add supported units
* 4b7d532  blank space above code blocks
* 913eb3d  Add examples for geometry types
* eef19db  Explain individual geometry types
* c65692f  off => of
* 3293731  Move general statements

## v0.1.5.post1
Fri Jun 11 14:50:16 2021 -0400

* 84abbed  (tag: refs/tags/v0.1.5.post1) Fix a minor bug; Sort test results
* 18d708d  Document unit=
* 5eb6ef1  Add unit= syntax
* e0794af  Support sqlite output format
* 80ed24e  Better wording?
* 68bae3c  Add postfix examples
* 84bcb21  Implement postfix logical operations (and, or, xor, not) for advanced spatial filtering
* 73529d8  rtree-oop is not under active development
* d96e5e5  Read release from VERSION
* a51717d  space
* cad7d4a  Fix sort; Add xy parsing test
* 83bcff2  Remove duplicate documentation from README.md
* 4c49171  point formats
* aa17c97  plural
* 09f015b  point formats
* cf6b6d8  coordinate systems
* a86d011  coordinate systems
* df10dce  Toolbox => toolbox
* dcbb42e  typo
* d58ec0c  Dedicate a section for ArcGIS Pro Toolbox
* 762776e  Dedicate a section for ArcGIS Pro Toolbox
* 8c7bbf9  Add GUI
* eedab43  webhook test
* 26bb0c2  lower-level header for indices
* 0b85ea2  Documentation reorganized
* 252d35a  single liner for sel_crs
* 819687a  Add link to win batch script
* 946ec3c  Tool to guess and assign projection for missing featureclasses/shapefiles
* 71eca07  Rename tool
* 7824a87  cd to chosen folder, fixed path issues
* 3f96b80  Windows style paths
* edf58c0  header
* 36352ed  Add comments
* b5ecc4d  Windows batch script for ArcGIS toolbox install
* 7ec5347  Explain the single argument
* 0db5d02  single selection mode for gui.select_bbox
* e944011  single selection mode for gui.select_bbox

## v0.1.5
Tue Jun 8 09:57:17 2021 -0400

* 4e2ea19  (tag: refs/tags/v0.1.5) 0.1.5 for GUI
* 05e5407  Fix sort and duplicated BBoxes for "or"
* 0b96ae8  Lowercase all; Fix double filtering
* 144ff6a  Minor update to package.sh
* 04ea6c5  Add user-friendly CRS info format
* 90dff78  Do not reset All
* b47ff26  Update README.md
* 3dd0295  GUI
* d14baf9  Moved most of the GUI code to the core
* 81853a7  Support easy install
* bbf425f  chmod gui.py
* 22165e9  Implement a tkinter GUI for CRS selection
* 1996ea7  Implement a tkinter GUI for CRS selection
* c80514b  Comments and shebangs
* 06a9b04  unsorted query_all
* 58dea80  sorted by area comments; TODO: OR will violate this rule

## v0.1.4.post2
Mon Jun 7 02:39:42 2021 -0400

* cb26c71  (tag: refs/tags/v0.1.4.post2) v0.1.4.post2
* 47e27d0  GitHub
* 857ea7a  Add dd:mm:ss formats
* de01694  Make it clear that it is a Python module from the beginning
* f77ace7  Now all dist files are in one directory
* a36011b  Not a single script anymore
* 3ba11a4  Fix and sync setup.py
* 83aab1b  Separator to pipe
* 9e052a5  Separator to pipe
* b3eca64  Forced true to keep moving
* 5dd23af  Use pipe as the default separator because some CRS names contain commas
* 36a3c8e  Two more colon examples
* c4b4dc7  Two more colon examples
* 813f9b9  Support dd:mm:ss coordinate format
* 19051f2  Support DD:MM:SS format
* 9e80e65  Remove colons
* 179f868  Use sentence case consistently
* 085c035  Remove collections import (used only in common.py)
* 87b5de4  Add IESA and UNG links
* 2e25433  polygon => poly; pip => pip3 for consistency
* 56aab8e  Add setup.py to root for easier installation from source (see installation docs)
* 3ada956  Add installation instructions
* 888b15b  Add link to missing proj example
* c40b61b  Add missing proj example
* e13fd49  Add missing proj example
* 320a024  Further api documentaion
* 5da4217  Add database documentation
* 3818911  Filtering examples
* b598dea  Add usage examples
* 069091b  latlon/xy -> coor_*
* 653674a  Update documentation for new structure
* 51d7d7c  Add link to github in top right corner
* 9bd9653  Update documentation for new structure
* 2af8003  Fix path for new structure
* cd25b22  Add missing CRS tests
* 96485b0  Rename latlon/xy => coor_latlon/xy to avoid potential conflicts and sorting
* 1d2d571  Restore coor system after mixed geom functions
* 204555d  Update projpicker folder
* 6458e31  Add more info about the finding output

## v0.1.4.post1
Fri Jun 4 20:08:09 2021 -0400

* 29454a9  (tag: refs/tags/v0.1.4.post1) Restructure the root and add missing files to the package
* 058cb29  Remove -g option

## v0.1.4
Fri Jun 4 19:49:21 2021 -0400

* a9049be  (tag: refs/tags/v0.1.4) Add pyproj as a requirement for recreating projpicker.db
* a21b007  Verion 0.1.4
* c71175e  Typo
* 7fb0280  Update README.md
* 198f097  Update README.md
* da01529  Update README.md
* 6b8139e  Add examples for missing spatial reference
* 1d436a2  Finding missing projection information
* 9110d3f  Delete an automatically generated file
* b406b6e  Add new py files
* ec55279  Move the experimental version to the root
* 3e27749  Add VERSION
* 97d606c  add __init__.py to experimental
* 89480f0  Make __main__ work with relative imports
* b3bef38  Import BBox
* 4db19af  Relative imports
* 3edc25e  Update test outfiles
* 93fd29b  Add experimental projpicker.db
* 17dfaf0  min/max x is largest along the equator
* c61f139  EXPERIMENTAL mixed latlong + xy
* 8d0ed80  Accept parseable geometries in more query functions
* f641514  Use BBox attributes
* d2e2ac7  Let's keep the old help for query-mode
* 59d015e  Query mode help
* 0fd82a2  indentation
* c048437  Reorder args for projpicker
* c881f92  Use bbox_columns for output formats
* 721fd6a  Add area to arcgispro list
* 7261c38  Add a missing newline
* 7b61a9f  Remove unused parameter; Use query_bbox
* a415fc5  WIP: Updates to interface, not quite the right layout
* 373a4f6  Add filtering tests
* e9e0ea0  Add filtering tests
* 2f16b0a  Updates to interface
* 031ec6d  Assign instead of append to sys.argv. More portable
* f2eaa5d  only add to sys.argv only if not currently in sys path
* 1f2ce83  WIP: Update for API changes, add filter methods *Dirty code*
* 960d1e1  Update README.md
* 607ab24  Do not rely on len() for AND
* c013566  Fix opts printing
* 927b0a2  Fix append
* bd47d5d  Improve run.sh
* 0daf602  Improve run.sh
* de2aeab  Fix a call to calc_area()
* 7c1b6bd  Rename gui to guis to be consistent with other plural directories
* 855e3c6  Update ArcGIS Pro README
* d07fda2  Add collections to README.md and resort modules (logical order)
* dea6428  Remove "import pprint"
* c423a8a  Shell examples for filtering
* 11c5203  Merge branch 'main' of github.com:HuidaeCho/projpicker into main
* 2a85ec4  Add filtering examples
* 6602496  Merge pull request #3 from HuidaeCho/esri

## v0.1.4.dev4
Wed Jun 2 20:26:26 2021 -0400

* 3205bdf  (tag: refs/tags/v0.1.4.dev4) Remove usage from README.md (annoying to update it frequently); Bump up the version
* 8f64cc6  Use BBox namedtuple instead of regular tuples; Change lat,lon to point and s,n,w,e to bbox; Add test scripts
* beee950  Spelling, GUI win title
* da79066  ESRI GUI Readme
* 53ffb84  ArcGIS Pro Toolbox for querying crs
* 22a5762  docstring for ith

## v0.1.4.dev3
Wed Jun 2 10:57:18 2021 -0400

* 4d51b01  (tag: refs/tags/v0.1.4.dev3) v0.1.4.dev3
* b4eab84  80 columns
* b61e331  degree unit name
* ddc04ed  Update test_pyproj.py to the current dev version
* d804013  Try to normalize unit names
* 7d9188e  Do not select unused columns
* 0d62b0f  Add unit of measure
* c979c3f  Add README.md for data
* 9491b64  Add proj.db from pyproj 3.1.0
* fd52579  Add back west_lon = east_lon for the sake of completeness and improve the test script
* cea3c03  Align test output
* 270aa80  proj.db from pyproj 3.1.0
* bc02425  Add test_pyproj.*

## v0.1.4.dev2
Tue Jun 1 23:29:20 2021 -0400

* f34b3de  (tag: refs/tags/v0.1.4.dev2) v0.1.4dev2
* c82a630  No extents whose west_lon = east_lon; Handle point bboxes
* 0e8a58c  WIP: Not complete.
* c237774  bbox entry => bbox row
* ec09360  Update usage in README.md
* 9fe60f2  Correct help for --input
* 8fe9aa0  More pip3 install examples
* b78c989  Move the screenshot below introduction
* f823c43  PyPI badge first
* f4dd124  Adda PyPI badge
* 0db8f38  Add the link to documentation in README.md
* 02ac4da  argument names on a separate line and indent once, not to = to save horizontal space
* e403c91  Remove an extra dot
* 4c4fc40  Indent to =
* 559f47e  Fix #2 for for missed CLI function returns
* 952a959  Fix #2 for for missed CLI description and positional arguments
* d740c97  Fix #2 for functions documentation
* e61bce7  Fix CLI api autodoc boldface
* 5ac35be  Autodoc functions
* edebdb1  Remove unused sphinx extentsion
* 2506cb0  Merge branch 'main' of github.com:HuidaeCho/projpicker
* 1c8acb0  Remove header
* 120aff1  Add Raises sections
* 9cadc45  Use the Google style docstring for Sphinx
* ad930b3  Get rid of WARNING: html_static_path entry '_static' does not exist
* 9809f60  Add module links
* ef762d8  Add the rtree link
* e5dde81  header depths
* 5e71bf9  Add more information about the rtree-oop branch
* 230f6dc  Remove a duplicated link
* 644af56  Add links to the GitHub repo and original GRASS feature request
* 44d03b0  Docs tag
* 65543c7  Add sphinx-argparse to requirements
* ed09fd3  WIP: Automate documentation
* e57e625  Merge branch 'main' of github.com:HuidaeCho/projpicker
* 19c54fc  Move parsing to seperate function for autodocumentation with sphinx-argparse
* f48b633  Help message for format
* 049bb3f  semicolon
* 5291e31  Update usage
* 7a98311  Merge branch 'main' of github.com:HuidaeCho/projpicker into main
* 972fe9a  Sort plain, json, pretty; Remove a programmer mistake exception (should not happen)
* c5d0d2f  Add TODOs for doc and gui
* 3c74e0f  Add doc folder
* 08a9a20  Reorder TODO items
* 662bd71  Add GUI folders

## v0.1.4.dev1
Mon May 31 13:24:55 2021 -0400

* 28b52a9  (tag: refs/tags/v0.1.4.dev1) docstrings updated
* 4545f53  a|b|rc|.dv|.post towards/away from the release
* 8d208e5  Fix example coordinates
* 355e847  Support for odms'' for DMS symbols
* 0f676aa  Merge branch 'main' of github.com:HuidaeCho/projpicker into main
* a6d0cc1  Comment and minor usage change
* 3d9b606  Update README.md
* 813f666  8 spaces to tabs in shell examples
* da8498d  better example
* 326807d  one more example
* 9940a5e  Examples
* e0e6be0  More supported input coordinate formats
* d528c46  Fix UNG and Atlanta coordinates
* 677fa2a  version 0.1.4.dev1
* d794083  Update README.md
* 7215c85  Update README.md
* 8004d3f  Update README.md
* c9e6821  Help message
* 44198ca  Help messages
* d5807e1  Allow whitespaces before a comma
* 28d43ad  whitespaces in README.md
* 06e9444  Comments for tidy_lines()
* 896aee0  Comments for tidy_lines()
* e52bc98  "a" comment
* 5f9b57b  neither nor
* a1e0023  Update usage in README.md
* 46645d8  More flexible input format; Add --print-geometries for input validation
* 2eaaf29  s,n,w,e => south,north,west,east in help
* 82a8db5  Current (four numbers) version already violates the versioning scheme
* 03259c8  Update README.md
* 0b764ab  clarify that proj.db is only required for optionally recreating projpicker.db
* 4af7bb4  clarify that proj.db is only required for optionally recreating projpicker.db
* 908b551  Version number in README.md

## v0.1.3.1.post1
Sun May 30 13:58:42 2021 -0400

* 281afb4  (tag: refs/tags/v0.1.3.1.post1) version 0.1.3.1.post1
* f0f81a0  Update versioning in README.md following PEP 440
* 0110d19  version 0.1.3.post2
* ab50dd2  version 0.1.4-1
* 163c578  ver => version
* be7da30  Make version and default paths dynamic
* 2ff4825  Explain when to use the build number

## v0.1.3.1
Sat May 29 21:32:42 2021 -0400

* c4a1f22  (tag: refs/tags/v0.1.3.1) Versioning
* eaf3930  Versioning
* 9cda4a7  Build number rule
* ff26d7b  execute permission for deploy.sh
* 47ac7ea  projPicker => projpicker
* 26f02b1  projPicker => projpicker
* f1bcb28  ignore deploy/
* bbcd4a7  projpicker.py => projpicker in README.md
* d8713ad  Version information
* c66c691  Update README.md

## v0.1.3
Sat May 29 17:23:02 2021 -0400

* 49d5153  (tag: refs/tags/v0.1.3) Add the pypi URL to README.md
* fc38fb6  Add Installation

## v0.1.2
Sat May 29 16:47:42 2021 -0400

* 5dbdfdf  (tag: refs/tags/v0.1.2) Add github URL to the source
* c3dba05  comma => and in copyright
* a55e674  80 cols
* 7cda00e  Pick up the default projpicker.db from the executable path
* ae9e35b  intersect => completely contain
* ad649e3  80 columns and updated usage in README.md
* 48bd517  Mutually exclusive --overwrite and --append; More docstring for the main function
* b9ffdb8  Add a TODO for agency and product information
* 114aeb8  Add an idea about ArcGIS Pro toolbox
* 9a6840c  Reformat copyright block to the GNU template
* a2b5cab  No comma between copyright year and authors following GNU practices
* 6b5bdf1  80 columns in README.md examples
* 1626918  80 columns
* e7c849e  Raise an exception on not being able to overwrite projpicker.db
* b0a853f  Make all parse_*() functions return input if their output is give as is
* 624d323  Fix and improve parse_polys()
* b00c8e7  Mention rtree-oop branch
* 4357a9b  reorganize single-file version
* b0ddcf2  Add missing parse_points()
* 7d8854c  80 cols
* 3c8fc2b  arrayify_bbox => listify_bbox
* c36001d  Fix bboxes/polys parsing
* 03ff492  Fix append
* 3c647d2  Better stdin reading
* 4c39e96  Fix areas for w>e
* 57fb9e3  Add docstrings with minor refactoring
* f60c2cc  compact empty lines
* 80bda0a  bboxes ignoring geometries? clarify it
* ca9bda1  help
* c42c80b  Do not prompt after creation ni a tty
* c472aa9  sort on db creation; query all mode
* b5e1c55  Move requirements
* bec5e9e  Update README.md
* 19e0a8d  Requirements
* e7ec907  Remove unused scripts
* 7725b94  restructure repo
* e88d7fe  Update README.md
* ede36e1  Add URL to help
* 170ac21  Fix parsing
* 8307e71  Update usage
* 8f25d21  sort_dicts for pprint for Python 3.8+
* c336375  Support for pretty print format
* d193dd9  points in a poly are separated by a space
* 89ad756  description
* d41aaf8  description
* 83fd3ff  Add usage
* 8f33e61  Add usage
* 41f20af  Support for arrays of polys in addition to flat polys with separators
* 5bd99f7  README
* 16981bb  Handle special cases where west_lon == east_lon or (west_lon == -180 and east_lon == 180); in other words, entire longitude space
* 9d0a37a  Handle special cases where west_lon == east_lon or (west_lon == -180 and east_lon == 180); in other words, entire longitude space
* bff2fee  Help messages
* 3528b6b  input from stdin if no geometries are given in command line
* 1f90717  Comments
* 5b7c010  Move parsing functions
* 010b68b  Try to handle antimeridian-cross geometries
* 8d43dda  Add single queries for poly and bbox
* 9e13cc9  query_points_bbox replaced by query_polys
* bb44fc7  Fix a message
* 61c46a0  Support for poly(line|gon) and bbox
* cd8d271  Properly handle reversed west_lon and east_lon (crossing antimeridian)
* dfdb724  Remove a debug message
* 8aa3578  minor refactoring
* 9264b6f  Lowercase help to be consistent with the default help
* 43a4b31  Implement query mode (and, or) for multiple points; TODO: poly(line|gon)
* 455a032  more info about polygon intersection
* 29244d3  Resolve conflicts
* 221f704  Sync
* a0a5e6c  Merge branch 'main' of github.com:HuidaeCho/projpicker into main
* 31e189a  Sort by bbox area (smallest first)
* a45806d  Update README.md
* 69833c9  Typos
* 735a3e0  Merge branch 'main' of github.com:HuidaeCho/projpicker into main
* bd8fe18  some comments
* a551081  Update README.md
* c36c1e1  Update README.md
* 01a68a5  TODO
* df57d42  Use crs_view and JOIN
* 1005d6c  Since May 13?
* 82946b3  markdown syntax
* f4085e6  Add single-file script
* 13a1229  WIP: unit tests
* 374a68a  Rename build_data.sh to build_rtree_data.sh
* c5e868f  python3
* 800ac39  Use set -e
* 5f27633  Let's keep the original build script names without _
* 7c815af  Owen Smith as 1st author; Add IESA, UNG affiliation
* 2223615  Update for new add method
* eb1a8d6  Add execution method
* 7dfd2d8  ProjPickCon -> ProjPicker
* 252ff80  Update connections
* 3c2e053  Proj connection class
* 2222f03  WIP: Connection wrapper
* 56666a0  Preliminary requirements
* 1499348  remove print statement
* b61bd9e  Add 'codes' table to provide ids for all potential PROJ authority codes. This is done so as to account for CRS codes from different authorities being either integers or a mix of both characters and integers. RTREE can only accept integers.
* 0f82dc2  Shell script to generate database and RTree index
* eed7de4  ignore data folder
* 83ca6cf  Add '_' to denote files which are not part of core apii
* 6824e39  utils -> core
* ef2683c  utils -> core
* 42264aa  Remove argparse
* 4025d32  Remove argparse
* f4eb1b2  Update constant file paths to ensure their constant location for both creation and reading
* 360d851  Add __all__ for * imports
* 5c270c0  Update Python submodule imports to import the neccesary front facing functions under the main namespace.
* 9a22bff  Remove spatialite module
* c6e8ab0  Remove densified bbox/spatialite operations
* b1e5b27  Rename back to projpicker
* 803f938  Add headers
* 5cf3972  Fix utils import
* c785d0f  Readd densified BBOX function import
* 74e2486  Overwrite db if exists
* bf67f9c  Rename generate_db and gen_rtree
* 1f8cb90  remove print statement, re import
* d078b87  remove print statement, re import
* 738ed5d  Fix utils import
* 71b793b  Create utils subpackage, rename projpicker.py to ppicker.py to avoid potential name space issues.
* 015364c  Fix connection parameter
* c74b2c0  WIP: Main API
* 9d9c127  Function for intersection
* 5a4ebd0  Import from const
* ebb3b70  move constants to file. Need to make functions to allow constants to detect paths dynamically
* d73a424  intersect.py -> projpicker.py
* 137ae7b  Float formatting
* 4e3f244  Auto increase key
* f140866  WIP
* 24bc791  Script to generate an RTree index on file
* 03d1dd0  Change densified functionality
* c674e05  Switch order of bbox, add get_bounds function
* 8e37c17  Switch order of bbox
* 740133e  Move denifying operations to geom.py
* 9dfaba9  spatial_operations.py -> geom.py
* e01b4d0  line
* da29e6f  Accept multiple tables as positional arguments, black formating
* 981e9ff  Move bounding box operations to spatial_operations.py
* ea494ef  Only create tables if they do not exists
* 641760f  Take one CRS only
* dd769a7  Change n to -n N
* b3fc97c  Consistent newlines
* 51c84e6  Close bbox; Add -p for gnuplotting
* e42c94c  newline
* c00689c  Reduce redundancy
* 00992fd  latlong to lat/long
* d6dfaa6  Add bbox script
* 7db42cc  Generate projbbox, densbbox
* 7e79cd9  Edit bbox
* 769aea4  Fix missing return
* 4300489  Projpicker connection
* 525f6fe  Geometry types for Spatialite creation
* 2c0b7d2  proj_operations.py -> db_operations.py
* a9ed561  Functions to create densified bbox
* 774da10  Remove deprecated CRS's from db. They have no bbox
* 2e0ee69  Correct bbox x, y order
* 4e63050  Remove linting for now
* 7190501  Update bbox polygon output
* 801de8b  Update bbox polygon output
* c3a770d  Black formatting
* 32fb8c4  Set up superlinter
* ccbaab6  crs_usage function to generate full usage dictionary for a crs table
* 66e298e  New line
* 56520fa  Move general proj.db operation functions into own file to increase extensibility
* e99aad1  Reformat SQL statements
* aa11b88  Make sqlite cursor a local variable
* 1a7c4ad  Update structure
* 543fc01  Create .gitignore
* d5e3af3  Correct spelling
* b21e1fa  Commenting
* 17282ae  python -> python3
* cba2bae  WIP: Get usage dictonary
* b4995ed  WIP: Flexible CLI script
* ba15122  Remove unused imports
* ea7c300  Remove print statement
* 7d341c5  WIP: BBOX creation
* 22918fb  Python script to generate intial projpicker db
* fb28f2e  Comment
* a5fae7c  Remove testing statements
* eba59c3  Black
* 4699167  Connection and validation functions
* e40dcb0  Update README.md
* 1ba84ba  Update README.md
* 2b0cbda  Update README.md
* f996aa5  Update README.md
* 9abc727  Update README.md
* 23f1f26  Update README.md
* f7b7bec  Update README.md
* ca9e7f8  Update README.md
* 36ac49e  Update README.md
* f46fb09  Update README.md
* a944354  Move Discussions to the Wiki
* 668c7e7  Update README.md
* b86fb1a  Update README.md
* a1dd00c  Update README.md
* 6243be8  Update README.md
* 92a82cf  Update README.md
* d15e673  Update README.md
* f401095  Update README.md
* 52715f1  Update README.md
* 2ac429c  Rename LICENSE to COPYING
* 1036cf4  Initial commit
# pestle_tools
  SigTools in Python
  
  pestle is a custom Python library meant to be used by the Connectivity Map (CMap) team to build tools 
  that can be run from the command line. Within is the infrastructure to generate templates for new Sigtools, 
  find and edit those tools, and run them from the command line.
  
  Author: Anup Jonchhe
  
  Date Created: May 11, 2020

## Usage

  Pestle can be used in two modes, either installed into the virtual environment, or run from the repository.
  Because the repo becomes dynamic with the addition of new tools to be editted and potentially committed to the repo, 
  the latter option is heavily recommended. 
  
  **Setup**  
  within the pestle_tools directory is a script `run_pestle` that is a shortcut from the traditional 
  
  `pipenv run python -m pestle [args]` syntax
  
  From within the pesltle_tools dir:
 
  `cd /path/to/pestle_tools`  
  `./run_pestle help`
  
  or by adding `export PATH="$PATH:/path/to/pestle_tools"` to ~/.bash_rc  
  `run_pestle help` also works, although this will error in other directories so it is still fragile.

  **setup.py**
  
  The tool can also be installed into a conda environment or virtualenv. 

  run `python setup.py install`
  
  However, while running tools in this mode is easier, creating tools places them within the venv folder.

  **Note**: in this mode, `pestle` can be run from the command line from anywhere and replaces `run_pestle` in 
  the following examples

## runtools

  `run_pestle runtool` is the interface running tools. Running that command without arguments shows a 
  help text for running tools. 

### Example tool: sig_subtract_tool

A **VERY** simple tool has been generated as an example of how the tools can be run. 

`run_pestle runtool sig_subtract_tool -h` prints tool info

`run_pestle runtool sig_subtract_tool --minued 100 --subtrahend 50` will show a basic example of the tool running

## toolify

`run_pestle toolify` is the interface for creating new tools and finding tools to edit.

Running `run_pestle toolify list_files` will show a list of tools and will display the filepaths of the one selected to edit
or examine.

`run_pestle toolify new` will run through a cookiecutter setup for making a new tool. This involves cookiecutter, 
post-gen and pre-gen hooks. **Do not adjust the pestlepath argument** this was a workaround how the 
hooks are unable to import from the package


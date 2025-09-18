hey, welcome to the agent guidelines for neuromancer! this is our little guide to keep things consistent and fun while we're coding and building stuff together. we're all about that collaborative vibe, so let's make programming and documenting a blast.

## build, lint, and test commands

different languages have their own ways of doing things, but here's the usual stuff we do to keep our code clean and working:

- **python:** set up a virtual environment with `python -m venv venv`, activate it with `source venv/bin/activate`, install deps via `pip install -r requirements.txt`, check style with `ruff check .`, and run tests with `pytest`
- **javascript/typescript:** grab dependencies with `npm install`, lint with `npm run lint`, test with `npm test`
- **shell scripts:** just run 'em with `bash script_name.sh`

for running a single test, it's like:
- **python (pytest):** `pytest path/to/test_file.py::test_function_name`
- **javascript (jest):** `npm test -- -t 'test name'` (or whatever your setup uses)

## code style guidelines

let's keep our code looking neat and readable. here's how we roll:

- **imports:** group 'em logically - standard library first, then third-party, then local stuff. no wildcard imports like `from module import *`, that's just messy.
- **formatting:** follow the style guides, like pep 8 for python or prettier for js/ts. use spaces over tabs, and add whitespace to make things easier to read.
- **types:** use type hints where it makes sense - python annotations or typescript types help everyone understand what's going on.
- **naming:** variables and functions in camelcase for js/ts, snakecase for python. classes in pascalcase everywhere. constants in screaming_snake_case. keep names descriptive but not crazy long.
- **error handling:** use try-except in python or try-catch in js/ts. give clear error messages, and know the difference between recoverable oopsies and total fails.
- **modularity:** write small, focused functions and modules. high cohesion, low coupling - keep things simple and connected.
- **comments:** explain the why, not just the what. keep 'em short and up to date.

## cursor and copilot rules

if there's a `.cursor/rules/` or `.github/copilot-instructions.md` file, check those out first. they might have specific tweaks for how we behave in different tools.

## project structure philosophy

check out `0_admin/00_index/00.01_structure_guide.md` for the full scoop on our folder setup and the johnny decimal system. it's our way of keeping things organized without going overboard.

## neuromancer design philosophy

neuromancer is this cool ai-augmented system for managing knowledge and building stuff across different ai platforms. we're all about turning info into insights, learning as we go, and keeping things consistent no matter which tool we're using.

### purpose
- **knowledge synthesis:** turn raw data into useful stuff
- **adaptive learning:** get better with every chat and project
- **cross-platform consistency:** act the same whether it's cursor, claude code, opencode, or whatever

### core behaviors
- **proactive structure:** use todo lists for big tasks, keep dev logs updated
- **context awareness:** always reference our project structure and docs
- **iterative development:** build step by step, test often, document everything
- **security first:** never mess with security or data integrity

### tasks and responsibilities
- **code development:** follow style guides, run lint and tests before commits
- **documentation:** update dev logs, keep agents.md fresh, write clear commit messages
- **knowledge management:** process inbox stuff, expand domains, execute projects
- **system maintenance:** update deps, watch for issues

### agent-specific adaptations
we keep the core philosophy but tweak for each platform:
- **cursor:** focus on editing code, use .cursor/rules if available
- **claude code:** lean into conversations, follow claude.md guidelines
- **opencode:** batch operations and tool workflows for efficiency

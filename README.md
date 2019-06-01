# Carrepsa
[![Build Status](https://travis-ci.com/pilino1234/DAT256.svg?token=XyHcbxehB8TtpGq4DuFW&branch=dev)](https://travis-ci.com/pilino1234/DAT256) [![codecov](https://codecov.io/gh/pilino1234/DAT256/branch/dev/graph/badge.svg?token=yX3pyaI7TF)](https://codecov.io/gh/pilino1234/DAT256)

## Getting Started
### Installing dependencies
The app is built using Python 3.7 (other versions have not been tested, so YMMV).
The app also requires some python libraries, such as [Kivy](https://github.com/kivy/kivy) as its frontend framework. Kivy, in turn, depends on Cython and PyGame, amongst others. The best and easiest way to install these is to use a [virtual environment](https://virtualenv.pypa.io/en/latest/).

1. Clone the repository and switch to the `app/` directory.
1. Run `virtualenv venv` to create a new virtual environment in the `venv/` directory
1. Activate the new virtual environment with `source venv/bin/activate`
1. Install the dependencies needed for the project: `pip install -r requirements.txt`.  
If you are running Windows, also install the requirements in `requirements-windows.txt` with the command `pip install -r requirements-windows.txt`.
1. If any of the requirements fail to install, make sure that you have the correct dependencies for that library. This varies a lot between different OSes and distributions.

### Running the app
Before running the app, a keyfile is needed so that the app can authenticate to the backend properly. Without it, the app will not start. Contact one of the authors to acquire one.

1. Activate the virtualenv (if it isn't already)
1. Once all the dependencies are installed successfully and the keyfile is in place, the app can be started by running `python3 main.py` in the `app/` directory. Make sure that you have activated the virtualenv created previously when doing this.

## Project Structure
The repository contains the following files and directories:

```
Repository root
├── .prospector  -- Configuration files for the Prospector tool
├── app  -- The project source code
│   ├── assets
│   ├── docs  -- Sphinx configuration files
│   ├── model  -- The model package
│   │   └── firebase  -- Firebase interface code as a subpackage
│   ├── presenter  -- The presenter package, and related subpackages
│   │   ├── auth
│   │   ├── screen
│   │   └── utils
│   ├── tests  -- The unit tests for the project
│   └── view  -- The views written in KVlang
│       ├── auth
│       ├── screens
│       └── utils
├── ci  -- Scripts for the CI pipeline
├── documents  -- Documentation of the team's process and reflections
│   ├── group-reflections  -- The weekly team reflections
│   ├── individual-reflections  -- The weekly individual reflections for each team member
│   │   ├── Elias
│   │   ├── Jacob
│   │   ├── Jimmy
│   │   ├── Kevin
│   │   ├── Martin
│   │   ├── Olle
│   │   └── Theodor
│   ├── presentation  -- Video files used during the product presentation
│   ├── gitinspector.log  -- Output from gitinspector
│   ├── Carrepsa Mockup.pdf  -- The mockup of the app's visuals
│   ├── Firestore specifikation.pdf  -- The specification for the backend datamodel
│   ├── Final Reflection.pdf -- The final reflection report
│   ├── Gruppkontrakt.pdf  -- The group contract
│   ├── KPI & DoD Specs.pdf  -- The KPIs and the team's Definition of Done
│   ├── Retrospective Sprint 1.pdf  -- Retrospective for sprint 1
│   ├── Retrospective Sprint 2.pdf  -- Retrospective for sprint 2
│   ├── Retrospective Sprint 3.pdf  -- Retrospective for sprint 3
│   ├── User Flows.pdf  -- Potential user flows used for testing and demonstration
│   ├── User Stories.pdf  -- The entire list of user stories
│   └── business-canvas-model.png  -- The business canvas
├── firebase  -- The Firebase backend code
│   └── functions
├── Several configuration files for different tools
├── .travis.yml  -- The Travis CI configuration
├── .mailmap  -- Who's who for the project contributors
└── keyfile-ci.json.env  -- Encrypted keyfile used by Travis to access the CI backend rather than the production backend.
```

## Where to find important files
### Code
`app/`: All application code is in this directory.

#### Unit tests
`app/tests`: All unit tests

### Reflections
`documents/group-reflections/`: Team reflections  
`documents/Final Reflection.pdf`: Final reflection report  
`documents/individual-reflections/`: Individual reflections

### Git Inspector (gitinspector)
`documents/gitinspector.log`: The output from running the command `gitinspector.py --grading --file-types=js,kv,py,sh,spec,yaml,yml`. Note the manual specification of several file types to make sure that all work is included (gitinspector does not automatically detect some, for example .kv files that are actual application code.

### Binaries
There are no binaries available for this project; the Python code can be run as-is. APK builds were planned and the infrastructure is in place. However, one of our dependencies' dependency does not cross-compile to ARM very easily, and we were not able pursue the development of a so-called [python-for-android](https://github.com/kivy/python-for-android) "recipe" for the `grpcio` library and its dependency on `c-ares` that would be required to solve the problems due to time constraints.


## Authors
Can be found in the .mailmap file in the repository root.

## Scrum
The team's use of Scrum is documented partly in the individual and weekly reflections, as well as the sprint retrospectives. The team also made use of a Slack App for handling the Daily Scrums via Slack.

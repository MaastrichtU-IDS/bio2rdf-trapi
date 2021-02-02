# Contributing

When contributing to this repository, please first discuss the change you wish to make via an [issue](https://github.com/MaastrichtU-IDS/bio2rdf-trapi/issues) if applicable.

If you are part of the [MaastrichtU-IDS organization on GitHub](https://github.com/MaastrichtU-IDS) you can directly create a branch in this repository. Otherwise you will need to first [fork this repository](https://github.com/MaastrichtU-IDS/bio2rdf-trapi/fork).

To contribute:

1. Clone the repository 📥

```bash
git clone https://github.com/MaastrichtU-IDS/bio2rdf-trapi.git
cd bio2rdf-trapi
```

2. Create a new branch from the `master` branch and add your changes to this branch 🕊️

```bash
git checkout -b my-branch
```

## Development process

Install from the source code, and update the package automatically when the files changes locally :arrows_counterclockwise:

```bash
pip3 install -r requirements.txt
```

> See the [main README](https://github.com/MaastrichtU-IDS/bio2rdf-trapi) for more details on the package installation.

### Start Bio2RDF API :rocket:

Start the **API in debug mode** on http://localhost:8808 with Flask (the API will be reloaded automatically at each change to the code)

```bash
python3 src/api.py debug
```

Or in **production** mode with Tornado:

```bash
python3 src/api.py
```

> By default the API will use the SPARQL endpoint of IDS Nanopublications server Virtuoso.

## Pull Request process

1. Ensure the API works before sending a pull request 🧪
2. Update the `README.md` with details of changes, this includes new environment variables, exposed ports, useful file locations and container parameters 📝
3. [Send a pull request](https://github.com/MaastrichtU-IDS/bio2rdf-trapi/compare) to the `master` branch, answer the questions in the pull request message 📤
4. Project contributors will review your change as soon as they can ✔️

## Versioning process

The versioning scheme for new releases on GitHub used is [SemVer](http://semver.org/) (Semantic Versioning).

Change version in `setup.py` before new release.

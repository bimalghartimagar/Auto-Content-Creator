#!/usr/bin/bash
pytest --cov -v --cov-report html --cov-report term
poetry export --without-hashes > requirements.txt
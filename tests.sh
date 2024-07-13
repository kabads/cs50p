#!/bin/bash

cd src/test_fuel
pytest --cov=.
cd ../..
cd src/test_plates
pytest --cov=.
cd ../..
cd src/test_twttr
pytest --cov=.
cd ../..
cd src/um
pytest --cov=.
cd ../..
cd src/working
pytest --cov=.
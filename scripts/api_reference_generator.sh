#!/bin/bash
# Fail on error
set -e

API_VERSION="201901"
# generate examples
python2 ./examples/api_reference_example_generator.py \
          --api-version ${API_VERSION} \
          --output-dir examples \
          --template examples/sample_template.py.template \
          --context examples/sample_context.yaml


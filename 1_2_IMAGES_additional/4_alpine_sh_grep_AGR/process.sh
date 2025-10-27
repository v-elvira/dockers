#!/bin/sh
echo "Running with $TEXT_TOOL on $1"

# Если TEXT_TOOL=grep, можно искать ERROR:
if [ -z "$TEXT_TOOL" ]; then
  echo "No TEXT_TOOL set, defaulting to grep"
  TEXT_TOOL="grep"

elif [ "$TEXT_TOOL" = "sed" ]; then

  $TEXT_TOOL "s/ERROR/NO_ERROR/" $1
  exit 0

fi

$TEXT_TOOL "ERROR" $1

#!/bin/bash
# Detect the platform (similar to $OSTYPE)
OS="`uname`"
case $OS in
  'Linux')
    OS='linux'
    ;;
  'WindowsNT')
    OS='windows'
    ;;
  'Darwin')
    OS='darwin'
    ;;
  *)
    echo "Unknown OS: $OS"
    exit 1
  ;;
esac


ARNOLD_VERSION=${REZ_BUILD_PROJECT_VERSION}

INSTALL_FILE="${REZ_BUILD_SOURCE_PATH}/../installers/Arnold-${ARNOLD_VERSION}-${OS}.tgz"

# extract archive content
tar -xf "${INSTALL_FILE}" -C "${REZ_BUILD_INSTALL_PATH}"

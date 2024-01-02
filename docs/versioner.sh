#!/bin/bash

# Get the current year and month
year=$(date +"%Y")
month=$(date +"%b")
month_int=$(date +"%m")

# Increase the Commit Depth in case of a Shallow Clone
git fetch --unshallow

# Count the number of commits made since the beginning of this month
commit_count=$(git --no-pager rev-list --count HEAD --since="${year}-${month_int}-01")
commit_count=$(printf "%03d" $commit_count)

# Construct the git tag
tag="${year}-${month}"

# Construct the version string
version_string="${year}-${month}-Patch-${commit_count}"
twine_version="${year}.${month_int}.${commit_count}"

# Get the commit SHA
commit_sha=$(git rev-parse HEAD)

# Get the machine name
machine_name=$(hostname)

# Format the TOML content and write to version.toml
cat <<EOF > ./version.toml
# Version Data
version = "$version_string"
twine_version = "$twine_version"
year = "$year"
month = "$month"
patch = "$commit_count"
commit = "$commit_sha"
machine_name = "$machine_name"
EOF

# Check if the current branch is 'main' and if running in a pipeline
if [ "$CI_COMMIT_REF_NAME" == "main" ]; then
    # Pull the latest tags
    git fetch --tags

    # Check if the tag already exists
    if ! git tag | grep -q "^$tag$"; then
       # Create a new tag
        git config user.email "priya@engineered.co.in"
        git config user.name "Priya"

        git tag -a "$tag" -m "Created on $(date +"%Y-%m-%d")"

        git remote add tag_origin "https://Twine:${CI_Twine}@gitlab.com/${CI_PROJECT_PATH}.git"

        # Push the tag
        git push tag_origin --tags

        # Create a new release
        RELEASE_NAME="Release $tag"
        RELEASE_NOTE="Release notes for version $tag"

        curl --request POST "https://gitlab.com/api/v4/projects/$CI_PROJECT_ID/releases" \
            --header "PRIVATE-TOKEN: $CI_Twine" \
            --form "name=$RELEASE_NAME" \
            --form "tag_name=$tag" \
            --form "description=$RELEASE_NOTE"

    fi
fi

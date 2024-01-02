# Get the current year and month
$year = Get-Date -Format "yyyy"
$month = Get-Date -Format "MMM"
$month_int = Get-Date -Format "MM"

# Increase the Commit Depth in case of a Shallow Clone
git fetch --unshallow

# Count the number of commits made since the beginning of this month
$commit_count = git --no-pager rev-list --count HEAD --since="$year-$month_int-01"
$commit_count = "{0:D3}" -f [int]$commit_count

# Construct the git tag
$tag = "${year}-${month}"

# Construct the version string
$version_string = "${year}-${month}-Patch-${commit_count}"
$twine_version = "${year}.${month_int}.${commit_count}"

# Get the commit SHA
$commit_sha = git rev-parse HEAD

# Format the TOML content
$versionTomlContent = @"
# Version Data
version = "$version_string"
twine_version = "$twine_version"
year = "$year"
month = "$month"
patch = "$commit_count"
commit = "$commit_sha"
machine_name = "$env:COMPUTERNAME"
"@

# Write to version.toml
Set-Content -Path '.\version.toml' -Value $versionTomlContent

# Check if the current branch is 'main' and if running in a pipeline
if ($env:CI_COMMIT_REF_NAME -eq 'main') {
    # Pull the latest tags
    git fetch --tags

    # Check if the tag already exists
    $tagExist = git tag -l $tag

    if(-not $tagExist) {
        # Create a new tag
        git config user.email "priya@engineered.co.in"
        git config user.name "Priya"

        git tag -a "$tag" -m "Created on $((Get-Date).ToString('yyyy-MM-dd'))"

        git remote add tag_origin "https://Twine:${CI_Twine}@gitlab.com/${CI_PROJECT_PATH}.git"

        # Push the tag
        git push tag_origin --tags

        # Create a new release

        $releaseName = "Release $tag"
        $releaseNote = "Release notes for version $tag"

        $headers = @{
            "PRIVATE-TOKEN" = "$CI_Twine"
        }

        $body = @{
            name        = $releaseName
            tag_name    = $tag
            description = $releaseNote
        }

        $response = Invoke-RestMethod -Method POST -Uri "https://gitlab.com/api/v4/projects/$env:CI_PROJECT_ID/releases" -Headers $headers -Body $body

        # Printing the response for logging or further handling
        $response

    }
}

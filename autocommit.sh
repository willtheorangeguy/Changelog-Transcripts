#!/bin/bash

# Define the current year to skip
CURRENT_YEAR=2026

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Function to print colored output
print_colored() {
    local message="$1"
    local color="$2"
    echo -e "${color}${message}${NC}"
}

# Function to execute git commands with output and error handling
run_git_command() {
    local args=("$@")
    print_colored "  → git ${args[*]}" "$CYAN"
    
    if ! git "${args[@]}" 2>&1; then
        print_colored "  ! Git command returned exit code $? - skipping this file type" "$YELLOW"
        return 1
    fi
    return 0
}

# Check if podcast folder argument is provided
if [ $# -eq 0 ]; then
    print_colored "ERROR: Podcast folder name required" "$RED"
    print_colored "Usage: $0 <PodcastFolder>" "$CYAN"
    exit 1
fi

PODCAST_FOLDER="$1"
PODCAST_PATH="$(pwd)/$PODCAST_FOLDER"

# Validate that the podcast folder exists
if [ ! -d "$PODCAST_PATH" ]; then
    print_colored "ERROR: Podcast folder '$PODCAST_FOLDER' not found at '$PODCAST_PATH'" "$RED"
    exit 1
fi

print_colored "\n========================================" "$GREEN"
print_colored "PODCAST TRANSCRIPT BATCH COMMIT SCRIPT" "$GREEN"
print_colored "========================================\n" "$GREEN"

print_colored "Podcast: $PODCAST_FOLDER" "$CYAN"
print_colored "Location: $PODCAST_PATH" "$CYAN"
print_colored "Current year (will skip): $CURRENT_YEAR\n" "$CYAN"

# Validate git repository
print_colored "Validating git repository..." "$CYAN"
if ! git status --porcelain >/dev/null 2>&1; then
    print_colored "ERROR: Not a valid git repository" "$RED"
    exit 1
fi
print_colored "✓ Repository is valid" "$GREEN"

# Get all year folders
print_colored "\nScanning year folders in '$PODCAST_FOLDER'..." "$CYAN"
year_folders=()
for folder in "$PODCAST_PATH"/*; do
    if [ -d "$folder" ]; then
        year=$(basename "$folder")
        # Check if folder name is a 4-digit year
        if [[ "$year" =~ ^[0-9]{4}$ ]]; then
            # Skip current year
            if [ "$year" != "$CURRENT_YEAR" ]; then
                year_folders+=("$year")
            fi
        fi
    fi
done

if [ ${#year_folders[@]} -eq 0 ]; then
    print_colored "No year folders found (excluding $CURRENT_YEAR)" "$YELLOW"
    print_colored "Exiting." "$YELLOW"
    exit 0
fi

# Sort the years
IFS=$'\n' sorted_years=($(sort <<<"${year_folders[*]}"))
unset IFS

print_colored "Found year folders: $(IFS=', '; echo "${sorted_years[*]}")\n" "$GREEN"

# Process each year folder
processed_count=0
skipped_count=0

for year in "${sorted_years[@]}"; do
    year_path="$PODCAST_PATH/$year"
    
    print_colored "\n-------------------------------------------" "$CYAN"
    print_colored "Processing year: $year" "$CYAN"
    print_colored "-------------------------------------------" "$CYAN"
    
    # Check if any matching files exist
    has_transcript=false
    has_summary=false
    has_corrected=false
    
    [ -n "$(find "$year_path" -maxdepth 1 -name '*_transcript.*' 2>/dev/null)" ] && has_transcript=true
    [ -n "$(find "$year_path" -maxdepth 1 -name '*_summary.*' 2>/dev/null)" ] && has_summary=true
    [ -n "$(find "$year_path" -maxdepth 1 -name '*_corrected.*' 2>/dev/null)" ] && has_corrected=true
    
    if [ "$has_transcript" = false ] && [ "$has_summary" = false ] && [ "$has_corrected" = false ]; then
        print_colored "  ⊘ No matching files found (*_transcript.*, *_summary.*, *_corrected.*)" "$YELLOW"
        ((skipped_count++))
        continue
    fi
    
    # Change to the year directory
    cd "$year_path" || exit 1
    
    year_has_changes=false
    
    # Step 1: Add and commit transcripts
    if [ "$has_transcript" = true ]; then
        print_colored "\n  [1/3] TRANSCRIPTS:" "$CYAN"
        if run_git_command add "*_transcript.*"; then
            # Check if there are actually changes to commit
            staged_changes=$(git diff --cached --name-only)
            if [ -n "$staged_changes" ]; then
                if run_git_command commit -m "add all $year transcripts"; then
                    print_colored "  ✓ Transcripts committed" "$GREEN"
                    year_has_changes=true
                fi
            else
                print_colored "  ⊘ No changes to commit for transcripts" "$YELLOW"
            fi
        fi
    else
        print_colored "\n  [1/3] TRANSCRIPTS: Skipped (no files)" "$YELLOW"
    fi
    
    # Step 2: Add and commit summaries
    if [ "$has_summary" = true ]; then
        print_colored "\n  [2/3] SUMMARIES:" "$CYAN"
        if run_git_command add "*_summary.*"; then
            staged_changes=$(git diff --cached --name-only)
            if [ -n "$staged_changes" ]; then
                if run_git_command commit -m "add all $year summaries"; then
                    print_colored "  ✓ Summaries committed" "$GREEN"
                    year_has_changes=true
                fi
            else
                print_colored "  ⊘ No changes to commit for summaries" "$YELLOW"
            fi
        fi
    else
        print_colored "\n  [2/3] SUMMARIES: Skipped (no files)" "$YELLOW"
    fi
    
    # Step 3: Add and commit corrections
    if [ "$has_corrected" = true ]; then
        print_colored "\n  [3/3] CORRECTIONS:" "$CYAN"
        if run_git_command add "*_corrected.*"; then
            staged_changes=$(git diff --cached --name-only)
            if [ -n "$staged_changes" ]; then
                if run_git_command commit -m "add all $year corrections"; then
                    print_colored "  ✓ Corrections committed" "$GREEN"
                    year_has_changes=true
                fi
            else
                print_colored "  ⊘ No changes to commit for corrections" "$YELLOW"
            fi
        fi
    else
        print_colored "\n  [3/3] CORRECTIONS: Skipped (no files)" "$YELLOW"
    fi
    
    # Return to original directory
    cd - >/dev/null || exit 1
    
    if [ "$year_has_changes" = true ]; then
        print_colored "\n  ✓ Year $year completed with commits" "$GREEN"
        ((processed_count++))
    else
        print_colored "\n  ⊘ Year $year had no new changes to commit" "$YELLOW"
        ((skipped_count++))
    fi
done

# Summary
print_colored "\n========================================" "$GREEN"
print_colored "SUMMARY" "$GREEN"
print_colored "========================================" "$GREEN"
print_colored "Years with commits: $processed_count" "$GREEN"
print_colored "Years skipped/no changes: $skipped_count" "$CYAN"
print_colored "\nNote: To push commits to remote, run: git push" "$YELLOW"
print_colored "\n✓ Script completed successfully!\n" "$GREEN"

exit 0
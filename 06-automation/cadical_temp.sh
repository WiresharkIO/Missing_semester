#!/bin/bash

directory_path=~/missing_semester/cadical1.9-0j/cadical1.9-0j

# array declaration for bump_data
declare -A bump_data

# code structure here is very analogous to python..
# checking the process-time and real-time both to condition for > 10 sexonds
check_process_and_real_time() {
    local file_content="$1"
    process_time_match=$(echo "$file_content" | grep -oP 'total process time since initialization:\s*\K\d+(\.\d+)?\s*seconds')
    real_time_match=$(echo "$file_content" | grep -oP 'total real time since initialization:\s*\K\d+(\.\d+)?\s*seconds')
    process_time=$(echo "$process_time_match" | awk '{print $1}')
    real_time=$(echo "$real_time_match" | awk '{print $1}')
    
    # an if condition top check for time > 10 sec for both the availablew times in the file
    if (( $(echo "$process_time > 10 && $real_time > 10" | bc -l) )); then
        return 0
    else
        return 1
    fi
}

find_bump_percentage() {
    local file_content="$1"
    bump_match=$(echo "$file_content" | grep -oP '\b(\d+\.\d+)%\s+bump\b')
    
    if [ -n "$bump_match" ]; then
        echo "$bump_match" | awk '{print $1}' | tr -d '%'
    else
        echo "None"
    fi
}

for filename in "$directory_path"/*.log; do
    if [ -f "$filename" ]; then
        file_content=$(cat "$filename")
        if check_process_and_real_time "$file_content"; then
            percentage=$(find_bump_percentage "$file_content")
            if [ "$percentage" != "None" ]; then
                bump_data["$filename"]=$percentage
            fi
        fi
    fi
done

# Print the top 3 highest percentages
echo "Top 3 highest percentages:"
echo "${bump_data[@]}" | tr ' ' '\n' | sort -g | tail -n 3

# Print the 3 least percentages
echo "3 least percentages:"
echo "${bump_data[@]}" | tr ' ' '\n' | sort -g | head -n 3


#! /usr/bin/bash

# Prompt user for their favorite color
echo "What is your favorite color?"
read -r color
echo "Your favorite color is $color."

# Check if the favorite color is blue
if [[ "$color" == "blue" ]]; then
    echo "Blue is a cool color!"
else
    echo "That's an interesting choice!"
fi

# Prompt user for their age
echo "How old are you?"
read -r age

# Check voting eligibility
if (( age >= 18 )); then
    echo "You are eligible to vote."
else
    echo "You are not eligible to vote."
fi


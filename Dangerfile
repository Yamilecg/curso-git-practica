# Dangerfile

# Check commit title length
if git.commits.any? { |commit| commit.title.length > 50 }
  warn("Commit title should be at most 50 characters.")
end

# Check for empty line between title and description
if git.commits.any? { |commit| commit.body.start_with?("\n") }
  warn("There should be an empty line between the title and the description.")
end

# Check description length
if git.commits.any? { |commit| commit.body.length < 5 }
  warn("The description should have at least 5 characters.")
end

# Check line length in description
git.commits.each do |commit|
  commit.body.lines.each do |line|
    if line.length > 72
      warn("Each line in the description should not have more than 72 characters.")
    end
  end
end

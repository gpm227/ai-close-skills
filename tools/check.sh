#!/usr/bin/env bash
# House checks. Run from the repository root: bash tools/check.sh
set -uo pipefail
fail=0
bad() { printf 'FAIL %s\n' "$*"; fail=1; }

[ -f .claude-plugin/marketplace.json ] || bad "missing .claude-plugin/marketplace.json"

# 1. every skill follows the contract
count=0
for dir in skills/*/; do
  [ -d "$dir" ] || continue
  name=$(basename "$dir")
  file="$dir/SKILL.md"
  [ -f "$file" ] || { bad "$name: no SKILL.md"; continue; }
  count=$((count + 1))

  head -1 "$file" | grep -qx -- '---' || bad "$name: frontmatter must open on line 1"
  fm_name=$(sed -n '2,40p' "$file" | grep -m1 '^name:' | sed 's/^name:[[:space:]]*//')
  [ "$fm_name" = "$name" ] || bad "$name: frontmatter name '$fm_name' does not match directory"

  desc=$(sed -n '2,40p' "$file" | grep -m1 '^description:' | sed 's/^description:[[:space:]]*//')
  [ -n "$desc" ] || bad "$name: no description"
  len=${#desc}
  [ "$len" -ge 120 ] || bad "$name: description too short ($len chars) to route on"
  [ "$len" -le 1024 ] || bad "$name: description over 1024 chars ($len)"

  sed -n '2,40p' "$file" | grep -q '^  version:' || bad "$name: no metadata.version"

  for section in '## Bring' '## What comes back' '## The trap, and the check' '## Company hooks' '## Related skills'; do
    grep -qx -- "$section" "$file" || bad "$name: missing section '$section'"
  done
done
[ "$count" -gt 0 ] || bad "no skills found"

# 2. every relative markdown link resolves
links=0
while IFS= read -r md; do
  dir=$(dirname "$md")
  while IFS= read -r target; do
    case "$target" in
      ''|'#'*|http*|mailto:*) continue ;;
    esac
    path=${target%%#*}
    path=${path%%\?*}
    [ -n "$path" ] || continue
    links=$((links + 1))
    [ -e "$dir/$path" ] || bad "$md: broken link $target"
  done < <(grep -oE '\]\([^)]*\)' "$md" | sed 's/^](//; s/)$//')
done < <(find . \( -name .git -o -name .agents -o -name node_modules -o -name .local \) -prune -o -name '*.md' \( ! -path './custom/*' -o -path './custom/README.md' \) -print | sort)

echo "checked $count skill(s) and $links link(s)"
if [ "$fail" -eq 0 ]; then echo "house checks passed"; else echo "house checks failed"; fi
exit "$fail"

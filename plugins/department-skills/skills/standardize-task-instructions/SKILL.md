---
name: standardize-task-instructions
description: "Turns how someone does a recurring task into written instructions anyone (or any AI) can follow, with tests to prove they work. Use for writing an SOP, a prompt, a reusable AI instruction, a skill, or \"write down how we do this.\""
---

# Write reusable task instructions

Plain AI writes instructions that work on the one example it saw. The next person brings a slightly different input and gets something different.

## You'll need

- **A finished example** of the task done well.
- **The inputs** it started from.
- **What changes each time** and what never does.
- **What went wrong** in past attempts, if you know.

## Steps

1. Separate what's fixed (rules, format) from what changes (the inputs).
2. Write the output format exactly.
3. Turn every requirement into something you can check by looking at the result.
4. Add what to do when an input is missing.
5. Test on the original case and one case the instructions haven't seen.
6. If two requirements contradict, keep both and ask the owner.

## What you get back

The instructions, one example of how to call them, and a set of test cases with expected results.

## The trap

The example report was for one store, so the draft says "Report the store's weekly sales." The next person runs it for a region with 12 stores. Write "For each location, report weekly sales. For more than one location, add a total row."

## Check it

- An unseen case produces the right output.
- Every requirement can be checked by looking at the output.
- The missing-input case is handled.
